# Current State

## Related
- [[projects/AI-Powered Woven Label Generator/overview]]
- [[projects/AI-Powered Woven Label Generator/decisions]]
- [[projects/AI-Powered Woven Label Generator/risks]]
- [[projects/AI-Powered Woven Label Generator/next-steps]]
- [[projects/AI-Powered Woven Label Generator/prompts]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-order-preview-submit-state-mapping-fix|Order Preview submit state mapping fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-preview-image-url-hotfix|Preview image URL hotfix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-email-thumbnail-hosted-url-fix|Email thumbnail hosted URL fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-handoff-sync-email-thumbnail|Handoff sync after email thumbnail hosted URL fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-batch2-generations-visibility|Batch 2 generations visibility]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-batch3-preorder-generation-asset-linkage|Batch 3 preorder-generation-asset linkage]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-17-batch4-ops-asset-retrieval|Batch 4 ops asset retrieval]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-post-m5-order-flow-polish|Post-M5 order-flow polish]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-batch-b-color-consistency-fix|Batch B color consistency fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-19-codex-moodboard-brand-leakage-fix|Codex: moodboard brand leakage fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-20-white-logo-fix-and-admin-metrics|White logo fix + admin metrics fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-20-non-json-generation-stability-fix|Non-JSON generation stability fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-21-qa-sweep-security-and-double-gen-fix|QA sweep: security fix + double-generation fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-21-legal-informational-foundation|Legal informational foundation]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-21-pre-generation-preview-polish|Pre-generation preview polish]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-21-input-guidance-softening|Input guidance softening]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-21-quote-email-unit-price-box|Quote email unit price box]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-21-legal-content-integration-and-consistency-audit|Legal content integration and consistency audit]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-24-vercel-deploy-sync-after-missing-push|Vercel deploy sync after missing push]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-24-wave-quality-regression-rebalance|Wave quality regression rebalance]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-24-sample-price-card-credit-message|Sample price card credit message]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-27-new-label-reset-credit-safety-and-sample-card-proof|New label reset, credit safety, and sample card proof]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-27-sample-price-card-email-rendering-fix|Sample price card email rendering fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-28-handoff-sync-memory-source-and-local-state|Handoff sync: memory source and local state]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-28-sample-price-ui-visibility-fix|Sample price UI visibility fix]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-05-08-moq-1000-r2-hotfix-and-freemium-ux|MOQ 1000, R2 hotfix, and freemium gate UX]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-memory-read-and-repo-sync|Memory read and repo sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-payment-confirmation-stabilization|Payment confirmation stabilization]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-payment-round-2-lifecycle-and-validation|Payment Round 2 lifecycle and validation]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-06-03-launch-analytics-foundation|Launch analytics foundation]]

Last updated: 2026-07-03

## 2026-07-03 forgot password visual polish

- Owner reported the `Forgot password?` link looked visually detached under the Clerk sign-in card.
- Reduced it to a subtle `text-xs` muted link placed closer to the card; hover uses primary color/underline.
- Commit `70a7e83` (`Polish forgot password link placement`) pushed to `origin/milestone4-auth-completion`.
- Verification: `npx tsc --noEmit` PASS, `npm run build` PASS.
- Production deployment `dpl_Bw763pSMurK7BaJ4ZYLB9rUGY9En` is READY and aliased to `https://methode.griffesvivienne.com`.

## 2026-07-03 Clerk sign-up route fix

- Fixed the broken `Create an account` behavior on `/sign-in`: the Clerk provider had `signUpUrl="/sign-in"`, so the prebuilt link reloaded the same login page.
- Added dedicated `/sign-up` route/page using Clerk `<SignUp />` and changed provider config to `signUpUrl="/sign-up"`.
- Added EN/FR copy for the sign-up page.
- Commit `a99ee08` (`Add dedicated Clerk sign-up route`) pushed to `origin/milestone4-auth-completion`.
- Verification: `npx tsc --noEmit` PASS, `npm run build` PASS.
- Production deployment `dpl_7DDa4Hs6u9iAFJoAhGAh6P3ZCqxn` is READY and aliased to `https://methode.griffesvivienne.com`; live `/sign-in` serves bundle `assets/index-BKs0nM8F.js`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-03-clerk-sign-up-route-fix|Clerk sign-up route fix]].

## 2026-07-03 Clerk password reset flow

- Implemented explicit password recovery for email/password users after Benjamin reported there was no "Forgot password?" path on the login page.
- Added `/forgot-password` route using Clerk `useSignIn()` with `reset_password_email_code`: user enters email, receives Clerk reset code, enters code + new password, and is signed in on success.
- Added a "Forgot password?" link below the embedded Clerk `<SignIn />` on `/sign-in`.
- Added EN/FR copy for the reset flow.
- Commit `0dfdf99` (`Add Clerk password reset flow`) pushed to `origin/milestone4-auth-completion`.
- Verification: `npx tsc --noEmit` PASS, `npm run build` PASS.
- Production deployment `dpl_23Ywua63CDBHQMecZt3bEQLfv9NZ` is READY and aliased to `https://methode.griffesvivienne.com`.
- Operational note: Clerk Dashboard production instance must have email/password and reset password email-code strategy enabled for the flow to send codes successfully.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-03-clerk-password-reset-flow|Clerk password reset flow]].

## 2026-07-03 paybox admin login issue triage

- Benjamin reported he cannot connect to admin anymore using `paybox@griffesvivienne.com`.
- Code review: recent commits did not change admin authorization logic; admin access still requires `ctx.user.role === "admin"` from the local `users` table.
- Production DB check confirmed `paybox@griffesvivienne.com` still exists with `role = admin`; it was not removed/demoted. The existing row's `lastSignedIn` had not updated today, suggesting the issue is before backend admin authorization (likely Clerk sign-in/session).
- Current likely cause: after production Clerk keys were added/switched, `paybox@griffesvivienne.com` may need to sign in/create a user in the production Clerk instance. The backend should relink by matching email when Clerk successfully returns the same email.
- Live bundle check shows production contains a `pk_live` Clerk publishable key; old/test-key strings may still exist in bundle text but live auth is not obviously missing from the public bundle.
- Next action: ask Benjamin for the exact error screen/message. If he can create/sign in with `paybox@griffesvivienne.com` in production Clerk, the app should relink to the existing admin row by email. If not, fix in Clerk Dashboard production instance or manually relink the new Clerk `user_...` id to the existing DB admin row.

## 2026-07-02 admin stats navigation hotfix

- Fixed a production admin UX regression where the new `Recent Generation Diagnostics` table rendered above the main admin tabs, making it look like `/admin/stats` had lost the other sections.
- Moved diagnostics into its own `Diagnostics` tab beside `Generations`, so `Preorders`, `Users`, `Generations`, `Payments & Credits`, `Guest Continuity`, and `Production Prep` are visible immediately after the top admin cards.
- Commit `812612f` (`Restore admin stats tab visibility`) pushed to `origin/milestone4-auth-completion`.
- Verification: `npx tsc --noEmit` PASS, `npm run build` PASS.
- Production deployment `dpl_H1g9WmY32pYwUYjgtJuUiPtdpy64` is READY and aliased to `https://methode.griffesvivienne.com`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-admin-stats-navigation-hotfix|Admin stats navigation hotfix]].

## 2026-07-02 gate tuning pushed and production deployed

- Pushed Claude's latest stabilization commit `96674e6` (`Relax input gate and enforce label format in output gate`) to `origin/milestone4-auth-completion`; local and remote branch now match.
- Production deployed with `vercel deploy --prod -y`: deployment `dpl_A7UutKtxygsPfRr9jx3x83mtmXzr`, status READY, target `production`, aliased to `https://methode.griffesvivienne.com`.
- Vercel inspect confirmed aliases: `https://methode.griffesvivienne.com`, `https://griffes-vivienne-studio-3vop.vercel.app`, and `https://griffes-vivienne-studio-3vop-tamertt931-8560s-projects.vercel.app`.
- Pre-deploy verification: `npx vitest run` PASS (44 files, 282 tests), `npx tsc --noEmit` PASS, `npm run build` PASS. Build still has the known large chunk warning only.
- Next required step remains live production smoke: test legitimate photographed-label inputs that were previously over-rejected, then verify 20x50/other elongated formats do not ship as square outputs; monitor `validatorReason` for `FORMAT_MISMATCH` and `recovered`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-gate-tuning-production-deploy|Gate tuning production deploy]].

## 2026-07-02 gate tuning after owner production feedback

- Owner tested live (screenshot: methode.griffesvivienne.com already serves the semantic-gates batch) and reported two issues: (1) input gate too strict - rejected a photographed woven label on a marble surface (legit reference) and logos with minor extra elements; (2) generation sometimes ignores the configured size (20x50 produced a square label).
- Commit `96674e6` (`Relax input gate and enforce label format in output gate`), tree clean:
  - Input classifier prompt relaxed: accept a single dominant mark even photographed/scanned on a plain surface with minor extras; reject only clear cases; explicit "if uncertain, accept" (output gate stays strict). Regression-guard test on the prompt wording.
  - Output classifier now receives `expectedLabelSize` (from result.labelConfig.size) and rejects clear proportion violations as `FORMAT_MISMATCH` - which triggers the existing automatic recovery re-roll. Enforced only for unambiguous ratios (<=1.2 square, >=1.8 elongated); 20x30-style ratios skipped.
- Verification: full `vitest run` PASS (44 files, 282 tests), `tsc --noEmit` PASS, `npm run build` PASS. Not pushed/deployed by me.
- Monitoring note: watch `output=rejected:FORMAT_MISMATCH` in validatorReason - high frequency means the generation prompt needs the next format fix, not the validator.

## 2026-07-02 release commit created for the semantic-gates batch

- Commit `72e8193` (`Add semantic input/output gates with recovery and diagnostics`) created on `milestone4-auth-completion`: 14 files, +1980/-19 (Blocks 1+2, retry seed entropy, automatic output recovery, gate observability, 422 error semantics). Working tree clean.
- IMPORTANT: `git push --dry-run` now SUCCEEDS from this machine (0e34242..72e8193 negotiated with GitHub) - the long-standing missing-HTTPS-credentials blocker is resolved. Branch is 9 commits ahead of origin and can be pushed when the owner authorizes.
- Not pushed and not deployed yet per instruction.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-release-readiness-handoff|Release readiness handoff]].

## 2026-07-02 semantic gate observability + error semantics

