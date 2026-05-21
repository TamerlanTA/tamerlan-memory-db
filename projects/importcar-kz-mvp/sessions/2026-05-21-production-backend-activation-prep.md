# Session 2026-05-21 — Production Backend Activation Prep

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Implemented Phase 3A production activation prep.
- Added dedicated Supabase migration:
  - `supabase/migrations/20260521_calculator_leads_metadata.sql`
  - makes `leads.car_id` and `leads.importer_id` nullable
  - adds `metadata jsonb`
  - adds `source text`
  - adds comments; no RLS weakening and no public read policy
- Reviewed `supabase/schema.sql` RLS posture:
  - anonymous insert into `leads` preserved
  - no anonymous select/update/delete for `leads`
  - cars/importers remain public read
  - service_role grants preserved
- Added env-based WhatsApp helper:
  - `src/config/contact.ts`
  - reads `VITE_WHATSAPP_PHONE`
  - supports `VITE_WHATSAPP_DEFAULT_MESSAGE`
  - no hardcoded placeholder number remains in source components
- Updated WhatsApp CTAs in:
  - `StickyCta.tsx`
  - `CalculatorScreen.tsx`
  - `RequestScreen.tsx`
  - `ProfileScreen.tsx`
- Updated lead payloads:
  - calculator leads now insert top-level `source: 'calculator'`
  - catalog leads now insert `source: 'catalog'`
  - calculator metadata remains JSON-serializable with numeric totals
- Updated `.env.example` and README env docs.
- Added `docs/production-activation-checklist.md`.

## Key findings
- RLS is already safe for public lead capture: anon can insert leads but cannot read leads.
- Admin view remains an internal/demo surface until authenticated admin access exists.
- Manual Supabase migration is still required in the production dashboard before real calculator lead use.

## Verification
- `rg` confirmed no `77071234567` placeholder remains in source/docs/env example.
- `npm run lint` — passed.
- `npm run build` — passed, output JS bundle about 469.75 kB.
- `npm run smoke:test` — passed against local Vite server.

## Blockers
- Production Supabase migration must still be run manually.
- `VITE_WHATSAPP_PHONE` must be set in Vercel before real traffic.
- Real iPhone test still pending after deploy.

## Next steps
- Run the migration in Supabase dashboard.
- Set production env vars in Vercel.
- Deploy and complete checklist in `docs/production-activation-checklist.md`.
