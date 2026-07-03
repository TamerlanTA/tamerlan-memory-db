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

## Key findings
- Competitor-style auto-apply is not one universal submitter; the durable pattern is staged automation with manual review/fallback.
- Workday is the highest-leverage hosted-form target for AMIGO now because current approved/future-adapter items are concentrated there.
- Live auto-submit should remain blocked until browser preflight/autofill and controlled evidence are proven.

## Validation
- `pnpm --filter @amigo/application-adapters test`
- `pnpm --filter @amigo/application-adapters check`
- `pnpm --filter @amigo/matching test`
- `pnpm --filter @amigo/matching check`
- `pnpm format:check`

## Blockers
- No browser preflight worker exists yet, so production cannot capture real Workday HTML snapshots automatically.
- Workday autofill/upload is not implemented yet.
- Temporary Railway token shared in chat still needs rotation.

## Next steps
- Implement a browser preflight worker for Workday/Four Seasons that captures sanitized HTML/screenshot evidence and runs `workday-form-v1`.
- Add Workday dry-run autofill for one allowlisted Four Seasons source after preflight is accepted.
- Keep live submit disabled until one controlled manager-reviewed dry-run and one controlled live submission pass certification.
