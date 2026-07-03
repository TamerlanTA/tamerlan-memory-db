# Risks

## Related
- [[projects/AI-Powered Woven Label Generator/overview]]
- [[projects/AI-Powered Woven Label Generator/current-state]]
- [[projects/AI-Powered Woven Label Generator/decisions]]
- [[projects/AI-Powered Woven Label Generator/next-steps]]
- [[patterns/git/verify-git-base-before-implementation|Verify git base before implementation]]
- [[patterns/auth/use-useauth-logout|Use useAuth.logout()]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-post-m5-order-flow-polish|Post-M5 order-flow polish]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-28-handoff-sync-memory-source-and-local-state|Handoff sync: memory source and local state]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-28-sample-price-ui-visibility-fix|Sample price UI visibility fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-memory-read-and-repo-sync|Memory read and repo sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-payment-confirmation-stabilization|Payment confirmation stabilization]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-payment-round-2-lifecycle-and-validation|Payment Round 2 lifecycle and validation]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-launch-analytics-foundation|Launch analytics foundation]]

Last updated: 2026-07-02

## Gate tuning production residual risks (2026-07-02)

- **Production smoke still pending for the new gate tuning:** commit `96674e6` is pushed and deployed as `dpl_A7UutKtxygsPfRr9jx3x83mtmXzr`, but real customer-like tests still need to prove the previous over-rejection case now passes and 20x50-style outputs no longer ship as square labels.
- **Format mismatch may require prompt tuning if frequent:** output validation now rejects obvious ratio violations as `FORMAT_MISMATCH` and can auto-recover once. If production shows frequent `FORMAT_MISMATCH` or `validatorStatus=recovered`, the next fix should improve generation prompt/layout control rather than only validator wording.
- **Semantic gate is still probabilistic:** input/output classifiers reduce bad outcomes but are model-based. Monitor false accepts/rejects from `/admin/stats` and `generationRuns.validatorReason`.
- **GitHub sync blocker resolved:** the stabilization branch is now pushed through `96674e6`; old "local-only commits" risk is closed for this workstream.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-gate-tuning-production-deploy|Gate tuning production deploy]].

## Emergency guest abuse control residual risks (2026-07-01)

- **Alert recipient fallback:** no dedicated `ABUSE_ALERT_EMAIL` / `EMERGENCY_ALERT_EMAIL` is configured in Vercel. Alerts currently fall back to `RESEND_REPLY_TO_EMAIL`; configure a dedicated ops recipient if needed.
- **Admin UI not browser-auth smoke tested:** deployment and DB were verified, but the Emergency Controls card still needs one authenticated admin browser check on `/admin/stats`.
- **Guest abuse is mitigated, not eliminated:** the kill switch can stop free guest spend quickly, but anonymous free trials remain cookie/session-based by product decision and can still be bypassed by incognito/cookie reset unless stronger identity is required.
- **GitHub sync blocked:** local commit `42ec05e` is deployed but not pushed because local HTTPS GitHub credentials are unavailable.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-emergency-guest-abuse-controls|Emergency guest abuse controls]].

## Stabilization batch residual risks (2026-07-01)

- **Production smoke still pending:** code/deploy are ready for the requested smoke matrix, but real mobile Safari HD, mobile Safari Taffeta, desktop HD, and paid final Taffeta have not been executed in this work block. Paid final Taffeta requires an authenticated account with paid credits.
- **Clerk production key blocker remains:** live bundle still contains `pk_test`, so production Clerk keys must be replaced in Vercel/Clerk Dashboard and redeployed before launch sign-off.
- **Sentry/log drain still not enabled from this machine:** no `SENTRY_AUTH_TOKEN` or log drain credentials are available locally. Configure Sentry/log drain in the hosting/observability dashboard.
- **Anonymous free-trial bypass remains by product choice:** free trial is again cookie/session-based only. Refresh and same-cookie attempts are protected, but deleting cookies/incognito/new browser can create a new guest session unless the product moves the free generation behind account/email verification.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-diagnostics-stale-runs-and-config-cleanup|Diagnostics, stale runs, and config cleanup]].

## Guest free-trial enforcement risks (2026-07-01)

