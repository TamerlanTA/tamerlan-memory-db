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

## What is not built
- Vacancy ingestion workers/connectors, normalized vacancy records, scoring, matching, and application adapters are not built yet.
- Full employer catalog, ingestion connectors, scoring, matching (Phase 4–5)
- Application workers, ATS adapters (Phase 6)
- No ATS adapter is certified for production use.

## Immediate milestone
Phase 4: employer catalog and vacancy discovery foundation.

**Requires next**: implement the first read-only discovery connector, starting with one high-yield source from the seeded catalog.

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
