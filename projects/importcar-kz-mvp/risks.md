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
- Current imagery is still demo imagery and should be validated for rights and exact listing fit before real launch.
- Supabase admin workflows are not production-ready without auth and role-based access.
- Proof artifacts are mock trust devices and must eventually be tied to real importer operations.

## Mitigated / reduced risks
- Anonymous lead select/update access is not exposed in public schema.
- Admin status updates are read-only in UI until authenticated access exists.
- Former dead buttons now open real inline mock content.
- Proof-case purchase price is data-driven.
- Phone validation exists before submit.
- Smoke tests exist as a repeatable verification path (`npm run smoke:test`).
