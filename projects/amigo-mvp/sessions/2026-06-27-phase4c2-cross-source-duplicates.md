# Session 2026-06-27 — Phase 4C.2 Cross-Source Duplicates

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented Phase 4C.2 as a read-only cross-source vacancy duplicate detector in `@amigo/vacancy-discovery`.
- Added canonical duplicate identity using canonical `apply_url` first; fallback is external id plus normalized title, employer, and location facts.
- Preserved existing source-scoped `vacancies.dedupe_key`; no migration, destructive merge, delete, or vacancy row rewrite was introduced.
- Added CLI command: `pnpm tsx scripts/discover-vacancies.ts --duplicates successfactors-v1`.
- Updated `docs/vacancy-discovery-runbook.md` with duplicate policy and command.

## Key findings
- Production duplicate report found 10 active cross-source duplicate groups / 20 rows.
- All current duplicate groups are `apply_url` overlaps between broad Kerzner and property-level sources.
- Repeated `successfactors-v1` discovery twice after implementation remained idempotent at the source-scoped level:
  - 180 vacancies;
  - 180 distinct `dedupe_key`;
  - 0 duplicate dedupe groups;
  - 0 stuck running `source_runs`;
  - latest health 8 succeeded / 1 `empty_result`.
- Source health after repeat runs: 9 configured sources, 98 active vacancies, 82 stale vacancies.

## Validation
- `CI=true pnpm --filter @amigo/vacancy-discovery test` passed: 20 package tests.
- `CI=true pnpm --filter @amigo/vacancy-discovery check` passed.
- `CI=true pnpm --filter @amigo/vacancy-discovery build` passed.
- `CI=true pnpm check` passed.
- `CI=true pnpm test` passed: 124 tests.
- `CI=true pnpm build` passed.
- `CI=true pnpm format:check` passed.

## Blockers
- No Phase 4C.2 implementation blocker remains.
- Phase 5 still must consume the duplicate report as a suppression guard before manager-facing vacancy batches.

## Next steps
- In Phase 5, suppress duplicate vacancies by canonical duplicate group before scoring/batch presentation.
- Keep One&Only umbrella source classified as `empty_result` until a stable public umbrella endpoint is found.