- Made the Block 1/2 + recovery behavior observable from `generationRuns` without raw logs, using existing columns only (no migration).
- `validatorReason` now persists a per-gate trail (`input=...; output=...; recovery=...`, plus `woven=...` internal validator verdict on success rows); `validatorStatus` becomes `recovered` when the stored image came from the automatic recovery generation, `fail` on semantic rejections.
- Input rejections now persist the classifier reason code (e.g. `input=rejected:PEOPLE_OR_FACES (...)`), not just the normalized error code.
- `OUTPUT_IMAGE_REJECTED` now returns tRPC `UNPROCESSABLE_CONTENT` (HTTP 422) instead of 500, and expected quality rejections log at warn (not error) in both catch layers, keeping error dashboards honest.
- Admin recent-runs table picks the richer strings up automatically.
- Verification: full `vitest run` PASS (44 files, 276 tests), `tsc --noEmit` PASS, `npm run build` PASS. Not committed/deployed per instruction.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-semantic-gate-observability|Semantic gate observability]].

## 2026-07-02 demo-stability audit: retry entropy + automatic output-rejection recovery

- End-to-end reliability audit after Blocks 1+2 confirmed credit ordering, admin diagnostics, stale-run handling, and client error CTAs are sound; two gaps were found and fixed.
- Fixed the deterministic retry loop: generation seed was a pure config hash, so retrying a rejected output reproduced the same composition. Added `deriveGenerationSeed(config, variation)`, `seedVariation` on `GenerateLabelInput`, optional `attempt` (0-100) on `label.generate`, and the Result page now sends its retry counter. Attempt 0 keeps the historical seed for visual consistency.
- Added one automatic in-request recovery when the output semantic gate rejects: regenerate once with an uncorrelated seed (offset 1000+attempt), re-validate, and only surface `OUTPUT_IMAGE_REJECTED` if the recovery also fails. Most output rejections become invisible to the customer at the cost of one extra generation.
- Worst case per request: 2 generations + 3 flash validations - similar envelope to the service's existing internal retries. No vercel maxDuration change; flagged for post-deploy monitoring.
- Verification: full `vitest run` PASS (44 files, 276 tests), `tsc --noEmit` PASS, `npm run build` PASS. Not committed/deployed per instruction.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-demo-stability-audit-and-retry-entropy|Demo-stability audit and retry entropy]].

## 2026-07-02 Block 2: post-generation output safety validation

- Implemented Block 2: after `generateLabel()` succeeds, the router classifies the generated image with Gemini 2.5 Flash before `storeGenerationResultAsset` and before any paid/free-trial/basic bookkeeping. Bad outputs (people, photo scenes, unrelated brands/text, collages, non-label/poster compositions) are hard-rejected without spending value.
- New module `server/label/outputSemanticValidation.ts`; classifier sees both the generated image and the customer's source logo to judge unrelated text (addresses the "American Vintage" complaint case).
- New retryable code `OUTPUT_IMAGE_REJECTED` -> client retry CTA with reassurance copy (FR/EN). Same fail-open policy as Block 1 when the validator itself is unavailable.
- Diagnostics on rejection: run row gets `validatorStatus=fail` + `validatorReason` (pre-throw partial update), then `status=failed`, `normalizedErrorCode=OUTPUT_IMAGE_REJECTED`, `diagnosticStage=label.generate.outputSemantics` via the existing failure handler. No migration.
- Verification: full `vitest run` PASS (43 files, 270 tests), `tsc --noEmit` PASS. Not committed/deployed per instruction.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block2-output-semantic-validation|Block 2 output semantic validation]].

## 2026-07-02 Block 1: pre-provider semantic input validation

- Implemented Block 1 of the generation-quality plan: `label.generate` now semantically classifies the uploaded image with Gemini 2.5 Flash (same `GOOGLE_AI_STUDIO_API_KEY` path) before asset storage, `generateLabel`, and any paid-credit or free-trial commit.
- New module `server/label/inputSemanticValidation.ts`; new error code `INPUT_IMAGE_NOT_LOGO` (shared taxonomy -> BAD_REQUEST -> client "use another image" CTA, FR/EN copy added).
- Safety policy: fail open with logged warning when the validator itself is unavailable (missing key, provider error, timeout, indeterminate response); hard reject only on a clear classifier "reject" verdict. Valid users are never blocked by classifier outages.
- Rejections persist in `generationRuns` diagnostics (status=failed, normalizedErrorCode=INPUT_IMAGE_NOT_LOGO) via the existing failure handler - no DB migration needed.
- Verification: full `vitest run` PASS (42 files, 259 tests), `tsc --noEmit` PASS. Not committed/deployed in this session.
- Codex review after Claude implementation: accepted for continuation. Focused tests, full `npx vitest run`, and `npx tsc --noEmit` passed locally. Nuance: the semantic gate uses a small Gemini Flash classifier call, so it prevents expensive generation spend, not all provider/token usage.
- Output-side validation (Block 2) is explicitly not started.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block1-input-semantic-validation|Block 1 input semantic validation]].
- Review session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block1-review-and-block2-prompt|Block 1 review and Block 2 prompt]].

## 2026-07-02 Codex review: Block 2 + recovery stabilization

- Reviewed Claude's follow-up stabilization batch covering Block 2 output safety validation, output-rejection recovery, and retry seed variation.
- Accepted core approach: generated outputs are semantically validated before result storage/bookkeeping; bad outputs can trigger one automatic regeneration with a non-deterministic seed variation; manual retries now send an attempt counter so they do not repeat the same deterministic seed.
- Verification by Codex: focused tests PASS, full `npx vitest run` PASS (44 files, 276 tests), `npx tsc --noEmit` PASS, `npm run build` PASS.
- Remaining review note before final release/deploy: successful output-recovery paths are visible in logs but not strongly persisted in admin/DB diagnostics, so monitoring recovery frequency would rely on logs instead of `generationRuns`.

## 2026-07-02 Codex review: observability release readiness batch

- Reviewed Claude's monitoring/observability follow-up for Blocks 1-2 + recovery.
- Accepted the batch: `generationRuns.validatorStatus` / `validatorReason` now carry a compact semantic-gate trail such as `input=ok; output=rejected:UNRELATED_TEXT_OR_BRAND (...); recovery=ok`, `validatorStatus=recovered` marks successful automatic recovery, input rejections persist their reason code, and fail-open validator windows persist `input=unavailable` / `output=unavailable`.
- `OUTPUT_IMAGE_REJECTED` now maps to tRPC `UNPROCESSABLE_CONTENT` (HTTP 422) instead of an internal-server-error style 500, and expected semantic quality rejections log at warn level.
- Verification by Codex: focused semantic/recovery tests PASS, full `npx vitest run` PASS (44 files, 276 tests), `npx tsc --noEmit` PASS, `npm run build` PASS.
- Local stabilization batch is ready for commit/deploy decision, pending operational blockers: GitHub push credentials and production env/Clerk live-key/DNS cleanup.

## 2026-07-02 release handoff review

- Reviewed Claude's release handoff for the semantic-gates stabilization batch and accepted it as the current release plan.
- Confirmed local state: 14 changed/untracked files in the working tree for this batch; branch `milestone4-auth-completion`; branch is 8 commits ahead of `origin/milestone4-auth-completion`.
- No DB migration is required by this batch; it uses existing `generationRuns.validatorStatus` and `validatorReason` columns from migration `0015`.
- Release gate is now operational, not code-level: commit the batch, decide push-vs-direct deploy, verify production env/Clerk live config, deploy, and run the smoke matrix with admin/DB/log checks.

## 2026-07-02 semantic-gates commit verification

- Claude created local commit `72e8193` (`Add semantic input/output gates with recovery and diagnostics`) on `milestone4-auth-completion`.
- Codex verified the commit exists at HEAD, working tree is clean, and the commit contains the intended 14-file semantic-gates batch (+1,980/-19).
- Branch is now 9 commits ahead of `origin/milestone4-auth-completion`: the previous 8 local-only stabilization commits plus `72e8193`.
- Important correction: Codex's own `git push --dry-run origin milestone4-auth-completion` still fails with `fatal: could not read Username for 'https://github.com': Device not configured`. Treat GitHub push credentials as still unresolved in this shell, despite Claude's report that dry-run succeeded elsewhere.

## 2026-07-02 push and production deploy

- Fixed GitHub push auth for the shell by running `gh auth setup-git`; `git push --dry-run origin milestone4-auth-completion` then succeeded.
- Pushed `milestone4-auth-completion` to GitHub: remote now matches local HEAD `72e8193291914debedda6b10dd2aa26ff02d399d`.
- Deployed production to Vercel with `vercel deploy --prod -y`.
- Production deployment is `dpl_2XcQgksz1SFGBYFoNKH74yYoJyNQ`, status READY, aliased to `https://methode.griffesvivienne.com`.
- Vercel inspect confirmed target `production`, status Ready, aliases `https://methode.griffesvivienne.com`, `https://griffes-vivienne-studio-3vop.vercel.app`, and `https://griffes-vivienne-studio-3vop-tamertt931-8560s-projects.vercel.app`.
- Next required step is the real production smoke matrix and post-generation admin/DB/log checks; deployment alone is not a full launch sign-off.

## 2026-07-01 emergency guest abuse controls

- Added and deployed emergency anti-abuse controls requested by client.
- New DB tables: `runtime_controls` for runtime kill switches and `abuse_alerts` for alert audit/cooldown. Production migration `0016_emergency_guest_generation_controls.sql` was applied and verified.
- `/admin/stats` now has an Emergency Controls card with a kill switch to disable/enable free guest generations without a deploy. Paid and signed-in credit generations are not blocked by this switch.
- `label.generate` checks `free_guest_generations_disabled` before storage/provider work for guests, so turning the switch on stops token spend from free guest traffic early.
- Added guest velocity monitoring: when guest generation attempts exceed 10 in 5 minutes, the app sends a Resend email alert and records an `abuse_alerts` row; cooldown prevents per-request email spam.
- Resend production env exists; no dedicated `ABUSE_ALERT_EMAIL` / `EMERGENCY_ALERT_EMAIL` is configured, so alerts currently fall back to `RESEND_REPLY_TO_EMAIL`.
- Verification: focused credit-safety tests PASS (4), full `vitest run` PASS (41 files, 247 tests), `tsc --noEmit` PASS, `npm run build` PASS, `git diff --check` PASS.
- Local commit created: `42ec05e` (`Add emergency guest generation controls`). GitHub push failed because local HTTPS credentials are unavailable.
- Vercel Production deploy completed: `dpl_4QGttkgEdT6qWQszTLH7xMSi3JQB`, READY, aliased to `https://methode.griffesvivienne.com`; live domain returns HTTP 200 and bundle is `assets/index-MvidJn4Q.js`.
- Production config blocker remains: live client bundle still contains Clerk `pk_test`; live Clerk keys must be replaced before launch stability sign-off.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-emergency-guest-abuse-controls|Emergency guest abuse controls]].

