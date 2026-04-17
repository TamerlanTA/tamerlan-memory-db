# Session 2026-04-17 — Batch 1 preorders / PO visibility

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Implemented Batch 1 of the bonus back-office mini-block inside the existing `/admin/stats` page
- Added a new `Preorders` tab as the sales-first admin view
- Extended the backend preorder admin read shape to include PO reference, contact email, confirmation email status, sent timestamp, and preview image URL
- Added search support for PO reference, raw numeric submission id, contact email, and product code
- Added focused pure tests for preorder reference formatting/search parsing and preorder payload extraction

## Key findings
- The smallest safe implementation path worked without schema migrations
- Existing preorder foundations were sufficient for a commercially useful first lookup table once the admin read shape was expanded
- Batch 1 still leaves exact preorder ↔ generation ↔ asset linkage unresolved; this remains correctly deferred to Batch 3

## Verification
- `pnpm exec vitest run server/preorderAdmin.test.ts client/src/domain/preorder.test.ts server/preorderConfirmationEmail.test.ts`: PASS
- `pnpm check`: PASS
- `pnpm build`: PASS

## Blockers
- No blocker for Batch 1 itself
- Remaining limitation: preorder rows still rely on parsed intent payload rather than exact persisted generation/asset linkage

## Next steps
- Move to `Batch 2 — Generations visibility`
- Keep Batch 3 and Batch 4 pending until Batch 2 is implemented and reviewed
