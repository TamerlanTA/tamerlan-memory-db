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

## P2 — Documents (in progress, due 2026-06-19–21)
Completed foundation:
1. `worker-documents` service implemented and deployed.
2. OpenAI structured extraction path implemented with deterministic fallback mode.
3. DOCX render, Gotenberg PDF render, private Supabase Storage upload, and generation audit implemented.
4. Telegram `/candidate_documents` flow implemented with signed PDF link and approve/reject callbacks.
5. Document schema, storage bucket, and `document_generate` queue applied to production.
6. CV template/content quality upgrade completed and deployed in commit `a11145b`.
7. Controlled candidate regenerated with improved CV version `9219995e-fed0-407c-a27f-f5ee3493cd71`; status is `pending_approval`, validation errors are empty, and PDF text extraction passed.

Remaining to close Phase 3:
1. Owner approves the improved CV template (`packages/document-templates/templates/hospitality-cv-en-v1.docx`) and consent text v1-ru-2026-06.
2. Approve the regenerated controlled candidate CV through `/candidate_documents`.
3. Verify manager approval callback and candidate status transition.
4. Confirm OpenAI model setting works in production or switch `OPENAI_DOCUMENT_MODEL` to an approved available model.
5. Decide what additional experience fields must be collected to make real CVs stronger than the deterministic fallback profile.

## P0 — Phase 2 review remediation ✅ COMPLETE (commit e5ad6e4)
1. ✅ Non-closed filter moved to SQL WHERE in edit.ts and close.ts
2. ✅ handleCloseConfirm verifies candidateId + assignedManagerId + status != closed before UPDATE
3. ✅ Location validation already fixed in steps.ts rewrite (city.length < 1 check)

## P1 — Search and matching
1. Implement the normalized vacancy contract.
2. Build Greenhouse-read, Lever-read, and generic sitemap/JSON connectors.
3. Implement deduplication and freshness rules.
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
1. Approve or revise the improved CV template and consent text.
2. Open `/candidate_documents`, select the controlled candidate, and approve/reject CV version `9219995e-fed0-407c-a27f-f5ee3493cd71`.
3. Verify manager approval callback and candidate status transition to `documents`.
4. Confirm OpenAI model setting for production content generation.
5. Start the 100-employer catalog while Phase 3 approval validation is finishing.

## Two-person working split
- **Tamerlan:** approve business rules, provide or create service accounts and secrets, approve the CV template, consent text, target employer scope, and pilot candidates.
- **Codex:** initialize and implement the repository, database, bot, workers, tests, CI, documentation, and project-memory updates.
- **Joint checkpoints:** approve schema before production migration, approve the first end-to-end candidate flow, certify application adapters, and make the July 5 launch decision.
