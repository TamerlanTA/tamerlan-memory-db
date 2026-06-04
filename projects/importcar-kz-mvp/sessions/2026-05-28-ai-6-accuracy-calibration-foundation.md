# Session 2026-05-28 — AI-6 Accuracy Calibration Foundation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented AI-6 foundation for collecting estimate-vs-manager/final cost data.
- Added `supabase/migrations/20260528_accuracy_calibration.sql` with `calculation_calibrations`, status/reason constraints, timestamps, lead reference, and RLS enabled.
- Kept calibration table closed to public anon/authenticated access; granted service-role access only.
- Added `src/domain/calibration/` with difference helper and reusable calibration types.
- Added `src/services/calibrations.ts` with create/update/get helpers and controlled errors for missing migration, missing Supabase config, and RLS/access denial.
- Extended AdminLeads with a compact calibration panel for calculator leads: verified/final totals, reason category/text, actual logistics/customs/service fee, exchange rate, notes, and immediate difference/target feedback.
- Added `docs/accuracy-calibration.md`, roadmap notes, and `npm run calibration:sanity`.

## Key findings
- Pricing logic remains unchanged; manager/final totals are stored separately for calibration.
- Because the project currently has feature-flag admin without real auth, safe production writes need a secure admin access path before enabling real browser-side calibration saves.
- Build passes, but main JS is now about 504.64 kB and Vite emits a chunk-size warning.

## Blockers
- Migration must be run manually in Supabase.
- Secure admin write path must be decided before relying on calibration saves in production.

## Next steps
- Run `supabase/migrations/20260528_accuracy_calibration.sql`.
- Decide authenticated admin policies vs secure backend/service-role endpoint for calibration writes.
- Consider lazy-loading AdminLeads/calibration code to remove the Vite chunk warning.