## 2026-07-01 stabilization batch: diagnostics, stale runs, and guest trial session guard

- User rejected the IP/user-agent/language anonymous free-trial claim hardening because it could block legitimate users; reverted that behavior in code.
- Guest free-trial enforcement is now back to cookie/session scope: `gv_guest_session` + `guest_sessions.freeTrialConsumedAt` + actor lock by guest session. This preserves refresh protection and same-session race safety without fingerprint/IP-style blocking.
- Removed `server/freeTrialGuard.ts`, removed `guestTrialClaims` schema usage, and deleted `drizzle/0014_guest_trial_claims.sql` from the repo. Production DB still has the unused table from the prior deploy; it is harmless and not referenced.
- Added persisted `generationRuns` diagnostics fields: `diagnosticStage`, `diagnosticAttempt`, `diagnosticPipeline`, `upstreamStatus`, `upstreamCode`, `normalizedErrorCode`, `validatorStatus`, `validatorReason`, `referenceCount`, `inputImageCount`, and `inputBytes`.
- Updated `server/nanoBananaService.ts` to return generation diagnostics on success/failure and `server/routers.ts` to persist those diagnostics in `generationRuns`.
- Added stale run cleanup: `cleanupStaleGenerationRuns()` marks `started` runs older than 45 minutes as `failed` with `GENERATION_RUN_STALE`. It is called best-effort during generation entitlement lock acquisition.
- Cleaned current production stale runs manually: 5 old `started` rows were marked failed; production now has 0 stale `started` rows older than 45 minutes.
- Added Recent Generation Diagnostics table in `/admin/stats` using existing `label.getUsageStats.recentRuns`.
- Hardened Umami loading: invalid/non-http `VITE_ANALYTICS_ENDPOINT` values such as `/analytics.local` are skipped instead of injecting a broken script. Live bundle still contains the baked string but includes the guard.
- Reduced legacy OAuth production noise: missing `OAUTH_SERVER_URL` now logs that legacy OAuth is disabled instead of a production error.
- Production DB migration for diagnostic columns was applied manually and verified (`diagnosticColumns = 11`).
- Verification: focused stability tests PASS (17), `tsc --noEmit` PASS, full `vitest run` PASS (41 files, 246 tests), `npm run build` PASS.
- Local commit created: `cf2a318` (`Stabilize generation diagnostics and guest trial session guard`). Branch is ahead of GitHub by 7 commits because local HTTPS GitHub credentials remain unavailable.
- Vercel Production deploy completed: `dpl_EGnB38QHeVPuB4beME4k5ck7KUM6`, READY, aliased to `https://methode.griffesvivienne.com`; live domain returns HTTP 200.
- Production config blocker remains: live client bundle still contains Clerk `pk_test`; live Clerk keys must be replaced in Vercel/Clerk Dashboard before launch stability sign-off.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-diagnostics-stale-runs-and-config-cleanup|Diagnostics, stale runs, and config cleanup]].

## 2026-07-01 guest free-trial hardening

- Audited guest free-trial enforcement after user asked whether the first free generation can be bypassed by refresh or other simple tricks.
- Superseded by the later 2026-07-01 stabilization batch: the IP/user-agent/language claim guard was removed from active code at user request.
- Same-browser refresh was already protected by the persistent `gv_guest_session` cookie plus `guest_sessions.freeTrialConsumedAt`.
- Critical gap found: deleting cookies, incognito, or a new browser could create a fresh guest session and receive another free generation because no server-side claim existed beyond the guest cookie.
- Implemented server-side guest trial claims: new `guest_trial_claims` table stores a SHA-256 claim hash derived from IP, user-agent, and accept-language; raw IP/UA are not stored.
- `label.generate` now computes the guest claim, checks consumed claims before expensive upload/generation work, and uses a claim-level DB advisory lock so parallel new guest sessions from the same claim cannot race into multiple free generations.
- `createFreeTrialGenerationWithCommit` now atomically records the claim and marks `guest_sessions.freeTrialConsumedAt` only after the generated result asset exists, preserving prior credit/free-trial safety behavior.
- Added regression coverage in `server/labelGenerationCreditSafety.test.ts` proving a second guest free trial is blocked even when a new guest session is created from the same client claim.
- Production DB migration `0014_guest_trial_claims.sql` was applied manually and verified before deploy.
- Verification: focused `vitest run server/labelGenerationCreditSafety.test.ts` PASS (4 tests), full `vitest run` PASS (41 files, 247 tests), `tsc --noEmit` PASS, `npm run build` PASS.
- Local commit created: `f930791` (`Harden guest free trial enforcement`). Branch is ahead of GitHub by 6 commits because local HTTPS GitHub credentials remain unavailable.
- Vercel Production deploy completed: `dpl_AXCHFYpWU6tjUyqZBZPmCe1iCJTj`, READY, aliased to `https://methode.griffesvivienne.com`; live domain returns HTTP 200.
- Remaining caveat: anonymous free trials still cannot be made mathematically impossible to bypass without stronger identity such as account/email OTP/phone/payment; VPN/new IP/new device can still look like a new claimant.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-guest-free-trial-hardening|Guest free-trial hardening]].

## 2026-07-01 generation retry fallback stabilization

- Implemented and deployed the first reliability fix from the root-cause audit.
- Changed `server/nanoBananaService.ts` so if a validator-driven retry generation fails after a previous image already exists, the service returns the previous generated image with a validation warning instead of surfacing a no-result error to the customer.
- Applied the same salvage behavior to HD Cotton motif refinement retry attempts.
- Reduced generation request fragility: material reference images are capped to 3 per request, single-pass retries send only 1 reference image, and HD Cotton motif retries send 0 extra material references because they already include the locked base, previous attempt, and source logo.
- Added retry diagnostics to generation logs: attempt-level `referenceCount`, retry fallback log with failed/returned attempt, error status, and `nextRetryReferenceCount`.
- Added regression coverage in `server/nanoBananaService.pipeline.test.ts` for the production failure mode where the first image exists, woven validation fails, and retry generation throws `INVALID_ARGUMENT`; expected behavior is now `success: true` with the first image.
- Verification: focused `vitest run server/nanoBananaService.pipeline.test.ts` PASS (11 tests), full `vitest run` PASS (41 files, 246 tests), `tsc --noEmit` PASS, `npm run build` PASS.
- Local commit created: `16447cd` (`Stabilize generation retry fallback`). Branch is ahead of GitHub by 5 commits because local HTTPS GitHub credentials remain unavailable.
- Vercel Production deploy completed directly from local workspace: `dpl_64beaG6APr3XdPmTf44QB2RAt3UC`, READY, aliased to `https://methode.griffesvivienne.com`; domain returns HTTP 200.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-generation-retry-fallback-stabilization|Generation retry fallback stabilization]].

## 2026-07-01 generation reliability root-cause audit

- Performed a production-only audit after Benjamin reported that too many users still see generation errors and the launch is not demo-stable.
- No code was changed during this audit.
- Current production deployment is `dpl_CWkgLwJ42GA34Mjq7cN4n5ir2shY`, READY, aliased to `https://methode.griffesvivienne.com`; live client bundle is `assets/index-CLadMgTo.js`.
- Production DB snapshot since `2026-06-30 00:00:00` DB time: 23 successful completed generations, 9 failed, 1 stuck `started`; failed share among completed runs is about 28.1%.
- Material split in that same window shows the strongest instability on Taffeta: `TAFFETA` has 7 successes and 7 failures, while `HD` has 7 successes / 2 failures and `SATIN` has 9 successes / 1 started.
- Critical live log root cause found on run `252` / request `lg_mr23zt3k_f3mlcf`: the first Gemini image was produced, the woven-textile validator rejected it as too printed/smooth, the server attempted a regeneration, and the retry request failed with Google/Gemini `400 INVALID_ARGUMENT`; the app then returned no image to the customer.
- Neighboring run `253` showed the same validator-retry pattern but succeeded after retry, proving the current pipeline is probabilistic rather than reliably customer-safe.
- Code root cause is in `server/nanoBananaService.ts`: when a later validation retry throws, `runSinglePassGeneration()` does not salvage and return the previously generated `lastImageBase64`, even though the product policy now intends to return a result whenever an image exists.
- Taffeta likely amplifies upstream failures because its reference selection can send 5 material/style references; retry then adds the previous generated image and source logo, creating a heavier multimodal request shape.
- Production is also not clean: browser console shows broken `/analytics.local/umami`, Clerk development-key warning, and Vercel logs repeatedly show missing `OAUTH_SERVER_URL`; these are launch-readiness issues but not the direct root of the generation failures.
- Sentry could not be audited because `SENTRY_AUTH_TOKEN` is not available locally.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-generation-reliability-root-cause-audit|Generation reliability root-cause audit]].

## 2026-07-01 generation stability hotfix

- User reported production generation frequently reaches the end and then fails at the final validation step, leaving customers without a result.
- Changed the product policy in `server/nanoBananaService.ts`: if Gemini has returned an image, non-pass validator results (`fail` or `protocol_error`) no longer block the response. The service logs a validation warning and returns the best generated image so the router can store it and the customer can see a result.
- Real provider/storage failures still remain failures: if Google returns no image, quota/timeout fails, or R2 result storage fails, the generation still errors and credits/free-trial value are protected by existing router ordering.
- Regression tests updated in `server/nanoBananaService.pipeline.test.ts` to prove failed config fidelity and malformed validator responses still return the generated image when image data exists.
- Verification: `vitest run` PASS (41 files, 241 tests), `tsc --noEmit` PASS, Vite/esbuild production build PASS.
- Local release commit `69751ed` (`Return generated image on validation warnings`) created. Branch is now ahead of GitHub by 2 commits because HTTPS GitHub credentials are still not configured locally.
- Vercel Production deploy completed directly from the local workspace: deployment `dpl_6AUjKBkYidVUua2s6dPvRNcEmXAd`, READY, aliased to `https://methode.griffesvivienne.com`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-generation-stability-hotfix|Generation stability hotfix]].

## 2026-07-01 mobile generation payload hotfix

