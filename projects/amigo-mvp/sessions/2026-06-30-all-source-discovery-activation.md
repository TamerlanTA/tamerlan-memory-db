# Session 2026-06-30 — All Source Discovery Activation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Activated all seeded vacancy discovery connector ids in code and production worker env: `successfactors-v1`, `workday-v1`, `marriott-careers-v1`, `accor-careers-v1`, `oracle-cx-v1`, `taleo-v1`, `ihg-careers-v1`, `generic-careers-v1`.
- Added a structured Marriott parser for `window.__PRELOAD_STATE__` job data.
- Added a best-effort HTML link parser for remaining non-certified sources so every catalog source is now checked and health-tracked.
- Registered all connectors in `@amigo/vacancy-discovery`.
- Added regression tests for Marriott parsing and generic HTML job-link extraction.
- Ran production manual discovery for the newly activated connectors.
- Updated Railway `worker-vacancy-discovery` env and deployed production deployment `37579492-ebd8-4401-b8ba-53059d2d7080`.

## Key findings
- Worker logs confirm all connector ids are loaded and `checkedSourceCount=31`, replacing the earlier `checkedSourceCount=10`.
- Production vacancy totals after activation: 533 total rows, 388 active, 145 stale, 399 distinct apply URLs.
- New active vacancy contribution by connector:
  - Marriott: 10 active.
  - Accor: 87 active.
  - Oracle CX/Hilton: 20 active.
  - Taleo/Hyatt: 2 active.
  - Generic pages: 69 active.
  - Workday/Four Seasons remains 100 active.
  - SuccessFactors remains 100 active and 145 stale historical rows.
- Validation passed locally with build-first order: `CI=true pnpm build`, `CI=true pnpm check`, `CI=true pnpm test`, `CI=true pnpm format:check`.

## Blockers
- Some sources are now active in health but not successfully ingesting:
  - Rixos/Accor endpoint returns HTTP 404.
  - Jumeirah Oracle CX returns `empty_result` with the current fallback parser.
  - IHG and Six Senses IHG endpoints fail from production with network errors.
  - Several generic sources return 403/410 or empty result.
- Best-effort generic rows often lack structured city/country, so matching hard filters may reject them until location extraction is improved.

## Next steps
- Keep Phase 6 as the main product next step: convert approved batch items into application jobs with duplicate prevention and evidence.
- In parallel, harden newly active discovery sources with dedicated parsers/APIs and better location extraction.
- Continue using `/source_health` to monitor failed sources now that all 31 sources are scheduled.
