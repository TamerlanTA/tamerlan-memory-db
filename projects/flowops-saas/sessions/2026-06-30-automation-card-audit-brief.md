# Session 2026-06-30 — Automation Card Audit Brief

## Related
- [[overview]]
- [[current-state]]
- [[roadmap]]
- [[next-steps]]
- [[pipeline-catalog]]
- [[pricing]]
- [[automation-card-audit-brief]]

## What was done
- Added [[automation-card-audit-brief]] as the source of truth for auditing and upgrading every FlowOps automation card before scaled outreach.
- Updated [[current-state]] with the new card-quality requirement.
- Updated [[roadmap]] with a dedicated "Automation Card Audit & Upgrade" block before outreach.
- Updated [[next-steps]] so agents run the card audit before scaled outreach.
- Updated [[pricing]] with productized pricing re-audit rules.
- Updated [[pipeline-catalog]] with a card quality standard.

## Key Decisions
- Every live automation card and coming-soon card must be checked for real buyer need, not just listed because it is technically possible.
- Current card descriptions are considered too sparse and must be expanded into richer buyer-facing explanations.
- Pricing should be rechecked against current market references. The working hypothesis is that productized ready automations can often be priced around 30% below comparable custom builds, while preserving premium positioning and delivery margin.
- Every automation card should receive an in-card illustration in the same visual language as the provided FlowOps SVGs:
  - `/Users/tamerlan/Downloads/flowops-custom-workflow.svg`
  - `/Users/tamerlan/Downloads/flowops-request-to-proof-v2_1.svg`
  - `/Users/tamerlan/Downloads/flowops-request-to-proof.svg`

## Blockers
- Actual market pricing research has not yet been performed.
- No catalog/UI implementation was done in this session.

## Next Steps
- Inventory `src/lib/catalog.ts` and build a per-card audit table.
- Research current market pricing by comparable automation type.
- Recommend keep/reposition/merge/remove and new pricing per card.
- After approval or strong alignment with the brief, update catalog copy/schema/UI and add the illustration system.
- QA `/os`, `/os/[slug]`, `/pricing`, and `/stacks` on desktop/mobile.
