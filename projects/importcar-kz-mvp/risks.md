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
- **Production WhatsApp env required**: WhatsApp CTAs now read `VITE_WHATSAPP_PHONE`; production deploy must set it in Vercel before real traffic.
- **Production migration required**: `supabase/migrations/20260521_calculator_leads_metadata.sql` exists, but must be run in Supabase dashboard before calculator leads are used in production.

## Mitigated / reduced risks
- Anonymous lead select/update access is not exposed in public schema.
- Admin status updates are read-only in UI until authenticated access exists.
- Former dead buttons now open real inline mock content.
- Proof-case purchase price is data-driven.
- Phone validation exists before submit.
- Smoke tests exist as a repeatable verification path (`npm run smoke:test`).
- WhatsApp placeholder number was removed from source components and replaced with env-based config.
- Desktop top nav exists, so calculator/catalog/favorites/request tabs are reachable on desktop.
