# Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]
- [[patterns/git/verify-git-base-before-implementation|Verify git base before implementation]]
- [[patterns/auth/use-useauth-logout|Use useAuth.logout()]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]

Last updated: 2026-04-15

## Header system

- Desktop and mobile headers are intentionally allowed to diverge in composition
- Mobile header quality took priority once it became stable; later passes were constrained to preserve mobile behavior
- Desktop header was restored after the minimalist refinement reduced premium brand presence too much

## Brand treatment

- Use the real brand asset `client/public/logo-gv.png` in the shared brand system
- Preferred visual direction is premium and restrained, but desktop may still carry more visual weight than mobile to support the hero

## Verification policy

- `pnpm build` is sufficient for quick confirmation during UI polish passes
- `pnpm check` failures during this block are treated as pre-existing until the server env typing issue is addressed

## Pre-order confirmation email

- Resend is the transactional provider for quote / pre-order confirmations
- The integration uses a minimal direct HTTP call instead of adding a broader email abstraction layer
- Confirmation email sending happens only after a validated preorder submission is stored successfully
- Submission persistence remains authoritative even if email delivery fails
- Delivery state is persisted directly on `preorder_submissions` instead of building a separate messaging subsystem