- **Cookie-reset bypass risk is intentionally open again:** `f930791` blocked repeat anonymous claims by IP + user-agent + language, but that approach was removed from active code at user request in `cf2a318` because it could block legitimate users. Current protection is cookie/session + DB atomic commit + guest-session lock only.
- **Residual anonymous-abuse risk:** deleting cookies/incognito/new browser can create a fresh guest session. To make the free generation truly non-bypassable, require account/email OTP/phone/payment verification before granting the free generation.
- ~~**Shared-network false-positive risk from IP/UA/language claim:**~~ resolved by removing the claim guard from active code in `cf2a318`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-guest-free-trial-hardening|Guest free-trial hardening]].

## Generation reliability root-cause risks (2026-07-01)

- ~~**Critical no-result retry risk:** production still returns customer-facing generation errors when the first Gemini attempt produced an image but a later validator-driven retry fails with upstream `400 INVALID_ARGUMENT`. The previous image is discarded instead of being returned as best-effort output.~~ Fixed and deployed on 2026-07-01 in `16447cd` / `dpl_64beaG6APr3XdPmTf44QB2RAt3UC`: retry failures now return the previous generated image when one exists.
- **High Taffeta instability risk:** fresh production data before the fix showed Taffeta at 7 successes / 7 failures since `2026-06-30 00:00:00` DB time. The code now caps material references and lightens retry payloads, but real production Taffeta smoke testing is still required before closing this risk.
- ~~**High retry-payload complexity risk:** validation retries combine a long corrective prompt, previous generated image, source logo, and material references. This is the most likely current trigger for provider `INVALID_ARGUMENT` responses.~~ Reduced on 2026-07-01: references are capped to 3 per request, single-pass retries use 1 reference, and HD Cotton motif retries use no extra material references.
- **Medium stuck-run risk:** production DB contains a new `started` generation row from 2026-07-01 plus older stale `started` rows, indicating some interruptions are not finalized into success/failure state.
- **Medium customer-trust UX risk:** retryable provider failures are still surfaced through generic interruption screens in some paths/screenshots, so users cannot distinguish a temporary provider failure from a bad upload or app crash.
- **Medium production cleanliness risk:** live console/runtime still has broken Umami script loading, Clerk development-key warning, and missing `OAUTH_SERVER_URL` log noise.
- **Medium observability risk:** production run records do not persist enough structured metadata to rapidly separate validator retry failures, provider invalid arguments, payload image counts/sizes, model id, and exact attempt stage.
- See audit note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-generation-reliability-root-cause-audit|Generation reliability root-cause audit]].

## Generation platform health risks (2026-06-30)

- ~~**High no-result UX risk:** the 2026-06-30 fail-closed validator policy caused generations that already had an image to fail at the final validation step, leaving customers without a result.~~ Fixed and deployed on 2026-07-01: `server/nanoBananaService.ts` now returns the best generated image when image data exists and validator status is `fail` or `protocol_error`.
- **Generation quality tradeoff:** because validator warnings no longer block the image response, some returned images may be off-spec on material/color/format. This is an intentional stability tradeoff until persistent validator metadata and a softer retry/regenerate UX exist.
- ~~**High mobile upload crash risk:** large iPhone logo/image uploads could be stored as full DataURLs in `localStorage` during upload continuation, triggering Safari quota errors and the generic React fallback screen before generation.~~ Fixed and deployed on 2026-07-01 in `cac32db` / `dpl_CWkgLwJ42GA34Mjq7cN4n5ir2shY`: previews are rasterized/capped, heavy originals are skipped, and generator storage reads/writes are guarded.
- ~~**High provider/error UX risk:** recent production logs show Gemini `400 INVALID_ARGUMENT` mapped to `GENERATION_FAILED_UNKNOWN` and surfaced as HTTP 500.~~ Improved locally on 2026-06-30: provider `INVALID_ARGUMENT` without image context maps to `TEMPORARY_UPSTREAM_UNAVAILABLE`.
- **High auth readiness risk:** production Vercel env and live client bundle are using Clerk test keys (`pk_test` / `sk_test`) while the deployment is production.
- ~~**Medium entitlement UX risk:** exhausted guest free-trial paths throw plain `Error` strings and appear in production logs as 500s rather than a clear domain state such as `GUEST_FREE_TRIAL_EXHAUSTED`.~~ Improved locally on 2026-06-30: generation router throws explicit `FORBIDDEN` codes and Result page routes these into premium-lock state.
- **Medium observability risk:** `generationRuns.errorMessage` stores coarse messages like `GENERATION_FAILED_UNKNOWN`; upstream status/code/model/attempt/validation reason are mostly only in ephemeral logs.
- ~~**Medium release operations risk:** `git status` and local `.vercel` project linking are broken in the workspace, increasing hotfix/deploy mistake risk.~~ Fixed locally on 2026-06-30: stale `.claude/worktrees/*` gitlinks were removed from the index, worktree/Vercel local paths are ignored, `.vercel/project.json` was restored, and Vercel CLI can inspect the linked production project.
- **Current non-blocker:** R2 is no longer the active storage blocker in production; recent generation assets are being persisted to R2-backed keys.
- See audit note: [[projects/AI-Powered Woven Label Generator/sessions/2026-06-30-generation-platform-health-audit|Generation platform health audit]].

