# Session 2026-07-01 — Automation Card Audit Phase 2: Enriched Copy + Mobile Responsive Pass

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[automation-card-audit-brief]]

## What was done

### catalog.ts — enriched copy for all 25 live pipeline systems
- `description`: expanded from 1 thin sentence to 2-3 buyer-facing sentences per system
- `problem`: made concrete with specific workflow symptoms and before-state pain
- `whatItDoes`: expanded to full trigger → steps → result chain showing exact automation sequence
- Added two new optional fields to Pipeline type: `setupScope` (what's included in deployment) and `monthlySupport` (what's maintained/monitored monthly)
- All 25 systems now have `setupScope` and `monthlySupport` filled with deployment-specific copy

### os/[slug]/page.tsx — Setup Scope + Monthly Support section
- New two-column section rendered between "Best for" and "Expected outcomes" when pipeline has `setupScope` or `monthlySupport` fields
- Section only renders when at least one field is present (conditional rendering with ?? operator)

### RevealOnView.tsx — new scroll-reveal utility component
- Client component wrapping children with IntersectionObserver
- Uses lazy `useState(() => typeof IntersectionObserver === "undefined")` initialization to avoid synchronous setState in useEffect (lint-safe)
- Renders `data-shown` attribute that CSS animations can key off

### Mobile responsive pass (committed with this session, previously uncommitted)
- All page h1/h2/price nodes: fluid mobile sizes (`text-[2.5rem]`, `text-[2.05rem]`) with `sm:` breakpoint restoring desktop sizes
- HeroIllustration: min-h reduced on mobile (`min-h-[380px]` vs `sm:min-h-[520px]`), border-radius smaller
- RequestToProofIllustration: portrait mobile SVG variant added; shown/hidden via CSS

### globals.css
- `.reveal` animation utility added for RevealOnView component

## Key findings
- Pricing kept as-is — current prices are already productized (well below custom-build market rates). A dedicated pricing review session with the user is still needed before changing any prices.
- `description` field in the Pipeline type is used in OG metadata and card hover. `problem`, `whatItDoes`, `bestFor` are shown on the detail page. The new `setupScope` and `monthlySupport` fields add the missing "what you're actually buying" content for buyer trust.
- Coming-soon cards (7 systems) were NOT touched — they only have `slug`, `categorySlug`, `name`, `tagline`. No enrichment needed until they move to live.
- Build: 68 pages, clean lint and TypeScript. Commit: 75f996f

## Blockers
- Pricing verification against current market references is still pending — needs a dedicated review session with user before changing prices
- Illustrations are already done (per 98af96c session). Per-pipeline illustration variants for detail pages remain future polish.

## Next steps
- Pricing verification session: research current market rates per system category and produce a price recommendation table before outreach; get user approval before changing any setup/monthly prices
- Update stack/bundle pricing in pricing.ts if card prices change after the pricing session
- QA desktop/mobile on /os, /os/[slug], /pricing, /stacks — check new Setup Scope and Monthly Support sections render correctly at mobile widths
- Deploy to Vercel (git push → Vercel auto-deploy)
- Manually verify/enrich the 20-account seed list
- Start first outreach batch
