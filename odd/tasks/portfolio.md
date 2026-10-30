# GitHub Portfolio and Profile README

## Objective

Turn verified GitHub work into an accurate, polished profile README and a responsive portfolio at `https://antoniodavid.github.io/`.

## Problem and Why

The existing README contains stale or overstated claims and points to a missing `PORTFOLIO.md`. The Pages repository exists, but its root `index.html` is blank. The portfolio should foreground verified Odoo/Python integrations, OCA work, and developer tooling.

## Scope

- Refresh the profile `README.md` using public, verified projects and contribution links.
- Add maintainable static site source under `site/` and focused standard-library tests.
- Publish the site files to the existing Pages root in `antoniodavid/antoniodavid.github.io`, then verify the deployed page.

## Constraints and Evidence

- Use the authenticated GitHub CLI keyring account only. Unset `GH_TOKEN` and `GITHUB_TOKEN` for all GitHub CLI commands; do not use SSH credentials.
- Do not feature the private OpenUpgrade MCP repository in public copy.
- Do not describe OCA `l10n-usa#166` as complete: it remains open with changes requested and a stale notice.
- Prefer merged, linked outcomes over raw line-count or follower statistics. OCA migration diffs include translations/scaffolding.
- Preserve existing untracked `.atl/` and `.codegraph/` content.
- The existing `.gitignore` ignores `/site`; leave it unchanged and force-add only the two intended site files.
- Hallmark created untracked `.hallmark/salt`; it is excluded from the candidate and publication pending cleanup approval.
- RDD is globally off; do not change it. No native review transaction is authorized by this task.

## Authorized Scope

- Local: `README.md`, `site/index.html`, `site/styles.css`, `tests/test_portfolio.py`, and this task document.
- Remote: update only root `index.html` and `styles.css` on `antoniodavid/antoniodavid.github.io` via the authorized `gh` keyring session.

## Effective TDD and Checks

- Strict TDD: enabled by the supplied project instructions.
- Runner: `python -m unittest discover -s tests` using Python standard-library `unittest`, approved by the user.
- Required sequence: observe RED on the new tests, implement to GREEN, then refactor and rerun GREEN.
- After publishing, check the Pages build and fetch/read the live page; record any unavailable or failed checks honestly.

## Delivery Strategy

- Strategy: `ask-on-risk`; the user selected `stacked-to-main` on 2026-10-30.
- Current candidate: 976 authored lines (898 additions + 78 deletions), including this task document.
- One reviewable slicing pass: PR1 semantic page + base CSS/tests + this doc (~385); PR2 layout/accessibility CSS + tests (~368); PR3 OCA/contact/footer CSS (~99); PR4 README + its regression test (~124).
- Stack order: PR1 → PR2 → PR3, each retargeted to `main` after its parent merges; publish Pages after PR3, then deliver PR4.

## Acceptance Criteria

- README claims match GitHub evidence, omit private project links, remove the broken `PORTFOLIO.md` link and remote stats widgets, and link to selected merged OCA work.
- Site has responsive, accessible semantic HTML/CSS, clear project case studies and correct open/merged status, with no external runtime dependencies.
- The approved unittest command passes; local source corresponds to the files published to the Pages root.
- GitHub Pages at `https://antoniodavid.github.io/` serves the new site over HTTPS.

## Tasks

- [ ] T1 — Commit PR1: semantic site, base styles, content/status tests, and this task doc (~380 lines); test with the approved runner.
- [ ] T2 — Commit PR2: core layout, responsive/accessibility styles and related tests (~368); stack on T1, retarget after T1 merges.
- [ ] T3 — Commit PR3: OCA/contact/footer styles (~99); stack on T2, retarget after T2 merges.
- [ ] T4 — Publish the tested site files to the authorized Pages repository after PR3 merges; use `gh` without token variables or SSH and record the commit/build/live-page evidence.
- [ ] T5 — Deliver PR4: profile README refresh and its regression test (~124), after Pages publication.

## Progress

- GitHub/profile/OCA research and local implementation complete; parent spot-check: `python -m unittest discover -s tests` — 7 tests passed on the full candidate.
- Branch: `feat/portfolio-site`; current source diff is mixed staged/unstaged, with unrelated untracked directories preserved.
- Running count: 976 authored changed lines; the selected PR slices are estimates and will be recounted after task-document progress updates.
- Next: commit/test each stacked slice, wait for ordered merges, publish/verify Pages, then deliver the README slice.

## Relevant Files

- `README.md` — GitHub profile landing page to refresh.
- `site/` — canonical static portfolio source to add.
- `tests/` — standard-library regression checks to add.
- `odd/tasks/portfolio.md` — recovery document for this work.
