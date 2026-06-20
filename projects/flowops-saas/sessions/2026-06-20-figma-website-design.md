# Session 2026-06-20 — Figma Website Design (premium redesign concept)

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[pricing]]
- [[pipeline-catalog]]

## What was done
- Built a full premium homepage design in Figma from Tamerlan's 4 hand sketches (refs: juanmora.co, FlowOps logo).
- Style: modern light, bright blue/cyan + indigo accents, technological. Brand gradient cyan→blue→indigo derived from the logo.
- Figma file: **FlowOps OS — Website Design** → https://www.figma.com/design/Pv2Rkr3W6pbbspoxT6B0DH
- Root frame `FlowOps — Homepage`, 1440px desktop, 7 sections:
  1. Navbar (gradient logo mark + FlowOps wordmark, nav, Get started)
  2. Hero — "Put your operations on autopilot." (gradient word), dual CTA, glow blobs, stats row (40+ / 7 / 60–90d)
  3. How it works — 4 connected step cards (Connect → Deploy → AI runs → Live dashboard)
  4. Catalog — category filter pills + 3×3 pipeline cards w/ tier badges ($/$$/$$$), real prices from [[pricing]]
  5. Custom-build CTA — vibrant gradient panel "Can't find your workflow? We'll build it"
  6. Subscription — Maintain $149 / Scale $299 (highlighted) / Operator $549 / Enterprise Custom, feature lists
  7. Footer (navy) — final CTA + link columns + status pill + legal bar

## Key findings / decisions
- Fonts: Space Grotesk (display) + Inter (UI), with Inter fallback baked into the generator code.
- Figma MCP build pattern: incremental per-section use_figma calls; root must stay primaryAxisSizingMode=AUTO (calling resize() forces FIXED and clips stacked sections).
- Content pulled from existing memory (positioning, 40-pipeline catalog, full pricing/subscription tiers).

## Blockers
- Figma Starter plan hit the MCP tool-call limit at the very end (only a cosmetic rename/zoom call failed; design fully complete).

## Next steps
- Optional: design Pipeline detail page, /pricing, mobile (375px) frames; add real screenshots/illustration to hero.
- Decide whether to implement this concept into the existing Next.js site (current code already has /os, /pricing).
