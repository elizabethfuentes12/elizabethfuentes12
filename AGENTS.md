# AGENTS.md

## What this is
GitHub profile repository (`elizabethfuentes12/elizabethfuentes12`). `README.md` is the public profile page.

## Structure
- `README.md`: profile. The block between `<!-- BLOG-POST-LIST:START -->` and `<!-- BLOG-POST-LIST:END -->` is rewritten by a workflow; do not edit it by hand.
- `.github/workflows/blog-post-workflow.yml`: every 12 hours (and on manual run) it reads the dev.to RSS feed and commits the 5 latest posts into the README.
- `mejorar.md`: local, untracked notes about dev.to strategy. Do not commit (the repo is public).

## Commands
No build. Preview: render `README.md` on GitHub or with `grip`. Run the workflow manually: `gh workflow run "Latest blog posts"`.

## Conventions
- Projects are grouped by theme; keep at most about 15 rows. Stars use shields.io badges (live).
- Verify every repo link (`gh repo view <owner>/<repo>`) before adding it.
- No SEO keyword blocks, no github-readme-stats cards (unmaintained).
- The profile is positioned as an open-source creator, not as an AWS employee: no employer mention and no AWS Blog badge/link. Employer details live on LinkedIn.
- Bio wording (from Eli): Developer Advocate and AI engineer specializing in agent harness architecture. Keep it.

## Recent changes
- Rewrote the README: new agent-focused projects, grouped tables, auto-updating latest posts, shorter stack and contact badges. Removed the keywords block and old ReactJS/anime/event rows.
- Local backup of the pre-rewrite state: branch `backup-local-oct2025` and `git stash` entry `readme-local-edits-backup`.
- Intro rewritten to the Developer Advocate / agent harness bio; removed AWS Blog badge and link.
