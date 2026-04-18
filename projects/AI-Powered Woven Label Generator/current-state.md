# Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-order-preview-submit-state-mapping-fix|Order Preview submit state mapping fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-preview-image-url-hotfix|Preview image URL hotfix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-email-thumbnail-hosted-url-fix|Email thumbnail hosted URL fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-handoff-sync-email-thumbnail|Handoff sync after email thumbnail hosted URL fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-batch2-generations-visibility|Batch 2 generations visibility]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-batch3-preorder-generation-asset-linkage|Batch 3 preorder-generation-asset linkage]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-batch4-ops-asset-retrieval|Batch 4 ops asset retrieval]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-post-m5-order-flow-polish|Post-M5 order-flow polish]]

Last updated: 2026-04-18

- Active branch: `milestone4-auth-completion`
- Latest pushed commit on branch before current local batch: `46c2474` — `Strip inline preview image URLs from preorder submit`
- Repo status for product code: local uncommitted batch present for the hosted email-thumbnail fix
- Remaining untracked local noise: `.claude/` only, intentionally excluded from commits

## What changed today

- Completed a multi-pass refinement of the Griffes Vivienne shared header system
- Improved mobile header responsiveness and tap safety
- Reworked the shared header into intentionally different desktop and mobile compositions
- Added the real brand asset `client/public/logo-gv.png`
- Refined the header from decorative luxury toward minimalist luxury
- Restored stronger premium desktop branding after the minimalist pass weakened desktop too much
- Implemented reliable transactional pre-order confirmation email delivery with Resend
- Synced the order-boundary guest email capture path into the current branch so the backend now receives the final email address during preorder submission
- Added persisted delivery tracking on `preorder_submissions` for contact email, status, sent timestamp, provider message ID, and last error
- Added setup documentation in `docs/preorder-confirmation-email.md`
- Applied migration `0012_preorder_confirmation_email.sql` manually against Railway MySQL with `drizzle-kit migrate`
- Finished the Milestone 5 preorder email batch:
  - EN / FR email rendering based on current user language
  - generated label thumbnail included from the existing result asset URL
  - semi-manual V1.5 email copy with unit-pricing row only, manual confirmation note, reply instruction, and mailto CTA
  - fixed `Reply-To` to `devis@griffesvivienne.com`
- Fixed `/order-preview` contradictory submit UI by making header / confirmation / failure / email-warning rendering state-aware instead of always success-like
- Fixed preorder submit payload construction so inline / oversized `previewImageUrl` values are omitted instead of failing backend validation
- Fixed the missing email thumbnail path by propagating the hosted generation-result asset URL through Result -> order intent draft -> preorder submit, with a backend fallback to the validated draft when the submit payload omits the preview URL
- Completed a grounded code audit for the new post-Milestone-5 back-office / ops visibility mini-block
- Confirmed the current `/admin/stats` page is a support-oriented dashboard, while preorder / PO visibility foundation exists mostly in backend/storage and is not yet surfaced in the admin UI
- Confirmed original logo assets, generation-result assets, and production-prep/vectorization foundation already exist, including SVG passthrough handling for original vector uploads
- Accepted a small bonus scope for Benjamin after Milestone 5 focused on back-office / sales-ops visibility
- This bonus scope is explicitly a structured mini-block, not a new milestone and not a broad admin redesign
- Active source of truth for the mini-block is now the fixed four-batch execution order recorded in project memory
- Implemented Batch 1 locally: sales-first preorder / PO visibility inside the existing admin page
- Added a new preorder-focused admin tab with PO lookup, contact email, product code, material, size, quantity, mode, confirmation email status, sent timestamp, and preview image visibility
- Extended the preorder admin backend read shape and search behavior for `PO-000014`, raw numeric ids, contact email, and product code
- Added focused pure tests for preorder reference/search logic and preorder payload extraction
- Implemented Batch 2 locally: improved generations visibility inside the existing `/admin/stats` page without redesigning the broader admin surface
- Extended the admin generations read-model with parsed display fields from `configSnapshotJson`, including product code, material, size, color, and generated mockup preview URL
- Improved generation search coverage safely by including owner name and snapshot-backed product context in the existing admin query
- Replaced the metadata-heavy generations table with a more visual sales/ops-friendly table showing preview, customer context, product context, status, and created date
- Added focused pure tests for generation admin snapshot parsing and fallback behavior
- Implemented Batch 3 locally: persisted exact preorder linkage to `generationId`, `sourceAssetId`, and `resultAssetId`
- Extended the order-intent draft contract so linkage travels through the existing Result → order intent → preorder submit path instead of introducing a new side channel
- Extended `preorder_submissions` schema and persistence to store exact generation/asset linkage for new preorders
- Exposed linkage through the admin preorder read-model and surfaced compact linkage context in the existing preorders table
- Added focused tests for draft linkage preservation, submit-path persistence, and admin preorder visibility of linkage fields
- Implemented Batch 4 locally: ops asset retrieval inside the existing preorder admin view
- Added a compact preorder asset action area in `/admin/stats` with retrieval actions for original logo, generated preview, and vector asset when available
- Added durable admin asset resolution using fresh `storageKey`-based signed URLs, with exact-generation fallback URLs only when needed for inline/local cases
- Exposed original logo type (`SVG` / `Raster` / `Unknown`) and vector availability status in the preorder read-model
- Reused exact Batch 3 linkage for retrieval and exposed vector readiness based on original SVG passthrough or `vector_logo` production artifacts when present
- Added focused tests for asset availability mapping and durable asset URL resolution helpers
- Implemented a post-M5 / V1.5 polish batch for the ordering flow
- Removed the extra recap-step friction by turning `/order-preview` into an auto-submit sending/confirmation route
- Kept preorder creation, PO generation, confirmation email delivery, and admin/back-office visibility intact during the flow refactor
- Removed the misleading `mailto` CTA from the quote email and replaced it with reply-in-thread guidance so sales context stays attached to the original email
- Tightened the Result screen so backend order-intent creation is now required before leaving the result page

## Active mini-block

### Bonus scope — Back-office / sales-ops improvement

- Status: complete locally through all four agreed batches
- Scope type: post-Milestone-5 bonus block
- Execution rule: follow the agreed batches strictly in order and do not collapse them

### Fixed execution order

1. `Batch 1 — Preorders / PO visibility`
2. `Batch 2 — Generations visibility`
3. `Batch 3 — Preorder ↔ generation ↔ asset linkage`
4. `Batch 4 — Asset retrieval for ops`

### Current active batch

- Mini-block complete

### Explicitly out of scope for this mini-block

- full ERP / SAGE integration
- inbound email parsing or thread-state tracking
- full CRM
- true vectorization pipeline
- broad admin redesign
- full production workflow management

## Current UX state

- Mobile header is considered good and was preserved in the final pass
- Desktop header now has stronger brand presence and better visual support for the hero
- Header-related changes affect:
  - Home
  - Prepare
  - Result
  - My Account
  - Order Preview
  - Credits

## Verification state

- `pnpm build`: PASS
- `pnpm check`: PASS
- Focused preorder email tests: PASS
- Focused Milestone 5 email finishing tests: PASS
- Focused Order Preview submit-state tests: PASS
- Focused preorder payload hotfix tests: PASS
- Focused hosted-thumbnail propagation + email fallback tests: PASS
- Focused post-M5 order-flow polish tests: PASS