## Pre-launch technical audit risks (2026-06-23)

- ~~**High launch risk: full test suite is red.**~~ Resolved locally on 2026-06-30 after generation stabilization and stale test updates: `vitest run` PASS (41 files, 241 tests), `tsc --noEmit` PASS, build PASS.
- **High storage/env risk: R2 is mandatory in production.** `server/assets.ts` only falls back to inline data URLs when `!ENV.isProduction`; missing R2 credentials in production will fail asset storage/generation rather than degrade gracefully.
- **High migration risk: `0013_preorder_generation_linkage.sql` is outside Drizzle journal.** The file exists but `drizzle/meta/_journal.json` ends at `0012_preorder_confirmation_email`; production/staging must be checked or manually migrated before relying on linkage columns.
- **High live validation gap remains:** one real production generation/download, one live Stripe purchase + webhook replay/idempotency, one preorder email, Resend delivery, Stripe receipt, and flow-specific GA4 events still require proof.
- ~~**Medium release operations risk:** ordinary `git status` still fails due to stale worktree metadata, so release dirty-state checks are unreliable until repaired.~~ Resolved locally on 2026-06-30; `git status --short --branch` is reliable again after removing tracked `.claude/worktrees/*` gitlinks.
- **Medium signing secret risk:** `ORDER_INTENT_SIGNING_SECRET` falls back to `JWT_SECRET`, then a fixed dev fallback with a production warning. Production must have a strong explicit signing secret.

## GA4 activation residual risks (2026-06-09)

- ~~Production missing `VITE_GA4_MEASUREMENT_ID`.~~ Resolved; `G-W5B405NSQE` is present in Production and deployed.
- ~~DebugView verification remains open.~~ Resolved: official Tag Assistant debug mode produced `page_view` and `landing_view` in GA4 DebugView.
- ~~Production validation access blocker.~~ Resolved: the authorized Chrome session connected and production was validated directly.
- Do not report generation, preorder, checkout, or payment-success events as GA4-verified until each appears in DebugView/Realtime during a real authenticated flow.
- ~~A real production landing visit did not produce a visible `landing_view` in Realtime.~~ Resolved after deployment `dpl_95CwShem7HEmRtXQxXfeuwZXy8wA`; Realtime showed `landing_view` twice.
- ~~The gtag wrapper queued rest-parameter arrays instead of Google's required `arguments` command object.~~ Fixed in commit `808feb0` and regression-tested.
- Production Umami remains misconfigured at `/analytics.local/umami`; this does not block the now-verified GA4 pipeline but still produces a console syntax error.

## Analytics truth audit risks (2026-06-08)

- **Critical analytics configuration gap**: production Vercel env is missing `VITE_GA4_MEASUREMENT_ID`, so the deployed GA4 loader never initializes.
- **Critical verification gap**: no GA4 DebugView or Realtime proof exists for any launch event.
- **High fallback analytics failure**: the production Umami script URL `/analytics.local/umami` returns non-JavaScript content and throws `SyntaxError: Unexpected token '<'`.
- Event instrumentation is deployed, but production traffic, generation, preorder, checkout, and payment-success events are not currently proven in any functioning analytics destination.

## Post-payment success UI risk (2026-06-05)

