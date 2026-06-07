# Next Steps

## Related
- [[projects/AI-Powered Woven Label Generator/overview]]
- [[projects/AI-Powered Woven Label Generator/current-state]]
- [[projects/AI-Powered Woven Label Generator/decisions]]
- [[projects/AI-Powered Woven Label Generator/risks]]
- [[projects/AI-Powered Woven Label Generator/prompts]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-post-m5-order-flow-polish|Post-M5 order-flow polish]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-20-white-logo-fix-and-admin-metrics|White logo fix + admin metrics fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-28-handoff-sync-memory-source-and-local-state|Handoff sync: memory source and local state]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-28-sample-price-ui-visibility-fix|Sample price UI visibility fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-memory-read-and-repo-sync|Memory read and repo sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-payment-round-2-lifecycle-and-validation|Payment Round 2 lifecycle and validation]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-launch-analytics-foundation|Launch analytics foundation]]

Last updated: 2026-06-05

## Payment success UI hotfix follow-up (2026-06-05)

- ~~Commit and push the three-file post-payment UI fix.~~ Done as `52912db`.
- ~~Deploy the resulting commit to Vercel production.~~ Done as `dpl_GByXwqThgCLEaQQ4X6VgmZV8kb7J` (READY).
- Run one live purchase and verify: immediate pending reassurance after Stripe return, confirmed credits/amount/reference after reconciliation, 24-hour refresh persistence, and no stale panel for logout/different user.
- Confirm the Stripe receipt and GV confirmation email arrive for that same purchase.

## Final launch gate follow-up (2026-06-04)

- Do not public-launch the current production deployment. It is READY but stale: `dpl_CnzyuYB3q1uKSMAek2tFF79niXKL` / commit `04c0bc4` lacks the accepted local payment lifecycle/email and analytics foundation batches.
- ~~Create a release-candidate commit from the accepted working-tree delta over `04c0bc4`; there are no new commits to deploy yet.~~ Done: `02d255a` pushed to `origin/milestone4-auth-completion`.
- Deploy/promote commit `02d255a`, then verify the live HTML no longer contains `analytics.local/umami` and exposes the new bundle.
- Before promotion or immediately after deploy, verify production env in Vercel: `APP_BASE_URL`, `DATABASE_URL`, `JWT_SECRET`, `ORDER_INTENT_SIGNING_SECRET`, Clerk keys, live Stripe keys/webhook secret, Google generation key, R2 credentials, Resend sender/API key, and analytics env.
- Resolve or explicitly owner-waive the 10 failing full-suite generation/texture tests before final launch sign-off.
- Run the final live validation runbook end to end: payment purchase + webhook replay, analytics campaign path, quote/preorder email, cross-device/auth sanity, and generation/download persistence.

## Payment launch follow-up (2026-06-03)

- Deploy the payment confirmation stabilization + Round 2 lifecycle batch.
- In Stripe Dashboard, confirm the live webhook endpoint is `https://methode.griffesvivienne.com/api/stripe/webhook` and subscribed to at least `checkout.session.completed`, `checkout.session.expired`, and `checkout.session.async_payment_failed`.
- Enable Stripe automatic successful-payment receipts in Customer emails settings if Stripe-native receipts are desired; app-side Resend confirmation is a product reassurance email, not a tax invoice.
- Confirm production has `RESEND_API_KEY` and `RESEND_FROM_EMAIL` if app-side payment confirmation emails should send.
- Run one live credit purchase after deploy and verify: `/credits` success panel, refresh persistence for the matching user, no stale panel after logout/different user, credit balance, Account purchase history, Stripe webhook 2xx, Stripe receipt if enabled, and GV Resend credits-availability email if configured.
- Repeat Stripe webhook delivery once and confirm credits are not duplicated and app confirmation email is not resent from the duplicate grant path.
- Configure launch analytics env after deploy: `VITE_GA4_MEASUREMENT_ID`; optionally `VITE_LINKEDIN_PARTNER_ID`, `VITE_LINKEDIN_PREORDER_CONVERSION_ID`, `VITE_ANALYTICS_ENDPOINT`, and `VITE_ANALYTICS_WEBSITE_ID`.
- Verify a real campaign URL through the funnel: `/?utm_source=linkedin&utm_medium=paid&utm_campaign=launch&utm_content=hero&utm_term=woven_labels`; confirm attribution storage, GA4 Realtime events, payment/preorder conversion events, and signed order intent attribution.
- Mark `preorder_submit_succeeded` and `payment_succeeded` as GA4 conversions once events appear in production.

