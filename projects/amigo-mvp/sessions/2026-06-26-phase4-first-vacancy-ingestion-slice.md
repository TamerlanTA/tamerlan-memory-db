# Session 2026-06-26 — Phase 4 First Vacancy Ingestion Slice

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]
- [[technical-architecture]]

## What was done
- Implemented `@amigo/vacancy-discovery` package with connector abstraction, normalization, idempotent vacancy upsert, source run lifecycle, stale marking, and source health summary.
- Chose Kerzner / `successfactors-v1` as the first connector because the public search page exposes server-rendered read-only job rows without login, CAPTCHA, OTP, or application submission.
- Added `scripts/discover-vacancies.ts` CLI for one source, all sources by connector, and source health summary.
- Added Telegram `/source_health` command that reads latest source run health without starting ingestion.
- Updated Dockerfiles so the new workspace package is available during frozen-lockfile installs.
- Ran production discovery twice for `https://jobs.kerzner.com/`.

## Key findings
- Initial live run failed safely and recorded a `failed` `source_runs` row because raw postgres Date params needed ISO serialization.
- After the fix, two production runs succeeded:
  - 15 discovered/upserted Kerzner vacancies per run;
  - 15 total Kerzner vacancy rows;
  - 15 distinct `dedupe_key` values;
  - `first_seen_at` preserved across repeated run;
  - `last_seen_at` updated on repeated run;
  - sampled rows are `freshness_status = active`.
- `/source_health` summary now shows three configured SuccessFactors sources: Kerzner succeeded, Atlantis Dubai and One&Only never run.

## Blockers
- No scheduled ingestion worker yet; ingestion is manual CLI-driven.
- Only Kerzner base source has been live-verified.
- Application adapters remain unbuilt and uncertified.
- Phase 5 scoring/batch approval is not started.

## Next steps
- Run/certify Atlantis Dubai and One&Only SuccessFactors sources.
- Add error classification beyond raw error text.
- Implement Phase 5 hard filters, weighted scoring, explanation records, and daily manager batch generation.
- Decide whether manual CLI ingestion is enough for pilot or whether to add a scheduled worker.
