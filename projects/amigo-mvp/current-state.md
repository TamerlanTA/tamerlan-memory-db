# AMIGO MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[roadmap]]
- [[technical-architecture]]

## Status
- Project status: Active
- Health: Yellow
- Priority: P0
- Planning window: 2026-06-12 to 2026-07-05
- Launch target: controlled pilot for 10 candidates
- Post-launch target: 30 active candidates
- Current phase: Phase 5 matching and approval production deployed; Telegram UI manual click-through remains useful before manager rollout
- Working mode: two-person execution — Tamerlan owns business decisions, access, credentials, and approvals; Codex owns technical implementation, validation, and memory synchronization.

## What is complete
- Product workflow and MVP boundaries are defined.
- Target market is restricted to international hospitality.
- Manager-led Telegram intake and batch approval are confirmed.
- Algorithm-first search, matching, and application logic are confirmed.
- LLM use is restricted to document translation and preparation.
- Initial technical architecture, data model, connector strategy, and delivery roadmap are documented.
- Private repository created and pushed: `https://github.com/TamerlanTA/amigo-mvp`, local path `/Users/tamerlan/Documents/amigo-mvp`.
- TypeScript/pnpm monorepo, CI, typed environment contracts, redacting logs, Fastify/grammY API, and PGMQ foundation worker are implemented.
- Supabase project `amigo-mvp` (`ibebnmlwjjkibfwdnffr`, Frankfurt) is provisioned and the first migration is applied.
- Railway project `amigo-mvp` has successful production deployments for `bot-api` and `worker-foundation`.
- Production health endpoint is live at `https://bot-api-production-e076.up.railway.app/health`.
- Telegram bot `@amigomvpbot` has an authenticated production webhook and manager allowlist for Telegram ID `405182031`.
- Transactional queue processing was verified in production: one job produced one audit event and queue depth returned to zero.
- Draft Russian candidate consent and an ATS-friendly English hospitality CV template were created.

## What is complete (Phase 2 extended — as of 2026-06-16, commit d1bf79d)
- `/candidate_new` — 25-field form, consent flow, atomic DB transaction
- `/candidate_find`, `/candidate_view`, `/candidate_edit` (25 fields), `/candidate_close`, `/cancel`
- 25 fields: name, email, phone, age, gender, race, nationality, location, target countries/roles, English level (categorical нулевой/низкий/средний/высокий), additional languages (CEFR+native), education year, height, weight, 9 boolean experience flags
- `checkCompleteness()` requires: name, email, phone, age, nationality, location, target countries, target roles, English level, consent
- Migration `202606160001_candidate_extended_profile.sql` applied to Supabase production
- 34 tests passing, deployed on Railway
- Webhook issue fix pattern: after `railway up`, run deleteWebhook+setWebhook to avoid Telegram IP cache timeout

## What is complete (Phase 3 foundation — as of 2026-06-16)
- Phase 2 review remediation is complete in commit `e5ad6e4`.
- Supabase migration `202606160002_document_pipeline.sql` is applied in production.
- Added document tables: `document_templates`, `document_versions`, `generation_runs`.
- Added private Supabase Storage bucket `candidate-documents`.
- Added PGMQ queue `document_generate`.
- Added `worker-documents` service:
  - reads `document_generate`;
  - checks candidate completeness and consent before generation;
  - calls OpenAI Responses structured output unless `OPENAI_DOCUMENT_MODEL=deterministic`;
  - renders DOCX from `hospitality-cv-en-v1.docx`;
  - renders PDF through Gotenberg;
  - uploads DOCX/PDF to private Supabase Storage;
  - records generation run, document version, and audit event.
- Added Railway `gotenberg` service from `gotenberg/gotenberg:8`.
- Added Telegram `/candidate_documents` flow:
  - candidate selection;
  - completeness blocking;
  - enqueue document generation;
  - signed PDF link for pending approval;
  - approve/reject callbacks with manager ownership checks.
