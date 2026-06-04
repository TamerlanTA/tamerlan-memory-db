# Session 2026-05-28 — AI-5C Browser Render Deep Extraction

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented AI-5C Browser Render Deep Extraction for `analyze-car-link`.
- Replaced the Browserless `/content` approach with Browserless `/function` page evaluation.
- Browser render now collects final URL, title, visible body text, meta tags, JSON-LD, selected vehicle-like script snippets, and diagnostic flags.
- Added vehicle-like signal gating so empty/unrelated rendered pages are not sent to AI.
- Added controlled errors: `BROWSER_RENDER_NO_VEHICLE_TEXT`, `BROWSER_RENDER_BLOCKED_OR_EMPTY`, `BROWSER_RENDER_DYNAMIC_DATA_UNAVAILABLE`.
- Added safe diagnostics to controlled error details and live check output.
- Updated docs and sanity scripts.

## Key findings
- AI-5B live test proved Browserless is configured and callable, but rendered page content can still contain no useful vehicle data.
- AI-5C now distinguishes "browser opened" from "browser found useful vehicle content".
- No pricing logic was changed; deterministic pricing engine remains final-price authority.

## Blockers
- AI-5C still needs Supabase deploy and live acceptance on the problematic Encar URL.

## Next steps
- Deploy updated `analyze-car-link`.
- Run URL-only live acceptance.
- If controlled no-vehicle-data diagnostics remain, inspect whether Encar data is behind protected API calls and decide whether a site-specific API replay or manual listingText remains the correct fallback.
