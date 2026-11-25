"""Write the latest dev.to posts into README.md between the BLOG-POST-LIST markers."""
import re
import urllib.request
import xml.etree.ElementTree as ET

FEED = "https://dev.to/feed/elizabethfuentes12"
README = "README.md"
MAX_POSTS = 5
START, END = "<!-- BLOG-POST-LIST:START -->", "<!-- BLOG-POST-LIST:END -->"

req = urllib.request.Request(FEED, headers={"User-Agent": "profile-readme-bot"})
with urllib.request.urlopen(req, timeout=30) as resp:
    root = ET.fromstring(resp.read())

posts = []
for item in root.iter("item"):
    title = (item.findtext("title") or "").strip()
    link = (item.findtext("link") or "").strip()
    # Skip dev.to reposts ("[Boost]") and empty items.
    if not title or not link or title.startswith("[Boost]"):
        continue
    title = title.replace("[", "\\[").replace("]", "\\]")
    posts.append(f"- [{title}]({link})")
    if len(posts) == MAX_POSTS:
        break

with open(README, encoding="utf-8") as f:
    text = f.read()
block = START + "\n" + "\n".join(posts) + "\n" + END
new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
with open(README, "w", encoding="utf-8") as f:
    f.write(new)
print(f"{len(posts)} posts written")
