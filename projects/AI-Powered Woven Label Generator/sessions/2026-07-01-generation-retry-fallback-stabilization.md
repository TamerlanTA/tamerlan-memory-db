# Session 2026-07-01 — Generation Retry Fallback Stabilization

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented the first two reliability batches from the root-cause plan.
- Updated `server/nanoBananaService.ts` to salvage and return the previous generated image if a later validator-driven retry generation fails.
- Applied the salvage behavior to both single-pass generation and HD Cotton motif refinement.
- Reduced provider request complexity by capping reference images to 3, using 1 reference on single-pass retry, and using no extra material references on HD Cotton motif retry.
- Added attempt-level reference-count logging and retry-fallback diagnostics.
- Added regression coverage for the production failure mode: first image exists, woven validation fails, retry generation throws `INVALID_ARGUMENT`, customer still receives the first image.

## Key findings
- The previous no-result failure mode is now covered by tests and production-deployed.
- Reference counts in logs now confirm initial requests are capped and retry requests are lighter.
- The fix intentionally keeps validator warnings visible in logs while prioritizing customer result delivery.

## Validation
- `node_modules/.bin/vitest run server/nanoBananaService.pipeline.test.ts` PASS: 11 tests.
- `node_modules/.bin/vitest run` PASS: 41 files, 246 tests.
- `node_modules/.bin/tsc --noEmit` PASS.
- `npm run build` PASS with the existing large chunk warning.
- Vercel Production deployment `dpl_64beaG6APr3XdPmTf44QB2RAt3UC` READY and aliased to `https://methode.griffesvivienne.com`.
- Live domain returned HTTP 200 after deploy.

## Blockers
- GitHub push remains blocked by local HTTPS credentials; local branch is ahead of origin by 5 commits.
- Sentry remains unavailable locally without `SENTRY_AUTH_TOKEN`.

## Next steps
- Run real production smoke matrix: mobile Safari HD, mobile Safari Taffeta, desktop HD, paid final Taffeta, and retry-warning log watch.
- Persist richer structured generation diagnostics in DB/admin.
- Add stale `started` run cleanup.
- Clean production config noise: Clerk live keys, Umami endpoint, `OAUTH_SERVER_URL`, and Sentry/log-drain access.
