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

Last updated: 2026-07-02

## Generation input/output validation blocks (2026-07-02)

1. ~~Blocks 1 (input), 2 (output), demo-stability recovery, semantic-gate diagnostics, and the 2026-07-02 gate-tuning commit are pushed and production deployed.~~ Latest deployment: `dpl_A7UutKtxygsPfRr9jx3x83mtmXzr`, READY, aliased to `https://methode.griffesvivienne.com`.
2. Run live production smoke for the exact client complaints: photographed woven label / logo on neutral surface should pass input validation; `20x50` and other elongated formats should not ship as square outputs after recovery.
3. Watch production `generationRuns` for `INPUT_IMAGE_NOT_LOGO`, `OUTPUT_IMAGE_REJECTED`, `FORMAT_MISMATCH`, and `recovered` frequency; tune classifier prompts or generation prompt if any category spikes.
4. Optional follow-up: dedicated `generationRuns` column for semantic rejection reasonCodes if analytics need more than the normalized error code (output reasonCode currently lands in `validatorReason`).
- See session notes: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block1-input-semantic-validation|Block 1 input semantic validation]] and [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block2-output-semantic-validation|Block 2 output semantic validation]].
- Review session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block1-review-and-block2-prompt|Block 1 review and Block 2 prompt]].

## Immediate emergency control validation (2026-07-01)

1. Log in as admin on production and confirm `/admin/stats` renders the Emergency Controls card.
2. Temporarily toggle "Disable free guests" during a controlled test window, attempt one guest free generation, and confirm it stops before provider usage with the temporary-service-unavailable UX; then re-enable free guests.
3. Configure `ABUSE_ALERT_EMAIL` or `EMERGENCY_ALERT_EMAIL` in Vercel Production if abuse alerts should go to a dedicated operations address instead of the current `RESEND_REPLY_TO_EMAIL` fallback.
4. ~~Push local commit `42ec05e` plus prior local-only stabilization commits to GitHub once HTTPS credentials are available.~~ Resolved on 2026-07-02: branch push auth was fixed and `origin/milestone4-auth-completion` now includes the stabilization stack through `96674e6`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-emergency-guest-abuse-controls|Emergency guest abuse controls]].

## Immediate stabilization continuation (2026-07-01)

1. Run the requested production smoke matrix on real devices/accounts: mobile Safari HD, mobile Safari Taffeta, desktop HD, paid final Taffeta.
2. After each real generation, inspect Vercel logs and `/admin/stats` Recent Generation Diagnostics for `diagnosticStage`, `diagnosticAttempt`, `upstreamStatus`, `normalizedErrorCode`, `validatorReason`, `referenceCount`, `inputImageCount`, and `inputBytes`.
3. Replace Clerk test keys with live keys in Vercel Production (`VITE_CLERK_PUBLISHABLE_KEY`, server `CLERK_SECRET_KEY` / publishable companion if used), redeploy, and confirm live bundle no longer contains `pk_test`.
4. Decide whether to clear the stale `VITE_ANALYTICS_ENDPOINT=/analytics.local` env var from Vercel Production. The app now skips invalid Umami endpoints, but removing the env cleans the bundle/config.
5. Configure Sentry/log drain access and record the project DSN/token or Vercel integration status; current local environment cannot enable it.
6. ~~Push local commits through `cf2a318` to GitHub once local GitHub HTTPS credentials are configured.~~ Resolved on 2026-07-02; the branch is synced through `96674e6`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-diagnostics-stale-runs-and-config-cleanup|Diagnostics, stale runs, and config cleanup]].

## Immediate guest free-trial validation (2026-07-01)

1. Smoke production from one real mobile device: complete one guest free generation, refresh, and confirm retrying does not grant another free generation for the same cookie/session.
2. Cookie-reset/incognito bypass is open by product decision after `cf2a318`; do not treat it as fixed unless free generation moves behind account/email verification.
3. Smoke a legitimate logged-in first free generation and a paid-credit generation to confirm authenticated entitlement paths still work.
4. Push local commits `d25e7b1`, `69751ed`, `883ca3c`, `cac32db`, `16447cd`, `f930791`, and `cf2a318` to GitHub once local GitHub HTTPS credentials are configured.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-guest-free-trial-hardening|Guest free-trial hardening]].