- ~~Production showed no post-payment confirmation when the protected checkout-status query was delayed or unavailable after Stripe redirect.~~ Fixed and deployed in production commit `52912db`, deployment `dpl_GByXwqThgCLEaQQ4X6VgmZV8kb7J`.
- Live bundle verification confirms the pending/confirmed copy and persistent lifecycle code are present on `methode.griffesvivienne.com`.
- Real live purchase validation is still required after deploy to prove the pending panel transitions to confirmed summary and persists for the authenticated user.

## Final launch validation risks (2026-06-04)

- ~~**Critical production drift**: Vercel production is on commit `04c0bc4`, while accepted local payment lifecycle/email and analytics foundation work is not deployed. Live HTML still contains the old `analytics.local/umami` placeholder.~~ Resolved for RC deploy: production now shows `02d255a` READY and live HTML no longer contains `analytics.local/umami`.
- **Critical validation gap**: real post-deploy live payment, Stripe webhook replay/idempotency, Resend email receipt, analytics Realtime/campaign attribution, quote/preorder, and cross-device/auth checks are not yet complete on the final deployed build.
- **High generation confidence risk**: full test suite fails 10 tests in generation configuration/fidelity and texture preset expectations. Focused payment/analytics tests pass, but generation remains a launch confidence blocker.
- **High env risk**: production env values were not readable through the available Vercel tool in this audit. Required production vars must be verified manually/through Vercel settings before launch; prior memory says R2 production credentials were missing and persistent download behavior depends on them.
- **Payment communication config risk**: Stripe successful-payment receipt setting and Vercel `RESEND_API_KEY` / `RESEND_FROM_EMAIL` presence remain unverified from available tools; both must be checked directly in Dashboard/Vercel before declaring payment communication ready.
- **Medium deployment risk**: latest Vercel production build logs include `Warning: Failed to fetch one or more git submodules`; no immediate runtime failure was observed, but this should be cleared or explicitly accepted before final launch.

## Payment confirmation risks (2026-06-03)

- App payment confirmation emails depend on existing Resend production env (`RESEND_API_KEY`, `RESEND_FROM_EMAIL`). If not configured, credits still reconcile and webhook returns success, but only Stripe-native receipts / UI confirmation are available.
- Stripe-native receipts are controlled in Stripe Dashboard Customer emails settings; app code passes a Customer with email and receipt description context, but the Dashboard setting must be enabled for Stripe to send automatic receipts.
- Current payment flow remains card-only (`payment_method_types: ["card"]`). If delayed payment methods are enabled later, add `checkout.session.async_payment_succeeded` handling before relying on delayed fulfillment.
- `/credits` success confirmation is intentionally same-browser/same-device only. It now expires after 24 hours and is user-bound, but cross-device reassurance depends on durable account balance/purchase history and email.
- Browser smoke was verified locally with dummy analytics + dummy-format Clerk key; the UI rendered and persistent confirmation worked, but real authenticated live browser QA with the production Clerk key remains the final proof.

## Analytics risks (2026-06-03)

- ~~Analytics was not launch-complete for attribution: no code-level GA4/GTM loader, no UTM persistence, no LinkedIn attribution, and no payment funnel events were found~~ — **FOUNDATION IMPLEMENTED LOCALLY**: GA4 dynamic loader, optional LinkedIn/Umami loaders, UTM first-touch/session persistence, payment funnel events, and order-intent attribution were added.
- Production analytics remains unverified until `VITE_GA4_MEASUREMENT_ID` and any LinkedIn env vars are configured and checked in GA4 Realtime / LinkedIn Campaign Manager.
- LinkedIn preorder conversion tracking needs a real `VITE_LINKEDIN_PREORDER_CONVERSION_ID`; the base Insight tag alone does not prove campaign conversion mapping.

## Sync risks (2026-06-03)

- ~~**Local git-status reliability issue remains open**: `git status` and `git diff HEAD` still fail with `fatal: not a git repository: /Users/tamerlan/.git/worktrees/elated-engelbart`, even though `git rev-parse`, `git log`, `git show`, and `git ls-remote` work.~~ Resolved locally on 2026-06-30 by removing tracked `.claude/worktrees/*` gitlinks and ignoring local worktree folders.
- **Stripe hardening is now on remote branch but still needs production/live verification**: `milestone4-auth-completion` and `origin/milestone4-auth-completion` point to `04c0bc4`, but do not treat live Stripe as verified until production is confirmed on that commit and one real payment/webhook/idempotency pass succeeds.

