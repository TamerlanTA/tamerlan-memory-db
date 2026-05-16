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
- Dead UI buttons from the supervisor audit were converted into working interactions.
- Phone capture now has basic validation before submit.
- Smoke tests now exist as a repeatable verification path.
