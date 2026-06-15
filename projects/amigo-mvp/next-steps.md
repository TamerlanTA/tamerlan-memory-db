# AMIGO MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]
- [[roadmap]]
- [[technical-architecture]]

## P0 — 2026-06-12 to 2026-06-14
1. Create and link the application repository.
2. Provision Supabase and Railway development/staging environments.
3. Initialize the TypeScript/pnpm monorepo and CI checks.
4. Implement the first Drizzle migrations from [[data-model]].
5. Configure private Storage buckets, service roles, RLS, and audit logging.
6. Implement the grammY webhook, manager allowlist, and role middleware.
7. Create PGMQ queues and worker health checks.
8. Prepare the first 100-employer catalog import.

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
- Telegram bot token and allowed manager Telegram IDs.
- Supabase and Railway projects.
- OpenAI API key and monthly model budget.
- Approved hospitality CV template.
- First 100–200 employer list or approval to assemble it from target brands.
- Candidate consent text and business privacy contact.

## Two-person working split
- **Tamerlan:** approve business rules, provide or create service accounts and secrets, approve the CV template, consent text, target employer scope, and pilot candidates.
- **Codex:** initialize and implement the repository, database, bot, workers, tests, CI, documentation, and project-memory updates.
- **Joint checkpoints:** approve schema before production migration, approve the first end-to-end candidate flow, certify application adapters, and make the July 5 launch decision.