## Live Stripe risks (2026-05-28)

- **Live-payment verification still pending**: code audit/build/tests pass, but production cannot be called live-payment verified until one real Stripe live payment is completed and checked in Stripe Dashboard, app UI, and DB/admin.
- **Env configuration is user-reported, not independently read from Vercel in this session**: expected production vars are `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, and `APP_BASE_URL=https://methode.griffesvivienne.com`; no secrets were printed or committed.
- **Webhook fail-closed hardening added locally**: `checkout.session.completed` now grants credits only when `payment_status === "paid"`. This reduces accidental grant risk, but the new change still needs deployment before it protects production.
- ~~**Local git-status reliability issue remains**: branch/commit can be verified with plumbing/remote commands, but `git status` still errors against stale `/Users/tamerlan/.git/worktrees/elated-engelbart` metadata.~~ Resolved locally on 2026-06-30; ordinary `git status` works again.

## Resolved / newly identified (2026-05-11)

- ~~**Production 500 pcs option returned** — Benjamin saw `500 pcs` visible again in production quote flow~~ — **FIXED LOCALLY**: active branch `milestone4-auth-completion` now has MOQ 1000 constants/copy/shared validation/tests. Root cause was branch/deployment drift: earlier fix was on `claude/magical-mendel-0ac677` (`35faedc`) and was missing from the active branch at `a8a8e5a`.
- **Deployment risk remains until production commit is verified**: confirm the live Vercel deployment commit includes the 2026-05-11 MOQ hotfix before treating Benjamin's browser report as resolved in production.
- **Branch drift risk remains**: `milestone4-auth-completion` and `claude/magical-mendel-0ac677` have carried overlapping hotfixes. Future urgent fixes must start by checking branch/commit/deployment target.

## Production blockers (2026-05-08)

- **R2 credentials NOT set in Vercel production env** — `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET` are missing on `griffes-vivienne-studio-3vop` (`prj_LkPZqybEyxElduycv9y1O1qu6G4j`). Generation now works in degraded inline-key mode after hotfix `ab9b86c`, but **re-download of any label generated without R2 returns NOT_FOUND**. Owner must add env vars in Vercel and redeploy for persistent storage to work.
- **MySQL TEXT overflow risk** — `generations.logoUrl`/`labelUrl` are `text() NOT NULL` (65535-byte cap). Storing base64 data URLs there would overflow for typical PNG output (~200KB+). Hotfix `ab9b86c` stores short `inline://...` keys instead. If anyone later changes the fallback to write data URLs, this overflow will return.
- **Favicon not yet replaced** — owner provided new gold "F" circle logo image but it must be saved manually to `client/public/favicon.png`. `?v=2` cache-bust already shipped in `index.html`.


## Resolved this session

- ~~**25x25 generates as long horizontal label** — owner screenshots showed selected `25x25` output rendering as a wide rectangular label~~ — **FIXED LOCALLY**: prompt/domain controls now lock `25x25` as a physical square label body with 1:1 aspect ratio; HD Cotton no longer hardcodes long-horizontal composition for all sizes.
- ~~**New label stale active-flow leak** — after a quote request, uploading a new logo could still inherit `lastGenerated*` result linkage and behave like the previous result/order session was still active~~ — **FIXED LOCALLY**: `SET_LOGO` now clears previous generation result linkage and Home upload continue now clears persisted local order-intent draft before entering Prepare.
- ~~**Uncertain generation value safety** — it was unclear whether provider/storage failures could still burn paid credits or free-trial value~~ — **VERIFIED / TESTED**: bookkeeping still happens only after provider success and successful result-asset storage; new router-level tests cover paid provider failure, guest storage failure, and paid success ordering.
- ~~**previewImageUrl injection** — `submitPreOrderInputSchema.previewImageUrl` accepted any string, allowing crafted requests to inject arbitrary image URLs into the preorder confirmation email~~ — **FIXED** (`fb0c5e4`, `466f897`): `.url().max(4096)` + http/https refine added to schema boundary
- ~~**Back-forward double-generation** — `canStartGeneration` was blind to `state.isGenerating`; back-navigate + forward-navigate during in-flight generation fired a second `label.generate` and consumed a second credit~~ — **FIXED** (`e6b7739`): `isGenerating` added to `GeneratorFlowSnapshot` and gates `canStartGeneration`
- ~~**Non-JSON generation response crash** — large `label.generate` requests could trigger plain-text upstream/body-parser responses such as `Request Entity Too Large`, which the tRPC client tried to parse as JSON and surfaced as `Unexpected token 'R'`~~ — **FIXED LOCALLY**: generation payload budget, 1280px logo canvas cap, tRPC non-JSON response normalization, and server schema payload guard added

