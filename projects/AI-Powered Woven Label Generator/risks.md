# Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]
- [[patterns/git/verify-git-base-before-implementation|Verify git base before implementation]]
- [[patterns/auth/use-useauth-logout|Use useAuth.logout()]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-post-m5-order-flow-polish|Post-M5 order-flow polish]]

Last updated: 2026-04-21

## Resolved this session

- ~~**previewImageUrl injection** — `submitPreOrderInputSchema.previewImageUrl` accepted any string, allowing crafted requests to inject arbitrary image URLs into the preorder confirmation email~~ — **FIXED** (`fb0c5e4`, `466f897`): `.url().max(4096)` + http/https refine added to schema boundary
- ~~**Back-forward double-generation** — `canStartGeneration` was blind to `state.isGenerating`; back-navigate + forward-navigate during in-flight generation fired a second `label.generate` and consumed a second credit~~ — **FIXED** (`e6b7739`): `isGenerating` added to `GeneratorFlowSnapshot` and gates `canStartGeneration`
- ~~**Non-JSON generation response crash** — large `label.generate` requests could trigger plain-text upstream/body-parser responses such as `Request Entity Too Large`, which the tRPC client tried to parse as JSON and surfaced as `Unexpected token 'R'`~~ — **FIXED LOCALLY**: generation payload budget, 1280px logo canvas cap, tRPC non-JSON response normalization, and server schema payload guard added

## Open technical risks

- **Confirmed before client review** — Client generation defaults still resolve `DEFAULT_LOGO_TYPE = "text_only"` and send `TEXT_ONLY` to `label.generate`, bypassing the accepted server default `SYMBOL_ONLY` from the anti-hallucination fix. This can encourage invented text behavior for symbol-only logo uploads unless corrected or deliberately accepted.
- **Confirmed before client review** — White/near-white logo preview contrast is fixed in loading hero/config summary, but the main Prepare mockup preview still renders white logo pixels directly on selected white/off-white backgrounds.
- **Confirmed but lower-risk** — `auth.logout` clears the legacy cookie with only `{ path: "/" }`; focused test expects deletion with secure/httpOnly/sameSite/maxAge options matching the original session cookie.
- Non-JSON generation stability fix still needs production/browser smoke testing with a large/high-resolution logo after deploy
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
- The current preorder flow still has no canonical numeric unit-pricing source; the finishing batch uses semi-manual unit-pricing wording in the email
- Thumbnail rendering depends on email client image-loading behavior, so some recipients may not see the preview until remote images are enabled
- The hosted thumbnail path is fixed locally, but still requires one live preorder + inbox verification to confirm the signed/public asset URL is fetchable by real email clients
- The new reply-in-thread instruction is correct conceptually, but still needs one real inbox/client verification after removing the `mailto` CTA

## Build/runtime warnings

- Build warns about missing `VITE_ANALYTICS_ENDPOINT`
- Build warns about missing `VITE_ANALYTICS_WEBSITE_ID`
- Client bundle still triggers large chunk warning after minification

## Product / UX risks

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
- The Railway database URL with password was exposed in chat during migration application; safest follow-up is to rotate the credential
