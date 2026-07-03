# Session 2026-07-01 — Diagnostics, Stale Runs, and Config Cleanup

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Removed active IP/user-agent/language guest-trial claim enforcement at user request.
- Restored guest free-trial behavior to cookie/session scope with existing guest-session lock and atomic DB commit after result storage.
- Added `generationRuns` diagnostic columns for stage, attempt, pipeline, upstream status/code, normalized error code, validator status/reason, reference count, input image count, and input bytes.
- Updated generator/router code to persist diagnostics on success and failure.
- Added stale run cleanup for `generationRuns.status = started` rows older than 45 minutes.
- Manually cleaned production stale rows: 5 old `started` rows marked failed; stale count is now 0.
- Added a Recent Generation Diagnostics table to `/admin/stats`.
- Hardened Umami script loading so invalid endpoints such as `/analytics.local` are skipped.
- Changed missing `OAUTH_SERVER_URL` logging from production error noise to a legacy-OAuth-disabled warning.
- Applied production DB diagnostic-column migration and deployed `cf2a318` to Vercel production.

## Key findings
- Live bundle still contains Clerk `pk_test`; production Clerk live keys are not yet configured.
- Live bundle still contains the baked `/analytics.local` env string, but the new invalid-URL guard is present, so the broken script should not be injected.
- Sentry/log drain cannot be enabled from this local environment without dashboard credentials/tokens.

## Blockers
- Real production smoke matrix needs a physical mobile Safari device and a paid/authenticated account for final Taffeta.
- GitHub push remains blocked by local HTTPS credential configuration; branch is ahead of origin by 7 commits.

## Verification
- Focused tests PASS: `server/labelGenerationCreditSafety.test.ts`, `server/nanoBananaService.pipeline.test.ts`, `client/src/domain/generationErrorPresentation.test.ts`.
- `node_modules/.bin/tsc --noEmit` PASS.
- Full `node_modules/.bin/vitest run` PASS (41 files, 246 tests).
- `npm run build` PASS.
- Production DB: diagnostic column count 11; stale started older than 45 minutes count 0.
- Production deploy `dpl_EGnB38QHeVPuB4beME4k5ck7KUM6` READY and aliased to `https://methode.griffesvivienne.com`.

## Next steps
- Run real production smoke matrix and inspect diagnostics/logs after each generation.
- Replace Clerk test keys with live keys and redeploy.
- Remove stale Umami env value from Vercel Production if Umami is not being used.
- Configure Sentry/log drain.