## Immediate reliability fixes from root-cause audit (2026-07-01)

1. ~~Patch `server/nanoBananaService.ts` so validation retry failures salvage `lastImageBase64` and return the previously generated image with validator warning metadata instead of throwing a no-result error.~~ Done in `16447cd`, deployed as `dpl_64beaG6APr3XdPmTf44QB2RAt3UC`.
2. ~~Reduce retry request complexity: cap material/style references to at most 3 overall, and use fewer references on retry, especially for Taffeta.~~ Done in `16447cd`: 3 references max, 1 reference on single-pass retry, 0 extra material references on HD Cotton motif retry.
3. ~~Add a Taffeta-specific safety pass: prefer 2-3 curated references and avoid sending previous image + source logo + 5 material references together.~~ Done in `16447cd`: Taffeta dark/light variants now cap material references to 3, white still uses the dedicated white reference.
4. Persist structured generation diagnostics: normalized error code, upstream status/code, model id, generation stage, attempt number, validator status/reason, reference count, input image count, and input byte sizes.
5. Convert retryable provider failures into a clear structured client state (`TEMPORARY_UPSTREAM_UNAVAILABLE` / service unavailable), not a generic interrupted-generation screen.
6. Add a cleanup/reaper path for stale `generationRuns.status = started` rows and log whether the request was aborted, timed out, or failed before finalization.
7. After the reliability patch, run a production smoke matrix: mobile Safari guest HD, mobile Safari Taffeta, desktop control HD, paid final Taffeta, and retry/validator-warning log watch.
8. Production cleanup after the stability patch: replace Clerk development keys with live keys, fix/remove `/analytics.local/umami`, set or disable `OAUTH_SERVER_URL`, and enable Sentry/log-drain access.
- See audit note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-generation-reliability-root-cause-audit|Generation reliability root-cause audit]].

## Immediate generation stability follow-up (2026-07-01)

1. Run a real production generation smoke after deployment `dpl_CWkgLwJ42GA34Mjq7cN4n5ir2shY`: at minimum one mobile Safari guest upload/continue with the same phone logo from the screen recording, one full mobile generation, and one desktop control generation.
2. Watch Vercel logs for `[NanoBanana] Returning generated image despite validation warning`; these should now end in successful customer results rather than final-step errors.
3. Push local commits `d25e7b1`, `69751ed`, `883ca3c`, and `cac32db` to GitHub once local GitHub HTTPS credentials are configured.
4. Add persistent generation metadata for validator status/reason so admin can distinguish perfect `pass` results from best-effort results.
5. Keep provider/storage failure behavior fail-closed: do not spend credit/free-trial when no image exists or result storage fails.
6. If mobile still fails after the upload/storage hotfix, add browser-side telemetry around upload file size, preview DataURL length, storage persistence failures, and `label.generate` request shape; then consider a server-side mobile/photo preprocessor.

## Immediate generation recovery (2026-06-30)

1. ~~Decide/implement fail-closed validator policy for the current recovery path.~~ Done locally on 2026-06-30: non-pass validation now returns failure before storage/bookkeeping.
2. ~~Normalize Gemini `400 INVALID_ARGUMENT` into a clearer code path.~~ Done locally on 2026-06-30: provider invalid argument without image context maps to `TEMPORARY_UPSTREAM_UNAVAILABLE`.
3. ~~Convert exhausted free-trial and insufficient-credit paths to explicit tRPC/domain errors.~~ Done locally on 2026-06-30: router emits `FORBIDDEN` with `GUEST_FREE_TRIAL_EXHAUSTED` / `INSUFFICIENT_CREDITS`; Result uses premium-lock flow.
4. ~~Repair local release tooling before hotfix deploy: fix stale git worktree metadata and restore a stable `.vercel/project.json`.~~ Done locally on 2026-06-30; `git status` works and Vercel CLI is linked to the production project.
5. ~~Deploy the local generation stabilization hotfix after reviewing the changed files and creating the release commit/deploy package.~~ Done via direct Vercel production deploy `dpl_HkE8JkNdaiQkDiCLkBgB5EE5pMuv`; local commit is `d25e7b1`, but GitHub push is still blocked by local HTTPS credentials.
6. Replace production Clerk test keys with live keys and redeploy; then smoke auth, guest claim, credits, and generation access.
7. Improve generation run observability: persist normalized error code, upstream status/code, model id, attempt count, and validator reason in DB or admin-visible metadata.
8. After deploy, run a live generation matrix: guest first preview, exhausted guest, paid user final, zero-credit user, HD/HD_COTTON/SATIN/TAFFETA, and one download-after-refresh check.
- See audit note: [[projects/AI-Powered Woven Label Generator/sessions/2026-06-30-generation-platform-health-audit|Generation platform health audit]].