- Deployed `bot-api`, `worker-documents`, and `gotenberg` successfully on Railway.
- Telegram webhook was refreshed after `bot-api` deploy; pending updates were 0.
- Local verification passed: TypeScript check, 37 tests, build, and Prettier.
- First real document-generation bug was fixed: Docxtemplater did not resolve dot-path tags like `{candidate.full_name}`, producing `undefined` in the generated CV. Added a dot-path parser, regression test, redeployed `worker-documents`, regenerated the candidate CV, and verified PDF text extraction contains candidate data.
- CV quality upgrade completed in commit `a11145b`: the hospitality CV template now follows a warmer reference-style structure, adds a human summary/profile line, translates Russian role/country inputs, transliterates Cyrillic name/city values for English CV output, and removes visible internal placeholder phrases such as `pending manager enrichment`.
- Controlled candidate `ac3f8e19-790b-44df-a91b-8fe547d749c5` was regenerated after deployment. Latest document version `9219995e-fed0-407c-a27f-f5ee3493cd71` is `pending_approval`, has no validation errors, and PDF text extraction verifies `Tamerlan Tog`, `Waiter`, `Almaty, Kazakhstan`, and no old placeholder text.
- Phase 3 end-to-end approval was confirmed on 2026-06-22: document version `9219995e-fed0-407c-a27f-f5ee3493cd71` was approved in Telegram, `document_versions.status` became `approved`, and candidate status became `documents`.
- Partner-approved CV correction completed on 2026-06-22:
  - photo placeholder added to the DOCX template;
  - About Me moved below candidate header;
  - `Hospitality Strengths`, inferred skills, and pseudo-experience removed;
  - EXPERIENCE section now uses only stored `work_experience` facts or a neutral no-experience note;
  - OpenAI schema/prompt now uses `header`, `photo`, `about_me`, `personal_info`, `experience[]`, `education[]`, `languages[]`, `other[]` with source mappings;
  - grounding strips unsupported experience/other and normalizes unsafe About Me output.
- Production sample CV version `c20ddaa5-15a7-4aa9-9314-8db68adec1ab` was generated after the correction. PDF text and PNG visual verification passed: `PHOTO REQUIRED` appears, About Me is below header, no Hospitality Strengths, EXPERIENCE is exact, no fake experience, and no unsupported Other section.

## What is complete (Phase 4 catalog foundation — as of 2026-06-22)
- Added Supabase migration `202606220001_employer_catalog_sources.sql`.
- Extended `career_sources` with `tenant_identifier`, `discovery_connector`, `application_adapter`, `polling_schedule`, and `updated_at`; added `employers.updated_at`.
- Added idempotent importer `scripts/import-employer-catalog.ts`.
- Added seed file `data/employer-catalog.seed.csv` with 25 target hospitality employers / career sources.
- Applied migration to Supabase production and imported the seed catalog.
- Production verification: 25 `employers`, 25 `career_sources`, and 25 distinct endpoints.
- Commit `91bc7b0` pushed to `main`.
- Added normalized vacancy discovery schema in commit `b1f1411`:
  - `source_runs` for connector execution logs;
  - `vacancies` with `dedupe_key`, source/apply URLs, title, employer, location, freshness status, timestamps, and raw payload.
- Applied migration `202606220002_vacancy_discovery_foundation.sql` to Supabase production; verification showed `source_runs=0`, `vacancies=0`, `career_sources=25`.

## What is complete (Phase 4 first vacancy ingestion slice — as of 2026-06-26)
- Added isolated package `@amigo/vacancy-discovery` with connector abstraction, SuccessFactors read-only connector, normalization, idempotent `vacancies.dedupe_key` upsert, `source_runs` lifecycle, stale marking, and source health summary.
- Added CLI `scripts/discover-vacancies.ts`:
  - `--source <source-id-or-endpoint>`;
  - `--connector successfactors-v1`;
  - `--summary [connector-id]`.
