# Session 2026-04-17 — Back-office ops audit for sales-first mini-block

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Performed a grounded audit of the current Griffes Vivienne codebase for the new small-scope back-office / ops visibility block
- Reviewed the current admin UI, admin TRPC routes, DB schema, preorder flow, asset storage, and production-prep/vectorization foundation
- Compared client priorities against what already exists in code and data rather than proposing a broad redesign

## Key findings
- Existing `/admin/stats` is a support/ops dashboard, not a sales-first PO tracker
- PO references already exist implicitly as `PO-${submissionId}` in preorder confirmation flows, but there is no dedicated PO field, preorder list UI, or PO search
- Preorder storage and admin API foundation already exist (`preorder_submissions`, `order_funnel_events`, `getRecentPreorders`, `getFunnelSummary`), but the current admin page does not render them
- Generation visibility exists as records and counts, but the current admin page shows metadata only; it does not show the generated image or easy logo retrieval
- Original uploaded logos are preserved as assets, including original SVG uploads, and production-prep seeding already marks SVG sources as immediately ready
- Vectorization support exists mainly as schema/foundation; the code currently seeds `production_source` artifacts and placeholder vectorization jobs, but does not yet implement a real vector output pipeline or a usable retrieval flow in admin

## Blockers
- No current back-office UI for preorder rows, PO lookup, contact-email visibility, or confirmation-email delivery status
- No current admin retrieval path that resolves stored asset IDs / storage keys into clickable logo/result downloads
- No current admin-friendly join between preorder rows and the underlying generation / source logo asset

## Next steps
- Add a dedicated sales-first admin tab or page that lists preorder rows with PO reference, submitted date, contact email, product code, quantity, mode, and confirmation email status
- Extend the preorder admin payload so UI can search by PO and show the commercially useful fields already stored in DB
- Add lightweight asset actions for logo retrieval and generated mockup retrieval from admin
- If needed after that, add a linked generation detail drawer or compact side panel rather than expanding the whole admin system
