# Session 2026-06-03 — Payment Round 2 Lifecycle and Validation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Hardened `/credits` post-payment success lifecycle after Batch 1.
- Added `client/src/domain/creditsSuccessLifecycle.ts` and tests to make the confirmation summary user-bound, TTL-bound, and parse-safe.
- Updated `client/src/pages/Credits.tsx` so persisted success state survives refresh only for the matching authenticated user and expires after 24 hours.
- Adjusted `server/paymentConfirmationEmail.ts` wording so Stripe owns the official payment receipt while GV confirms credits are available on the platform.
- Updated `docs/payment-confirmation.md` with the final success lifecycle and communication split.
- Audited analytics only; no analytics implementation was added.

## Key findings
- Previous success state was `localStorage` only, indefinite, and not tied to a user, which created stale/shared-browser confusion risk.
- Final behavior: store `gv_last_confirmed_purchase` only after reconciled checkout; include `userKey`, `confirmedAt`, and `expiresAt`; show only to matching authenticated user; remove on malformed/legacy/expired/mismatched/no-auth state.
- Persistence is same-browser/same-device only; durable truth remains DB credit balance, purchase history, Stripe payment, and webhook reconciliation.
- Stripe receipts and GV confirmation now have clear roles: Stripe payment receipt/invoice-like reassurance; GV credits-added/platform reassurance.
- Analytics state: Umami placeholder exists in `client/index.html`; best-effort `window.umami.track` and `window.dataLayer.push` exist for order/preorder events; no in-code GA4/GTM loader, no UTM persistence, no LinkedIn attribution, and no payment funnel events yet.

## Validation
- `pnpm exec vitest run client/src/domain/creditsSuccessLifecycle.test.ts server/paymentConfirmationEmail.test.ts server/billing.test.ts` PASS: 12 tests.
- `pnpm check` PASS.
- `pnpm build` PASS with existing analytics env placeholder and bundle-size warnings.
- Full `pnpm test` still fails on pre-existing generation/texture expectation tests; payment/lifecycle/email tests pass.

## Blockers
- Production live purchase validation still needs deploy plus one real payment test.
- Production app confirmation email requires `RESEND_API_KEY` and `RESEND_FROM_EMAIL`.
- Stripe automatic receipts require Stripe Dashboard Customer email receipt setting to be enabled.
- Build warnings remain for missing `VITE_ANALYTICS_ENDPOINT` and `VITE_ANALYTICS_WEBSITE_ID`.

## Next steps
- Deploy the payment Round 2 changes.
- Verify production env: live Stripe keys/webhook secret, `APP_BASE_URL=https://methode.griffesvivienne.com`, Resend sender, and analytics env if Umami should be live.
- Run one live credit purchase and verify success panel, refresh persistence, credit balance, Account purchase history, Stripe webhook 2xx, Stripe receipt, GV email, and duplicate webhook idempotency.
