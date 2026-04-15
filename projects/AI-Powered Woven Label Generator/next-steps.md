# Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[prompts]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[sessions/session-2026-04-15-griffes-vivienne-conversion-polish|Conversion polish session]]

Last updated: 2026-04-15

## Immediate

- Set `RESEND_API_KEY` in production
- Set `RESEND_FROM_EMAIL` to a verified Griffes Vivienne sender
- Optionally set `RESEND_REPLY_TO_EMAIL`
- Apply DB migration `0012_preorder_confirmation_email.sql`
- Run one live or staging preorder submission and confirm the transactional email is received
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

## Process / memory

- Correct or clarify the vault path in `~/.codex/AGENTS.md`
- Continue writing session notes directly under the project `sessions/` folder after meaningful work blocks
