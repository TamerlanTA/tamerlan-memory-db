# AMIGO MVP — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]
- [[technical-architecture]]
- [[roadmap]]
- [[phase-5-execution-plan]]

## Accepted decisions

### D-001 — Manager-led operation
The manager, not the candidate, completes intake, reviews documents, and approves daily application batches.

### D-002 — Telegram-only MVP
Telegram is the only operational interface in the MVP. Complex workflows use conversations, inline buttons, pagination, search commands, and generated reports. A web operations panel is deferred until growth beyond 30 candidates or Telegram friction proves material.

### D-003 — International hospitality focus
Initial employers are hotels, resorts, restaurants, airlines, and adjacent hospitality businesses in the Maldives, Asia, the Middle East, and Europe.

### D-004 — Controlled launch and scale target
Launch 10 candidates by 2026-07-05. The deployed architecture must support 30 candidates immediately after launch because a waitlist already exists.

### D-005 — Algorithm-first execution
Vacancy collection, normalization, filtering, scoring, deduplication, batching, and application decisions are deterministic. AI output cannot decide whether to apply.

### D-006 — Limited LLM use
Use OpenAI only to translate Russian candidate facts into structured English text and prepare document drafts. Generated content must be traceable to source fields and approved by a manager.

### D-007 — Curated employer catalog
MVP discovery uses 100–200 approved employers and known career endpoints. Open-ended web crawling is outside the critical path.

### D-008 — Hybrid connector model
Use public feeds for vacancy discovery when available and Playwright adapters for public candidate forms. Greenhouse and Lever submission APIs cannot be assumed because employer-owned credentials are required.

### D-009 — Human approval before application
The system prepares a daily batch of 5–10 vacancies. Applications begin only after manager approval of the batch.

### D-010 — No protective-control bypass
CAPTCHA, OTP, assessments, video interviews, and unknown mandatory questions enter `NeedsAction`. The system never bypasses or guesses through them.

### D-011 — Candidate-owned identity
Applications use the candidate's own email and phone. Email passwords are not stored. One-time codes are requested through the assigned manager when needed.

### D-012 — Document approval
The manager approves each active CV version. Candidate approval is not required in MVP, but source facts and consent must be recorded.

### D-013 — Data retention
Candidate documents and sensitive personal data are deleted 90 days after the candidate is closed. Deletion is logged.

### D-014 — Cost-conscious infrastructure
Use Supabase Postgres, Storage, Cron, and PGMQ plus Railway services. Avoid Redis and separate managed queues until measured load requires them.

### D-015 — Unified candidate onboarding with durable post-consent session
`/candidate_new` is the default full onboarding path. The candidate is created only after consent, using status `intake`; the same `intake_sessions` row then stores the created candidate ID and drives CV enrichment to final review. Re-running `/candidate_new` resumes that session instead of creating a second candidate. Standalone enrichment commands remain available for later corrections.

### D-016 — Phase 5 execution lock
Phase 5 matching and approval must be implemented according to [[phase-5-execution-plan]] in order. The plan is the canonical scope-control document for matching, scoring, duplicate suppression, daily batches, and Telegram approval. Future implementation may deviate only if Tamerlan explicitly changes the plan or a verified blocker is documented in a session note / decision before continuing.
