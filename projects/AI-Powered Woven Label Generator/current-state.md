# Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/session-2026-04-15-griffes-vivienne-conversion-polish|Conversion polish session]]

Last updated: 2026-04-15

- Active branch: `milestone4-auth-completion`
- Latest pushed commit: `0a658ea` — `Add reliable preorder confirmation emails`
- Repo status for product code: synced to `origin/milestone4-auth-completion`
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
- `pnpm check`: PASS
- Focused preorder email tests: PASS
