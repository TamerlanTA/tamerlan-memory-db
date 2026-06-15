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

## P1 — Intake and documents
1. Implement `/candidate_new`, `/candidate_find`, `/candidate_edit`, and `/candidate_close`.
2. Implement resumable intake conversations and validation.
3. Add source-fact versioning, consent, and standard answer bank.
4. Implement structured OpenAI generation and fact-grounding validation.
5. Produce approved DOCX/PDF templates and manager review actions.

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
1. Expand candidate-domain migrations from [[data-model]].
2. Implement persistent resumable grammY conversations.
3. Deliver `/candidate_new`, search, edit, consent, completeness, and close flows.
4. Run the first real manager intake with a controlled test candidate.
5. Start the 100-employer catalog while intake implementation is being validated.

## Two-person working split
- **Tamerlan:** approve business rules, provide or create service accounts and secrets, approve the CV template, consent text, target employer scope, and pilot candidates.
- **Codex:** initialize and implement the repository, database, bot, workers, tests, CI, documentation, and project-memory updates.
- **Joint checkpoints:** approve schema before production migration, approve the first end-to-end candidate flow, certify application adapters, and make the July 5 launch decision.
