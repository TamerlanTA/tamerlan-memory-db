# Session 2026-06-24 — Unified Candidate Onboarding

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Converted `/candidate_new` from a basic-form-only flow into one guided onboarding:
  - basic profile and languages;
  - consent;
  - atomic `intake` candidate creation;
  - repeatable work experience;
  - repeatable education;
  - repeatable CV extras;
  - private portrait upload;
  - final CV readiness review.
- Stored the created candidate ID in the existing `intake_sessions` row so `/candidate_new` resumes instead of duplicating the candidate.
- Added stale callback protection and explicit post-consent `/cancel` behavior.
- Preserved all standalone enrichment commands.
- Added optional `whatsapp_phone` to candidates and propagated it into profile/edit/CV generation with primary-phone fallback.
- Updated the CV enrichment runbook and added onboarding/session/transition/private-path/WhatsApp/command-wiring tests.

## Key findings
- No new onboarding table was required; the existing one-session-per-manager model is sufficient.
- Candidate, consent, languages, and the post-consent session pointer are committed in one transaction.
- Production had one existing `awaiting_form` session for manager `405182031`; it was preserved and can be resumed safely with `/candidate_new`.
- Supabase migration `20260624172128_candidate_whatsapp_phone.sql` is applied.
- Supabase security and performance advisors found no issues.

## Validation
- `pnpm check` passed.
- `pnpm test` passed: 69 tests.
- `pnpm build` passed.
- `pnpm format:check` passed.
- Commit `8145245` pushed to `main`.
- Railway `bot-api` and `worker-documents` deployments succeeded.
- Telegram webhook URL/secret registration passed with zero pending updates.
- Production `/health` returned database/status OK.

## Blockers
- A full real-manager Telegram acceptance pass has not yet been completed.

## Next steps
- Send `/candidate_new` to resume the existing production form.
- Complete one candidate through all enrichment steps and final review.
- Confirm `/candidate_view`, regenerate the CV, and verify experience, education, extras, portrait, and WhatsApp.
- Separately test no-experience, skip-photo, and `/cancel`.