## Open technical risks

- 25x25 square-format fix is prompt/test verified but still needs live Gemini QA after deploy with HD beige/black and HD Cotton beige/black; if drift persists, add format-specific retry feedback on validator failure.
- ~~**Confirmed before client review** — Client generation defaults still resolve `DEFAULT_LOGO_TYPE = "text_only"` and send `TEXT_ONLY` to `label.generate`, bypassing the accepted server default `SYMBOL_ONLY` from the anti-hallucination fix~~ — **FIXED**: client default now resolves to `symbol_only` and focused tests were updated.
- ~~**Confirmed before client review** — White/near-white logo preview contrast is fixed in loading hero/config summary, but the main Prepare mockup preview still renders white logo pixels directly on selected white/off-white backgrounds~~ — **FIXED IN CODE**: Home and Prepare now use UI-only contrast preview surfaces; browser visual QA still needed.
- ~~**Confirmed but lower-risk** — `auth.logout` clears the legacy cookie with only `{ path: "/" }`; focused test expects deletion with secure/httpOnly/sameSite/maxAge options matching the original session cookie~~ — **FIXED**: logout clears with session cookie options plus `maxAge: -1`.
- Non-JSON generation stability fix still needs production/browser smoke testing with a large/high-resolution logo after deploy
- Product-photo brand-mark interpretation is now hardened in prompts, but it is still a prompt-level fix rather than a true crop/detection pipeline; live QA is still needed with chest-logo garments, centered product branding, and very tiny/low-contrast marks
- Prompt rebalance now restores exact-artwork handling for explicit logo types and keeps guarded ambiguity for `AUTO`, but there is still no explicit product-photo flag in the payload; `AUTO` remains the highest-risk branch for ambiguous uploads
- The rebalance should recover normal text/logo quality, but live QA is still needed to confirm typography elegance and fidelity are back for straightforward wordmarks/monograms
- Background-field stability is now hardened in prompt/profile language, but it is still a prompt-level control rather than a deterministic weave simulation; live QA is still needed to confirm beige/light luxury labels no longer show ripple, stretched rows, or warped field drift
- Generation error taxonomy is implemented in code, but live provider failure behavior still needs verification with actual 503/overload/timeout/rate-limit responses to confirm the right normalized code reaches the browser
- **Brand leakage fix rollback** — generation/moodboard portion of `320262f` was reverted after severe HD / HD Cotton quality regression; original ideal references are active again, so competitor text/brand leakage risk is open until a better material-specific fix is designed
- The crop-only safe-reference strategy from `320262f` should not be repeated for HD / HD Cotton without preserving full structural conditioning and validating live output quality
- Brand leakage fix did NOT add an explicit negative prompt line in `buildGenerationPrompt.ts` forbidding text/brand copying from references — consider adding as belt-and-suspenders before any future reference changes
- No automated test guards that `*_ideal_*` paths cannot re-enter active moodboard sets — if someone adds a new ideal ref with brand text, leakage could recur silently
- Batch B color fix pushed but live generation QA (multicolor logo → confirm black threads) still pending
- Pre-tinting uses browser canvas; if the canvas API fails (rare), fallback is the original colored logo, so generation still works but color may be wrong — monitor
- Owner mobile error hotfix is locally verified with Chrome mobile emulation; still needs one real mobile Safari smoke test after deploy, especially with iPhone photo-library formats
- White logo preview fix (`51db341`) is type-checked and unit-tested but not visually verified on a real device — browser QA still pending (upload white PNG, check Prepare preview and loading screen)
- Admin Users table metrics fix (`609dc3c`) requires live DB access to verify — no integration tests exist for SQL aggregation queries; confirm in production after deploy

