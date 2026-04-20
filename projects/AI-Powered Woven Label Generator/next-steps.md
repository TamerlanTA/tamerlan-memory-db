# Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[prompts]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-preorder-confirmation-email-delivery|Pre-order confirmation email delivery]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-handoff-sync-preorder-email|Handoff sync after preorder email delivery]]
- [[sessions/2026-04-15-conversion-polish|Conversion polish session]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-16-milestone5-email-finishing-batch|Milestone 5 email finishing batch]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-18-post-m5-order-flow-polish|Post-M5 order-flow polish]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-20-white-logo-fix-and-admin-metrics|White logo fix + admin metrics fix]]

Last updated: 2026-04-21

## Immediate

- **Legal details completion**: fill the real Griffes Vivienne company/legal data in Legal Notices before public production launch (company name, legal form/capital, registered office, registration number, VAT if applicable, publication director, hosting provider)
- **Non-JSON generation stability QA**: after deploy, upload a large/high-resolution PNG/JPG logo and generate; confirm `/api/trpc/label.generate` does not return plain text `Request Entity Too Large`, no `Unexpected token 'R'` toast appears, and any oversized-logo failure is a clear app error instead of a generic crash
- **Back-forward double-gen QA**: Start generation on Result → press Back mid-generation → press Forward → confirm only one `label.generate` network call fires and result appears normally (verifies `e6b7739`)
- **White logo browser QA**: upload a white PNG logo → Prepare → confirm logo shape visible in tinted preview (not blank) → generate → confirm white threads appear in result image
- **Admin Users table QA**: log in to `/admin/stats` → Users tab → check that generationCount and purchaseCount now match expected reality for admin/test accounts
- Run one live generation after deploy and watch for competitor brand leakage
- Run one real mobile Safari smoke test:
  - unsupported HEIC/HEIF selection is blocked with a clear message
  - PNG/JPG/WEBP/SVG still proceed into Prepare
  - selecting White keeps loading hero/config thumbnails visible
- **Batch B QA**: upload a multicolor logo (e.g. red/blue design), select BLACK logo color → confirm loading screen hero, config thumbnail, and generated result all show black threads. Repeat with GOLD to verify end-to-end color path.
- Run browser QA for the new Result -> auto-submit confirmation flow in EN and FR
- Run one live preorder to confirm the quote email arrives immediately after the order CTA and that replying preserves the original thread
- Apply DB migration `0013_preorder_generation_linkage.sql` in staging/production before relying on Batch 3/4 linkage fields in the real environment
- Validate the completed back-office mini-block against a real preorder row in an environment with R2 + DB migrations applied
- Investigate pre-existing server test failures: `texturePresets.test.ts` and `nanoBananaService.pipeline.test.ts`
- Keep the mini back-office / sales-ops scope closed unless new client asks extend it
- Optional: add explicit negative prompt line to `buildGenerationPrompt.ts`: "Do not reproduce any text, brand name, monogram, or logo from the reference images — use references only for weave structure, thread interlacing, fiber depth, fabric density, and lighting."

## Planned batch order

1. `Batch 1 — Preorders / PO visibility`
2. `Batch 2 — Generations visibility`
3. `Batch 3 — Preorder ↔ generation ↔ asset linkage`
4. `Batch 4 — Asset retrieval for ops`

## Explicitly out of scope for this mini-block

- full ERP / SAGE integration
- inbound email parsing or thread-state tracking
- full CRM
- true vectorization pipeline
- broad admin redesign
- full production workflow management

## Deferred until later batches

- Commit and push the hosted email-thumbnail fix batch
- Set `RESEND_API_KEY` in production
- Set `RESEND_FROM_EMAIL` to a verified Griffes Vivienne sender
- Optionally set `RESEND_REPLY_TO_EMAIL`
- Redeploy the app after Resend env setup
- Run one live or staging preorder submission and confirm the transactional email is received
- Confirm `preorder_submissions.confirmationEmailStatus = sent` on a successful live test
- Run one live preorder in EN and one in FR to confirm:
  - localized subject/body
  - thumbnail rendering from a hosted `https://...` image URL
  - the email instructs the user to reply directly in-thread instead of opening a blank compose
  - inbox uses `Reply-To: devis@griffesvivienne.com`
- Rotate the Railway DB credential because the full `DATABASE_URL` was exposed in chat
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
- If the client later wants richer ops tooling, the next natural extension would be lightweight backfill/support for older unlinked preorder rows rather than a broad admin redesign
- If the client later wants real numeric unit pricing inside the email, define a canonical pricing source before extending the current semi-manual quote template

## Process / memory

- Correct or clarify the vault path in `~/.codex/AGENTS.md`
- Continue writing session notes directly under the project `sessions/` folder after meaningful work blocks
