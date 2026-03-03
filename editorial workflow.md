# Editorial Workflow Prompt (for rapid new editions)

Use this prompt whenever you want a brand-new homepage edition built quickly from the existing Tokyo Postcard style.

---

## What I need from you (minimal input)
If you only send **these 5 items**, I can start immediately:
1. **Edition concept (1 sentence):** e.g., “Rainy Camden morning with neon and puddles.”
2. **Headline text:** the exact hero line (or “write 3 options”).
3. **Image source:** either folder paths in `assets/...` or new uploads (8–20 images preferred).
4. **Color direction:** 2–4 hex colors or a mood phrase (e.g., “electric blue + warm amber”).
5. **Archive label + blurb:** one line each for `archives/manifest.json`.

That is the smallest reliable brief to produce a new edition aligned with repo conventions.

---

## 5 kickoff questions that reliably unlock production
1. **Narrative intent:** Should this edition feel intimate, cinematic, playful, or documentary?
2. **Content ownership:** Are all provided images licensed/owned for publication, and do any require credits?
3. **Visual system:** Do you want gradient-led, photo-led, or hybrid treatment?
4. **Interaction level:** Static hero, tap-through scenes, or ambient audio + scene progression?
5. **Publishing plan:** Is this replacing `index.html` now, or landing as archive-first draft?

---

## Copy/paste prompt for fast collaboration
You can paste this directly to start a new build:

> You are my edition builder for this repo. Review `DEVELOPER_GUIDE.md`, current `index.html`, and `archives/` pages to match tone and architecture.
>
> **Goal:** ship one new postcard-style web edition quickly.
>
> Ask me only the critical missing info, then implement:
> 1) updated `index.html` (or archive draft if requested),
> 2) archive entry in `archives/manifest.json` when applicable,
> 3) relative path-safe asset usage,
> 4) return navigation for archive pages.
>
> Start by asking these questions (one compact block):
> - Edition concept + mood in one sentence
> - Headline text (or generate options)
> - Images to use (existing paths or new uploads)
> - Color palette (hex values or mood words)
> - Payment/budget constraints for commissioned assets (yes/no + cap)
> - Deadline and whether this is live-homepage or archive draft
>
> After I answer, produce:
> - A short build plan
> - Draft copy lines (headline, subline, microcopy)
> - The implementation in repo files
> - A brief QA checklist (paths, archives links, reduced motion)

---

## Image request checklist (ask this before implementation)
- Do you want me to curate from existing `assets/` or wait for new uploads?
- If new uploads: what orientation mix (portrait/landscape), and minimum resolution?
- Any faces/minors/logos that need removal, blur, or explicit consent checks?
- Preferred sequencing logic: chronological walk, color flow, or emotional arc?

---

## Payment & budget intake language (for project scoping)
Use this exact wording when needed:

> “If this edition needs paid assets (photography, licensing, illustration, audio), share your **budget cap**, **payment method preference**, and whether we should **only use no-cost existing repo assets**. I won’t process payments directly, but I can scope the build to your budget constraints.”

---

## Expected output standard
- Preserve archive history; do not rewrite prior editions unless fixing breakage.
- Keep references relative-path correct for homepage vs `archives/<slug>/index.html` depth.
- Keep tone concise, atmospheric, and postcard-like.
- Include accessible fallbacks (reduced motion, contrast-aware text, meaningful links).
