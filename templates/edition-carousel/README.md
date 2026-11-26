# Edition Carousel Template (Derived from the first 5 editions)

This template is based on structural patterns shared by:

1. `archives/2026-02-14-tokyo/index.html`
2. `archives/2026-02-14-london-relay-v1/index.html`
3. `archives/2026-02-14-london-relay-v2/index.html`
4. `archives/2026-02-15-shoreditch-relay/index.html`
5. `archives/2026-02-15-shoreditch-walk/index.html`

## Observed baseline (what these editions have in common)

- **Fullscreen carousel**: one slide/screen per tap.
- **Layer stack**: background + vignette + HUD + story text + footer.
- **Scene data model**: each scene provides `whisper`, `line`, `micro`, and visual (`image` or gradient fallback).
- **Navigation model**: tap/click advances, then loops to an epilogue/replay state.
- **Persistent archive navigation**: `LAURARCHIVE` link always visible.
- **Optional sound**: sound toggle is hidden when no `data-audio` source is provided.

## Mandatory rules for new editions

1. **Use slide-by-slide scenes**, not blog/post blocks.
2. Keep a `scenes` array (or JSON equivalent) where each item maps to exactly one screen.
3. Keep the footer archive link visible and clickable.
4. Keep `prefers-reduced-motion` handling.
5. Keep a deterministic fallback background when an image fails to load.
6. Ensure archive page links back to `../../` and `../../archive.html`.

## Files in this folder

- `edition-carousel.template.html`: production-ready starter HTML.
- `edition-scenes.template.json`: external scene-data template.

## Build checklist for future editions

1. Copy `edition-carousel.template.html` to either:
   - `index.html` (new live edition), or
   - `archives/<new-slug>/index.html` (archive snapshot/draft).
2. Replace `EDITION_*` placeholders in `<title>`, hero intro, and epilogue copy.
3. Fill `edition-scenes.template.json` and inline/import as `scenes`.
4. Validate relative paths from destination directory.
5. Verify interaction:
   - Tap/click advances
   - Keyboard `ArrowRight`/`Space` advances
   - Sound toggle works only when audio exists
   - LAURARCHIVE + NEWAIYORK links are visible and unobstructed