- User reported desktop generation mostly works, but mobile Safari shows `Service temporarily unavailable` during generation.
- Vercel logs did not expose request logs for the deployment/domain, so root cause was inferred from code path and mobile behavior: iPhone uploads can produce heavier image data and send a large original upload alongside the generation-ready logo image.
- Implemented client-side mobile hardening in `client/src/domain/logoAssets.ts`: generation canvas max dimension reduced from `1280` to `960`, and `shouldSendOriginalLogoDataUrl` now excludes heavy original uploads above `750_000` chars from the generation request.
- This keeps the actual generation input smaller and more predictable on mobile while preserving real provider/storage failure handling.
- Verification: focused tests PASS (28), full `vitest run` PASS (41 files, 242 tests), `tsc --noEmit` PASS, Vite/esbuild production build PASS.
- Local commit `883ca3c` (`Harden mobile logo generation payloads`) created. Branch is now ahead of GitHub by 3 commits because GitHub HTTPS credentials are still not configured locally.
- Vercel Production deploy completed directly from the local workspace: deployment `dpl_iP1YJvhGLkZmQcs9eh3vvzKBUtVh`, READY, aliased to `https://methode.griffesvivienne.com`; live bundle is `assets/index-CRTJ2pq0.js`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-mobile-generation-payload-hotfix|Mobile generation payload hotfix]].

## 2026-07-01 mobile upload storage hotfix

- User provided a mobile screen recording where the app showed the generic `Something went wrong` fallback immediately after pressing continue from the logo upload screen, before visible generation.
- Root cause was inferred from the reproduced flow and code path: raster uploads were used as full original DataURLs for preview and then synchronously written to `localStorage` along with the original upload. Large iPhone image DataURLs can trigger `QuotaExceededError` on mobile Safari, causing the React fallback screen.
- Implemented client hardening: Home upload now rasterizes all supported image previews through canvas with the existing `960px` max dimension, skips reading/passing oversized original uploads into generator state, and store localStorage reads/writes/removes are guarded.
- Oversized originals are no longer persisted to `gv_original_logo_data_url`; the generation flow uses the lightweight preview instead, prioritizing successful customer progression over preserving large original context.
- Verification: full `vitest run` PASS (41 files, 245 tests), `tsc --noEmit` PASS, Vite/esbuild production build PASS.
- Local commit `cac32db` (`Prevent mobile logo upload storage crashes`) created. Branch is now ahead of GitHub by 4 commits because local GitHub HTTPS credentials are still not configured.
- Vercel Production deploy completed directly from the local workspace: deployment `dpl_CWkgLwJ42GA34Mjq7cN4n5ir2shY`, READY, aliased to `https://methode.griffesvivienne.com`; live bundle is `assets/index-CLadMgTo.js`.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-07-01-mobile-upload-storage-hotfix|Mobile upload storage hotfix]].

## 2026-06-30 generation platform health audit

- Production `https://methode.griffesvivienne.com` is live and Vercel deployment `dpl_FsiZLHuxjxBREUzZrTmkpCVKYbQH` is READY, but generation is degraded rather than fully healthy.
- Production DB shows `generationRuns`: 204 successful generations, 20 failed, 5 old `started` rows; overall failure rate is about 8.7%. Current 2026-06-30 operating day shows 7 successes and 1 failed run in the checked window.
- Recent live logs show Google/Gemini image generation intermittently returning `400 INVALID_ARGUMENT` for valid-looking requests; the app retries and sometimes succeeds, but failures surface as generic 500 / `GENERATION_FAILED_UNKNOWN`.
- R2 storage is currently working in production: required R2 env vars are present and recent `logo_original`, `logo_derivative`, and `generation_result` assets are being written with storage keys.
- Production Clerk env/client bundle uses Clerk test keys (`pk_test` / `sk_test`) while `NODE_ENV=production`; this is a production readiness/auth risk.
- Local validation from the current workspace: `node_modules/.bin/tsc --noEmit` PASS, manual build PASS, full Vitest FAILS with the known 10 generation/texture tests.
- The most important code finding is `server/nanoBananaService.ts`: validation failures and `protocol_error` states intentionally return the best available image with `success: true`, so users can receive off-spec output and spend trial/credit value even when validator expectations failed.
- Local release operations are still impaired: `git status` fails due stale worktree metadata and local `.vercel` points to a temp symlink; use plumbing/Vercel CLI workarounds until repaired.
- See audit note: [[projects/AI-Powered Woven Label Generator/sessions/2026-06-30-generation-platform-health-audit|Generation platform health audit]].

## 2026-06-30 generation stabilization step 1

- Implemented local generation stabilization changes after the health audit: `server/nanoBananaService.ts` now fails closed when final validation status is not `pass` instead of returning best-effort output as `success: true`.
- Gemini/provider `400 INVALID_ARGUMENT` without input-image context now normalizes to `TEMPORARY_UPSTREAM_UNAVAILABLE`, matching recent production behavior where a retry could succeed.
- `label.generate` now throws explicit `FORBIDDEN` tRPC errors for `INSUFFICIENT_CREDITS` and `GUEST_FREE_TRIAL_EXHAUSTED`; Result page maps those states into existing premium-lock flow instead of a generic generation error.
- Updated stale generation/texture tests to current production defaults: default size `20x50`, default logo type `SYMBOL_ONLY`, taffeta density/reference/prompt expectations.
- Verification is now green locally: `node_modules/.bin/vitest run` PASS (41 files, 241 tests), `node_modules/.bin/tsc --noEmit` PASS, manual Vite/esbuild build PASS. Build still has the known large client chunk warning.
- Release tooling was repaired after the stabilization batch: accidental `.claude/worktrees/*` gitlink entries were removed from the index, `.claude/worktrees/` and `.vercel/` were ignored, and local `.vercel/project.json` was restored for Vercel project `prj_LkPZqybEyxElduycv9y1O1qu6G4j` / org `team_JfRybqpC6WsadUDMtKRb857f`.
- `git status --short --branch` now works again, Vercel CLI can inspect the linked project and list Production env vars, and the full verification cycle still passes: `vitest run` PASS (41 files, 241 tests), `tsc --noEmit` PASS, Vite/esbuild build PASS.
- Release commit was created locally as `d25e7b1` (`Stabilize generation failure handling`). GitHub push failed from this machine because HTTPS credentials are not configured: `could not read Username for 'https://github.com'`.
- Vercel production deploy was completed directly from the local workspace: deployment `dpl_HkE8JkNdaiQkDiCLkBgB5EE5pMuv`, READY, aliased to `https://methode.griffesvivienne.com`; live JS bundle `assets/index-DCe4fzhf.js` contains `GUEST_FREE_TRIAL_EXHAUSTED` and `INSUFFICIENT_CREDITS`.
- Remaining before production recovery: replace production Clerk test keys with live keys and run live generation/auth smoke tests.

## 2026-06-23 pre-launch technical audit

- Pre-launch audit completed for planned 2026-06-24 launch. Local workspace is `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu`, branch `milestone4-auth-completion`, HEAD `0e34242`.
- `pnpm check` PASS and `pnpm build` PASS. Build still reports the known large client bundle warning.
- `pnpm test` FAILS: 230 passing, 10 failing across label config defaults (`20x50` vs `50x20` expectations), production batch logo type default, Nano Banana config-fidelity validation behavior, and texture preset expectations.
- `git status --short` still fails with stale worktree metadata pointing to `/Users/tamerlan/.git/worktrees/elated-engelbart`; use plumbing commands or repair the worktree before release operations.
- `drizzle/0013_preorder_generation_linkage.sql` is present but missing from `drizzle/meta/_journal.json`; production DB migration state must be verified manually before relying on preorder-generation asset linkage/admin visibility.
- Production R2 behavior is fail-closed if R2 credentials are missing because inline fallback is gated to non-production only.
- Launch verdict from audit: not green for public launch until full tests are resolved or owner-waived and live env/payment/generation/preorder/analytics gates are proven.

## 2026-06-09 GA4 event delivery fix

- Fixed the GA4 queue wrapper to use Google's required `dataLayer.push(arguments)` command format instead of pushing rest-parameter arrays.
- Added regression coverage proving the `js`, `config`, and custom `event` commands enter the queue in the supported shape.
- Verification passed: focused analytics tests (3), `pnpm check`, and `pnpm build`.
- Committed and pushed as `808feb0` (`Fix GA4 event command delivery`) on `milestone4-auth-completion`.
- Vercel production deployment `dpl_95CwShem7HEmRtXQxXfeuwZXy8wA` is READY and aliased to `https://methode.griffesvivienne.com`.
- Live bundle `assets/index-D605PAt-.js` contains `window.dataLayer?.push(arguments)`, the Google tag loader, and `landing_view`.
- GA4 Realtime showed one active user and `landing_view` twice after production visits.
- Official Google Tag Assistant connected to `G-W5B405NSQE` and showed the Config command plus two `landing_view` commands.
- GA4 DebugView showed `page_view` and `landing_view` at 2026-06-09 13:37 +05.
- GA4 base delivery is now verified and READY. Generation, preorder, checkout, and payment events remain implemented but require separate flow-specific production validation.

## 2026-06-09 GA4 production activation

- Added `VITE_GA4_MEASUREMENT_ID` to Vercel Production with Measurement ID `G-W5B405NSQE`.
- Deployed the unchanged production commit `e295729` from a clean Git archive.
- Production deployment `dpl_6CVJgn1tR5WTPY26Q7WYAq9WnfR3` is READY and aliased to `https://methode.griffesvivienne.com`.
- Live bundle `assets/index-D8FBP2sA.js` contains the Measurement ID, Google tag loader, and existing launch events.
- Production DOM contains `https://www.googletagmanager.com/gtag/js?id=G-W5B405NSQE`; the Google script endpoint returns HTTP 200 JavaScript.
- GA4 DebugView and end-to-end event receipt remain unverified. The independent browser is stopped at the production `Staging access` gate, and the authorized Chrome session could not be controlled because the Codex Chrome extension channel did not connect.
- Analytics status is **configured and deployed, not fully verified**.

## 2026-06-09 GA4 final verification result

- GA4 Realtime was opened for property `399976814` and production was visited with validation UTMs.
- `landing_view` did not appear after the initial visit, a repeat reload, and waiting for Realtime refresh.
- `generation_started`, `generation_succeeded`, and `preorder_submit_succeeded` were not triggered because Chrome extension local-file upload permission blocked the validation logo upload.
- DebugView showed zero debug devices and zero events.
- Final analytics sign-off remains **HOLD**.

## 2026-06-09 GA4 pipeline root cause