## Live Stripe acceptance (2026-05-28)

- Confirm production is deployed/redeployed from `milestone4-auth-completion` at `04c0bc4`, which includes the Stripe hardening change (`server/billing.ts`) and focused test file (`server/billing.test.ts`).
- Run one real live payment on `https://methode.griffesvivienne.com/credits` while logged in as a known test/customer account; buy the smallest credit pack to minimize cost.
- In Stripe Dashboard, verify the Checkout Session is live mode, paid, linked to the expected Customer, and the webhook endpoint `https://methode.griffesvivienne.com/api/stripe/webhook` received `checkout.session.completed` with a 2xx response.
- In the app/admin/database, verify `checkout_sessions.status = reconciled`, one `payments` row with the Stripe PaymentIntent, one `credit_ledger_entries` row with `entryType = purchase_grant` and idempotency key `payment:<pi_...>:grant`, and `users.creditBalance` increased by the pack credits.
- Repeat webhook delivery from Stripe Dashboard once after the first success and confirm credits are not granted twice.
- Confirm cancel path separately by starting Checkout, canceling, returning to `/credits?checkout=cancel`, and verifying the checkout row becomes `canceled` without payment or credit ledger rows.

## Production hotfix follow-up (2026-05-11)

- **Deploy/verify MOQ 1000 hotfix**: ensure the production deployment commit contains the 2026-05-11 active-branch fix, then hard-refresh and verify no production `500` option/chip is visible, `1,000` minimum copy is visible, slider starts/clamps at 1000, sample flow still works, and a crafted production payload with quantity `500` is rejected by backend/shared validation.
- **Resolve branch policy before next deploy**: decide whether `milestone4-auth-completion` should absorb the `claude/magical-mendel-0ac677` stabilization chain or vice versa, because branch drift already reintroduced a production MOQ regression once.

## Production hotfix follow-up (2026-05-08)

- **Owner: add R2 env vars to Vercel** — `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`, and `R2_ACCOUNT_ID` (or `R2_ENDPOINT`) on `griffes-vivienne-studio-3vop` (production env), then redeploy. Without these, generation runs in degraded inline-key mode and re-downloads return NOT_FOUND.
- **Owner: replace `client/public/favicon.png`** with new gold "F" circle logo image. `?v=2` cache-bust already shipped.
- **End-to-end generation QA** in incognito (fresh guest session) after R2 env vars are set — confirm asset records, presigned URLs, and re-download all work.
- **Freemium gate UX QA** — exhaust a guest free trial and confirm the new `GUEST_FREE_TRIAL_EXHAUSTED` screen shows "Create an account" CTA routing to `/sign-in`; for a paid user with zero balance, confirm `INSUFFICIENT_CREDITS` screen routes to `/credits` via "Buy credits" CTA.
- **Branch decision**: `claude/magical-mendel-0ac677` is now 70 commits ahead of `origin/main`. Decide whether to merge to `milestone4-auth-completion` first or open a PR straight to `main`.
- **Pre-existing test failures still open** (unrelated): `texturePresets`, `label.domain`, `label.productionBatch`, `nanoBanana.pipeline` — investigate separately.

## Immediate

