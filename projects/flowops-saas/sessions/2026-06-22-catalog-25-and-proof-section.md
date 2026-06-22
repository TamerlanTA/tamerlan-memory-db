# Session 2026-06-22 — Catalog 25 And Proof Section

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Continued after Vercel deployment by completing the deployed smoke checklist.
- Verified production public pages/API, internal access protection, cookie access flow, public QA order creation, Telegram notification response, and cleanup of QA order data.
- Expanded the FlowOps catalog from 20 to 25 systems in `src/lib/catalog.ts`.
- Added Supabase migration `202606220001_expand_catalog_to_25.sql`.
- Applied the migration to remote Supabase; live published pipeline count is now 25.
- Added a homepage proof/case-study section with operational metrics and deployment signals.
- Redeployed production to Vercel. Current deployment: `dpl_HdoJ5gcsjsJKqijeYum4WG6gAzdT`.

## Key findings
- Production `/api/pipelines` now returns 25 systems.
- New detail page `/os/revenue-forecast-pulse` renders on production.
- `/internal/orders` remains protected and returns 401 without access.
- Stripe/Resend are still intentionally deferred.

## Blockers
- Live Stripe/Resend verification still waits for real keys and user decision to resume that block.

## Next steps
- Refine homepage copy/case-study wording into final sales language.
- Add search/filter interaction to `/os`.
- Return to Stripe/Resend verification when payment/email keys are ready.
