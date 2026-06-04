# Session 2026-05-26 — AI-3.5 Link Mode Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Hardened AI-3 link mode without adding AI-4 features.
- Added `src/domain/aiCalculator/pricingMapping.ts` for explicit extraction-to-pricing-engine mapping.
- Updated `CalculatorScreen` to validate malformed URLs before Edge Function invocation.
- Cleaned AI-assisted snapshot objects so nested `undefined` values are omitted before JSON/localStorage/Supabase use.
- Changed frontend type imports away from the broad AI calculator index where runtime imports were unnecessary.
- Added `scripts/ai-link-ui-sanity.mjs` and `npm run ai:link-ui`.
- Updated AI roadmap and endpoint docs with AI-3.5 status, setup notes, and bundle-size status.

## Key findings
- Manual quick calculator remains default and unchanged in pricing behavior.
- Link mode failure states are controlled for empty input, invalid URL, missing Supabase/AI config, and switching back to manual.
- Mocked link-mode success path renders extracted data, allows edit, calculates via deterministic `calculateCost()`, and saves `inputSource: ai_link` with AI metadata.
- Old saved calculations/local requests remain compatible because AI fields are optional.
- AdminLeads handles missing AI metadata and now uses Russian confidence copy.
- Previous Vite chunk warning around 547 kB is gone; build produced about 481.77 kB main JS.

## Blockers
- Supabase CLI/Deno Edge runtime verification is still manual because local Supabase CLI/Deno setup is not available.
- Real deployed `analyze-car-link` behavior depends on Supabase Edge Function secrets and provider configuration.

## Next steps
- Deploy/configure `analyze-car-link` Edge Function secrets in Supabase and do a live endpoint acceptance test.
- Then proceed to AI-4 Risk Reviewer + Explanation Layer, keeping deterministic pricing as the final-price authority.