- `initAnalytics()` is definitely executed in production before React render.
- Home mounts and invokes `trackConversionEvent("landing_view", ...)`.
- Root cause is the noncanonical gtag queue wrapper: production pushes rest-parameter arrays into `dataLayer`, while Google tag requires the function's `arguments` object.
- As a result, the queued `config` command does not initialize the GA4 target and queued custom `event` commands are not processed.
- The separate `{ event: ... }` object push is GTM-style, but no GTM container is installed to consume it.
- Property and Measurement ID are correct: GA4 property `399976814` stream shows `G-W5B405NSQE`.
- Code fix is required; no code was changed during this trace.

## 2026-06-08 analytics truth audit

- GA4 integration code and all 19 launch event names are present in production commit `e295729` and live bundle `assets/index-C5WFDkZ5.js`.
- Production Vercel env does not contain `VITE_GA4_MEASUREMENT_ID`.
- Live `https://methode.griffesvivienne.com` creates no `window.gtag`, no `window.dataLayer`, and loads no GA4/gtag script. Therefore the implemented events are not currently delivered to GA4.
- No repository, memory, or operational evidence confirms any GA4 DebugView or Realtime validation. All GA4 events remain unverified.
- The production Umami script currently loads from `/analytics.local/umami` and fails with `SyntaxError: Unexpected token '<'`; Umami cannot be treated as a working fallback.
- Launch analytics status: **NOT READY** until GA4 env is added, production is redeployed, and core events are proven in DebugView/Realtime.

## 2026-06-08 success moment conversion polish

- Improved only the existing `/credits` post-payment panel; Stripe, billing, webhook, analytics, email, and confirmation lifecycle logic were not changed.
- Confirmed state now uses the approved "Your atelier is ready" hierarchy: animated checkmark, `+X credits`, updated balance, create-label CTA, account CTA, and compact amount/reference footer.
- Pending state now says payment was received and credits are being prepared, with no Stripe/webhook technical wording.
- Added one-shot premium motion with `prefers-reduced-motion` support; no looping celebration effects.
- Files changed: `client/src/pages/Credits.tsx`, `client/src/contexts/LanguageContext.tsx`, `client/src/styles/credits-success-moment.css`.
- QA: desktop/mobile and FR/EN visual checks completed; primary CTA navigation passed; focused lifecycle tests, `pnpm check`, and `pnpm build` pass.
- Committed and pushed as `a2828ab` (`Polish post-payment success moment`) on `milestone4-auth-completion`.
- Vercel production deployment `dpl_Cg7nmpbUSUMTPukLJydqMeUN2zjk` is READY on commit `a2828ab`; `https://methode.griffesvivienne.com` serves the new JS/CSS bundles.
- Production smoke: `/credits` HTTP 200, live bundle contains the new FR/EN copy and success animation classes, no production-origin console errors, and 390px viewport has no horizontal overflow.
- Follow-up micro-polish implemented locally: the confirmed icon now draws its thin circle first and the checkmark second in a restrained one-shot sequence completed in about 820ms.
- Micro-polish changes are limited to `client/src/pages/Credits.tsx` and `client/src/styles/credits-success-moment.css`; reduced-motion renders the complete static icon.
- Micro-polish QA: desktop/mobile and FR/EN browser checks pass, no horizontal overflow or relevant console errors, `pnpm check`, `pnpm build`, and lifecycle tests pass. Commit/deploy still pending.
- Micro-polish committed and pushed as `e295729` (`Add subtle success checkmark animation`).
- Vercel production deployment `dpl_58iSzmD3Pv6BiuesXjiQm8Fdvp5Q` is READY on commit `e295729`.
- Production smoke: `/credits` HTTP 200, live JS `assets/index-C5WFDkZ5.js` and CSS `assets/index-CjhbZgZi.css` contain the circle/check animation classes and reduced-motion rule; no production-origin console errors.

## 2026-06-05 post-payment success UI bugfix

- Root cause confirmed in `Credits.tsx`: the success panel was gated on `getCheckoutStatus` already returning data, so a Stripe success return displayed no reassurance while auth/status polling was delayed or unavailable. The persisted confirmation was also only created inside the exact `status === "reconciled"` branch.
- Implemented immediate pending reassurance for `/credits?checkout=success&session_id=...`, before the protected status query resolves.
- Added fallback to the checkout session id persisted before redirect when `session_id` is missing from the return URL.
- Confirmation now accepts either checkout `status === "reconciled"` or payment `paymentStatus === "succeeded"` as authoritative.
- Existing 24-hour, same-user lifecycle remains intact; persisted confirmation is not cleared during transient unauthenticated state on an active success return.
- Files changed: `client/src/pages/Credits.tsx`, `client/src/domain/creditsSuccessLifecycle.ts`, `client/src/domain/creditsSuccessLifecycle.test.ts`.
- Verification: 14 focused lifecycle/billing/email tests PASS, `pnpm check` PASS, `pnpm build` PASS, Prettier PASS. Browser simulation at `http://localhost:3007/credits?checkout=success&session_id=cs_test_simulated` rendered the pending panel immediately and kept it visible after refresh.
- Fix committed and pushed as `52912db` (`Fix post-payment confirmation race`) on `milestone4-auth-completion`.
- Vercel production deployment `dpl_GByXwqThgCLEaQQ4X6VgmZV8kb7J` is READY on commit `52912db`; aliases include `https://methode.griffesvivienne.com`.
- Live production bundle `assets/index-D2O9Z2Iu.js` contains the pending/confirmed UI copy and `gv_last_confirmed_purchase` lifecycle key.
- Final proof still requires one owner-authorized live purchase to validate the real pending-to-confirmed transition, Stripe receipt, and GV email delivery.

## 2026-06-04 final launch validation

- Final launch readiness audit completed without feature changes.
- Current Vercel production for `griffes-vivienne-studio-3vop` is READY but still built from GitHub branch `milestone4-auth-completion` commit `04c0bc4` (`Add payment_status guard and billing webhook tests`), deployment `dpl_CnzyuYB3q1uKSMAek2tFF79niXKL`.
- Live domain `https://methode.griffesvivienne.com` returns HTTP 200, but production HTML still contains the old static `analytics.local/umami` placeholder and asset `index-6WiJmhUx.js`; this confirms the accepted local payment lifecycle/email copy and analytics foundation are not deployed to production yet.
- Local candidate verification: focused payment/analytics/preorder/order-intent/credit-safety tests PASS (62 tests), `pnpm check` PASS, `pnpm build` PASS.
- Full `pnpm test` still fails 10 tests in generation/texture/fidelity expectations across `label.domain`, `label.productionBatch`, `nanoBanana`, `nanoBananaService.pipeline`, and `texturePresets`.
- Launch recommendation from audit: **not launch-ready for public launch** until latest accepted local changes are deployed, production env is verified, full/live validation runbook passes, and the generation test failures are resolved or explicitly accepted by owner as non-blocking.

## 2026-06-04 production release candidate preparation

- Verified production drift: local `HEAD` and production are the same commit, `04c0bc4`; there are no committed changes missing from production.
- Accepted local candidate exists as uncommitted working-tree delta over `04c0bc4`, so a release-candidate commit must be created before Vercel can deploy the accepted payment/analytics stabilization work.
- Tracked modified files: `client/index.html`, `client/public/favicon.png`, `client/src/contexts/LanguageContext.tsx`, `client/src/domain/orderIntent.ts`, `client/src/lib/analytics.ts`, `client/src/main.tsx`, `client/src/pages/Credits.tsx`, `client/src/pages/Home.tsx`, `client/src/pages/Prepare.tsx`, `client/src/pages/Result.tsx`, `server/billing.test.ts`, `server/billing.ts`, `shared/orderIntentBridge.ts`.
- New candidate files: `client/src/domain/creditsSuccessLifecycle.ts`, `client/src/domain/creditsSuccessLifecycle.test.ts`, `client/src/lib/analytics.test.ts`, `server/paymentConfirmationEmail.ts`, `server/paymentConfirmationEmail.test.ts`, `docs/payment-confirmation.md`, `docs/analytics-foundation.md`.
- Local `.claude/worktrees/*` directories are untracked local noise and should not be included in the RC package.
- RC commit created and pushed: `02d255a` (`Prepare production launch stabilization candidate`) on `origin/milestone4-auth-completion`.
- Verification before commit: `pnpm check` PASS; focused RC tests PASS (47 tests across analytics, credits success lifecycle, payment confirmation email, billing, order intent, preorder).
- Vercel production later showed `02d255a` promoted and READY as deployment `dpl_995BnbLbCCkhAaxVBf83uPJDdfgs`; live HTML no longer contains the old `analytics.local/umami` placeholder.
- Payment communication live verification: code path is reachable in production build after `checkout.session.completed` creates a new `purchase_grant`, but Stripe receipt Dashboard status and Vercel `RESEND_API_KEY` / `RESEND_FROM_EMAIL` presence could not be read through available tools and must be verified in Stripe/Vercel dashboards.

## 2026-06-03 launch analytics foundation

- Implemented lightweight launch analytics using the existing `trackConversionEvent` helper.
- Added first-touch and session UTM persistence (`gv_first_touch_attribution`, `gv_session_attribution`) and automatic attribution enrichment for all tracked events.
- Optional analytics scripts now load dynamically from env: `VITE_GA4_MEASUREMENT_ID`, `VITE_LINKEDIN_PARTNER_ID`, `VITE_LINKEDIN_PREORDER_CONVERSION_ID`, `VITE_ANALYTICS_ENDPOINT`, `VITE_ANALYTICS_WEBSITE_ID`.
- Removed static Umami placeholder from `client/index.html`, clearing the previous missing analytics env build warnings.
- Added launch funnel events for landing, upload, configuration, generation, freemium, paywall, checkout/payment, and preorder conversion.
- Added attribution to signed order intent drafts/shared schema so preorder/quote submissions retain campaign context without DB migration.
- Verification: focused analytics/order-intent tests PASS, `pnpm check` PASS, `pnpm build` PASS. Full `pnpm test` still fails only on pre-existing generation/texture tests.

## 2026-06-03 payment Round 2 lifecycle and validation

