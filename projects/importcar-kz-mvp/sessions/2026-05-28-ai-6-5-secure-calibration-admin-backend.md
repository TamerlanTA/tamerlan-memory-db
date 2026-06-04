# Session 2026-05-28 — AI-6.5 Secure Calibration Admin Backend

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented AI-6.5 secure backend path for calibration saves without weakening RLS.
- Added Supabase Edge Function `supabase/functions/admin-calibrations/` with actions `create`, `update`, and `getByLeadId`.
- Added server-side validation for UUID-like ids, positive numeric totals, allowed reason categories, allowed calibration statuses, and JSON payload shape.
- Edge Function computes `difference_kzt` and `difference_percent` server-side and writes with `SUPABASE_SERVICE_ROLE_KEY`.
- Added temporary internal `ADMIN_API_KEY` / `x-admin-key` protection.
- Updated frontend calibration service to call `admin-calibrations` instead of direct `calculation_calibrations` table writes.
- AdminLeads now loads existing calibration by `lead_id` and saves/updates via Edge Function.
- Lazy-loaded AdminLeads in `App.tsx`, creating a separate admin chunk and removing the main chunk warning.
- Updated `.env.example`, calibration docs, production activation checklist, Vercel preview checklist, and roadmap.
- Added `npm run admin:calibration`.

## Key findings
- RLS remains strict; no public calibration policies were added.
- Service role is used only inside the Edge Function.
- `VITE_ADMIN_API_KEY` is temporary internal protection and must not be enabled in public production.
- Build main JS dropped to about 494.75 kB; admin chunk is about 11.01 kB.

## Blockers
- Need to run the calibration migration in Supabase.
- Need to deploy `admin-calibrations` and set Edge Function secrets before live admin calibration saves work.
- Final production-grade admin auth still needs Supabase Auth plus admin roles.

## Next steps
- Run `supabase/migrations/20260528_accuracy_calibration.sql`.
- Deploy `supabase functions deploy admin-calibrations`.
- Set Supabase Edge Function secrets: `ADMIN_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`.
- Set matching `VITE_ADMIN_API_KEY` only in protected internal preview/admin Vercel environment.
