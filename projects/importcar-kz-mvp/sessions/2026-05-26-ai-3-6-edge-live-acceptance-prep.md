# Session 2026-05-26 — AI-3.6 Edge Live Acceptance Prep

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Prepared AI-3.6 live acceptance materials for the Supabase Edge Function `analyze-car-link`.
- Added `docs/ai-edge-live-acceptance-runbook.md`.
- Added safe sample payloads under `docs/examples/ai-link-*.json`.
- Added `scripts/ai-edge-live-check.mjs` and `npm run ai:edge:live`.
- Updated `docs/ai-link-extraction-endpoint.md` to point to the live acceptance runbook and script.
- Verified no AI provider secrets are documented as frontend `VITE_` variables.

## Key findings
- Local Supabase CLI is not installed on this machine, so live deploy/runtime verification could not be executed here.
- The runbook follows current Supabase Edge Function docs: CLI login/link, `supabase secrets set`, `supabase functions deploy`, invoke with function URL plus public anon/publishable key headers.
- `npm run ai:edge:live -- --dry-run` works and does not print secrets.
- Local sanity scripts, lint, and build all pass.

## Blockers
- Manual Supabase CLI deploy and live runtime acceptance remain pending.
- Real AI provider behavior depends on valid Supabase Edge Function secrets and provider quota/availability.

## Next steps
- Run the manual commands in `docs/ai-edge-live-acceptance-runbook.md`.
- Confirm live `listingText`, URL-only, invalid input, and frontend link-mode tests pass.
- Start AI-4 only after live Edge acceptance passes.
