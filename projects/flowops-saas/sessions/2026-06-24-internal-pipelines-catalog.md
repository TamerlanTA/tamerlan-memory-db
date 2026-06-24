# Session 2026-06-24 — Internal Pipeline Catalog Page

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

## What was done
- Created `/internal/pipelines` page — internal catalog management workspace for the FlowOps team.
- Page reads entirely from `src/lib/catalog.ts` (no Supabase migration needed; catalog source of truth is in code).
- Features:
  - Stats row: total published systems (25), tier 1/2/3 counts, coming soon count (7).
  - Pipelines grouped by category (7 groups), each in a card table with: system name, tagline, category, pricing (setup + monthly), tier badge, deploy-day estimate, external link to public page.
  - Coming soon section: 7 announced systems in a 2–4 column card grid.
  - Source file hint at the bottom.
- Added "Catalog →" navigation link to `/internal/orders` and `/internal/audits` pages so all three internal workspaces are cross-linked.
- `npm run lint` passed, `npm run build` passed. `/internal/pipelines` renders as static prerendered page (○).

## Key findings
- No Supabase migration needed; the catalog is static in `catalog.ts`.
- Build warning: "middleware file convention is deprecated, please use proxy instead" — this is documented in memory and intentionally kept as `middleware.ts` because `proxy.ts` was the bug (blank manifest issue). Not a regression.
- `/internal/pipelines` is now static (○) alongside `/internal/orders` and `/internal/audits`.

## Blockers
- None. This was a pure code task with no dependencies on external services.

## Next steps
- Deploy this update to Vercel production (or preview).
- Consider implementing the testimonials section on the homepage next — most impactful for outreach conversion.
- Bundle/Stack pages (Sales Stack, Support Stack, Voice Stack) — Phase 2E loyalty mechanics.
- Promote rate-limited preview to production if ready.