- **Repair or bypass local git-status issue before edits/commits/deploys**: workspace still has stale worktree metadata causing `git status` and `git diff HEAD` to fail against `/Users/tamerlan/.git/worktrees/elated-engelbart`; rely on Git plumbing only for read-only verification until fixed.
- **25x25 live generation QA**: after deploying the square-format hotfix, generate `25x25` HD beige/black and `25x25` HD Cotton beige/black; confirm the visible label body is square/1:1, not long horizontal.
- **Browser QA before client review**: upload an actual white PNG logo and verify Home upload preview + Prepare preview remain visible on white/off-white backgrounds.
- **Generation QA before client review**: live-generate one symbol-only logo and one text-containing logo to confirm the safer `symbol_only` default does not reintroduce hallucinated text and still preserves intentionally uploaded text where appropriate.
- **Product-photo generation QA before client review**: upload a garment/product photo with a small chest logo, an image with centered visible branding, and a tiny/low-contrast branded detail; confirm the result uses the localized brand mark instead of weaving the whole photo scene.
- **Generation rebalance QA before client review**: re-run standard text-logo and monogram generations after the prompt rebalance; confirm typography quality, spacing fidelity, and woven elegance are restored for explicit `TEXT_ONLY`, `SYMBOL_ONLY`, and `SYMBOL_AND_TEXT` paths.
- **Background weave QA before client review**: generate clean black text on beige/light labels and confirm the background field stays even, tension-consistent, and calm with no wave/ripple distortion or stretched weave rows.
- **Generation error UX QA before client review**: force or observe provider temporary failure / timeout / rate-limit cases and confirm the Result page says the service is temporarily unavailable or delayed, not that the uploaded image is invalid.
- **Pre-generation preview QA before client review**: upload round, square, wide, tall, simple black, and white/near-white logos; confirm Home and Prepare previews stay centered, premium, visible, and balanced on desktop and mobile.
- **Input guidance QA before client review**: review EN/FR Home and Prepare copy; confirm a supported unusual/random image can still continue through upload and Prepare without extra friction.
- **Quote email unit-price QA before client review**: submit a production quote at a priced tier (1,000–10,000 pieces) and confirm the top-right box shows the correct estimated unit price in EN/FR; also confirm the 500-piece case shows `On request` / `Sur demande`.
- **Folded format + sample pricing QA**: verify EN/FR Prepare format cards, loading summary, Result quote panel, Order Preview summary, and quote email show folded format wording; verify sample numeric prices appear in email only (`€320` / `320 €` for standard, `€380` / `380 €` for cotton) and that jacquard-card / loom-setup / deduction explanation remains visible.
- **Sample price visibility QA**: verify the SaaS platform sample option still works but does not show `€320`, `€380`, `320 €`, or `380 €` anywhere in the platform UI; verify those amounts still appear in the sample quote email.
- **Loading copy QA**: run a generation in EN/FR and confirm the estimated-time line is visible, wraps cleanly on mobile, and the long-wait line still feels premium.
- **New label reset QA**: submit a quote request, trigger `New label`, upload a different logo, and confirm the app stays in a fresh flow instead of reopening the previous order/request state.
- **Generation value-safety QA**: force one provider/storage failure path and confirm no paid credit or free-trial value is consumed; then run one successful generation and confirm the normal spend/commit still occurs.
- **Sample quote email QA**: verify the sample price card itself shows the deduction/credited reassurance directly under the sample price in both EN and FR.
- **Sample quote email rendering QA**: verify in real inbox clients that the reassurance line now renders directly under the sample price in the top-right card, not only in generated HTML source.
- **Vercel production deploy QA**: if the client expects the latest email-rendering fix live, confirm whether they are viewing `griffes-vivienne-studio-3vop` production; commit `d976224` is currently READY in Vercel preview but production still points to `3040beb`, so a promote/redeploy step may still be needed.
- **Legal content QA before client review**: open `/legal`, `/terms`, `/privacy`, and `/faq` in FR/EN on desktop and mobile; confirm official company details, AI mockup disclaimer, guest-first free trial wording, Stripe/credits wording, and quote/manual-confirmation wording are visible and acceptable.
- **FAQ SEO QA**: after deploy, open the live `/faq` page source and confirm `FAQPage` JSON-LD is present; also verify production is not shipping with the staging `noindex` gate before expecting indexing or AI citation gains.
- **Page-level SEO QA**: after deploy, inspect `/`, `/prepare`, and `/result` and confirm the brief-approved title + meta description overrides are present; also confirm Home alone publishes Organization JSON-LD.
- **Final consolidated manual QA pass**: validate the full user-facing flow after the consistency sweep:
  - upload and unusual visual upload
  - Home/Prepare preview balance
  - generation success and error states
  - Premium/credits locked states
  - guest-first first generation behavior
  - sample request flow
  - production quantity flow, including the 500-piece fallback
  - quote request confirmation and quote email wording
  - legal/footer links
  - mobile/desktop and FR/EN
