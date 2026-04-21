# Session 2026-04-21 — Quote Email Unit Price Box

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Status: accepted by user for this batch.
- Added estimated unit-price display to the quote / preorder confirmation email.
- Inspected `/Users/tamerlan/Downloads/price list.xlsx` and mapped production unit prices by material, size, and quantity tier.
- Added `server/quoteUnitPricing.ts` as the server-side pricing display helper derived from the workbook.
- Updated `server/preorderConfirmationEmail.ts` so the top quote metadata area shows reference on the left and estimated unit price on the right.
- Kept sample and unsupported-tier behavior honest with `Sur demande` / `On request`.
- Did not touch generation, textures, materials, preview UX, billing/credits, legal pages, or order workflow beyond email display.

## Key findings
- Quote emails are built in `server/preorderConfirmationEmail.ts`.
- The existing email had a reference block and a summary row that used placeholder copy (`Custom per-unit quote` / `Devis unitaire personnalisé`), not a numeric price.
- The workbook has one sheet, `Feuil1`, with production tiers from `1 000 pcs` to `10 000 pcs` in 500-piece steps.
- App production quantity currently allows 500 pieces, but the workbook has no 500-piece price; this remains `On request` / `Sur demande`.
- Workbook does not state VAT/tax/shipping terms, so the displayed price is labeled as estimated and final manual confirmation wording remains.

## Verification
- `pnpm exec vitest run server/quoteUnitPricing.test.ts server/preorderConfirmationEmail.test.ts`: PASS
- `pnpm check`: PASS
- `pnpm build`: PASS with known analytics env and bundle-size warnings
- `git diff --check`: PASS

## Blockers
- No code blockers.

## Next steps
- Browser/inbox QA a production quote for a priced tier, e.g. TAFFETA `20x50`, 1,000 pieces → `€0.60 / unit` or `0,60 € / pièce`.
- QA sample and 500-piece production requests to confirm they show `On request` / `Sur demande`.
- If the client wants 500-piece numeric pricing or tax/shipping semantics, obtain an updated price source before changing display logic.
