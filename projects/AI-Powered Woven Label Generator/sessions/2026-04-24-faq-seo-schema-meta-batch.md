# Session 2026-04-24 — FAQ SEO, schema, and meta batch

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Read the approved FR and EN FAQ SEO briefs from local PDFs in Downloads.
- Installed `react-helmet-async` and wrapped the app with `HelmetProvider` in `client/src/main.tsx`.
- Added a small reusable `SeoHelmet` component for route-specific title, meta, canonical, OG, and JSON-LD injection.
- Replaced the `/faq` page content in the legal-content registry with the full 15 approved Q&A entries in FR and EN.
- Added route-specific `/faq` SEO tags and `FAQPage` JSON-LD.
- Added page-level title + description metadata for `/`, `/prepare`, and `/result`.
- Added Organization JSON-LD on Home only.
- Preserved staging `noindex, nofollow` exactly as-is.
- Added focused tests for FAQ content/schema and SEO content helpers, then ran `vitest`, `pnpm check`, `pnpm build`, and `git diff --check`.

## Key findings
- The app already had a clean FAQ/legal registry pattern in `client/src/domain/legalContent.ts`; extending that was safer than creating a separate FAQ page system.
- `react-helmet-async` was not previously installed.
- Staging `noindex, nofollow` is still handled by `client/src/components/StagingGate.tsx` and remains untouched.
- The approved briefs contain some truncated PDF-extraction lines for the `/faq` meta descriptions and Organization description, so those strings were completed conservatively from the visible approved phrasing.
- The brief references `https://methode.griffesvivienne.com/favicon.svg`, but the app currently serves `/favicon.png`; the Organization schema was pointed to the real live asset path instead of a non-existent SVG.

## Blockers
- No code blocker.
- Live SEO impact still depends on production not shipping the staging noindex flag, and on validating final head output after deploy.

## Next steps
- Open live `/faq` after deploy and confirm title, meta description, canonical, OG tags, and FAQ JSON-LD are present.
- Open live `/`, `/prepare`, and `/result` and confirm page-level title + description overrides are present.
- Confirm Home page Organization schema renders in page source.
- Verify production is not shipping `noindex, nofollow` before expecting search or AI citation benefits.
