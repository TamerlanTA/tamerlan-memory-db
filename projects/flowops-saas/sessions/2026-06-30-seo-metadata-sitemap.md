# Session 2026-06-30 — SEO Metadata, OpenGraph, Sitemap, Robots

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

## What was done

### Root layout.tsx — enriched metadata defaults
- Added `metadataBase: new URL("https://flowops.agency")` — required for relative OG URLs to resolve correctly
- Added `title` as a template object: `default: "FlowOps OS — AI Operations Platform"`, `template: "%s | FlowOps OS"` — sub-pages now inherit `| FlowOps OS` suffix automatically
- Added full `openGraph` block: type, siteName, title, description, url
- Added `twitter` card block: `summary_large_image` card type

### Per-page static metadata
Added `export const metadata: Metadata = {...}` to:
- `src/app/page.tsx` — homepage (title: "FlowOps OS — AI Operations Platform", specific description)
- `src/app/os/page.tsx` — marketplace (title: "Systems Marketplace")
- `src/app/pricing/page.tsx` — pricing (title: "Pricing", mentions $349 setup + $149/mo)
- `src/app/stacks/page.tsx` — stacks overview (title: "System Stacks", mentions 23% savings)

### Dynamic metadata for pipeline detail pages
Added `export async function generateMetadata` to `src/app/os/[slug]/page.tsx`:
- If slug matches a pipeline: title = pipeline.name, description = tagline + description + price, OG + Twitter tags
- If slug matches a category: title = "{Category} Systems", description = category.description, OG + Twitter tags
- Falls back to `{}` (inherits root defaults) if not found

### Dynamic metadata for stack detail pages
Added `export async function generateMetadata` to `src/app/stacks/[slug]/page.tsx`:
- title = stack.name, description = tagline + description + setup price + savings vs individual
- OG + Twitter tags with savings amount highlighted

### sitemap.ts (new file)
Created `src/app/sitemap.ts`:
- Static routes: `/` (priority 1.0), `/os` (0.9), `/pricing` (0.8), `/stacks` (0.8)
- Pipeline pages: all 25 active pipelines at `/os/[slug]` (priority 0.7)
- Category pages: 7 category routes at `/os/[slug]` (priority 0.6)
- Stack detail pages: 4 stacks at `/stacks/[slug]` (priority 0.7)
- Generates `/sitemap.xml` route automatically

### robots.ts (new file)
Created `src/app/robots.ts`:
- Allows all crawlers on public routes
- Disallows `/internal/`, `/portal/`, `/api/`
- Points to `https://flowops.agency/sitemap.xml`
- Generates `/robots.txt` route automatically

## Key findings
- Build went from 65 pages to 67 pages (sitemap + robots as static routes added)
- All 32 pipeline detail pages and 4 stack detail pages now have unique OG titles and descriptions
- `metadataBase` is required for Next.js OG URLs to resolve correctly in production — this was missing before
- lint: clean, TypeScript: clean, build: clean

## Blockers
- No OG image (static opengraph-image.jpg) — link previews will show title + description without a card image. This is a follow-up to create a proper 1200×630 OG image for the brand.
- Business tasks remain: manually verify/enrich 20-account outreach list, start first outreach batch

## Next steps
- Create a static OG image (`src/app/opengraph-image.jpg` or `.png`, 1200×630) for the brand — will improve social preview when sharing flowops.agency links
- Deploy to Vercel (commit + push)
- Manually verify/enrich the 20-account seed list
- Start first outreach batch
