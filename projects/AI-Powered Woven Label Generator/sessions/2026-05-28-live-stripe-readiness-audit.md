# Session 2026-05-28 — Live Stripe Readiness Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Audited live Stripe credit-pack implementation in the real workspace `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu`.
- Confirmed active commit/branch by Git plumbing despite broken `git status`: `milestone4-auth-completion` at `ed3fd26` / `origin/milestone4-auth-completion`, commit message `Fix production MOQ regression`.
- Confirmed `ed3fd26` includes the active-branch MOQ 1000 fix: `client/src/domain/order.ts`, `shared/orderIntentBridge.ts`, `OrderLabelsPanel`, and EN/FR copy.
- Audited Stripe Checkout creation, webhook raw-body verification, app/env routing, billing router, Credits success/cancel UX, and `0007_phase3_checkout_payments.sql`.
- Added minimal hardening: `server/billing.ts` now refuses to reconcile/grant credits from `checkout.session.completed` unless `session.payment_status === "paid"`.
- Added focused tests in `server/billing.test.ts` for raw-body verification, unpaid fail-closed behavior, and paid payment/credit grant persistence.

## Key findings
- Checkout uses Stripe-hosted Checkout Sessions with `mode: "payment"`, customer linkage, `client_reference_id`, success/cancel URLs from `APP_BASE_URL`, and app DB persistence of the checkout session.
- Webhook endpoint disables Vercel body parsing and Express mounts `express.raw({ type: "application/json" })` before JSON middleware, so Stripe signature verification receives raw bytes.
- Credit grants are idempotent via `credit_ledger_entries.idempotencyKey = payment:<paymentIntentId>:grant`; schema also has unique constraints on Stripe checkout session and payment intent.
- Payment persistence writes `payments`, credit ledger writes `purchase_grant`, and `users.creditBalance` is updated transactionally.
- Credits page polls `billing.getCheckoutStatus` after Stripe success until status is `reconciled`, then invalidates auth/balance queries and clears URL params; cancel flow marks open checkout as canceled.
- Live production env is user-reported configured, but not independently verified from Vercel during this session.

## Blockers
- Do not claim live payments work until one real live payment is completed and verified in Stripe, app UI, and DB/admin.
- Local `git status` still fails with `fatal: not a git repository: /Users/tamerlan/.git/worktrees/elated-engelbart`; commit/remote were verified with `git rev-parse`, `git log`, `git show`, and `git ls-remote`.

## Verification
- `pnpm check`: PASS.
- `pnpm build`: PASS, with pre-existing analytics env and large chunk warnings.
- `pnpm vitest run server/billing.test.ts`: PASS, 3 tests.
- `pnpm vitest run client/src/domain/order.test.ts server/orderIntentBridge.test.ts server/orderIntent.router.test.ts`: PASS, 19 tests; preorder email failure logs are expected test fixtures.

## Next steps
- Deploy the new hardening commit after review.
- Run one real live Stripe payment on `https://methode.griffesvivienne.com/credits`.
- Verify Stripe Dashboard event delivery for `checkout.session.completed`.
- Verify app UI credit balance increases and DB/admin rows exist in `checkout_sessions`, `payments`, `credit_ledger_entries`, and `users.creditBalance`.