- Pre-order confirmation emails will not send in production until `RESEND_API_KEY` and `RESEND_FROM_EMAIL` are configured
- A verified Resend sending domain is required for reliable branded delivery
- Railway DB migration is applied, but live delivery is still unverified until Resend env vars are configured and a real preorder is tested
- The preorder quote email now has a numeric unit-price helper derived from the client spreadsheet for supported production tiers, but this is still a display/helper table rather than a full contractual pricing engine
- Quote email unit-price display is now derived from `/Users/tamerlan/Downloads/price list.xlsx`, but the workbook does not define 500-piece pricing or tax/shipping terms; 500-piece production intentionally shows `On request` / `Sur demande`, and displayed production prices remain estimated until manually confirmed
- Sample pricing is now explicit in email only, not the SaaS platform UI: standard samples `€320`, cotton samples `€380`; current implementation assumes only `HD_COTTON` is the cotton tier and `HD`, `SATIN`, `TAFFETA` are standard, so client should confirm this material-to-sample-pricing mapping for email/ops use.
- Legal content is now populated from the client document and aligned to current app behavior, but it still needs client/legal-owner approval before final public sign-off; some wording was intentionally softened where the document conflicted with the live guest-first flow, credit validity, and quote-before-production behavior
- Final consistency sweep reduced the biggest quote/order wording mismatch, but one full manual QA pass is still required to confirm the app, quote email, and legal pages feel coherent in real browser/email contexts across FR/EN and desktop/mobile
- Thumbnail rendering depends on email client image-loading behavior, so some recipients may not see the preview until remote images are enabled
- The hosted thumbnail path is fixed locally, but still requires one live preorder + inbox verification to confirm the signed/public asset URL is fetchable by real email clients
- The new reply-in-thread instruction is correct conceptually, but still needs one real inbox/client verification after removing the `mailto` CTA

## Build/runtime warnings

- Build warns about missing `VITE_ANALYTICS_ENDPOINT`
- Build warns about missing `VITE_ANALYTICS_WEBSITE_ID`
- Client bundle still triggers large chunk warning after minification

## Product / UX risks

- Pre-generation preview polish is code/build verified, but still needs browser visual QA with real client-like round, wide, tall, square, black, and white logos before treating it as client-approved
- Embedded `/sign-in` is now code-branded, but Clerk hosted/account-portal surfaces can still show Clerk Dashboard application identity if the dashboard app name/logo remain generic
- Header work is build-verified but still needs browser-based visual QA on target breakpoints
- Desktop should be checked specifically on Home, Prepare, Result, and My Account
- Mobile should be sanity-checked on Home to ensure no regression after desktop restoration
- The new auto-submit confirmation route needs browser QA to confirm the user sees a clean sending -> received transition without confusing intermediate states
- If email delivery fails, the preorder is still stored successfully; ops should monitor logs or DB status until a resend/recovery workflow exists
- The hosted-thumbnail fix batch is still local until it is committed and pushed
- The new admin generations preview relies on stored generation result URLs, which may expire over time because the current model persists signed asset URLs rather than refreshing them from storage on demand
- Batch 3 code introduces schema migration `0013_preorder_generation_linkage.sql`; production/staging must apply it before the new linkage columns are available in the real DB
- Exact linkage is now stored for new preorders going forward, but older preorder rows created before Batch 3 remain unlinked unless backfilled manually
- Batch 4 durable asset retrieval is implemented to refresh signed URLs from `storageKey`, but local inline-dev assets still depend on exact generation fallback URLs rather than true durable object storage
- Vector retrieval only exposes assets already known by the current production foundation: original SVG passthrough or existing `vector_logo` artifacts; no new vector generation is performed by this scope


## Process risk

- ~~`~/.codex/AGENTS.md` vault path mismatch~~ — **RESOLVED** (2026-04-15): path already points to the correct nested path `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`
- ~~**Local git-status reliability issue** — `git status` in the current workspace fails with `fatal: not a git repository: /Users/tamerlan/.git/worktrees/elated-engelbart`, even though `.git` exists and `git log` / `git rev-parse --show-toplevel` work. Treat local dirty-state checks as unreliable until stale worktree metadata/config is repaired or explicitly bypassed.~~ Resolved locally on 2026-06-30 by removing accidental tracked `.claude/worktrees/*` gitlinks and ignoring worktree folders.
- The Railway database URL with password was exposed in chat during migration application; safest follow-up is to rotate the credential
