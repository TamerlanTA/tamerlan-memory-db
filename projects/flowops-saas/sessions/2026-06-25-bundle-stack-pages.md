# Session 2026-06-25 — Bundle/Stack Pages

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done
- Added `slug` field to all 3 `bundleOffers` entries in `src/lib/pricing.ts` (`sales-stack`, `support-stack`, `voice-operations`).
- Added `StackDetail` type and `stackDetails` array to `src/lib/pricing.ts` with full metadata for each stack: tagline, description, who-it's-for, setupPrice, individualTotal, subscriptionName, subscriptionPrice, pipelineSlugs, and outcomes.
- Created `/src/app/stacks/page.tsx` — Stacks overview page listing all 3 bundles with savings badges, system tags, and pricing. Links to each individual stack detail page.
- Created `/src/app/stacks/[slug]/page.tsx` — Individual stack detail page with `generateStaticParams`. Includes: hero with pricing card (setup + savings), included PipelineCards (4 per stack), outcomes grid, per-system outcomes, subscription plan card, CTA section.
- Updated `/src/app/pricing/page.tsx` — Bundle card links now point to `/stacks/[slug]` instead of `/os`.
- Updated `SiteHeader.tsx` — Added "Stacks" nav item between Systems and Pricing.
- Updated `SiteFooter.tsx` — Added "Stacks" footer link.
- Updated homepage `/src/app/page.tsx` — Added "View system stacks — save up to 23%" link below the subscription pricing section.
- `npm run lint`: passed (clean).
- `npm run build`: passed — 52 static pages (up from 48), all 3 `/stacks/[slug]` paths generated statically.

## Stack data implemented

| Stack | Setup | Individual Total | Savings |
|-------|-------|-----------------|---------|
| Sales Stack | $1,799 | $2,346 | $547 (23%) |
| Support Stack | $1,549 | $1,846 | $297 (16%) |
| Voice Operations | $2,799 | $3,046 | $247 (8%) |

## Key findings
- `bundleOffers as const` required adding `slug` field — updated the const object, TypeScript infers the literal type correctly.
- The `params` in Next.js 16.2.9 are `Promise<{slug: string}>` (async), so `await params` is needed in the page — implemented correctly.
- The known middleware deprecation warning (`middleware.ts` → `proxy.ts`) is still present; it's intentional per prior decisions and not a regression.
- No new npm packages or Supabase migrations needed — purely static pages using existing catalog and pricing data.

## Blockers
- None. All stack pages are fully functional and statically generated.

## Next steps
- Deploy to Vercel production (promote preview or redeploy main).
- Next code priority: Start Phase 3 client portal planning/spec, OR verify Stripe/Resend live keys when ready.
- Business priority: manually verify/enrich the 20-account seed list and start first outreach batch.
