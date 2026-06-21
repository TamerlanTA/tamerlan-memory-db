# Session 2026-06-21 — Catalog 20 and Order SOP

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- User decided to postpone live Stripe/Resend verification and continue with the next plan items.
- Recorded deferred Stripe/Resend verification in [[next-steps]] so it is not forgotten.
- Expanded static catalog from 15 to 20 systems:
  - WhatsApp Lead Reply
  - Cold Email Pipeline
  - Call Summary
  - Contact Enrichment
  - Document Processing
- Added Supabase migration `202606210002_expand_catalog_to_20.sql`.
- Applied migration to remote FlowOps Supabase.
- Added internal manual order SOP at `docs/internal-order-sop.md`.
- Linked SOP from `README.md`.

## Key findings
- Remote Supabase now has 20 published pipelines.
- `/api/pipelines` returns 20 systems.
- New detail page `/os/document-processing` works.
- Category page `/os/crm-data` works.

## Verification
- `supabase migration list` shows:
  - `202606200001`
  - `202606210001`
  - `202606210002`
- `npm run lint` passes.
- `npm run build` passes and generates 40 pages.
- Playwright smoke passed for marketplace, new detail page, and category page.

## Blockers
- Live Stripe/Resend verification remains intentionally deferred:
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET`
  - `RESEND_API_KEY`
  - production `EMAIL_FROM`

## Next steps
- Decide deployment target and deploy the app.
- Add testimonials/case study section.
- Expand catalog from 20 to 25 systems when useful.
- Return to Stripe/Resend live verification when keys are ready.
