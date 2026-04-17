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

Last updated: 2026-04-17

## Open technical risks

- Pre-order confirmation emails will not send in production until `RESEND_API_KEY` and `RESEND_FROM_EMAIL` are configured
- A verified Resend sending domain is required for reliable branded delivery
- Railway DB migration is applied, but live delivery is still unverified until Resend env vars are configured and a real preorder is tested
- The current preorder flow still has no canonical numeric unit-pricing source; the finishing batch uses semi-manual unit-pricing wording in the email
- Thumbnail rendering depends on email client image-loading behavior, so some recipients may not see the preview until remote images are enabled
- The hosted thumbnail path is fixed locally, but still requires one live preorder + inbox verification to confirm the signed/public asset URL is fetchable by real email clients

## Build/runtime warnings

- Build warns about missing `VITE_ANALYTICS_ENDPOINT`
- Build warns about missing `VITE_ANALYTICS_WEBSITE_ID`
- Client bundle still triggers large chunk warning after minification

## Product / UX risks

- Header work is build-verified but still needs browser-based visual QA on target breakpoints
- Desktop should be checked specifically on Home, Prepare, Result, and My Account
- Mobile should be sanity-checked on Home to ensure no regression after desktop restoration
- If email delivery fails, the preorder is still stored successfully; ops should monitor logs or DB status until a resend/recovery workflow exists
- The hosted-thumbnail fix batch is still local until it is committed and pushed
- The new admin generations preview relies on stored generation result URLs, which may expire over time because the current model persists signed asset URLs rather than refreshing them from storage on demand
- Preorders still are not linked to exact `generationId` / asset ids yet, so PO-to-generation retrieval remains approximate until Batch 3 lands


## Process risk

- ~~`~/.codex/AGENTS.md` vault path mismatch~~ — **RESOLVED** (2026-04-15): path already points to the correct nested path `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`
- The Railway database URL with password was exposed in chat during migration application; safest follow-up is to rotate the credential
