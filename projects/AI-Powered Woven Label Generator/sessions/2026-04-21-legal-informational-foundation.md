# Session 2026-04-21 — Legal Informational Foundation

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Added the minimum trust/legal page set for the V1.5 stabilization block:
  - Terms of Use and Sale (`/terms`)
  - Privacy Policy (`/privacy`)
  - Legal Notices / Mentions légales (`/legal`)
  - FAQ (`/faq`)
- Added bilingual FR/EN content via a structured legal content registry instead of scattering text through page components.
- Made the Home upload acceptance text clickable, linking to `/terms` and `/privacy` in both FR and EN flows.
- Added a compact legal footer with links to all legal/informational pages.
- Kept the implementation intentionally minimal: no broad marketing rewrite, no gallery/testimonials, no admin changes.

## Key findings
- Existing legal acceptance text existed only as a plain translation string on Home and was not clickable.
- Exact company/legal details are still missing, so Legal Notices uses isolated placeholder fields rather than fabricated claims.
- The current app already supports FR/EN, so the legal pages were implemented bilingually.

## Verification
- `pnpm check`: PASS
- `pnpm vitest run client/src/domain/legalContent.test.ts`: PASS
- `pnpm build`: PASS with existing analytics env and chunk-size warnings
- Local route smoke via dev server returned HTTP 200 for `/terms`, `/privacy`, `/legal`, `/faq`

## Blockers
- Legal Notices still needs real company/legal data:
  - legal company name
  - legal form and share capital
  - registered office address
  - registration number
  - VAT number if applicable
  - publication director
  - hosting provider details

## Next steps
- Fill official company/legal details before public production launch.
- Manually review legal page copy with the client/legal owner; content is placeholder-safe but not legal advice.
