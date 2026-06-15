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
- Current phase: candidate intake
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

## What is complete (Phase 2 — as of 2026-06-15, commit 2be4a04)
- `/candidate_new` — 9-field form (incl. languages), consent flow, atomic DB transaction
- `/candidate_find` — numbered list with status labels
- `/candidate_view` — full profile with completeness check
- `/candidate_edit` — select candidate → select field → type value → validate → update + audit event
- `/candidate_close` — select candidate → inline confirm → status=closed + audit event
- `/cancel` — clear active session
- `profile.ts` — `checkCompleteness()` reusable for document-generation gate
- Languages stored in `candidate_languages` (CEFR A1–C2 + native)
- 34 tests passing
- Deployed and health check confirmed

## What is not built
- Document generation service (Phase 3)
- Full employer catalog, ingestion connectors, scoring, matching (Phase 4–5)
- Application workers, ATS adapters (Phase 6)
- No ATS adapter is certified for production use.

## Immediate milestone
Phase 3: document generation — OpenAI structured CV extraction → Docxtemplater DOCX fill → Gotenberg PDF → manager approval in Telegram. Planned 2026-06-19–21.

**Requires first**: business/legal approval of CV template (`packages/document-templates/templates/hospitality-cv-en-v1.docx`) and consent text v1-ru-2026-06.

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
