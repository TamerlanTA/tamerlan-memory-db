# ImportCar.kz MVP

## Related
- [[current-focus]]

## Current status
- 2026-05-15: Created first standalone React + TypeScript MVP in `~/Desktop/importcar-kz-mvp`.
- 2026-05-15: Upgraded MVP into a more product-like v2 with a dedicated detail state, richer listings, sticky mobile CTA, stronger importer comparison cards, and lead modal flow.
- 2026-05-15: Added trust polish layer: car verification badges, stronger detail hero pricing, FAQ, importer support credentials, pricing disclaimer, and safer lead-request copy.
- 2026-05-15: Added proof layer inside car detail: recent import case study, auction sheet preview, and verification-progress checklist.
- 2026-05-15: Added optional Supabase backend layer for lead persistence plus lightweight admin leads view and setup docs.
- 2026-05-15: Hardened public-test posture: added `.env.example`, seed SQL, removed anonymous lead read/update access, and gated admin UI behind `VITE_ENABLE_ADMIN_VIEW=true`.
- 2026-05-15: Replaced ad-hoc mock pricing with a configurable Kazakhstan import estimate engine and aligned all UI totals to the new calculator output.
- 2026-05-15: Upgraded calculator config into a versioned pricing-rules engine with active/default rule selection and draft support.
- 2026-05-15: Added calculator explainability with rule metadata, confidence levels, and a collapsible calculation explanation UI.
- 2026-05-15: Redesigned the home screen into a premium marketplace landing page and replaced random catalog data with curated Korea-focused demo listings.
- 2026-05-16: Replaced the mixed Korea catalog with a premium-only demo inventory (BMW, Mercedes-Benz, Porsche, Lexus, Audi), introduced model-safe luxury visual placeholders instead of risky mismatched photos, and shifted copy toward a premium import marketplace tone.
- Current UX flow: home → listing → car detail → importer comparison → request modal → success.

## Key decisions
- Keep Vite + React + TypeScript for MVP v1/v2 to stay lightweight and easy to extend.
- Keep frontend car/importer listings mocked while preparing database tables and seed data for the next phase.
- Use local state rather than routing/backend for most UI; Supabase is an optional persistence layer for leads.
- Make final Kazakhstan price the primary commercial signal in listings and detail hero; foreign/source price remains secondary context.
- Add explicit trust copy and proof artifacts before conversion points instead of relying on visuals alone.
- For public testing, allow anonymous lead insert only; require future authenticated admin roles for lead read/update access.
- Treat the import calculator as an estimate engine, not legal/tax advice; keep rates and customs placeholders configurable.
- Keep future draft pricing rules available for comparison without making them active by default.
- Expose calculation reasoning to users so low-confidence rules are visible instead of hidden.
- Treat catalog listings as demo/sample records inspired by public marketplace patterns, never as live offers.

## Blockers / risks
- Current car visuals are intentional model-safe placeholders; exact listing-linked or licensed production imagery is still needed before a real launch.
- Pricing logic and proof artifacts are still mock-only and should be validated against real Kazakhstan import rules and importer workflows before production use.
- Admin UI is intentionally only a hidden internal demo surface until authenticated admin access exists.
- Calculator customs formulas are placeholders and must be replaced with jurisdiction-validated rules before production use.

## Next steps
- Create/configure real Supabase project and apply `supabase/schema.sql` plus `supabase/seed.sql` if desired.
- Validate pricing rules and confidence levels against real Kazakhstan regulations and importer quotes.
- Replace model-safe placeholders with exact listing-linked or licensed car-specific assets once trustworthy media sourcing is available.
- Add auth/role protection around admin leads before any real operations.

## 2026-05-16 update
- Premium-only catalog now uses manually curated Korean marketplace-style sample data and keeps all final KZT prices inside the pricing engine.
- Exact remote listing photos were intentionally not used because a one-to-one trustworthy match could not be guaranteed from the available public context; premium placeholders are the safer MVP choice.
- 2026-05-16: Production deployment refreshed on Vercel after premium catalog redesign; live alias remains `https://importcar-kz-mvp.vercel.app`.
- 2026-05-16: Repositioned the frontend from premium marketplace into cinematic private-showroom styling without changing the product flow: dark luxury hero, softer emerald accent, glass search panel, elevated inventory cards, floating detail summary, concierge-oriented importer copy, and subtle motion.
- 2026-05-16: Ran final release checks (`npm run lint`, `npm run build`), redeployed production on Vercel, and smoke-tested desktop/mobile flow locally through listing → detail → importer comparison → lead modal with no console/page errors observed.
- 2026-05-16: Closed supervisor-audit issues before demo: admin statuses are read-only pending authenticated admin access, proof case pricing now uses typed KRW data, importer and auction-sheet detail buttons now expand real mock content, lead form has phone validation, Korea-only filters show a polished empty state, and Playwright smoke testing is now a documented project dependency.
- 2026-05-16: Production deployment refreshed after supervisor-audit fixes; live alias remains `https://importcar-kz-mvp.vercel.app`.
