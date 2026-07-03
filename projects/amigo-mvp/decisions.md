# AMIGO MVP — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]
- [[technical-architecture]]
- [[roadmap]]
- [[phase-5-execution-plan]]
- [[phase-6-execution-plan]]

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

### D-017 — Phase 6 execution lock
Phase 6 applications and reporting must be implemented according to [[phase-6-execution-plan]] in order. The canonical first safe execution mode is manual deep-link tasks; auto-submit is allowed only for a narrow certified adapter or email flow after duplicate prevention, evidence persistence, worker state handling, and manager approval checks exist. Future agents must not implement universal ATS auto-apply, bypass protective controls, invent answers, or submit real applications outside the plan.

### D-018 — Next automation layer is certification-gated email/apply readiness
After manual deep-link evidence acceptance and 85-source expansion, the next automation layer is not universal ATS auto-submit. It is a controlled adapter-readiness layer:
- add worker/runtime support for `email-apply-v1` in dry-run/feature-flag mode first;
- keep live email sending disabled until source-level enablement, sender configuration, rate limits, duplicate prevention, and one controlled evidence review are complete;
- add adapter eligibility reporting so managers can see which approved vacancies are manual-only, email-capable, or future adapter candidates;
- keep all non-certified ATS/form URLs routed to manual actions.

Production check on 2026-07-03 found `0` active `mailto:` vacancies and all `85` career sources have `application_adapter = null`, so live email sending would not improve current volume yet. Source quality hardening continues in parallel, but the next application automation implementation should create the safe routing/certification foundation before any real sending.
