# Session 2026-06-23 — Coming Soon Cards & Site Footer

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done

### Implemented: "Coming Soon" pipeline cards on `/os`
- Added `ComingSoonPipeline` type to `src/lib/catalog.ts`
- Added `comingSoonPipelines` array with 7 announced-but-not-built systems:
  - AI Receptionist (voice-calls)
  - Contract Tracker (operations)
  - Churn Risk Detector (support-communication)
  - Deal Stage Automation (crm-data)
  - Social Publisher (marketing)
  - Executive Pulse (reporting)
  - Referral Tracker (lead-sales)
- Added `ComingSoonPipelineCard` component to `src/components/PipelineCard.tsx`
  - Renders with grayscale icon, opacity 62%, "Soon" badge with Clock icon
  - No navigation link — shows "Launching soon — request early access via the audit form"
  - Uses same category color system as live pipeline cards
- Updated `MarketplaceExplorer.tsx` to accept `comingSoonPipelines?: ComingSoonPipeline[]` prop
  - Shows coming soon cards in a separate "On the Roadmap" section below live cards
  - Section only appears when not actively searching (disappears on search)
  - Category filter applies to coming soon cards too
  - Count row shows "X live systems · Y coming soon"
- Updated `/os/page.tsx` to import and pass `comingSoonPipelines`

### Implemented: Site footer (`SiteFooter`)
- Created `src/components/SiteFooter.tsx`
  - Clean, minimal footer: branding + nav links (Systems, Pricing, Free Audit) + © 2026
  - Uses existing design tokens and `flow-container` class
  - Subtle `border-t` separator on `bg-[#fffffb]/60`
- Added `SiteFooter` to all 4 public pages:
  - `src/app/page.tsx` (homepage)
  - `src/app/os/page.tsx` (marketplace)
  - `src/app/pricing/page.tsx` (pricing)
  - `src/app/os/[slug]/page.tsx` (pipeline detail — both category and pipeline returns)
- Footer is NOT in `layout.tsx` — intentional, so it doesn't appear on `/internal/*` pages

## Key findings
- Coming soon pipelines are kept in a SEPARATE array from `pipelines` — they are not passed to `generateStaticParams`, so they have no detail pages (correct behavior)
- Category filter works for both live and coming soon sections consistently
- Search clears the coming soon section — makes sense since users searching are looking for live systems
- Build: lint clean, build clean, 47 static pages

## Blockers
- None

## Next steps
- Deploy to Vercel to make coming soon cards and footer live in production
- Next code options:
  1. Rate limiting on `/api/pipeline-order` and `/api/audit-request`
  2. `/internal/pipelines` — internal catalog management page
  3. Testimonials/social proof section on homepage
  4. Bundle/Stack pages (Sales Stack, Support Stack, Voice Stack)
