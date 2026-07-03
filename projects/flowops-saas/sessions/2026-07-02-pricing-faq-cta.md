# Session 2026-07-02 — Pricing page FAQ + CTA section

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

## What was done

### Build state verified
- `npm run lint` — clean (no errors)
- `npm run build` — 68 pages, TypeScript clean
- Pre-existing homepage `RevealOnView` hydration mismatch noted (data-shown attr); does not affect pricing page or any other page; not introduced by this session

### Pricing page improvements (`src/app/pricing/page.tsx`)

1. **FAQ section** — 10 buyer-facing Q&A entries added using `<details>/<summary>` (native HTML accordion, no JS needed, SSR-safe):
   - "Do I pay anything before you start work?"
   - "How long does deployment take?"
   - "Can I start with just one system?"
   - "What does the monthly subscription cover?"
   - "What happens if something breaks after deployment?"
   - "Do I need to be technical to work with FlowOps?"
   - "Can I cancel the subscription?"
   - "What tools do you integrate with?"
   - "What's the difference between a system and a stack?"
   - "How is FlowOps different from hiring an automation freelancer?"

2. **Bottom CTA section** — Full-width card with gradient background (warm white → light blue), "Start with a free workflow audit" heading, short description, dual CTAs (primary: `/#audit`, secondary: `/os`), and trust line "No credit card. No commitment. Audit takes 15–30 minutes."

3. **Bundle grid fix** — Changed `lg:grid-cols-3` to `sm:grid-cols-2` so all 4 bundles display in a clean 2×2 grid instead of 3+1 awkward layout.

4. **Bundle section description** — Added short descriptor paragraph "Bundle 4 coordinated systems into one deployment scope and save 18–23% vs. individual setup. Each stack covers a complete operating function."

### Verified in preview
- All 10 FAQ entries render (confirmed via DOM inspection)
- Bundle grid shows 4 articles in `sm:grid-cols-2` layout
- CTA heading and links present

## Key findings
- Pricing page had no bottom CTA (user visiting from outreach had no clear next step after reviewing pricing)
- Bundle grid was 3-col for 4 items — now 2-col for clean 2×2
- `<details>/<summary>` accordion is SSR-safe and requires no client component
- Build and lint stay clean after changes

## Blockers
- Pricing recheck (market research + user approval) still pending — need dedicated session with user before changing any setup/monthly prices
- First outreach batch still pending (business task)

## Next steps
- QA /os, /os/[slug], /stacks desktop+mobile visually (quick spot-check)
- Deploy pricing page changes to Vercel: `vercel deploy --prod`
- Pricing recheck session: market research per pipeline category → recommended prices → user approval → update catalog.ts
- First outreach batch (highest business priority)
