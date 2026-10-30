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
- Remote: push branches and open PRs in `antoniodavid/antoniodavid` (no merge) and update only root `index.html`/`styles.css` on `antoniodavid/antoniodavid.github.io`, via the `gh` keyring session with `GH_TOKEN`/`GITHUB_TOKEN` unset and no SSH.
- Direct-main setup authorized: add `.github/ISSUE_TEMPLATE/feature_request.yml` and labels `status:approved`, `type:feature`, `type:docs` to `antoniodavid/antoniodavid`; create the portfolio issue using the user's `Closes` intent. Do not apply `status:approved` without exact issue-specific authorization.

## Effective TDD and Checks

- Strict TDD: enabled by the supplied project instructions.
- Runner: `python -m unittest discover -s tests` using Python standard-library `unittest`, approved by the user.
- Required sequence: observe RED on the new tests, implement to GREEN, then refactor and rerun GREEN.
- After publishing, check the Pages build and fetch/read the live page; record any unavailable or failed checks honestly.

## Delivery Strategy

- Strategy: `ask-on-risk`; the user selected `stacked-to-main` on 2026-10-30.
- Current candidate: 2,148 authored lines (1,793 additions + 355 deletions) including the task document and the redesign work unit `0a89b42`.
- The earlier PR1/PR2/PR3 slices preceded the redesign; re-plan the slices against the rewritten site before any push. Publication still needs fresh user authorization.
- Stack order remains PR1 → PR2 → PR3, each retargeted to `main` after its parent merges; publish Pages after the site slices, then deliver the README slice.

## Acceptance Criteria

- README claims match GitHub evidence, omit private project links, remove the broken `PORTFOLIO.md` link and remote stats widgets, and link to selected merged OCA work.
- Site has responsive, accessible semantic HTML/CSS, clear project case studies and correct open/merged status, with no external runtime dependencies.
- The approved unittest command passes; local source corresponds to the files published to the Pages root.
- GitHub Pages at `https://antoniodavid.github.io/` serves the new site over HTTPS.

## Tasks

- [x] T1 — PR1 semantic site baseline committed as `ae1af88` (~385 lines); staged-tree `python -m unittest discover -s tests` passed (4 tests).
- [x] T2 — PR2 layout/accessibility committed as `c333d97` (~376 lines); staged-tree `python -m unittest discover -s tests` passed (6 tests).
- [x] T3 — PR3 OCA/contact/footer styles committed as `7097ae0` (107 lines including task progress); staged-tree tests passed (6).
- [ ] T4 — Add the authorized YAML form/labels to profile-repo `main` (form commit `2de2bc2e3a86eb057d9be93e39b02c0508ae2fe1`, labels read back); create the portfolio issue and record identity/read-back. The create attempt returned an unknown outcome; a post-attempt read-only listing found 0 issues, so no issue identity is available.
- [ ] T5 — After explicit authorization for `status:approved` on the exact issue, push/open the stacked PRs (no merge).
- [ ] T6 — Publish the tested site files to the authorized Pages repository after PR3 merges; use `gh` without token variables or SSH and record the commit/build/live-page evidence.
- [ ] T7 — Deliver PR4: profile README refresh and its regression test (~124), after Pages publication.
- [x] T8 — Redesign the site from the verified GitHub audit: editorial workbench direction, merge wall, six projects, OCA ledger, numbers, method, timeline, toolbox, contact. `site/index.html` and `site/styles.css` rewritten; committed as `0a89b42`.
- [x] T9 — Refresh local README copy: replace the broken `odoo-language-server` entry with `odoo.nvim` and Conecta, add the ten-merged-change OCA link, and keep the regression test; committed as `0a89b42`. Delivery remains tracked by T7.
- [x] T10 — Fix the two findings from the Lighthouse audit: raise the featured project stat-label contrast and align the brand link accessible name with its visible text; committed as `0a89b42`.

## Progress

- PR1 `ae1af88`, PR2 `c333d97`, and PR3 `7097ae0` are committed; staged-tree verification passed 4, 6, and 6 tests. The full candidate previously passed 7 tests.
- PR3 branch: `feat/portfolio-site-03-oca`; README and the redesign are committed in `0a89b42`, and unrelated `.atl/`, `.codegraph/`, `.hallmark/` remain untracked and preserved.
- Running count: 2,148 authored changed lines across the portfolio work; the redesign replaced most of the earlier site source, so recount the slices before opening PRs.
- PR preflight: the base repo has issues enabled and actor permission `ADMIN`, but no issues, no `.github` YAML issue form, and no `status:approved` or `type:*` labels; no write occurred.
- The feature form was read back byte-for-byte from `main`; labels `status:approved`, `type:feature`, and `type:docs` were created and confirmed. No issue has been confirmed.
- A complete open/closed search for `portfolio OR website OR README` returned zero candidates.
- A later exact-title lookup and full issue listing before the create attempt both returned 0 matches / 0 issues. The single `gh issue create` attempt returned no verifiable identity; the immediate post-attempt full issue listing still returned 0 issues. No further GitHub mutation was attempted; diagnose or get user direction before any new create attempt.
- Next: decide with the user whether to publish; resolve the unknown issue-create outcome first, then request issue-specific approval-label authorization before pushing/opening any stack.
- Redesign evidence: `python -m unittest discover -s tests -v` passed 10 tests on 2026-10-30. Chrome DevTools checked 1440×1000 and 390×844 with no horizontal overflow; the mobile hero stat strip appears only under 60rem.
- Lighthouse on the local page: mobile 100 accessibility / 100 best practices / 100 SEO / 100 agentic browsing; desktop the same, 54 audits passed and 0 failed in both runs.
- The redesign is committed locally as `0a89b42`; it is not pushed or published.
- Engram mirror pending: `mem_save` refused with `ambiguous_project` because the server process cwd is the parent workspace. This local document is authoritative; retry the mirror from the repository workspace or after adding repo-local Engram config.

## Log

- L1 (2026-10-30, user request, verbatim): "Revisa mi github analiza todos mis proyectos personales, mis contribuciones a la OCA y demas y crea un portfolio donde seas creativo, mostrando la proactividad, buenas practicas, trabajo en equipo. Hazlo llamativo pero facil de usar y ver los logros. Se creativo"
- L2: Audited GitHub with the active `gh` keyring account and `GITHUB_TOKEN` unset. Verified 365 authored public PRs, 290 merged, 10 merged OCA PRs across 8 repositories, 37 OCA PRs across 19 repositories, 78 reviews across 34 repositories and 28 authors, 53 OCA reviews across 26 repositories and 22 authors, 19 public repositories, and 524 public contributions from 2018 to 2026.
- L3: Chose an editorial workbench direction (paper, ink, Odoo plum, orange, lime) with a 290-tile merge wall as the signature element. The wall is decorative but tied to a real count; no interaction is required to understand it.
- L4: Removed the stale `odoo-language-server` project claim after confirming the repository returns 404; the README now lists `odoo.nvim` and Conecta instead.
- L5: Fixed two Lighthouse findings rather than accepting a lower score: featured project stat labels now use 0.68 paper opacity over plum, and the brand link's accessible name contains its visible "AD Antonio David" text.
- L6: No push, publication, PR, or merge was performed. Publishing to `https://antoniodavid.github.io/` still needs explicit user authorization.

## Relevant Files

- `README.md` — GitHub profile landing page to refresh.
- `site/` — canonical static portfolio source to add.
- `tests/` — standard-library regression checks to add.
- `odd/tasks/portfolio.md` — recovery document for this work.