## Pre-launch gate (2026-06-23)

1. Resolve or explicitly owner-waive the 10 failing `pnpm test` failures before public launch.
2. Repair or bypass the broken `git status` worktree metadata before any release commit/deploy decision.
3. Verify Vercel production is on intended commit `0e34242` or the chosen release commit, with production env present: `DATABASE_URL`, `JWT_SECRET`, `ORDER_INTENT_SIGNING_SECRET`, Clerk keys, Stripe live secret/webhook secret, `APP_BASE_URL`, Google generation key, R2 credentials, Resend sender/API key, and GA4 measurement ID.
4. Apply or manually verify DB migrations through `0013_preorder_generation_linkage.sql`; note that `0013` is not currently in `drizzle/meta/_journal.json`.
5. Run one live generation and confirm R2-backed result URL plus download retrieval work after refresh.
6. Run one live Stripe purchase and verify checkout return UI, webhook 2xx, credit grant, Account/admin payment visibility, duplicate webhook idempotency, Stripe receipt, and GV Resend confirmation.
7. Run one preorder/quote submission and verify DB row, email delivery, thumbnail URL, reply-to, and admin preorder visibility.
8. Validate GA4 production events for generation, preorder, checkout, and payment success; only `landing_view` has prior proof.

## GA4 activation follow-up (2026-06-09)

1. ~~Correct the gtag queue wrapper to use Google's canonical `dataLayer.push(arguments)` contract.~~ Done in `808feb0`.
2. ~~Add regression coverage for GA4 `config` and custom `event` command shape.~~ Done; focused suite passes.
3. ~~Deploy the focused fix.~~ Done as `dpl_95CwShem7HEmRtXQxXfeuwZXy8wA`.
4. ~~Verify `landing_view` in Realtime and DebugView.~~ Done at 2026-06-09 13:37 +05.
5. Validate `generation_started` and `generation_succeeded` with a real production generation.
6. Validate `preorder_submit_succeeded` with a real quote/preorder submission.
7. Validate `checkout_started` and `payment_succeeded` with the next real successful credit purchase.
8. Correct or remove the invalid Umami production endpoint to eliminate its unrelated console error.

## Analytics launch gate (2026-06-08)

1. Add the real `VITE_GA4_MEASUREMENT_ID` to Vercel Production.
2. Correct or remove the invalid production Umami configuration.
3. Redeploy production and verify the GA4 script, `window.gtag`, and `window.dataLayer` are active.
4. Validate at minimum `landing_view`, `generation_started`, `generation_succeeded`, `preorder_submit_succeeded`, `checkout_started`, and `payment_succeeded` in GA4 DebugView/Realtime.
5. Record validation evidence and only then mark launch analytics ready.

## Success moment polish follow-up (2026-06-08)

- ~~Review and commit the three-file success-moment UI batch.~~ Done as `a2828ab`.
- ~~Deploy to Vercel production.~~ Done as `dpl_Cg7nmpbUSUMTPukLJydqMeUN2zjk` (READY).
- ~~Commit and deploy the two-file success checkmark micro-polish.~~ Done as commit `e295729`, production deployment `dpl_58iSzmD3Pv6BiuesXjiQm8Fdvp5Q`.
- Verify the confirmed panel after one real purchase on desktop/mobile.
- Confirm the updated balance has refreshed before the customer reaches the confirmed state; existing query invalidation remains unchanged.

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

- ~~**Repair or bypass local git-status issue before edits/commits/deploys**: workspace still has stale worktree metadata causing `git status` and `git diff HEAD` to fail against `/Users/tamerlan/.git/worktrees/elated-engelbart`; rely on Git plumbing only for read-only verification until fixed.~~ Done locally on 2026-06-30; ordinary `git status --short --branch` works again.
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
