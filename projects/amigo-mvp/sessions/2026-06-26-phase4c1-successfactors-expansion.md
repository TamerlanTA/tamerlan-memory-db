# Session 2026-06-26 — Phase 4C.1 SuccessFactors Expansion

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[technical-architecture]]

## What was done
- Inspected `data/employer-catalog.seed.csv`, production `career_sources`, importer behavior, and `successfactors-v1`.
- Verified current non-Kerzner seed sources are not safe to switch to `successfactors-v1` without separate connector work.
- Diagnosed original One&Only umbrella endpoint `https://jobs.kerzner.com/go/OneOnly/4167422/` as a SuccessFactors error-page redirect under read-only search parameters.
- Added six verified One&Only property-level SuccessFactors sources:
  - One&Only The Palm;
  - One&Only Aesthesis;
  - One&Only Kea Island;
  - One&Only Palmilla;
  - One&Only Mandarina;
  - One&Only Moonlight Basin.
- Updated `successfactors-v1` to preserve explicit endpoint `q` query parameters.
- Added regression coverage for explicit SuccessFactors keyword queries.
- Updated `docs/vacancy-discovery-runbook.md`.
- Imported the expanded seed into production twice; importer remained idempotent by endpoint and production now has 31 employers/sources.
- Ran manual production discovery for `successfactors-v1` multiple times after rebuilding `@amigo/vacancy-discovery`.
- Found production `/source_health` timed out after catalog expansion because the deployed bot-api still uses the older sequential per-source query implementation.
- Replaced local bot-api source-health implementation with the optimized `PostgresVacancyDiscoveryStore.getSourceHealthSummary()` path and revalidated locally.

## Key findings
- Production `successfactors-v1` now has 9 configured sources.
- Latest manual connector run:
  - 8 sources succeeded;
  - original One&Only Resorts umbrella failed safely as `empty_result`;
  - no source run is stuck in `running`;
  - errors remain classified.
- Latest source health:
  - configured sources: 9;
  - succeeded last run: 8;
  - failed last run: 1;
  - active vacancies: 96;
  - stale vacancies: 82.
- DB invariants:
  - total vacancies: 178;
  - distinct dedupe keys: 178;
  - duplicate dedupe keys: 0;
  - active vacancies: 96;
  - running source runs: 0.
- Active `apply_url` overlap remains between the broad Kerzner source and property-level One&Only sources. This is not a `dedupe_key` violation because Phase 4 dedupe is source-scoped, but it must be resolved before Phase 5 batches.

## Blockers
- Railway CLI auth expired again. Browserless login code `JXNB-CKFQ` was generated but not completed, so `bot-api` and `worker-vacancy-discovery` were not redeployed.
- A later rollout retry generated browserless login code `QTFD-RKVC`, but authentication was still not completed. `railway status` remains unauthorized and no deployment was performed.
- Phase 4C.1 should not be marked fully production-accepted until bot-api `/source_health` and worker scheduled discovery are redeployed and verified in Railway.

## Next steps
- Refresh Railway auth and deploy `bot-api` plus `worker-vacancy-discovery`.
- Verify production `/source_health` returns HTTP 200 after `bot-api` deploy.
- Verify Railway scheduled run after worker deploy for all 9 SuccessFactors sources.
- Decide whether to disable broad Kerzner before Phase 5 or add a cross-source vacancy identity model.
- Keep One&Only umbrella endpoint visible as `empty_result` until a stable umbrella URL is found.