- Hardened `/credits` success confirmation lifecycle: persisted confirmation now includes `userKey`, `confirmedAt`, and `expiresAt`; it survives refresh for the matching authenticated user only and expires after 24 hours.
- Added `client/src/domain/creditsSuccessLifecycle.ts` and focused tests for TTL, user binding, legacy/malformed storage rejection, and mismatched-user hiding.
- Updated GV payment confirmation email wording to confirm credits availability and explicitly defer official payment receipt responsibility to Stripe receipts.
- Analytics audit completed without implementation: Umami placeholder and best-effort `dataLayer` pushes exist for order/preorder events; no code-level GA4/GTM loader, UTM persistence, LinkedIn attribution, or payment funnel events found.
- Verification: lifecycle/email/billing tests PASS, `pnpm check` PASS, `pnpm build` PASS. Full `pnpm test` still fails only on pre-existing generation/texture tests.

## 2026-06-03 payment confirmation stabilization

- Implemented launch-safe post-payment reassurance on `/credits`: successful reconciled checkouts persist a local confirmation summary and show a visible success panel with credits added, amount, and Stripe Checkout Session reference after redirect/refresh.
- Added `server/paymentConfirmationEmail.ts`: a simple Resend payment confirmation email sent after a new credit grant is created from `checkout.session.completed`.
- Payment email is best-effort and does not affect webhook success or credit fulfillment; duplicate webhooks with an existing grant do not resend the app confirmation email.
- Stripe Checkout Sessions now set `payment_intent_data.description` for clearer Stripe receipt context.
- Added docs at `docs/payment-confirmation.md` covering webhook endpoint, required events, Stripe receipt configuration, and Resend payment email behavior.
- Verification: focused payment/email tests PASS, broader payment/order/credit safety tests PASS, `pnpm check` PASS, `pnpm build` PASS. Full `pnpm test` still fails only on pre-existing generation/texture expectation tests, not payment flow.

## 2026-06-03 sync

- Project memory was reread and matched to workspace `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu`.
- Active branch/remote verified by Git plumbing: `milestone4-auth-completion` at `04c0bc4` / `origin/milestone4-auth-completion`, commit `Add payment_status guard and billing webhook tests`.
- `04c0bc4` contains the Stripe hardening from the 2026-05-28 readiness audit: `server/billing.ts` payment-status guard plus `server/billing.test.ts`.
- `main` remains far behind at `f51482c`; branch/deployment target must stay explicit before production work.
- `git status` and `git diff HEAD` still fail with stale worktree metadata pointing at `/Users/tamerlan/.git/worktrees/elated-engelbart`; use `git rev-parse`, `git log`, `git show`, and remote checks until repaired.
- No implementation work was done in this sync; this was a memory/readiness alignment pass.

## 2026-05-28 deltas

- **Live Stripe readiness audit completed locally** on real workspace `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu`.
- Active branch/commit verified despite broken `git status` during that session: `milestone4-auth-completion` at `ed3fd26` / `origin/milestone4-auth-completion` (`Fix production MOQ regression`). As of the 2026-06-03 sync, branch/remote are now at `04c0bc4`.
- Latest production-fix content confirmed in code: MOQ 1000 is present in `client/src/domain/order.ts`, `shared/orderIntentBridge.ts`, `OrderLabelsPanel`, and EN/FR copy; focused MOQ/order-intent tests pass.
- Stripe implementation audited: Checkout Session creation, raw-body webhook verification, billing router, env loading, Credits success/cancel UX, and checkout/payment schema are coherent for a card-only Stripe Checkout credit-pack flow.
- Minimal Stripe hardening added: `server/billing.ts` now grants credits from `checkout.session.completed` only when Stripe reports `payment_status === "paid"`.
- Focused Stripe tests added in `server/billing.test.ts` for raw body verification, unpaid no-grant fail-closed behavior, and paid payment/credit grant persistence.
- Verification: `pnpm check` PASS, `pnpm build` PASS, `pnpm vitest run server/billing.test.ts` PASS, and `pnpm vitest run client/src/domain/order.test.ts server/orderIntentBridge.test.ts server/orderIntent.router.test.ts` PASS.
- Live payment remains **unverified** until one real payment is completed and checked in Stripe + app + DB/admin. See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-05-28-live-stripe-readiness-audit|Live Stripe readiness audit]].

## 2026-05-11 deltas

- **MOQ 1000 regression hotfix implemented locally on `milestone4-auth-completion`** after Benjamin reported `500 pcs` visible again in the production quote flow. Root cause: branch/deployment drift. The earlier MOQ 1000 fix existed on `claude/magical-mendel-0ac677` at `35faedc`, but active branch `milestone4-auth-completion` at `a8a8e5a` did not contain it.
- Re-applied canonical production minimum to the active branch: `client/src/domain/order.ts:PRODUCTION_MIN_QUANTITY = 1_000`; quick options no longer include 500; slider minimum clamps to 1000; EN/FR copy now says `1,000 – 10,000 pieces` / `1 000 – 10 000 pièces` and `Minimum 1,000 pcs` / `Minimum 1 000 pcs`.
- Shared backend/order-intent validation now rejects production quote draft payloads below 1000 while keeping sample payloads accepted. Added focused regression tests for production 500 rejection, production 1000 acceptance, sample acceptance, option generation, and quantity clamping.
- Verification: targeted order/domain and order-intent/preorder tests PASS, `pnpm check` PASS, `pnpm build` PASS. Remaining `500` search hits are either intentional tests, the 500-piece quantity step, HTTP 500/error fixtures, CSS/timing/font-weight classes, or unrelated image dimensions.
- See session note: [[projects/AI-Powered Woven Label Generator/sessions/2026-05-11-moq-1000-branch-drift-hotfix|MOQ 1000 branch-drift hotfix]].

## 2026-05-08 deltas

- **25x25 square-format generation hotfix implemented and pushed** (`a8a8e5a` on `milestone4-auth-completion`) after owner screenshots showed `25x25` selections generating as long horizontal labels. Prompt/domain control now treats `25x25` as a physical square label body with 1:1 aspect ratio, not just a reference code. HD Cotton compact prompts no longer hardcode `One long horizontal woven cotton label only`; HD/HD Cotton regression tests added. Verification: focused prompt/generation tests PASS, `pnpm check` PASS, `pnpm build` PASS.
- Active branch is now `claude/magical-mendel-0ac677` (worktree `magical-mendel-0ac677` at `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu/.claude/worktrees/magical-mendel-0ac677`). 70 commits ahead of `origin/main`.
- Latest commits on this branch: `35faedc` (MOQ 1000 + 25×25 + brand-leakage prompts) → `ab9b86c` (R2 storage hotfix) → `5e54191` (freemium gate UX).
- **Production MOQ raised from 500 to 1000 pcs**. Sample flow unchanged. `client/src/domain/order.ts:PRODUCTION_MIN_QUANTITY = 1_000`. Backend Zod refines on `orderIntentDraftPayloadSchema` reject production quantity < 1000.
- **R2 storage: degraded inline-key mode** active in production until `R2_ACCESS_KEY_ID` / `R2_SECRET_ACCESS_KEY` / `R2_BUCKET` are set in Vercel. `server/assets.ts` no longer gates the inline fallback on `!ENV.isProduction`; it stores `inline://assets/<kind>-<nanoid>.<ext>` as the URL placeholder (NOT data URLs — would overflow MySQL TEXT 65535-byte limit). `getGenerationDownloadUrl` returns NOT_FOUND when it sees an inline-key labelUrl.
- **Freemium gate now surfaces actionable errors**. `GUEST_FREE_TRIAL_EXHAUSTED` and `INSUFFICIENT_CREDITS` codes added to `shared/generationErrors.ts`; mapped to tRPC FORBIDDEN; Result page CTAs route to `/sign-in` and `/credits`.
- Vercel project: `griffes-vivienne-studio-3vop` (`prj_LkPZqybEyxElduycv9y1O1qu6G4j`), team `team_JfRybqpC6WsadUDMtKRb857f`. Production domain `methode.griffesvivienne.com`. Latest production deployment is `dpl_3chqiCXLhRD8Y69AuwTANjkrFVZt` (commit `35faedc`); `ab9b86c` and `5e54191` will deploy on next push trigger.
- Vercel runtime log MCP tool is severely capped (~5 entries per query, only first log line per request). Use `web_fetch_vercel_url` or code analysis when you need full error context.

- Active long-running branch: `milestone4-auth-completion` — HEAD `416b742` (Hide sample pricing in platform UI, 2026-04-28) — **NOT yet merged to `main`**
- `origin/main` HEAD: `f51482c` (Integrate Clerk auth across client and backend, 2026-04-13) — **30+ commits behind `milestone4-auth-completion`**
- Current worktree session (`magical-mendel-0ac677`): on `main`, clean, no new work yet
- R2 storage integration fully committed and included in `milestone4-auth-completion`
- Handoff sync confirmed the active memory protocol source is `/Users/tamerlan/AGENTS.md`, not a project-local `AGENTS.md`; it points to `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`.
- Local workspace path for this handoff: `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu`.
- Local `git log` confirms `HEAD` at `d976224`, but `git status` currently fails with stale/conflicting worktree metadata: `fatal: not a git repository: /Users/tamerlan/.git/worktrees/elated-engelbart`.
- Implemented and pushed the client clarification that sample pricing must not appear on the SaaS platform UI: removed sample price display from `OrderLabelsPanel` and `OrderPreview`, kept sample request/explanation copy, and preserved email-side sample price rendering.
- Repo status: local generation-stability fixes are committed and pushed through `e12c8ba`; a follow-up local prompt rebalance now softens the wave/ripple hardening language after it degraded generation quality and contaminated support surfaces with swirl-like artifacts
- Local SEO/content polish now extends the FAQ page with richer citation-friendly answers plus `FAQPage` JSON-LD on `/faq`; the copy now includes verified facts such as Italy manufacturing, ~4-week lead time, 4 materials, 4 folded formats, and the truthful nuance that standard production pricing starts at 1,000 pieces while some 500-piece requests can still remain manual/on-request
- A new local SEO implementation batch now replaces the FAQ with the approved 15-question FR/EN brief, adds `react-helmet-async`, route-specific `/faq` meta tags + FAQPage JSON-LD, per-page meta titles/descriptions for Home / Prepare / Result, and Organization schema on Home
- Staging safety remains preserved: the staging gate still owns `noindex, nofollow`; this batch does not change robots behavior
- One intentional launch-readiness deviation from the brief: Organization schema uses the real existing `/favicon.png` asset instead of `/favicon.svg`, because the SVG file is not currently served by the app
- Search-indexing caveat remains unchanged: `noindex` is still intentionally controlled by the staging gate (`VITE_IS_STAGING === "true"`), so production crawlability still depends on the real environment not shipping with staging mode enabled
- Deploy status: `milestone4-auth-completion` is now pushed through `d976224`, and Vercel has built preview deployments for both `griffes-vivienne-studio` and `griffes-vivienne-studio-3vop` at commit `d976224` (`Fix sample price card email rendering`)
- Production nuance: the live production deployment on `griffes-vivienne-studio-3vop` still points to `3040beb` (`Fix new label reset and prove generation credit safety`); `d976224` is present in Vercel as a READY preview deployment, not as the current production target
- Remaining untracked local noise: `.claude/` only, intentionally excluded from commits

