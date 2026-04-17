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

Last updated: 2026-04-17

## Immediate

- Execute `Batch 3 — Preorder ↔ generation ↔ asset linkage`
- Store exact linkage from preorder rows to `generationId`, `sourceAssetId`, and `resultAssetId`
- Make retrieval of the exact logo/result for a PO reliable without overbuilding a broader workflow
- Keep Batch 4 pending until Batch 3 is completed

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

- `Batch 3 — Preorder ↔ generation ↔ asset linkage`
  - store exact linkage to `generationId`, `sourceAssetId`, and `resultAssetId`
  - make exact logo/result retrieval reliable for a PO
- `Batch 4 — Asset retrieval for ops`
  - expose original logo retrieval
  - expose generated preview retrieval
  - indicate SVG/vector availability when known
  - expose vectorized asset when it already exists
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
  - CTA opens a reply draft to `devis@griffesvivienne.com`
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
- If the client later wants real numeric unit pricing inside the email, define a canonical pricing source before extending the current semi-manual quote template

## Process / memory

- Correct or clarify the vault path in `~/.codex/AGENTS.md`
- Continue writing session notes directly under the project `sessions/` folder after meaningful work blocks
