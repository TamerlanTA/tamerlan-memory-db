# Session 2026-07-01 — Ops Status And Shortage Diagnosis

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Added and deployed Telegram command `/ops_status` in `bot-api`.
- `/ops_status` returns one compact live operational summary: configured sources, active employers, connectors, active/total vacancies, distinct active apply URLs, vacancies first seen today, vacancies refreshed today, source runs today, running/stuck runs, connector breakdown, and latest failed sources.
- Wrapped `/source_health` and `/ops_status` with command-level error handling so a source-status failure replies to the manager instead of looking like a silent bot outage.
- Deployed `bot-api` on Railway; deployment `1f93effb-640e-4ec8-ae76-f39627f749c0` reached `SUCCESS`.
- Verified production `/health`: `status=ok`, `database=ok`.
- Verified Telegram webhook pending updates: `0`.

## Key findings
- Production vacancy catalog is not empty: at verification time it had 756 total vacancies, 386 active vacancies, 366 distinct active apply URLs, 130 new vacancies first seen today, and 470 refreshed today.
- Recent `0/10` batches are caused by hard-filter intersections, not by an empty catalog.
- For candidate `ac3f8e19-790b-44df-a91b-8fe547d749c5` (`официант`, target `Катар`), production had 0 active Qatar/Doha vacancies and 0 active Qatar/Doha waiter/server vacancies.
- For candidate `db0e2aff-89a8-4cd8-aea1-eaafa1f931f1` (`ресепшионист`, target `ОАЭ/Катар/Бахрейн`), production had 0 active Gulf receptionist/front-office matches.
- Large portion of active rows still have `location_country = null`, so location extraction improvements remain important before widening matching safely.

## Blockers
- No production-enabled auto-submit adapter exists yet; Phase 6 remains safe manual-action handoff.
- Current source coverage does not guarantee 5-10 daily eligible vacancies for narrow country+role pairs such as Qatar waiter or Gulf receptionist.
- Railway token shared in chat still must be rotated.

## Next steps
- Use `/ops_status` and `/source_health` together during daily operations: `/ops_status` for compact totals, `/source_health` for detailed source diagnostics.
- Expand or fix sources that cover Qatar/Bahrain/front-office/waiter roles before expecting those candidates to get full batches.
- Improve location extraction for generic/best-effort sources so rows with null country can become safely matchable.
- Continue toward a certified production auto-submit path only through narrow, explicitly enabled adapters.
