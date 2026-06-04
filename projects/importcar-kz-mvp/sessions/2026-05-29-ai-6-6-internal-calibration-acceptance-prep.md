# Session 2026-05-29 — AI-6.6 Internal Calibration Acceptance Prep

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Prepared internal acceptance flow for secure calibration saves through `admin-calibrations`.
- Added `docs/internal-calibration-acceptance-checklist.md`.
- Added `scripts/admin-calibration-live-check.mjs` and package script `npm run admin:calibration:live`.
- Live-check supports `--dry-run` and live synthetic create using `ADMIN_CALIBRATIONS_FUNCTION_URL` and `ADMIN_API_KEY`.
- Script prints only safe response summaries: HTTP status, ok, error code, row id, status, reason category, and computed difference values.

## Key findings
- Current backend contract already keeps service role server-side and RLS strict.
- Acceptance still requires manual Supabase deployment and secrets before live script can create a row.
- Build remains split: AdminLeads is a separate lazy chunk and no Vite chunk warning appears.

## Blockers
- Live acceptance not run yet because deployed endpoint/admin key were not provided in local env.

## Next steps
- Run `supabase/migrations/20260528_accuracy_calibration.sql`.
- Deploy `supabase functions deploy admin-calibrations`.
- Set `ADMIN_API_KEY` and `SUPABASE_SERVICE_ROLE_KEY` in Supabase Edge Function secrets.
- Run `ADMIN_CALIBRATIONS_FUNCTION_URL=... ADMIN_API_KEY=... npm run admin:calibration:live`.
- Test AdminLeads save in protected internal preview with matching `VITE_ADMIN_API_KEY`.