- Added Telegram/admin summary command `/source_health` in `bot-api`; it reads configured sources and latest source runs without triggering ingestion.
- Chosen first live connector: `successfactors-v1` for Kerzner because `https://jobs.kerzner.com/search/` exposes server-rendered public search rows with title, department, facility, location, date, and apply URL.
- Production run results for Kerzner source `a751ef51-fabd-452e-b929-652b362df455`:
  - one initial failed `source_runs` row recorded a Date serialization bug without corrupting vacancies;
  - two subsequent successful runs discovered/upserted 15 rows each;
  - production has 15 Kerzner `vacancies` and 15 distinct `dedupe_key` values;
  - repeated run preserved `first_seen_at` and updated `last_seen_at`;
  - all sampled vacancies are `freshness_status = active`.
- Local validation passed: `pnpm check`, `pnpm test` (111 tests), `pnpm build`, and `pnpm format:check`.

## What is complete (Phase 4B scheduled ingestion and health hardening — as of 2026-06-26)
- Added scheduled discovery execution path in `@amigo/vacancy-discovery`:
  - due-source selection from `career_sources.polling_schedule`;
  - `--scheduled` CLI one-shot;
  - `--daemon` CLI loop;
  - dedicated `apps/worker-vacancy-discovery` service and `Dockerfile.worker-vacancy-discovery`.
- Added overlap protection: existing unfinished `source_runs.status = running` blocks a second run for the same source.
- Added connector error taxonomy in `source_runs.metadata.errorCategory`: `network_error`, `http_error`, `parse_error`, `empty_result`, `blocked_or_auth_required`, `rate_limited`, `unknown_error`.
- Hardened source health summaries for CLI and `/source_health`: connector totals, last success/failure, discovered/upserted counts, active/stale vacancy counts, latest error category/message.
- Added runbook `docs/vacancy-discovery-runbook.md`.
- Live verification on 2026-06-26:
  - manual Kerzner single-source run still succeeded with 15 discovered/upserted;
  - connector-level run processed three `successfactors-v1` sources independently;
  - Atlantis Dubai succeeded with 3 active vacancies;
  - Kerzner succeeded with 15 active vacancies;
  - One&Only failed safely as `empty_result` without blocking other sources;
  - scheduled one-shot found 0 due sources immediately after connector-level run;
  - production totals: 18 `vacancies`, 18 distinct `dedupe_key`, 18 active, 0 stale.
- Railway production activation on 2026-06-26:
  - Railway CLI auth restored for project `amigo-mvp`, environment `production`;
  - `bot-api` redeployed successfully, deployment `7ba716e6-7a98-43a4-8bb4-06601c19e0c5`;
  - new Railway service `worker-vacancy-discovery` created and deployed successfully, deployment `2a4ebecc-228e-4965-89c2-23de840a274a`;
  - worker env confirmed: `RAILWAY_DOCKERFILE_PATH=Dockerfile.worker-vacancy-discovery`, `VACANCY_DISCOVERY_CONNECTORS=successfactors-v1`, `VACANCY_DISCOVERY_INTERVAL_MS=300000`;
  - worker logs showed daemon startup and repeated scheduled checks with `checkedSourceCount=3`, `dueSourceCount=0`;
  - Telegram webhook is registered to `https://bot-api-production-e076.up.railway.app/telegram/webhook`, pending updates are 0, and `/source_health` webhook invocation returned HTTP 200;
  - DB verification remained deduplicated: 18 vacancies, 18 distinct dedupe keys, 18 active, 0 stale, 0 stuck running source runs.
- First scheduled due-cycle evidence on 2026-06-26:
  - production DB shows three new `source_runs` after worker deployment at `2026-06-26T16:51Z`, matching the first due window after the manual `10:48Z` runs;
  - Atlantis Dubai succeeded with 2 discovered/upserted and marked 1 previously active vacancy stale;
  - Kerzner International succeeded with 15 discovered/upserted and marked 1 previously active vacancy stale;
  - One&Only Resorts failed safely again as `empty_result`;
  - production totals are now 19 vacancies, 19 distinct dedupe keys, 17 active, 2 stale, 0 duplicate dedupe keys, and 0 running source runs;
  - `/source_health` remains operational through the production webhook and reflects the scheduled-cycle results.
