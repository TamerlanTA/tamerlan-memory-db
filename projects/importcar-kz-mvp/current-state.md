# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Content
## Status as of 2026-05-16
- Frontend showroom MVP is implemented and deployed.
- Main flow works: home → listing → detail → importer comparison → request modal → success.
- Catalog is premium-only demo data: BMW, Mercedes-Benz, Porsche, Lexus, Audi.
- Pricing uses a versioned estimate engine with explanations, warnings, and importer-specific totals.
- Supabase integration exists for lead submission; public-test schema intentionally allows anonymous insert only on `leads`.
- Admin view is hidden by default; admin status-update calls will fail with RLS error until authenticated admin is added.
- Playwright added to `package.json` devDependencies; `smoke:test` script wired; README updated.

## Open bugs from supervisor audit (2026-05-16)
- `DealProofSection.tsx:27` — purchase price hardcoded as `39 800 000 ₩`; `proofCase.purchasePriceUsd` field exists but is 0 and unused.
- `ImporterCard.tsx:57` — "Details" button has no `onClick`, does nothing.
- `AuctionSheetPreview.tsx:43` — "View sample report" button has no `onClick`, does nothing.
- `LeadForm.tsx:108` — phone field has only `required`, no format or min-length validation.
- `Car.sourceCountry` field exists on type but is never read in app logic (same as `country` for all cars).

## Verification completed
- `npm run lint` passes
- `npm run build` passes
- TypeScript — 0 errors
