# Session 2026-06-27 — Phase 4C.1 Production Acceptance

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Completed Phase 4C.1 production rollout after Railway token auth was restored for project `amigo-mvp`, environment `production`.
- Redeployed `bot-api`; final successful deployment ID: `adc456b8-11cd-464c-872f-61f2d4e8a5d4`.
- Fixed a production-only `/source_health` runtime bug by sending the health summary as plain text instead of Telegram Markdown, because `empty_result` caused a Telegram entity parse error.
- Redeployed `worker-vacancy-discovery`; successful deployment ID: `db58da6e-101e-4163-a8f3-7a61242e1057`.
- Confirmed worker env: `RAILWAY_DOCKERFILE_PATH=Dockerfile.worker-vacancy-discovery`, `VACANCY_DISCOVERY_CONNECTORS=successfactors-v1`, `VACANCY_DISCOVERY_INTERVAL_MS=300000`.
- Verified `/source_health` through production webhook simulation: HTTP 200 in about 3.3 seconds, no timeout.

## Key findings
- Railway status confirmed workspace `tamerlanta's Projects`, project `amigo-mvp`, environment `production`; both `bot-api` and `worker-vacancy-discovery` are Online.
- Worker logs show daemon startup and scheduled checks: `connectorIds=["successfactors-v1"]`, `intervalMs=300000`, `checkedSourceCount=9`, `dueSourceCount=0`.
- `dueSourceCount=0` is expected immediately after recent manual connector verification; DB rows show the expanded 9-source SuccessFactors family has already run.
- Production DB verification:
  - `successfactors-v1` sources: 9;
  - vacancies: 178 total / 178 distinct `dedupe_key`;
  - duplicate dedupe groups: 0;
  - stuck `source_runs.status = running`: 0;
  - freshness: 96 active / 82 stale;
  - latest source health: 8 succeeded, 1 failed as classified `empty_result`.
- Latest successful sources: Atlantis Dubai, Kerzner International, One&Only Aesthesis, Kea Island, Mandarina, Moonlight Basin, Palmilla, and The Palm.
- The original One&Only umbrella source remains a visible classified `empty_result` health issue and does not block other sources.

## Blockers
- No Phase 4C.1 production blocker remains.
- Residual product risk remains: broad Kerzner and property-level sources can overlap by `apply_url` because current vacancy identity is source-scoped.

## Next steps
- Proceed to Phase 5 only after deciding how to handle cross-source vacancy identity for manager-facing batches.
- Keep monitoring `/source_health` and worker scheduled runs as source count grows.
- Keep One&Only umbrella endpoint visible as `empty_result` until a stable public umbrella URL is found.
