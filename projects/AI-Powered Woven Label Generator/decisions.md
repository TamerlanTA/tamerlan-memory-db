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
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]

Last updated: 2026-04-16

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
- The finishing-batch email follows the user language already present in the current flow (`en` / `fr`)
- The quote confirmation CTA stays semi-manual for Milestone 5 and uses a `mailto:` action to `devis@griffesvivienne.com`
- `Reply-To` is fixed to `devis@griffesvivienne.com` for the client-facing preorder / quote flow
- The generated label thumbnail is reused from the existing result asset URL instead of introducing a separate attachment or asset-persistence subsystem
- Because the preorder path still has no canonical numeric pricing engine, the unit-pricing row uses semi-manual quote wording rather than inventing new pricing logic inside Milestone 5

## Bonus back-office mini-block

- The accepted post-Milestone-5 back-office work is a small bonus scope for Benjamin, not a new milestone
- The work must be executed in strict batch order and must not collapse multiple batches into one implementation pass
- The fixed order is:
  1. `Batch 1 — Preorders / PO visibility`
  2. `Batch 2 — Generations visibility`
  3. `Batch 3 — Preorder ↔ generation ↔ asset linkage`
  4. `Batch 4 — Asset retrieval for ops`
- The implementation should stay inside the existing admin / back-office surface unless a later batch clearly requires a minimal extension
- Visible commercial value takes priority over deeper technical expansion
- The following are explicitly out of scope for this mini-block:
  - full ERP / SAGE integration
  - inbound email parsing or thread-state tracking
  - full CRM
  - true vectorization pipeline
  - broad admin redesign
  - full production workflow management