- Local validation passed: `pnpm check`, `pnpm test` (118 tests), `pnpm build`, and `pnpm format:check`.
- Phase 4C.1 partial expansion on 2026-06-26:
  - seed/import catalog expanded from 25 to 31 sources, with `successfactors-v1` configured for 9 Kerzner-family sources;
  - added verified One&Only property keyword sources: The Palm, Aesthesis, Kea Island, Palmilla, Mandarina, and Moonlight Basin;
  - `successfactors-v1` now preserves explicit endpoint `q` query parameters for property-specific search pages;
  - production manual connector run verified 8 successful sources and 1 expected `empty_result` failure for the original One&Only umbrella endpoint;
  - source health after manual verification: 9 configured, 8 succeeded last run, 1 failed last run, 96 active vacancies, 82 stale historical rows, 0 stuck running runs, and 0 duplicate `dedupe_key` rows;
  - caveat: active `apply_url` overlap remains between broad Kerzner and property-level sources because current `dedupe_key` is source-scoped;
  - `/source_health` initially hit a production timeout after catalog expansion because bot-api still used a sequential per-source query path; code was fixed to use the optimized vacancy-discovery health summary store;
  - production rollout completed on 2026-06-27 after Railway token auth was restored:
    - `bot-api` redeployed successfully, final deployment `adc456b8-11cd-464c-872f-61f2d4e8a5d4`;
    - `worker-vacancy-discovery` redeployed successfully, deployment `db58da6e-101e-4163-a8f3-7a61242e1057`;
    - worker env confirmed: `RAILWAY_DOCKERFILE_PATH=Dockerfile.worker-vacancy-discovery`, `VACANCY_DISCOVERY_CONNECTORS=successfactors-v1`, `VACANCY_DISCOVERY_INTERVAL_MS=300000`;
    - worker logs show daemon startup and scheduled checks with `checkedSourceCount=9`, `dueSourceCount=0`;
    - `/source_health` production webhook simulation returns HTTP 200 without timeout;
    - DB verification remains clean: 9 `successfactors-v1` sources, 178 vacancies, 178 distinct `dedupe_key`, 0 duplicate groups, 0 stuck running source runs, 96 active and 82 stale vacancies, latest health 8 succeeded / 1 classified `empty_result`.
  - Phase 4C.1 is production accepted for read-only SuccessFactors vacancy ingestion expansion.
- Phase 4C.2 cross-source duplicate detection was implemented on 2026-06-27:
  - kept existing source-scoped `vacancies.dedupe_key` behavior unchanged and backward-compatible;
  - added read-only canonical duplicate detection in `@amigo/vacancy-discovery` using canonical `apply_url` first, then external id plus normalized title/employer/location fallback;
  - added CLI report: `pnpm tsx scripts/discover-vacancies.ts --duplicates successfactors-v1`;
  - no migration was added and no existing vacancy rows are deleted, merged, or rewritten;
  - tests cover same apply URL across sources, tracking query parameter differences, same title with different locations, unrelated jobs, and source-scoped dedupe stability;
  - full local validation passed: `pnpm check`, `pnpm test` (124 tests), `pnpm build`, and `pnpm format:check`;
  - production duplicate report found 10 active cross-source duplicate groups / 20 rows, all by identical canonical `apply_url`, mostly broad Kerzner plus property-level sources;
  - after two repeated `successfactors-v1` discovery runs, production remained clean: 180 vacancies, 180 distinct `dedupe_key`, 0 duplicate dedupe groups, 0 stuck running source runs, latest health 8 succeeded / 1 classified `empty_result`.
  - Phase 4C.2 is accepted as a read-only pre-Phase-5 duplicate detection guard.

## What is complete (Phase 5 local implementation — as of 2026-06-28)
- Implemented Phase 5 according to [[phase-5-execution-plan]] Batch 0 through Batch 8 in local code.
- Added production migration draft `202606280001_phase5_matching_batches.sql` for:
  - `vacancy_scores`;
  - `daily_batches`;
  - `daily_batch_items`;
  - Phase 5 enums for score bucket, batch status, and item decision.
