# Session 2026-07-01 — Emergency Guest Abuse Controls

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Added production emergency protections for anonymous/free guest generation abuse.
- Added `runtime_controls` DB table plus `/admin/stats` emergency card with a kill switch for free guest generations.
- Added `abuse_alerts` DB table and `server/abuseMonitor.ts` email alerting when guest generation attempts exceed 10 within 5 minutes.
- `label.generate` now blocks guest free generations before storage/provider work when the kill switch is enabled. Paid and signed-in credit generations remain available.
- Kill switch UX maps `GUEST_FREE_GENERATIONS_DISABLED` to the existing temporary-service-unavailable presentation instead of consuming the free trial.
- Production DB migration `0016_emergency_guest_generation_controls.sql` was applied manually and verified.
- Committed locally as `42ec05e` (`Add emergency guest generation controls`) and deployed to Vercel production `dpl_4QGttkgEdT6qWQszTLH7xMSi3JQB`, aliased to `https://methode.griffesvivienne.com`.

## Key findings
- Production Resend env is configured (`RESEND_API_KEY`, `RESEND_FROM_EMAIL`, `RESEND_REPLY_TO_EMAIL`); no dedicated `ABUSE_ALERT_EMAIL` / `EMERGENCY_ALERT_EMAIL` exists, so alerts fall back to `RESEND_REPLY_TO_EMAIL`.
- Production DB after migration: `runtime_controls` exists, `abuse_alerts` exists, free guest kill switch row is absent, which means enabled by default.
- Current production 5-minute guest generation count was 0 and `abuse_alerts` had 0 rows at verification time.
- Live client bundle is `assets/index-MvidJn4Q.js`; live domain returns HTTP 200.

## Verification
- `npx vitest run server/labelGenerationCreditSafety.test.ts` PASS (4 tests).
- Full `npx vitest run` PASS (41 files, 247 tests).
- `npx tsc --noEmit` PASS.
- `npm run build` PASS.
- `git diff --check` PASS.

## Blockers
- GitHub push failed because local HTTPS credentials are unavailable: `fatal: could not read Username for 'https://github.com': Device not configured`.
- Live bundle still contains Clerk `pk_test`; this remains a production config cleanup blocker outside this emergency-controls commit.

## Next steps
- Configure `ABUSE_ALERT_EMAIL` or `EMERGENCY_ALERT_EMAIL` in Vercel production if alerts should go somewhere other than `RESEND_REPLY_TO_EMAIL`.
- Admin should open `/admin/stats` and confirm the Emergency Controls card renders under an authenticated admin session.
- Replace Clerk dev publishable/secret keys with live keys and redeploy.
- Push local commits once GitHub credentials are available.
