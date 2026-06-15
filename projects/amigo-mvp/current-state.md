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
- Current phase: architecture and foundation
- Working mode: two-person execution — Tamerlan owns business decisions, access, credentials, and approvals; Codex owns technical implementation, validation, and memory synchronization.

## What is complete
- Product workflow and MVP boundaries are defined.
- Target market is restricted to international hospitality.
- Manager-led Telegram intake and batch approval are confirmed.
- Algorithm-first search, matching, and application logic are confirmed.
- LLM use is restricted to document translation and preparation.
- Initial technical architecture, data model, connector strategy, and delivery roadmap are documented.

## What is not built
- No confirmed application repository is linked to project memory.
- Supabase and Railway environments are not recorded as provisioned.
- Telegram bot workflow is not implemented.
- Candidate schema, employer catalog, ingestion connectors, scoring, document generation, and application workers are not implemented.
- No ATS adapter is certified for production use.

## Immediate milestone
The original 2026-06-14 foundation milestone is overdue as of 2026-06-15. The immediate recovery milestone is:
- create the application repository and environments;
- implement the database foundation and Telegram webhook skeleton;
- load the initial employer catalog structure;
- establish CI, logging, migrations, and queue conventions.

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