- Added `@amigo/matching` package with deterministic:
  - role taxonomy and synonym matching;
  - candidate/vacancy hard filters;
  - weighted scoring and structured explanations;
  - canonical duplicate suppression using Phase 4C.2 duplicate identity;
  - daily batch preparation with primary/reserve/rejected buckets and shortage reporting;
  - Postgres store for candidate/vacancy loading, score persistence, batch persistence, and manager decisions.
- Added Telegram `/candidate_batch` flow:
  - lists manager-owned candidates with approved CVs;
  - prepares/persists today's pending approval batch;
  - shows primary/reserve vacancies with score;
  - supports item approve/reject and whole-batch approve/reject callbacks;
  - enforces manager ownership and current pending batch status;
  - does not submit applications or enqueue Phase 6 application jobs.
- Phase 5 tests cover deterministic scoring, hard-filter rejection, canonical duplicate suppression without row mutation, and batch shortage behavior.
- Full local validation passed on 2026-06-28:
  - `CI=true pnpm check`;
  - `CI=true pnpm test` — 128 tests passed across current test suites;
  - `CI=true pnpm build`;
  - `CI=true pnpm format:check`.
- Supabase remote migration `202606280001` was applied successfully on 2026-06-28 and appears in `supabase migration list`.
- Railway token auth was provided and `bot-api` was deployed successfully on 2026-06-28 after two packaging fixes:
  - Dockerfiles now copy `packages/matching/package.json` before `pnpm install`;
  - `@amigo/matching` package exports were restored to runtime `dist` output instead of TS source.
- Production `bot-api` health returned `{"status":"ok","service":"bot-api","database":"ok"}` after deploy.
- Telegram webhook info after deploy: pending updates 0, no last error.
- Production Phase 5 data acceptance:
  - candidate `61ac04f1-b04c-4f35-a324-0a8c99182109` with approved CV `689f61c4-ff82-426b-97fe-b44a7072939d`;
  - batch `c7c7fcb1-58a3-4f0a-bc24-e66eb8906877`;
  - final strict re-audit batch has 6 primary vacancies, 0 reserves, shortage `eligible_vacancy_shortage:6/10`;
  - canonical duplicate suppression check passed;
  - item rank 1 approved and rank 2 rejected through Phase 5 store, batch remains `pending_approval` because other items are still pending.
- Added country normalization fixes for Russian target countries and ISO country codes (`ОАЭ`/`AE`, `Катар`/`QA`, `Бахрейн`/`BH`, etc.) after production acceptance initially showed false `country_mismatch`.
- 2026-06-28 strict plan re-audit found and fixed a regeneration safety issue: re-preparing an existing `pending_approval` batch now returns the existing batch instead of deleting/recreating items and losing decisions. Production verification confirmed rank 1 stayed `approved` and rank 2 stayed `rejected` after re-prepare.
- 2026-06-28 strict plan re-audit also fixed local test reliability by making `bot-api` tests build `@amigo/matching` before resolving its runtime `dist` export.
- 2026-06-28 strict plan re-audit found and fixed a role-family hard-filter gap:
  - unknown non-target roles now fail with `role_mismatch` unless the title explicitly contains a target role;
  - broad F&B markers were removed from waiter matching because they let kitchen/host/stewarding roles enter approvable batches;
  - production batch `c7c7fcb1-58a3-4f0a-bc24-e66eb8906877` was intentionally expired and regenerated under the stricter filter;
  - excluded examples now include `F&B Intern`, `Restaurant Hostess`, `Stewarding Supervisor`, `Sushi Commis Chef`, and `Public Area Attendant`.
