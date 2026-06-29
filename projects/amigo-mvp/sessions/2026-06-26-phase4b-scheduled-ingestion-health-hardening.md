# Session 2026-06-26 — Phase 4B Scheduled Ingestion and Health Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]
- [[technical-architecture]]

## What was done
- Added scheduled discovery logic to `@amigo/vacancy-discovery` using `career_sources.polling_schedule`.
- Added CLI modes:
  - `--scheduled [connector-id]`;
  - `--daemon [connector-id]`.
- Added `apps/worker-vacancy-discovery` and `Dockerfile.worker-vacancy-discovery` for Railway scheduled ingestion service.
- Added overlap protection: unfinished `running` source runs block duplicate runs for the same source.
- Added error taxonomy in `source_runs.metadata.errorCategory`.
- Improved CLI and Telegram source health summaries with connector totals, last success/failure, discovered/upserted counts, active/stale counts, and latest error category/message.
- Added `docs/vacancy-discovery-runbook.md`.

## Key findings
- Manual Kerzner single-source discovery still works and remains idempotent.
- Connector-level `successfactors-v1` run processed three seeded sources independently:
  - Atlantis Dubai succeeded with 3 discovered/upserted vacancies;
  - Kerzner succeeded with 15 discovered/upserted vacancies;
  - One&Only failed safely as `empty_result`.
- Scheduled one-shot after the connector-level run found 0 due sources, confirming polling-schedule gate.
- Production DB verification: `vacancies=18`, `distinct_dedupe=18`, `active=18`, `stale=0`.
- Source run verification: 5 succeeded, 1 old unclassified failed run from the fixed Date serialization bug, 1 classified `empty_result` failed run.

## Blockers
- `/source_health` is ready in code but not deployed to Railway yet.
- `worker-vacancy-discovery` service is ready in code but not deployed/provisioned on Railway yet.
- One&Only endpoint returns no parseable rows through the generic SuccessFactors search parser.
- Phase 5 scoring/batches and Phase 6 application adapters remain unbuilt.

## Next steps
- Deploy `bot-api` with `railway up --service bot-api` to activate `/source_health`.
- Create/deploy `worker-vacancy-discovery` Railway service if continuous scheduled ingestion should begin.
- Investigate whether One&Only needs a source-specific URL/query or should stay disabled/health-failed.
- Start Phase 5 hard filters, weighted scoring, explanation records, and daily manager approval batches.
