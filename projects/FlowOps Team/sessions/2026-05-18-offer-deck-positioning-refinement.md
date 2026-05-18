# Session 2026-05-18 — Offer Deck Positioning Refinement

## Related
- [[../00 - Overview|overview]]
- [[../01 - Strategy/Positioning|Positioning]]
- [[../01 - Strategy/Main Offer|Main Offer]]
- [[../../patterns/flowops-pdf-presentations|FlowOps PDF Presentations]]

## What was done
- Refined both separate FlowOps offer decks:
  - `/Users/tamerlan/Desktop/FlowOps-Offer-English/index.html`
  - `/Users/tamerlan/Desktop/FlowOps-Offer-Russian/index.html`
- Replaced the previous ROI-heavy impact slide with an operational before/after slide centered on:
  - `<30 sec` first response
  - `24/7` lead coverage
  - one controlled pipeline
  - less manual coordination
- Removed hard pricing from the cover footer and replaced the cost slide with a value-first engagement model:
  - AI Sales System Implementation
  - Continuous Optimization & AI Operations
  - Runtime Infrastructure
- Rebuilt and verified both PDFs:
  - `/Users/tamerlan/Desktop/FlowOps-Offer-English/FlowOps-AI-Sales-Operating-Systems-EN.pdf`
  - `/Users/tamerlan/Desktop/FlowOps-Offer-Russian/FlowOps-AI-Sales-Operating-Systems-RU.pdf`
- Fixed PDF-only shadow artifacts by keeping the original soft HTML shadows but disabling card shadows entirely inside `@media print` for both decks and the shared FlowOps deck template.

## Key findings
- For premium B2B positioning, FlowOps should lead with predictability, speed, system control, and reduced chaos before talking about ROI.
- Aggressive revenue projections and early price anchoring make the offer feel less enterprise-grade when there is no case-study proof beside them.
- Client-facing decks read stronger when exact pricing is deferred until interest is established and the slide explains the scope of the engagement instead.
- Headless Chrome can flatten soft card shadows into gray rectangular artifacts in PDF output; for FlowOps decks, the reliable rule is: shadows in HTML, no card shadows in PDF.

## Blockers
- None for the current deck revision.

## Next steps
- Keep future outbound decks value-first by default.
- Add exact pricing only in late-stage proposals or client-specific commercial offers where scope is already understood.