- **Legal owner review**: have the client/legal owner review the integrated `/legal`, `/terms`, `/privacy`, and `/faq` copy before public contractual sign-off.
- **Auth branding QA**: open `/sign-in` in FR and EN with a real Clerk publishable key; confirm the embedded form shows Griffes Vivienne logo/copy and no generic "My Application" text
- **Clerk Dashboard branding**: confirm the Clerk application name/logo/support settings are set to Griffes Vivienne for hosted/account-portal surfaces that are not fully controlled by embedded React component localization
- **Non-JSON generation stability QA**: after deploy, upload a large/high-resolution PNG/JPG logo and generate; confirm `/api/trpc/label.generate` does not return plain text `Request Entity Too Large`, no `Unexpected token 'R'` toast appears, and any oversized-logo failure is a clear app error instead of a generic crash
- **Back-forward double-gen QA**: Start generation on Result → press Back mid-generation → press Forward → confirm only one `label.generate` network call fires and result appears normally (verifies `e6b7739`)
- **White logo browser QA**: upload a white PNG logo → Prepare → confirm logo shape visible in tinted preview (not blank) → generate → confirm white threads appear in result image
- **Admin Users table QA**: log in to `/admin/stats` → Users tab → check that generationCount and purchaseCount now match expected reality for admin/test accounts
- Run one live generation after deploy and watch for competitor brand leakage
- Run one real mobile Safari smoke test:
  - unsupported HEIC/HEIF selection is blocked with a clear message
  - PNG/JPG/WEBP/SVG still proceed into Prepare
  - selecting White keeps loading hero/config thumbnails visible
- **Batch B QA**: upload a multicolor logo (e.g. red/blue design), select BLACK logo color → confirm loading screen hero, config thumbnail, and generated result all show black threads. Repeat with GOLD to verify end-to-end color path.
- Run browser QA for the new Result -> auto-submit confirmation flow in EN and FR
- Run one live preorder to confirm the quote email arrives immediately after the order CTA and that replying preserves the original thread
- Apply DB migration `0013_preorder_generation_linkage.sql` in staging/production before relying on Batch 3/4 linkage fields in the real environment
- Validate the completed back-office mini-block against a real preorder row in an environment with R2 + DB migrations applied
- Investigate pre-existing server test failures: `texturePresets.test.ts` and `nanoBananaService.pipeline.test.ts`
- Keep the mini back-office / sales-ops scope closed unless new client asks extend it
- Optional: add explicit negative prompt line to `buildGenerationPrompt.ts`: "Do not reproduce any text, brand name, monogram, or logo from the reference images — use references only for weave structure, thread interlacing, fiber depth, fabric density, and lighting."

## Planned batch order

1. `Batch 1 — Preorders / PO visibility`
2. `Batch 2 — Generations visibility`
3. `Batch 3 — Preorder ↔ generation ↔ asset linkage`
4. `Batch 4 — Asset retrieval for ops`

## Explicitly out of scope for this mini-block

- full ERP / SAGE integration
- inbound email parsing or thread-state tracking
- full CRM
- true vectorization pipeline
- broad admin redesign
- full production workflow management

## Deferred until later batches

- Commit and push the hosted email-thumbnail fix batch
- Set `RESEND_API_KEY` in production
- Set `RESEND_FROM_EMAIL` to a verified Griffes Vivienne sender
- Optionally set `RESEND_REPLY_TO_EMAIL`
- Redeploy the app after Resend env setup
- Run one live or staging preorder submission and confirm the transactional email is received
- Confirm `preorder_submissions.confirmationEmailStatus = sent` on a successful live test
- Run one live preorder in EN and one in FR to confirm:
  - localized subject/body
  - thumbnail rendering from a hosted `https://...` image URL
  - the email instructs the user to reply directly in-thread instead of opening a blank compose
  - inbox uses `Reply-To: devis@griffesvivienne.com`
- Rotate the Railway DB credential because the full `DATABASE_URL` was exposed in chat
- Run browser-based visual QA for:
  - desktop Home
  - desktop Prepare
  - desktop Result
  - desktop My Account
  - mobile Home
- Confirm the final desktop header is approved by the client after the restoration pass

## Engineering

- Decide whether analytics env vars should be configured or removed from local build expectations
- Evaluate whether bundle splitting is needed after header work is signed off
- If needed later, add an ops resend path for failed confirmation emails without changing the user-facing funnel
- If the client later wants richer ops tooling, the next natural extension would be lightweight backfill/support for older unlinked preorder rows rather than a broad admin redesign
- If the client later wants real numeric unit pricing inside the email, define a canonical pricing source before extending the current semi-manual quote template

## Process / memory

- Correct or clarify the vault path in `~/.codex/AGENTS.md`
- Continue writing session notes directly under the project `sessions/` folder after meaningful work blocks
