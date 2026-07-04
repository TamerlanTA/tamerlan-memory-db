# Session 2026-07-03 — Workday Automation Foundation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Researched how auto-apply products structure automation: discovery/matching, profile-backed autofill, auto/manual modes, evidence/tracking, and manual fallback for blockers.
- Checked current production Workday supply; recent active Four Seasons vacancies use `fourseasons.wd3.myworkdayjobs.com`.
- Added `runtime.htmlSnapshot` to the application adapter context and wired certification fixtures to pass snapshots.
- Implemented `workday-form-v1` as a preflight-only adapter:
  - supports `*.myworkdayjobs.com`;
  - detects CAPTCHA, OTP, login/account creation, assessment, video interview, and unknown required fields;
  - maps only stored candidate facts, approved CV storage keys, or manual fields;
  - captures hashed preflight evidence;
  - never live-submits.
- Updated `/adapter_eligibility` classification to report Workday approved items as `preflight-capable`.
- Updated adapter certification documentation with the Workday automation ladder.
- Added handoff routing so new Workday/MyWorkdayJobs applications use `workday-form-v1` / `preflight-v1`.
- Added `workday_preflight` execution in `worker-applications`: snapshot evidence, adapter preflight evidence, manual fallback, and no submit.
- Deployed `bot-api` and `worker-applications` after token auth was provided.
- Accepted the first real Workday handoff after Tamerlan ran `/application_handoff` for the 2026-07-03 Жанибек Иванов batch.
- Fixed two acceptance issues found by production verification:
  - Workday missing/empty snapshot preflight now records `confirmation_text_hash` evidence.
  - Worker manual-action routing now rereads an existing open manual action after `on conflict do nothing` instead of marking the attempt failed.
- Deployed the worker fix and recovered the one affected production attempt.

## Key findings
- Competitor-style auto-apply is not one universal submitter; the durable pattern is staged automation with manual review/fallback.
- Workday is the highest-leverage hosted-form target for AMIGO now because current approved/future-adapter items are concentrated there.
- Live auto-submit should remain blocked until browser preflight/autofill and controlled evidence are proven.
- Existing historical application rows remain `manual-deep-link-v1`; do not rewrite them because they already carry manual evidence/history.
- Production `/adapter_eligibility` for 2026-07-03 now reports `10` preflight-capable Workday approved items and `10` future adapter candidates.
- The first real handoff created 20 application jobs/manual tasks: 10 Workday preflight applications and 10 manual-deep-link applications.
- Workday evidence acceptance passed: 10 `html_snapshot` rows and 10 `confirmation_text_hash` rows.

## Validation
- `pnpm --filter @amigo/application-adapters test`
- `pnpm --filter @amigo/application-adapters check`
- `pnpm --filter @amigo/matching test`
- `pnpm --filter @amigo/matching check`
- `pnpm --filter @amigo/bot-api test`
- `pnpm --filter @amigo/bot-api check`
- `pnpm format:check`
- Railway deploy: `bot-api` uploaded successfully after token auth was provided.
- Production health check passed: `{"status":"ok","service":"bot-api","database":"ok"}`.
- Railway deploy: `worker-applications` uploaded successfully after token auth was provided.
- Production `worker-applications` logs show fresh `Application worker started`.
- Production application queues are empty.
- Post-handoff DB verification shows all 20 new applications are `manual_action_required`; queues are empty.

## Blockers
- Production uses an initial fetch-based HTML snapshot provider; if Workday requires client-rendered form state, replace it with Playwright/browser capture.
- Workday autofill/upload is not implemented yet.
- Temporary Railway token shared in chat was used for deploy and still needs rotation.

## Next steps
- In Telegram, open `/manual_actions`, process one of the new Жанибек Иванов tasks manually, and press Applied.
- Verify `/application_report` after the manual confirmation.
- Then decide whether to replace fetch snapshot capture with Playwright/browser capture before building Workday dry-run autofill.
- Add Workday dry-run autofill for one allowlisted Four Seasons source after preflight is accepted.
- Keep live submit disabled until one controlled manager-reviewed dry-run and one controlled live submission pass certification.
