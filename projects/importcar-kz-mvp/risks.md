# ImportCar.kz MVP — Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

## Content
## Current risks
- Pricing and customs formulas are still estimates/placeholders and need jurisdiction-validated rules before real use.
- Catalog records are demo data, not live inventory.
- Current visuals use intentional placeholders; exact listing-linked or licensed imagery is still missing.
- Supabase admin workflows are not production-ready without auth and role-based access.
- Proof artifacts are mock trust devices and must eventually be tied to real importer operations.

## Mitigated / reduced risks
- Anonymous lead select/update access is not exposed in public schema.
- Smoke tests now exist as a repeatable verification path (`npm run smoke:test`).

## Open risks from supervisor audit (2026-05-16)
- Admin `updateStatus` will return RLS error until authenticated admin session exists.
- Two dead buttons (ImporterCard "Details", AuctionSheetPreview "View sample report") — no `onClick`.
- DealProofSection purchase price is hardcoded, not driven by data.
- Phone validation is `required`-only — no format check.
- `Car.sourceCountry` field is redundant noise in the type until multi-source inventory is introduced.
