# Developer Guide (Read Before Editing)

This repository is a postcard-style static site with a rotating current homepage and archived editions.

## Core operating model
- `index.html` is the current live homepage experience.
- Historical homepages are preserved under `archives/<edition-slug>/index.html`.
- `archives/manifest.json` is the source of truth for archive links shown on the current homepage.
- Shared media lives under top-level `assets/` and is referenced by relative paths from each page.

## Editing principles
1. **Preserve archives:** never overwrite archived narratives unless fixing breakages (paths, links, accessibility, critical UX defects).
2. **Homepage can evolve:** new editions should update `index.html` while keeping old versions in `archives/`.
3. **Manifest drives discovery:** when adding an archive, append an entry to `archives/manifest.json` with `slug`, `label`, and `blurb`.
4. **Snapshot on promotion:** every time you ship a new homepage edition, first copy the outgoing `index.html` (plus any supporting assets/data) into `archives/<edition-slug>/`, then register that slug in the manifest so the archive page gains a card immediately.
5. **Relative paths first:** verify path correctness from each page location (`index.html` vs `archives/<slug>/index.html` differ).
6. **Return path UX:** archive pages should provide a clear navigation path back to homepage.

## Pre-commit checklist
- Confirm changed image/audio paths resolve from the edited page location.
- Validate archive navigation links (`../../` from `archives/<slug>/index.html`).
- Run a local static server and load both homepage and at least one archive page.
- Ensure no accidental content drift in archived copy beyond intended fixes.

## Known structure
- Live page: `index.html`
- Werkwelt page: `blog.html`
- Archives index data: `archives/manifest.json`
- Archive pages: `archives/*/index.html`
- Asset roots: `assets/`, plus some edition-local `archives/<slug>/assets/`

## Werkwelt email capture workflow
- `blog.html` includes a `mailto:` quick-action for drafting Werkwelt posts.
- To make `werkwelt@tokyopostcard.com` usable, configure mailbox forwarding at your DNS/email host (Cloudflare Email Routing, Fastmail alias, or Google Workspace alias all work).
- Incoming email is an editorial inbox only. Publishing still requires manual copy/edit into `blog.html`.

## Risk areas
- Broken relative paths after moving assets.
- Archive links failing when directory depth assumptions change.
- Regressions from broad find/replace in narrative text blocks.

## Repository workflow preference
- Default workflow is to commit directly to `main` for routine changes in this repo.
- Use a feature branch only when explicitly requested or when isolating high-risk/experimental work.
- If tool defaults conflict with this preference, treat this guide as the repo-local source of truth.
