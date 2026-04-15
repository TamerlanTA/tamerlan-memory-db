# Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]
- [[feedback_git_base_check]]
- [[feedback_logout_pattern]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[sessions/session-2026-04-15-griffes-vivienne-conversion-polish|Conversion polish session]]

Last updated: 2026-04-15

## Open technical risks

- Pre-order confirmation emails will not send in production until `RESEND_API_KEY` and `RESEND_FROM_EMAIL` are configured
- A verified Resend sending domain is required for reliable branded delivery
- Production DB needs migration `0012_preorder_confirmation_email.sql` before delivery status persistence will work correctly

## Build/runtime warnings

- Build warns about missing `VITE_ANALYTICS_ENDPOINT`
- Build warns about missing `VITE_ANALYTICS_WEBSITE_ID`
- Client bundle still triggers large chunk warning after minification

## Product / UX risks

- Header work is build-verified but still needs browser-based visual QA on target breakpoints
- Desktop should be checked specifically on Home, Prepare, Result, and My Account
- Mobile should be sanity-checked on Home to ensure no regression after desktop restoration
- If email delivery fails, the preorder is still stored successfully; ops should monitor logs or DB status until a resend/recovery workflow exists

## Process risk

- Root `~/.codex/AGENTS.md` points to `/Users/tamerlan/Documents/TamerMemoryDB`, but the actual working vault is nested at `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`
- That path mismatch can cause future agents to miss project memory unless they inspect the real vault location
