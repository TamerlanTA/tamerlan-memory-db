# Session 2026-06-30 — Post Preview Roadmap Sync

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]
- [[technical-architecture]]

## What was done
- Synced the MVP scope reversal and Vercel preview deployment across project memory after preview `dpl_92thMKzyip2qEvXBSi1MtV37EiKu`.
- Updated global `current-focus.md` so FlowOps now points to MVP Sales Validation, not active portal work.
- Updated [[roadmap]] active focus and implementation order:
  - public order flow restored in preview;
  - Portal/deal-room removed from public buyer flow in preview;
  - next action is production promotion if preview is accepted, then outreach.
- Updated [[current-state]] to mark June 29 Phase 3 execution/order-flow entries as historical/superseded by the June 30 reversal.
- Updated [[next-steps]] so Phase 3 planning is explicitly future-only, not an immediate MVP task.
- Updated [[decisions]] so D-014 and D-017 remain valid future targets but are not current MVP scope.

## Key findings
- The latest preview is ready, but production still points to the over-scoped portal/deal-room build.
- Future account/chat/deal-room work remains documented and intentionally preserved.
- Current MVP should focus on public audit, public system request/order form, internal order workspace, manual follow-up, and outreach.

## Blockers
- Production promotion has not been done yet.
- MVP scope reversal still needs commit if the user wants git history cleaned up.

## Next steps
- Promote preview to production if accepted.
- Verify production `/portal` gate and public order form after promotion.
- Manually verify/enrich the 20-account seed list.
- Start first outreach batch.
