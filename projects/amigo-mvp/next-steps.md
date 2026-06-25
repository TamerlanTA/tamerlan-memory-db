# AMIGO MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]
- [[roadmap]]
- [[technical-architecture]]

## P0 — 2026-06-12 to 2026-06-14
Completed on 2026-06-15:
1. Application repository created and linked.
2. Supabase and Railway production foundation provisioned.
3. TypeScript/pnpm monorepo and CI initialized.
4. First Drizzle schema and SQL migration implemented.
5. RLS baseline and append-oriented audit logging implemented.
6. grammY webhook and manager allowlist deployed.
7. PGMQ queue and worker health processing verified.
8. Employer catalog CSV import format prepared.

## P1 — Intake ✅ COMPLETE (2026-06-16, commit d1bf79d)
- `/candidate_new`, `/candidate_find`, `/candidate_view`, `/candidate_edit`, `/candidate_close`, `/cancel` all functional
- 25-field form with age, gender, race, English level, education year, height, weight, 9 boolean experience flags
- Languages (CEFR) collected in intake and editable
- Profile completeness check implemented (`profile.ts:checkCompleteness`)
- 34 tests passing, deployed on Railway, Supabase migration applied

## P2 — Documents ✅ COMPLETE (closed 2026-06-22)
Completed foundation:
1. `worker-documents` service implemented and deployed.
2. OpenAI structured extraction path implemented with deterministic fallback mode.
3. DOCX render, Gotenberg PDF render, private Supabase Storage upload, and generation audit implemented.
4. Telegram `/candidate_documents` flow implemented with signed PDF link and approve/reject callbacks.
5. Document schema, storage bucket, and `document_generate` queue applied to production.
6. CV template/content quality upgrade completed and deployed in commit `a11145b`.
7. Controlled candidate regenerated with improved CV version `9219995e-fed0-407c-a27f-f5ee3493cd71`; status is `pending_approval`, validation errors are empty, and PDF text extraction passed.
8. Manager approval callback was verified in Telegram: document version `9219995e-fed0-407c-a27f-f5ee3493cd71` became `approved`, and candidate status became `documents`.

Residual follow-up:
1. Business/legal owner still needs to formally approve consent text v1-ru-2026-06 before pilot scale.
2. Use the new `/candidate_experience`, `/candidate_education`, `/candidate_extra`, and `/candidate_photo` flows to enrich real pilot candidates before regenerating CVs.
3. Re-upload any unsupported WebP portrait photos as JPEG/PNG when the generated CV shows `PHOTO UPLOADED - EMBEDDING FAILED`; JPEG/PNG embedding is implemented.
4. Optional: approve the latest corrected sample CV version `c20ddaa5-15a7-4aa9-9314-8db68adec1ab` or reject it after visual review.

## Phase 3.5 — CV Enrichment ✅ COMPLETE (2026-06-22, commit 3a7bd48)
Completed:
1. Added production tables for candidate photos, work experience, education, and CV extras.
2. Added Telegram manager commands `/candidate_photo`, `/candidate_experience`, `/candidate_education`, and `/candidate_extra`.
3. Updated `/candidate_view` with CV readiness warnings.
4. Updated `worker-documents` to load structured enrichment data and keep generated CVs grounded.
5. Added runbook `docs/cv-enrichment-runbook.md`.
6. Applied Supabase migration, deployed `bot-api` and `worker-documents`, refreshed Telegram webhook, and pushed commit `3a7bd48`.

Manual remaining:
1. Add real enrichment data for each pilot candidate through Telegram.
2. Regenerate and approve each enriched CV.
3. Review final portrait crop/quality in generated PDFs before approval.
4. Review and approve or reject production sample `84e1f6bf-fe95-40c8-b294-4e6e9588d3a8`.
5. Review and approve or reject compact-header production sample `689f61c4-ff82-426b-97fe-b44a7072939d`.

## Unified Candidate Onboarding ✅ DEPLOYED (2026-06-24, commit 8145245)
Completed:
1. `/candidate_new` continues after consent through experience, education, extras, portrait, and final review.
2. Repeatable add-another loops and explicit skip/no-experience paths are implemented.
3. Re-running `/candidate_new` resumes the same durable session without creating another candidate.
4. Optional separate WhatsApp is stored and used in generated CVs.
5. Standalone enrichment commands remain available.
6. Production migration, Supabase advisors, Railway deployments, webhook, and `/health` passed.

Manual remaining:
1. Continue the existing production `awaiting_form` session by sending `/candidate_new`.
2. Complete one candidate with one experience, education, extra, and portrait.
3. Confirm `/candidate_view`, regenerate the CV, and inspect all collected data.
4. Run separate skip-photo, no-experience, and `/cancel` acceptance checks.

## P0 — Phase 2 review remediation ✅ COMPLETE (commit e5ad6e4)
1. ✅ Non-closed filter moved to SQL WHERE in edit.ts and close.ts
2. ✅ handleCloseConfirm verifies candidateId + assignedManagerId + status != closed before UPDATE
3. ✅ Location validation already fixed in steps.ts rewrite (city.length < 1 check)

## P1 — Search and matching
Completed foundation:
1. Added employer catalog source columns and production migration `202606220001`.
2. Added idempotent catalog importer `scripts/import-employer-catalog.ts`.
3. Seeded 25 hospitality employers / career sources into production (`data/employer-catalog.seed.csv`).
4. Added normalized vacancy discovery schema in migration `202606220002`: `source_runs` and `vacancies`.

Next:
1. Build the first read-only discovery connector from the seeded catalog.
2. Implement deduplication/freshness upsert behavior against `vacancies.dedupe_key`.
3. Add source-run metrics and error classification.
4. Implement hard filters and weighted scoring with explanation records.
5. Generate manager approval batches with reserve vacancies.

## P1 — Applications and reports
1. Define the adapter SDK and fixture contract.
2. Certify the first hosted-form adapters.
3. Implement email apply.
4. Add `NeedsAction` handling for CAPTCHA, OTP, assessments, and unknown questions.
5. Store confirmation evidence and send daily manager/candidate reports.

## Required owner inputs
- Telegram bot and initial manager ID: provided and configured.
- Supabase, Railway, and OpenAI: provided/provisioned and configured.
- Hospitality CV template: draft v1 created; team approval still required.
- Employer catalog: Codex is authorized to assemble the first 100 target brands.
- Candidate consent: draft v1 created; business/legal approval and privacy contact still required.

## Immediate execution order
1. Complete the unified `/candidate_new` manual Telegram acceptance pass.
2. Collect/enrich pilot candidate CV facts through unified onboarding or standalone Phase 3.5 commands.
3. Build the first read-only discovery connector, preferably Accor or Kerzner because the seeded endpoints expose hospitality jobs in target regions.
4. Add dedupe/freshness upsert logic for imported vacancies.
5. Add a Telegram/admin summary command for catalog/source health.
6. Continue expanding employer catalog from 25 toward 100 approved brands.

## Two-person working split
- **Tamerlan:** approve business rules, provide or create service accounts and secrets, approve the CV template, consent text, target employer scope, and pilot candidates.
- **Codex:** initialize and implement the repository, database, bot, workers, tests, CI, documentation, and project-memory updates.
- **Joint checkpoints:** approve schema before production migration, approve the first end-to-end candidate flow, certify application adapters, and make the July 5 launch decision.
