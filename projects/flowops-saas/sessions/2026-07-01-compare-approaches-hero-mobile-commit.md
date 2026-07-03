# Session 2026-07-01 — CompareApproachesSection + HeroIllustrationMobile commit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

## What was done

### Critical git fix
- `src/components/HeroIllustrationMobile.tsx` was untracked but already imported in `page.tsx` — any Vercel deploy from git would have failed with a missing module error. Committed it with the session changes. This is a phone-native hero illustration (SVG, CSS-only animations, RevealOnView, staggered entrance, dashed flow connectors, outputs: calendar/checklist/dashboard).

### CompareApproachesSection — new homepage section
- Added to `src/app/page.tsx` between `DeploymentScenariosSection` and `PlatformCapabilitySection`
- Answers the buyer question "Why not just use Zapier?" or "Why not hire an agency?" — the one conversion question previously unanswered on the homepage
- 3-column cards:
  - **DIY tools** (Zapier, Make, n8n): neutral/muted styling; honest 1 pro / 4 challenges breakdown
  - **Agency build**: warm orange; 2 pros (complex logic, custom) / 3 challenges (cost, code ownership, support gaps)
  - **FlowOps OS**: blue highlighted; all 5 points positive; CTA "Get a free workflow map" → `#audit`
- Uses existing design tokens: `stagger-in`, `fo-pill`, `flow-button-primary`, `CSSProperties` cast, existing phosphor `Check` icon, no new imports, no new packages
- Section label: "Why FlowOps" / headline: "Most businesses automate the wrong way."

### Commit
`9b7ba12` — Homepage: CompareApproachesSection + commit HeroIllustrationMobile

## Key findings
- The git state had a build-breaking inconsistency: page.tsx referenced HeroIllustrationMobile but the file was not tracked. Local builds passed (file existed on disk), but any Vercel deploy from git would have failed.
- The homepage had 10 content sections but none explicitly addressed "why FlowOps over DIY/agency". That objection is now handled.
- Build: 68 pages, lint clean, TypeScript clean. No new warnings.

## Blockers
- Pricing verification session still pending — needs user review before any price changes in catalog.ts or pricing.ts
- QA on /os, /os/[slug], /pricing, /stacks — still pending (needs deployment + visual inspection)
- Vercel deploy has not been triggered (no git push in this session — requires user)

## Next steps
- Deploy to Vercel: `git push origin main` → Vercel auto-build triggers
- QA desktop/mobile on /os, /os/[slug], /pricing, /stacks after deploy
- Pricing verification session: market research per system category → price recommendation table → user approval → update catalog.ts + pricing.ts
- First outreach batch (20 accounts)
