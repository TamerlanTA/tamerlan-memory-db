# Session 2026-06-03 — Launch Analytics Foundation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Implemented lightweight launch analytics using the existing `trackConversionEvent` helper instead of adding a heavy stack.
- Rebuilt `client/src/lib/analytics.ts` to capture UTM attribution, enrich all analytics payloads, and optionally load GA4, Umami, and LinkedIn Insight scripts from env.
- Removed the static Umami placeholder from `client/index.html`; scripts now load only when configured, removing missing analytics env build warnings.
- Added first-touch `localStorage` and session `sessionStorage` attribution persistence for `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, and `utm_term`.
- Embedded attribution snapshots into order intent drafts and shared schema so quote/preorder flows carry campaign context without a backend rewrite.
- Added funnel events across Home, Prepare, Result, Credits, and existing OrderPreview events.
- Added `docs/analytics-foundation.md` with stack recommendation, env vars, event plan, and validation steps.

## Key findings
- Minimal recommended launch stack: GA4 + app-side UTM persistence + optional LinkedIn Insight + optional Umami.
- GA4 integration is low-risk through `VITE_GA4_MEASUREMENT_ID`; all custom events also push to `dataLayer`.
- LinkedIn base tag is feasible through `VITE_LINKEDIN_PARTNER_ID`; preorder conversion tracking needs `VITE_LINKEDIN_PREORDER_CONVERSION_ID` from LinkedIn Campaign Manager.
- No PII is persisted in attribution; file upload analytics uses file type/size/extension only.

## Validation
- `pnpm exec vitest run client/src/lib/analytics.test.ts client/src/domain/orderIntent.test.ts client/src/domain/preorder.test.ts server/orderIntentBridge.test.ts server/orderIntent.router.test.ts` PASS: 44 tests.
- `pnpm check` PASS.
- `pnpm build` PASS; analytics env warnings are gone, only existing large chunk warning remains.
- Full `pnpm test` still fails on pre-existing generation/texture tests; analytics/order/payment-adjacent tests pass.

## Blockers
- Production GA4/LinkedIn requires env configuration and post-deploy verification in GA4 Realtime / LinkedIn Campaign Manager.
- Local `git status` / `git diff --stat` remains broken by stale worktree metadata.

## Next steps
- Set `VITE_GA4_MEASUREMENT_ID` in production and mark `preorder_submit_succeeded` and `payment_succeeded` as GA4 conversions.
- If LinkedIn campaign attribution is needed, set `VITE_LINKEDIN_PARTNER_ID` and `VITE_LINKEDIN_PREORDER_CONVERSION_ID`.
- Validate a campaign URL through upload, generation, checkout, and preorder submission after deploy.
