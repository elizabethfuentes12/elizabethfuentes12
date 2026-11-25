# AGENTS.md

## What this is
GitHub profile repository (`elizabethfuentes12/elizabethfuentes12`). `README.md` is the public profile page.

## Structure
- `README.md`: profile. The block between `<!-- BLOG-POST-LIST:START -->` and `<!-- BLOG-POST-LIST:END -->` is rewritten by a workflow; do not edit it by hand.
- `scripts/update_posts.py`: reads the dev.to RSS feed, skips `[Boost]` reposts, writes the 5 latest posts as plain `- [title](url)` lines (no dates) between the markers. Standard library only.
- `.github/workflows/blog-post-workflow.yml`: runs that script every 12 hours, on manual run, and when the workflow or script is pushed; commits only if README changed.
- `mejorar.md`: local, untracked notes about dev.to strategy. Do not commit (the repo is public).

## Commands
No build. Update posts locally: `python3 scripts/update_posts.py`. Preview: render `README.md` on GitHub or with `grip`. Run the workflow manually: `gh workflow run "Latest blog posts"`.

## Conventions
- Projects are grouped by theme; keep at most about 15 rows. Stars use shields.io badges (live).
- Verify every repo link (`gh repo view <owner>/<repo>`) before adding it.
- No SEO keyword blocks, no github-readme-stats cards (unmaintained).
- The profile is positioned as an open-source creator, not as an AWS employee: no employer mention in the bio; employer details live on LinkedIn. The AWS Blog badge and link stay (Eli publishes there).
- Bio wording (from Eli): Developer Advocate and AI engineer specializing in agent harness architecture. Keep it.

## Recent changes
- Rewrote the README: new agent-focused projects, grouped tables, auto-updating latest posts, shorter stack and contact badges. Removed the keywords block and old ReactJS/anime/event rows.
- Local backup of the pre-rewrite state: branch `backup-local-oct2025` and `git stash` entry `readme-local-edits-backup`.
- Intro rewritten to the Developer Advocate / agent harness bio. AWS Blog badge kept.
- Workflow fix: added `actions/checkout@v4` (without it the action fails with `fatal: not in a git directory`).
- Replaced `gautamkrishnar/blog-post-workflow` with `scripts/update_posts.py`: the action put all posts on one line and could not filter `[Boost]` reposts.
