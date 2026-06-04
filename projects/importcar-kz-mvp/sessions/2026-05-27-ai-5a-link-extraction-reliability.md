# Session 2026-05-27 — AI-5A Link Extraction Reliability

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Implemented AI-5A reliability layer for `analyze-car-link`.
- Added source detection for `encar`, `youcar_encar`, `mobile_de`, `copart`, and `unknown`.
- Split Edge Function extraction into isolated modules: listing text, generic fetch, and Encar/YouCar adapter shell.
- Added extraction method tracking: `site_adapter`, `simple_fetch`, `listing_text`, and `unavailable`.
- Extended success/error response context with `sourceType`, `extractionMethod`, and `sourceUrl` where safe.
- Updated frontend client/types/snapshot metadata to preserve source/method fields.
- Added subtle source/method display in the extracted vehicle confirmation card.
- Added `docs/supported-listing-sources.md`, updated endpoint/roadmap docs and response examples.
- Added `scripts/ai-extraction-pipeline-sanity.mjs` and `npm run ai:pipeline`.

## Key findings
- URL-only extraction remains dependent on whether the listing page returns readable content to Supabase Edge runtime.
- Pasted listing text is still the most reliable fallback for dynamic/blocked pages.
- No AI final-price logic was added; deterministic `calculateCost()` remains the only final total path.
- The repo directory is not a git repository, so file status was checked by filesystem timestamps rather than `git status`.

## Blockers
- Deno binary is not installed locally, so full Edge runtime type/check was not run outside existing Node sanity scripts.
- AI-5A Edge Function changes still need to be deployed to Supabase and live-accepted.

## Next steps
- Deploy updated `supabase/functions/analyze-car-link` to Supabase.
- Rerun live checks with listing text and URL-only payloads.
- After AI-5A deploy acceptance, proceed to [[next-steps|Phase AI-5 — Accuracy Calibration]].