- 2026-06-29 manual Telegram click-through found a Phase 5 callback UX bug: pressing candidate buttons in `/candidate_batch` appeared to do nothing. Production logs showed callback queries reached the bot, but `answerCallbackQuery` failed after Telegram retries/expiry and `sendBatchSummary` could fail Markdown parsing because batch text contained underscores or unescaped vacancy text. Fixed in `apps/bot-api/src/intake/batch.ts` by answering callbacks safely/early and sending batch summaries without Markdown parsing. Deployed `bot-api` deployment `155670f9-f22e-4f78-bfe3-85eb73f39cb4`; `/health` and webhook smoke passed.

## What is complete (Phase 3.5 CV enrichment — as of 2026-06-22)
- Added production migration `202606220003_cv_profile_enrichment.sql` with:
  - `candidate_photos`;
  - `candidate_work_experiences`;
  - `candidate_education`;
  - `candidate_cv_extras`.
- Updated private `candidate-documents` bucket to allow JPEG/PNG/WebP uploads while remaining non-public.
- Added Telegram manager flows:
  - `/candidate_photo`;
  - `/candidate_experience`;
  - `/candidate_education`;
  - `/candidate_extra`.
- Updated `/candidate_view` with CV enrichment counts and readiness warnings for portrait photo, structured work experience, education, and extras.
- Updated `worker-documents` so CV generation reads structured work experience, education, extras, and portrait photo status from the new tables.
- CV grounding still blocks invented employers, skills, experience, certificates, software, courses, achievements, education names, and unsupported extras.
- Candidate portrait image embedding was implemented on 2026-06-23 in commit `04dda5d`: `worker-documents` downloads JPEG/PNG portrait files from private Supabase Storage, embeds them into the generated DOCX, and Gotenberg carries the image into PDF. The 2026-06-24 hardening changed unsupported/download failures to `PHOTO UPLOADED - EMBEDDING FAILED`.
- Tests/check/build/format passed locally; migration applied to production; `bot-api` and `worker-documents` deployed to Railway; Telegram webhook refreshed with `pending_update_count=0`.
- Commit `3a7bd48` pushed to `main`.
- Post-deploy webhook correction on 2026-06-22: Telegram must be registered to `https://bot-api-production-e076.up.railway.app/telegram/webhook` with `secret_token = TELEGRAM_WEBHOOK_SECRET`. The old `/webhook/<secret>` URL returns 404 because the app validates the secret through the `X-Telegram-Bot-Api-Secret-Token` header.
- Production verification for document version `0fb3b92b-2397-4ca6-bff5-d7db4072a6bb` confirmed placeholder text is gone and the PDF contains a JPEG image object.
- Portrait fallback hardening was completed on 2026-06-24 in commit `f3e4c9d`: private storage paths were removed from photo failure logs, JPEG/PNG loading was moved into a tested module, unsupported/download failures now render `PHOTO UPLOADED - EMBEDDING FAILED`, and DOCX/PDF render failures explicitly mark the version `validation_failed`.
- Production sample `84e1f6bf-fe95-40c8-b294-4e6e9588d3a8` is `pending_approval` with no validation errors. Visual PNG review confirms the portrait is visible, About Me remains under the header, Experience is grounded, and no photo placeholder text remains.
- Full validation passed with 57 tests; Railway deployment `67a874db-2780-4866-b59e-c3e83e414da3` succeeded and all services are Online.
- Unified `/candidate_new` onboarding was implemented and deployed on 2026-06-24 in commit `8145245`:
  - preserves the existing basic profile form, language parsing, and consent gate;
  - creates the `intake` candidate, consent, languages, and durable session pointer atomically after consent;
  - guides the manager through repeatable work experience, education, extras, portrait upload, and final readiness review;
  - resumes the same session on repeated `/candidate_new` and rejects stale inline buttons;
  - keeps `/candidate_photo`, `/candidate_experience`, `/candidate_education`, and `/candidate_extra` operational for later edits;
  - `/cancel` clears the wizard while preserving an already-created consented candidate.
