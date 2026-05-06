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

Last updated: 2026-04-28

- Active branch: `milestone4-auth-completion`
- Latest pushed commit: `416b742` — `Hide sample pricing in platform UI`
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
