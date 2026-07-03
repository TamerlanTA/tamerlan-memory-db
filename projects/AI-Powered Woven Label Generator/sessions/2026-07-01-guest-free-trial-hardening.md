# Session 2026-07-01 — Guest Free-Trial Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Audited the first-free-generation enforcement path.
- Confirmed ordinary refresh was already protected by the existing guest cookie/session path.
- Found a critical bypass: cookie deletion, incognito, or a new browser could create a new `guest_sessions` row and receive another free generation.
- Added `guest_trial_claims` schema and migration to persist a hashed anonymous claim.
- Added `server/freeTrialGuard.ts` to hash IP + user-agent + accept-language without storing raw IP/UA.
- Updated `label.generate` to pre-check consumed claims before storage/provider work and to use a claim-level advisory lock for guest free trials.
- Updated `createFreeTrialGenerationWithCommit` to atomically consume the guest trial claim only after a generated result asset is stored.
- Applied and verified the production DB migration.
- Committed `f930791` (`Harden guest free trial enforcement`) and deployed production `dpl_AXCHFYpWU6tjUyqZBZPmCe1iCJTj`, aliased to `https://methode.griffesvivienne.com`.

## Key findings
- The previous first-free-generation rule was real only within the same browser cookie.
- The new rule blocks simple anonymous bypasses from the same claim: refresh, same cookie, cookie reset, incognito/new guest session, and parallel same-claim attempts.
- Anonymous enforcement is still not absolute against VPN/new IP/new device; true non-bypassability requires stronger identity such as account/email OTP/phone/payment.

## Blockers
- GitHub push remains blocked by local HTTPS credential configuration; branch is ahead of origin by 6 commits.

## Verification
- `node_modules/.bin/vitest run server/labelGenerationCreditSafety.test.ts` PASS (4 tests).
- `node_modules/.bin/tsc --noEmit` PASS.
- `node_modules/.bin/vitest run` PASS (41 files, 247 tests).
- `npm run build` PASS.
- Live domain `https://methode.griffesvivienne.com` returns HTTP 200 after deploy.

## Next steps
- Run real-device production smoke for guest first generation, refresh, cookie reset/incognito, logged-in first free generation, and paid-credit generation.
- Decide whether the business needs anonymous claim enforcement or stricter email/account verification before the free generation.