- Added optional separate `whatsapp_phone` persistence in migration `20260624172128`; worker-documents uses it in CV output and falls back to the primary phone.
- Production migration is applied; Supabase security/performance advisors report no issues.
- Local validation passed with 69 tests. Railway deployments `9a8e1a8a-11d7-42b6-bb65-84ed51a754b8` (`bot-api`) and `1f11b5f8-23ab-4fc5-8adf-b461173963c4` (`worker-documents`) succeeded; webhook is healthy with zero pending updates.
- Compact CV header redesign was completed and deployed on 2026-06-25 in commit `63d9637`:
  - the old full-width photo frame and separate centered title block were replaced with a fixed two-column header;
  - portrait/photo fallback is in the left column at approximately 3.3 cm × 4.2 cm;
  - name, target role, current location, target relocation countries, age, nationality, email, phone, WhatsApp, and language summary are aligned in the right column;
  - About Me remains immediately below the complete header;
  - failed photo embedding now shows compact `PHOTO EMBEDDING FAILED`.
- Header identity/location/relocation is forced back to deterministic stored facts during grounding.
- Local LibreOffice samples with real portrait and missing-photo fallback passed visual QA.
- Production Gotenberg sample `689f61c4-ff82-426b-97fe-b44a7072939d` is `pending_approval` with no validation errors; PDF/PNG inspection confirms the compact layout and embedded JPEG.
- Full validation passed with 95 tests. Railway deployment `70b6d688-ffad-4f31-b36f-b12c0079db05` succeeded; all services are Online and `document_generate` queue depth is zero.
- Telegram photo upload outage was fixed on 2026-06-25 in commit `65ff305`:
  - Telegram `message:photo` is now treated as JPEG even when Telegram file download returns `application/octet-stream`;
  - JPEG/PNG/WebP image documents remain supported;
  - HEIC/HEIF receives a clear retry instruction instead of causing Supabase Storage `415` and webhook `500`;
  - Telegram download, Storage upload, and photo-record failures now reply safely while preserving the `cv_photo_upload` session;
  - bot error logs no longer serialize the full grammY context/API token.
- Railway `bot-api` deployment `04c55e2e-416d-427f-9a26-6ae87f2eb5d5` succeeded. The previously stuck HEIC update was redelivered and acknowledged with HTTP 200; Telegram pending update count returned to zero.
- Manager `935784686` remains safely on `cv_photo_upload` for candidate `db0e2aff-89a8-4cd8-aea1-eaafa1f931f1`; no invalid portrait row was created.
- Full validation passed with 99 tests.
- Native HEIC/HEIF photo acceptance was implemented and deployed on 2026-06-25 in commit `d029396`:
  - Telegram image documents are recognized by MIME type or `.heic`/`.heif` filename when Telegram sends `application/octet-stream`;
  - files are converted server-side to JPEG with `heic-convert` before private Supabase Storage upload;
  - empty and oversized files are rejected safely, conversion errors preserve the active upload session, and private storage paths remain unexposed;
  - a real 3024×4032 HEIC fixture converted successfully in 868 ms with orientation preserved.
- Full validation passed with 104 tests. Railway `bot-api` deployment `97bd9248-f720-499f-9acc-9e1d90a7b9bd` succeeded; all services are Online, `/health` is green, and Telegram webhook pending updates are zero.

## What is not built
- Broad non-SuccessFactors connector coverage and application adapters are not built yet.
- Full employer catalog and additional ingestion connectors remain incomplete.
- Application workers, ATS adapters (Phase 6)
- No ATS adapter is certified for production use.

## Immediate milestone
Phase 5 production acceptance.

**Requires next**: run one manual Telegram UI click-through of `/candidate_batch` as the manager, then proceed to Phase 6 application handoff/adapters only after approval rules are accepted.

## Capacity requirement
The design must run the 10-candidate pilot without a rewrite and scale to:
- 30 active candidates;
- 150–300 application attempts per day;
- 2–5 managers;
- multiple domain-specific rate limits;
- independent ingestion and application workers.

## Operating constraints
- Monthly pilot infrastructure budget: up to USD 100.
- Manager interface: Telegram chat only.
- Candidate email is used for applications.
- Passwords for candidate email accounts are not stored.
- CAPTCHA, OTP, assessments, and unknown required questions require human action.
