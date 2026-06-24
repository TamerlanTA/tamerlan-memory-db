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
- Current phase: employer catalog and vacancy discovery foundation
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

## What is not built
- Vacancy ingestion workers/connectors, normalized vacancy records, scoring, matching, and application adapters are not built yet.
- Full employer catalog, ingestion connectors, scoring, matching (Phase 4–5)
- Application workers, ATS adapters (Phase 6)
- No ATS adapter is certified for production use.

## Immediate milestone
Phase 4: employer catalog and vacancy discovery foundation.

**Requires next**: manually complete the new `/candidate_new` Telegram acceptance flow, then implement the first read-only discovery connector from one high-yield seeded source.

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
