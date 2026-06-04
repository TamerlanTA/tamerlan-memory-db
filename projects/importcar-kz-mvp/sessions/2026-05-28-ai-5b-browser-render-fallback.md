# Session 2026-05-28 — AI-5B Browser Rendering Fallback

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented AI-5B Browser Rendering Fallback for `analyze-car-link`.
- Added `supabase/functions/analyze-car-link/extractors/browserRender.ts`.
- Added `browser_render` extraction method.
- Updated Edge pipeline to try source adapter, generic fetch, optional Browserless render, listingText fallback, then controlled error.
- Added browser render error taxonomy: `BROWSER_RENDER_NOT_CONFIGURED`, `BROWSER_RENDER_FAILED`, `BROWSER_RENDER_CONTENT_EMPTY`, `BROWSER_RENDER_TIMEOUT`.
- Updated frontend method label to show "страница открыта в браузере".
- Updated `.env.example`, endpoint docs, supported sources docs, Edge live acceptance runbook, and roadmap.
- Updated sanity scripts to verify browser render method support, missing config safety, UI label mapping, and no frontend browser secrets.

## Key findings
- AI-5A live acceptance confirmed listingText works but URL-only Encar simple fetch fails with controlled `URL_FETCH_FAILED`.
- Browserless REST `/content` is the appropriate first HTTP fallback because it returns rendered HTML without running Playwright inside Supabase Edge Function.
- Browser rendering remains optional and server-side only.
- No pricing logic was changed; AI still does not calculate final import cost.

## Blockers
- AI-5B still needs Supabase deployment and live acceptance with Browserless secrets configured.

## Next steps
- Set Supabase Edge Function secrets: `BROWSER_RENDER_PROVIDER=browserless`, `BROWSERLESS_API_KEY`, `BROWSERLESS_ENDPOINT=https://production-sfo.browserless.io`.
- Deploy `analyze-car-link`.
- Run URL-only live acceptance and confirm `extractionMethod: browser_render` when Browserless can read the page.
- If accepted, proceed to [[next-steps|Phase AI-5 — Accuracy Calibration]].
