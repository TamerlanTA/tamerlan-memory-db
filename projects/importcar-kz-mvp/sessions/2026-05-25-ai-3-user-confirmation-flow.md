# Session 2026-05-25 — AI-3 User Confirmation Flow

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

## What was done
- Implemented AI-3 frontend flow without changing existing manual calculator behavior.
- Added calculator mode switch:
  - "Быстрый расчёт" remains default
  - "По ссылке" adds URL/listing text analysis flow
- Added `src/services/aiLinkExtraction.ts` to invoke Supabase Edge Function `analyze-car-link` with controlled success/error responses.
- Added link analysis UI states: idle, loading, error, success.
- Added extracted vehicle confirmation/edit card with editable price, currency, year, engine volume, fuel type, delivery city, plus brand/model/mileage/VIN/trim.
- Confirmed link-mode data maps into the existing deterministic `calculateCost()` path.
- Extended saved calculation and lead metadata snapshots with additive `inputSource`, `aiExtraction`, and `normalizedVehicle`.
- Added minimal AdminLeads display for AI input source, confidence, and brand/model.
- Updated AI roadmap and endpoint docs.

## Key findings
- Frontend does not include AI provider secrets; it invokes only Supabase Functions.
- Build bundle now warns that the main JS chunk is above 500 kB; this is a warning, not a failure. Future cleanup could code-split Supabase-heavy/admin paths if needed.
- Supabase Edge Function must be deployed/configured before live link analysis works; UI handles missing configuration gracefully.

## Validation
- `npm run lint` — passed.
- `npm run build` — passed with chunk-size warning.
- `npm run ai:contracts` — passed.
- `npm run ai:edge` — passed.
- `npm run smoke:test` — passed with local Vite server.
- `npm run calc:sanity` — passed all 5 scenarios.
- Playwright manual check: link mode opens, missing AI config/error state renders, switching back to manual and calculating still shows result; no console errors.

## Blockers
- Production activation still requires Supabase migration, Vercel env vars, deploy, and live acceptance.
- AI link mode requires deployed `analyze-car-link` Edge Function and Supabase secrets.
- Supabase CLI/Deno are unavailable locally, so Edge runtime verification remains manual.

## Next steps
- Manually deploy/configure `analyze-car-link`.
- Then implement AI-4: risk reviewer and grounded explanation layer, ensuring deterministic totals remain untouched.
