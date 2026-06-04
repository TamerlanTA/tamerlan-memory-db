# Session 2026-06-03 — Payment Confirmation Stabilization

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Audited Stripe Checkout creation, success/cancel URLs, webhook mounting, raw-body verification, reconciliation, idempotent credit grants, and purchase history.
- Implemented a persistent `/credits` post-payment confirmation panel that survives refresh via `localStorage`.
- Added a payment confirmation email through Resend after a newly created `purchase_grant`.
- Kept email sending best-effort: Resend failure logs a warning but does not fail the Stripe webhook or roll back credits.
- Prevented duplicate app confirmation emails on repeated webhook delivery by sending only when a new credit grant is inserted.
- Added `payment_intent_data.description` to Checkout Sessions for clearer Stripe receipt context.
- Added payment confirmation documentation at `docs/payment-confirmation.md`.

## Key findings
- Live webhook endpoint in code/deployment shape: `https://methode.griffesvivienne.com/api/stripe/webhook`.
- Current required Stripe events for this card-only launch flow: `checkout.session.completed`, `checkout.session.expired`, `checkout.session.async_payment_failed`.
- Stripe Customer creation passes `user.email` when creating a new customer; Checkout receives the Stripe Customer id.
- Stripe automatic receipts require Dashboard Customer emails settings. App code now adds a PaymentIntent description, but Dashboard must enable successful-payment receipts.
- One-time paid invoices are not enabled in code; adding them would require `invoice_creation[enabled] = true` and is separate from this launch-safe stabilization.

## Changed files
- `client/src/pages/Credits.tsx`
- `client/src/contexts/LanguageContext.tsx`
- `server/billing.ts`
- `server/billing.test.ts`
- `server/paymentConfirmationEmail.ts`
- `server/paymentConfirmationEmail.test.ts`
- `docs/payment-confirmation.md`

## Verification
- `pnpm exec vitest run server/paymentConfirmationEmail.test.ts server/billing.test.ts`: PASS, 8 tests.
- `pnpm exec vitest run server/paymentConfirmationEmail.test.ts server/billing.test.ts server/labelGenerationCreditSafety.test.ts client/src/domain/order.test.ts server/orderIntentBridge.test.ts server/orderIntent.router.test.ts`: PASS, 28 tests.
- `pnpm check`: PASS.
- `pnpm build`: PASS with known analytics env and bundle-size warnings.
- `pnpm test`: FAIL only on pre-existing generation/texture tests (`label.domain`, `label.productionBatch`, `nanoBanana`, `nanoBananaService.pipeline`, `texturePresets`); payment tests pass.
- Browser smoke on `http://localhost:3001/credits` with dummy analytics + dummy-format Clerk key rendered the page and confirmed the persistent success panel shows credits, amount, and Stripe reference after reload.

## Blockers
- Local `git status` remains broken because of stale worktree metadata at `/Users/tamerlan/.git/worktrees/elated-engelbart`.
- Production live confirmation still requires deploy plus one real post-deploy purchase through the live environment.

## Next steps
- Deploy this batch.
- Verify Stripe Dashboard webhook event subscriptions and successful-payment receipt setting.
- Confirm Resend env is configured if app-side payment emails should send.
- Run one live purchase and repeat webhook delivery to prove UI confirmation, email, receipt, credit grant, and idempotency together.