## What changed today

- Completed a multi-pass refinement of the Griffes Vivienne shared header system
- Improved mobile header responsiveness and tap safety
- Reworked the shared header into intentionally different desktop and mobile compositions
- Added the real brand asset `client/public/logo-gv.png`
- Refined the header from decorative luxury toward minimalist luxury
- Restored stronger premium desktop branding after the minimalist pass weakened desktop too much
- Implemented reliable transactional pre-order confirmation email delivery with Resend
- Synced the order-boundary guest email capture path into the current branch so the backend now receives the final email address during preorder submission
- Added persisted delivery tracking on `preorder_submissions` for contact email, status, sent timestamp, provider message ID, and last error
- Added setup documentation in `docs/preorder-confirmation-email.md`
- Applied migration `0012_preorder_confirmation_email.sql` manually against Railway MySQL with `drizzle-kit migrate`
- Finished the Milestone 5 preorder email batch:
  - EN / FR email rendering based on current user language
  - generated label thumbnail included from the existing result asset URL
  - semi-manual V1.5 email copy with unit-pricing row only, manual confirmation note, reply instruction, and mailto CTA
  - fixed `Reply-To` to `devis@griffesvivienne.com`
- Fixed `/order-preview` contradictory submit UI by making header / confirmation / failure / email-warning rendering state-aware instead of always success-like
- Fixed preorder submit payload construction so inline / oversized `previewImageUrl` values are omitted instead of failing backend validation
- Fixed the missing email thumbnail path by propagating the hosted generation-result asset URL through Result -> order intent draft -> preorder submit, with a backend fallback to the validated draft when the submit payload omits the preview URL
- Completed a grounded code audit for the new post-Milestone-5 back-office / ops visibility mini-block
- Confirmed the current `/admin/stats` page is a support-oriented dashboard, while preorder / PO visibility foundation exists mostly in backend/storage and is not yet surfaced in the admin UI
- Confirmed original logo assets, generation-result assets, and production-prep/vectorization foundation already exist, including SVG passthrough handling for original vector uploads
- Accepted a small bonus scope for Benjamin after Milestone 5 focused on back-office / sales-ops visibility
- This bonus scope is explicitly a structured mini-block, not a new milestone and not a broad admin redesign
- Active source of truth for the mini-block is now the fixed four-batch execution order recorded in project memory
- Implemented Batch 1 locally: sales-first preorder / PO visibility inside the existing admin page
- Added a new preorder-focused admin tab with PO lookup, contact email, product code, material, size, quantity, mode, confirmation email status, sent timestamp, and preview image visibility
- Extended the preorder admin backend read shape and search behavior for `PO-000014`, raw numeric ids, contact email, and product code
- Added focused pure tests for preorder reference/search logic and preorder payload extraction
- Implemented Batch 2 locally: improved generations visibility inside the existing `/admin/stats` page without redesigning the broader admin surface
- Extended the admin generations read-model with parsed display fields from `configSnapshotJson`, including product code, material, size, color, and generated mockup preview URL
- Improved generation search coverage safely by including owner name and snapshot-backed product context in the existing admin query
- Replaced the metadata-heavy generations table with a more visual sales/ops-friendly table showing preview, customer context, product context, status, and created date
- Added focused pure tests for generation admin snapshot parsing and fallback behavior
- Implemented Batch 3 locally: persisted exact preorder linkage to `generationId`, `sourceAssetId`, and `resultAssetId`
- Extended the order-intent draft contract so linkage travels through the existing Result → order intent → preorder submit path instead of introducing a new side channel
- Extended `preorder_submissions` schema and persistence to store exact generation/asset linkage for new preorders
- Exposed linkage through the admin preorder read-model and surfaced compact linkage context in the existing preorders table
- Added focused tests for draft linkage preservation, submit-path persistence, and admin preorder visibility of linkage fields
- Implemented Batch 4 locally: ops asset retrieval inside the existing preorder admin view
- Added a compact preorder asset action area in `/admin/stats` with retrieval actions for original logo, generated preview, and vector asset when available
- Added durable admin asset resolution using fresh `storageKey`-based signed URLs, with exact-generation fallback URLs only when needed for inline/local cases
- Exposed original logo type (`SVG` / `Raster` / `Unknown`) and vector availability status in the preorder read-model
- Reused exact Batch 3 linkage for retrieval and exposed vector readiness based on original SVG passthrough or `vector_logo` production artifacts when present
- Added focused tests for asset availability mapping and durable asset URL resolution helpers
- Implemented a post-M5 / V1.5 polish batch for the ordering flow
- Removed the extra recap-step friction by turning `/order-preview` into an auto-submit sending/confirmation route
- Kept preorder creation, PO generation, confirmation email delivery, and admin/back-office visibility intact during the flow refactor
- Removed the misleading `mailto` CTA from the quote email and replaced it with reply-in-thread guidance so sales context stays attached to the original email
- Tightened the Result screen so backend order-intent creation is now required before leaving the result page
- Implemented Batch B color consistency fix: pre-tints the logo to the selected color before sending to the generation API; loading screen hero and config thumbnail now use the tinted silhouette; `originalLogoDataUrl` preserved as source of record; `namedColorToHex` and `buildTintedLogoDataUrl` exported for reuse
- Fixed critical brand-leakage bug (Codex, commit `320262f`): all `*_ideal_*` moodboard reference images contained readable competitor brand names (Chloé Stora, DIOR, SAINT LAURENT); replaced with 6 new `*_material_safe_*` images that are text-free material crops; removed brand names from prompt guidance text; changed motif instructions from "replicate ideal reference" to "follow supplied logo artwork only"; added `client/src/domain/logoAssets.ts` with upload/generation format guards and `isNearWhiteHexColor` helper; loading screens now use contrast-aware logo surface for white logo colors
- Implemented owner-found post-M5/V1.5 hotfixes before broader QA:
  - fixed mobile upload/generation mismatch by blocking unsupported HEIC/HEIF-style mobile formats at upload and preventing unsupported Result-page tint fallbacks from reaching `label.generate`
  - improved white / near-white logo visibility in loading/mockup preview surfaces only, while preserving selected white generation semantics
- Added focused logo asset helper tests and verified the mobile owner flow with Chrome mobile emulation using local dummy env
- Fixed white source logo producing blank tinted output in `buildTintedLogoDataUrl`: the luminance formula `(1 - luminance)` incorrectly made white pixels fully transparent; added average-luminance pre-scan and inverted formula `(luminance - 0.1)/0.6` for light-source logos (avg luminance > 0.7); dark logos unchanged; generation behavior unaffected
- Fixed admin Users table generationCount to include generations from all guest sessions the user ever claimed (not just those with `ownerUserId` already set); fixed purchaseCount to read `payments WHERE status = 'succeeded'` instead of `creditLedgerEntries WHERE entryType = 'purchase_grant'` (latter misses payments that bypass the Stripe webhook)
- Reverted only the generation/moodboard portion of `320262f` after owner found HD / HD Cotton quality regression; `server/moodboards.ts` is back to the `8fe695c` version and the six `*_material_safe_*` moodboard assets are removed locally
- Fixed the client-reported non-JSON generation crash path (`Unexpected token 'R', "Request En..." is not valid JSON`): `Result.tsx` no longer always sends both tinted generation PNG and original upload data URL when the request body would exceed the safe budget; tinted logo canvas output is capped to 1280px; `/api/trpc` transport now normalizes unexpected non-JSON responses into JSON tRPC errors; `label.generate` schema rejects oversized logo payloads before generation work starts
- Added the minimum legal/informational trust foundation for V1.5 stabilization: bilingual `/terms`, `/privacy`, `/legal`, and `/faq` pages; Home upload acceptance text now links to Terms and Privacy; a compact legal footer exposes the legal page set; Legal Notices intentionally isolates missing official company/legal fields as placeholders
- Fixed the code-side unbranded Clerk login experience for V1.5 stabilization: `/sign-in` now uses the existing Griffes Vivienne header/footer shell; `ClerkProvider` receives Griffes Vivienne appearance, logo, support email, and FR/EN localized auth copy; a focused `clerkBranding` unit test guards against `"My Application"` copy in app-provided Clerk localization
- Updated the favicon to the provided gold GV mark as `client/public/favicon.png`; `pnpm check` and `pnpm build` passed before push
- Completed a final integrated QA audit of the assembled branch:
  - branch is pushed and aligned with origin at `858dfd1`
  - `pnpm check` PASS
  - `pnpm build` PASS with known analytics env and bundle-size warnings
  - 82 focused stabilization tests PASS across generation, tRPC transport, logo assets, order/preorder, legal content, Clerk branding, and server generation input guard
  - local SPA route smoke returned 200 for the core app/legal/auth/admin routes
- Fixed the highest-priority confirmed QA bugs:
  - client `DEFAULT_LOGO_TYPE` now aligns with server anti-hallucination default (`symbol_only` / `SYMBOL_ONLY`)
  - Home upload preview and Prepare preview now have UI-only contrast handling for white / near-white logos
  - `auth.logout` now clears the legacy cookie with the same session-cookie options plus expiry/maxAge
  - `pnpm check` PASS; focused targeted tests PASS (47 tests)
- Implemented generation error taxonomy / presentation stabilization:
  - typed generation error codes now distinguish temporary upstream outages, rate limits, timeouts, invalid/unsupported/too-large image input, and unknown failures
  - Nano Banana / Gemini failures are normalized server-side before reaching the client
  - Result page now shows dynamic FR/EN error copy and retry/new-image CTA behavior based on failure type
  - generic React crash boundary no longer blames the uploaded image
  - `pnpm check` PASS; focused error tests PASS (31 tests)
- Implemented post-Milestone-5 pre-generation preview polish:
  - Home upload preview now uses a smaller centered logo inside a neutral inset frame, with mobile-safe stacked action buttons
  - Prepare preview now uses a cleaner centered label frame, reduced max width, constrained logo viewport, and preserved near-white contrast surface
  - scope stayed limited to `Home.tsx` and `Prepare.tsx`; generation/pricing/legal/billing/order/result flows untouched
  - `pnpm check`, `pnpm build`, and `git diff --check` PASS; local `/` and `/prepare` returned 200 on `http://localhost:3001/`
