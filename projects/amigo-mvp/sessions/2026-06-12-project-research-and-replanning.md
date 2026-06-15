# Session 2026-06-12 — Project Research and Replanning

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]
- [[technical-architecture]]

## What was done
- Promoted AMIGO from a single-file project into a full project memory structure.
- Replaced self-service onboarding with a manager-led Telegram workflow.
- Defined the 10-candidate launch target for 2026-07-05 and immediate scale target of 30.
- Documented the technical stack, data model, intake, matching, connectors, security, roadmap, and prompt policy.
- Researched Greenhouse, Lever, enterprise ATS constraints, Telegram, Playwright, Supabase queues, document generation, and hosting.
- Rewrote the Notion project page, created 9 current phases and 25 execution tasks, added 7 decisions/risks, and created a new weekly review.
- Marked obsolete direct Greenhouse/Lever API auto-apply and LLM-consultant tasks as canceled without deleting history.

## Key findings
- Greenhouse and Lever public feeds are useful for vacancy discovery, but submission APIs generally require employer-controlled credentials.
- Hospitality employers often use Workday, Oracle, SAP, Taleo, and custom sites, so application automation must use certified employer-specific adapters.
- A universal ATS adapter is not a valid MVP promise.
- Telegram-only operations are feasible for the pilot but may require a web operations panel after 30 candidates.

## Decisions
- Search, scoring, batching, and applications remain deterministic.
- LLM use is restricted to English document preparation.
- Managers approve documents and daily vacancy batches.
- CAPTCHA, OTP, assessments, and unknown questions require human action.
- Closed candidate data is deleted after 90 days.

## Blockers
- Application repository and environments are not yet identified.
- Employer catalog and approved CV template are not yet provided.
- No application adapter has passed certification.

## Next steps
- Execute Phase 1 in [[roadmap]].
- Start implementation only after repository and credentials are available.
