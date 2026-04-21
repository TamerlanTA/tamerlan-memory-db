# Session 2026-04-21 — Legal Content Integration and Consistency Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Integrated the client-provided `Mentions_Legales_CGV_FINAL.docx` into the existing legal page registry rather than creating a new legal-page architecture.
- Updated bilingual legal content for:
  - `/legal` — official company details, SIRET, address, publication manager, webmaster, hosting stack
  - `/terms` — CGU / CGV terms with production, quote, AI mockup, rights, pricing, timing, and tolerance clauses
  - `/privacy` — GDPR/privacy content, processor categories, cookies, retention, data rights
  - `/faq` — practical clarification for AI mockups, guest first trial, quote confirmation, and on-request pricing
- Removed legal placeholder fields from public Legal Notices now that official company details are available.
- Softened user-facing wording that overclaimed production readiness:
  - Home feature copy now says high-definition mockup for quote review
  - Premium lock copy now says high-quality exports for quote review / production discussions
  - Credits feature copy no longer promises broad “advanced options included”
- Kept existing routes/footer pattern and made the footer legal nav aria label language-aware.

## Key findings
- The legal document says the first free generation is after account creation, but the current app supports a guest first generation. Legal copy was adjusted to state the current app truth.
- Stripe billing and credit-pack flows exist in code, but public legal copy uses “when offered” so it does not overstate deployment/env readiness.
- Quote/preorder flow is an order intent followed by email/manual confirmation, not a binding production order. Legal copy now says no production starts without written confirmation.
- The quote email estimated unit-price batch already aligns with the legal need for estimated/non-binding pricing.
- The workbook still has no 500-piece price tier while the production selector allows 500 pieces; public FAQ/legal copy says unsupported quantities remain on request.

## Verification
- `pnpm exec vitest run client/src/domain/legalContent.test.ts`: PASS
- `pnpm check`: PASS
- `pnpm build`: PASS with existing analytics env and bundle-size warnings
- `git diff --check`: PASS

## Blockers
- No code blocker.
- Legal copy should still receive client/legal-owner review before final public sign-off.

## Next steps
- Manual QA `/legal`, `/terms`, `/privacy`, and `/faq` in FR/EN on desktop and mobile.
- Confirm the legal owner accepts the softened account/free-trial and credit-validity wording, because it intentionally differs from parts of the provided document to match the live app behavior.
- Later commercial batch: resolve the 500-piece quantity/pricing mismatch by either adding a 500 tier to the pricing source or aligning the production selector.