- Implemented post-Milestone-5 input guidance softening:
  - Home upload copy now says “logo or visual” and frames recommendations as best-result guidance, not restrictions
  - Added EN/FR guidance that unusual visuals remain allowed and may sometimes produce surprisingly good results
  - Added a subtle Prepare note that unusual visuals are still possible but less predictable
  - technical format validation unchanged; no image-category blocking or new funnel friction added
  - `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Implemented quote email unit-price box:
  - inspected `/Users/tamerlan/Downloads/price list.xlsx` (`Feuil1`) and mapped production unit prices by material, size, and quantity tier
  - added `server/quoteUnitPricing.ts` as the server-side display helper for estimated unit prices
  - updated `server/preorderConfirmationEmail.ts` so the top metadata area shows quote reference plus estimated unit price
  - priced production tiers show locale-aware two-decimal values, e.g. `€0.60 / unit` or `0,60 € / pièce`
  - samples and unsupported tiers such as 500 pieces show `On request` / `Sur demande`
  - focused pricing/email tests, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Implemented the legal content integration / commercial wording consistency batch:
  - replaced placeholder legal notices with official Griffes Vivienne company details from `Mentions_Legales_CGV_FINAL.docx` (SAS, SIRET `383 927 464 00024`, Saint-Denis address, Benjamin JELIN, `devis@griffesvivienne.com`)
  - updated `/terms`, `/privacy`, `/legal`, and `/faq` content in FR/EN using the existing legal content registry and footer links
  - aligned legal copy with current app behavior: guest first trial, account/credits after trial, Stripe payments only when offered, quote/order intent before written confirmation, estimated pricing, AI mockup disclaimer
  - softened product wording that implied production-ready outputs before manual technical validation
  - `pnpm exec vitest run client/src/domain/legalContent.test.ts`, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Completed the final post-Milestone 5 consistency sweep before full manual QA:
  - reframed remaining order/preorder UI copy as quote/request copy in FR/EN
  - updated Result/order CTA, Order Preview submission states, reply instructions, and quote email labels/CTA to avoid implying immediate contractual confirmation
  - softened Premium/export and loading microcopy so AI visuals are presented as high-quality mockups/assets for quote and production discussions, not guaranteed production proofs
  - aligned residual legal wording from `order intent` toward `quote request`
  - confirmed remaining `pre-order` search hits are comments/test names, not live copy
  - `pnpm exec vitest run client/src/domain/legalContent.test.ts server/preorderConfirmationEmail.test.ts server/quoteUnitPricing.test.ts`, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Implemented folded format naming + sample pricing commercial polish:
  - added shared folded-format display helper so user-facing format labels show `+ fold` in EN and `+ replis` in FR while internal size codes remain unchanged
  - updated Prepare format cards, loading summary, Result quote panel, Order Preview summary, and quote confirmation email to use folded-format wording
  - added shared sample pricing helper: `HD_COTTON` -> cotton sample `€380`; `HD`, `SATIN`, `TAFFETA` -> standard sample `€320`
  - sample request UI now explains jacquard card creation, weaving loom setup, and full deduction from a later production order
  - sample quote emails now show sample price instead of `On request` and include the same development/deduction note
  - focused tests, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Added a small loading UX reassurance copy update:
  - generation loading footer now says EN/FR that a generation usually takes about 1 to 2 minutes, sometimes a little less or more
  - one long-wait rotating message now uses a restrained weaving line (`Good weaving takes a moment.` / `Un beau tissage prend un instant.`)
  - no generation logic, loading timing architecture, API calls, pricing, legal, or quote logic changed
  - `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Implemented a generation-interpretation reliability fix for product/fashion photo uploads with small visible branding:
  - verified the root cause in code: the pipeline sent the whole upload as the only source image, labeled it as logo artwork, and repeatedly told Nano Banana to preserve the supplied logo geometry with no product-photo branch or crop heuristic
  - added centralized source-image interpretation rules so prompts now treat uploads as brand-mark sources, explicitly isolate localized branding inside product photos, and ignore garment/person/product scene context
  - updated shared label prompt builder plus compact/single-pass/HD/HD-cotton refinement prompts and inline image labeling to reinforce brand-mark isolation without blocking product photos or unusual visuals
  - added focused regression coverage for the new prompt wording and payload labeling; `pnpm build`, `pnpm check`, `git diff --check`, and focused vitest runs PASS
- Rebalanced the product-photo safety fix after it degraded normal logo/text quality:
  - confirmed the regression came from applying product-photo defensive wording too broadly, including explicit `TEXT_ONLY`, `SYMBOL_ONLY`, and `SYMBOL_AND_TEXT` paths
  - added branched source-image interpretation modes so explicit logo types now use strong supplied-artwork fidelity wording again, while `AUTO` keeps conditional product-photo isolation guidance
  - narrowed inline source labels to `SUPPLIED LOGO ARTWORK:` for exact-artwork paths and `SOURCE IMAGE / BRAND MARK:` for ambiguous paths
  - updated focused prompt/pipeline tests; `pnpm check`, `pnpm build`, `git diff --check`, and targeted vitest runs PASS
- Hardened background weave stability after logo interpretation improved but the label field still drifted into wave/ripple distortion:
  - identified the root cause as missing even-field / stable-tension / anti-warp constraints in both full and compact runtime prompts
  - added a shared background-field stability helper and threaded it through the full prompt, compact runtime path, HD dark, HD refinement, HD Cotton Stage A/B/single-pass, and taffeta prompts
  - added anti-wave / anti-stretched-field wording without flattening the textile into a dead uniform map
  - updated focused generation/runtime tests; `pnpm exec vitest run server/generation.test.ts server/nanoBananaService.helpers.test.ts`, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Rebalanced the weave-stability hardening after live outputs showed a severe quality drop:
  - verified from real outputs that the issue was no longer just label-ground drift; support backgrounds and the whole scene were picking up swirl-like / thread-like contamination
  - identified the likely prompt cause: repeated aggressive wording around `wave`, `ripple`, `warped`, `stretched`, and `micro-variation` was being over-literalized by the model
  - replaced that language with calmer positive guidance about orderly premium weave plus an explicit guardrail that the wood/marble/paper support surface must stay smooth and non-textile
  - updated focused prompt tests; `pnpm exec vitest run server/generation.test.ts server/nanoBananaService.helpers.test.ts`, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Applied a small quote-email conversion tweak for sample requests:
  - moved the sample reimbursement benefit directly into the top-right sample price card under the amount
  - EN copy now reads `100% credited toward your future production order`; FR copy mirrors that deduction message
  - the lower explanatory note now focuses on jacquard card creation and loom setup instead of repeating the deduction line
  - `pnpm exec vitest run server/preorderConfirmationEmail.test.ts`, `pnpm check`, `pnpm build`, and `git diff --check` PASS
- Fixed the active flow reset leak after quote submission:
  - a fresh logo upload now clears previous generation result linkage (`lastGeneratedUrl`, hosted asset URL, generation id, source asset id, result asset id) instead of keeping the old result-ready session alive
  - Home upload continue now also clears any persisted local order-intent draft before entering Prepare, so a new label starts from a clean UI flow even if stale quote-preview draft data exists locally
  - focused reducer coverage now proves a new upload resets active result linkage while preserving free-trial exhaustion state
- Verified and proved credit/free-trial safety on generation failure:
  - actual paid spend and free-trial commit still happen only after provider success plus successful result-asset storage
  - added router-level tests proving provider failure does not spend a paid credit, result-storage failure does not consume guest free-trial value, and successful paid spend occurs only after the result asset has been stored
- Confirmed the sample reimbursement conversion message remains inside the quote email price card and added explicit FR sample-card test coverage
- Fixed the live sample price-card rendering bug in the quote confirmation email:
  - confirmed the reassurance copy was already present in the real payload-builder and send path
  - root cause was email-fragile markup in the right-hand price card (`div` stacking with margin-based spacing)
  - replaced the price card body with table-based email-safe rows and explicit padding so the reassurance line renders directly under the sample price in actual sent emails
  - added tests for EN/FR sample-card rendering and for the actual serialized send payload

## Active mini-block

### Bonus scope — Back-office / sales-ops improvement

- Status: complete locally through all four agreed batches
- Scope type: post-Milestone-5 bonus block
- Execution rule: follow the agreed batches strictly in order and do not collapse them

### Fixed execution order

1. `Batch 1 — Preorders / PO visibility`
2. `Batch 2 — Generations visibility`
3. `Batch 3 — Preorder ↔ generation ↔ asset linkage`
4. `Batch 4 — Asset retrieval for ops`

### Current active batch

- Mini-block complete

### Explicitly out of scope for this mini-block

- full ERP / SAGE integration
- inbound email parsing or thread-state tracking
- full CRM
- true vectorization pipeline
- broad admin redesign
- full production workflow management

## Current UX state

- Mobile header is considered good and was preserved in the final pass
- Desktop header now has stronger brand presence and better visual support for the hero
- Header-related changes affect:
  - Home
  - Prepare
  - Result
  - My Account
  - Order Preview
  - Credits

## Verification state

- `pnpm build`: PASS
- `pnpm check`: PASS (all recent commits)
- Client tests (66): PASS (+1 regression test for double-generation fix)
- Focused preorder email tests: PASS
- Focused Milestone 5 email finishing tests: PASS
- Focused Order Preview submit-state tests: PASS
- Focused preorder payload hotfix tests: PASS
- Focused hosted-thumbnail propagation + email fallback tests: PASS
- Focused post-M5 order-flow polish tests: PASS
- `generatorFlow.test.ts`: 9/9 PASS (added regression test for `isGenerating` gate)
- Focused non-JSON generation stability tests: PASS (`client/src/lib/trpcTransport.test.ts`, `client/src/domain/logoAssets.test.ts`, `server/generation.test.ts`)
- Focused legal content tests: PASS (`client/src/domain/legalContent.test.ts`)
- Focused Clerk branding tests: PASS (`client/src/lib/clerkBranding.test.ts`)
- Pre-existing server test failures (texturePresets, nanoBananaService.pipeline): still failing, unrelated to recent work — need separate investigation

## Security fixes applied this session

- `previewImageUrl` in `submitPreOrderInputSchema` now validated with `.url().max(4096)` + http/https refine — closes injection path into preorder email thumbnail
- `state.isGenerating` now included in `GeneratorFlowSnapshot` and gates `canStartGeneration` — closes back-forward double-generation credit leak
