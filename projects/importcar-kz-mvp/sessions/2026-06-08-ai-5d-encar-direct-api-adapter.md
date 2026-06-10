# Session 2026-06-08 — AI-5D Encar Direct API Adapter

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done

Completed full AI-5D implementation: Encar direct API adapter for the `analyze-car-link` Edge Function.

### Files changed

**Backend (Supabase Edge Function)**
- `supabase/functions/analyze-car-link/extractors/encarApi.ts` — NEW: Encar direct API adapter
  - Probes `api.encar.com/v1/cars/{carId}` and `api.encar.com/readside/car/{carId}`
  - Browser-like headers (not bot UA), no credentials
  - 만원 normalization: raw < 100,000 → × 10,000 KRW
  - `buildEncarApiListingText(apiData, carId)` — pure JSON → structured text
  - `extractWithEncarApi(carId, sourceType)` — controlled failure on all failure modes
- `supabase/functions/analyze-car-link/sourceDetection.ts` — added `extractEncarCarId(url)`
  - Extracts 6–12 digit carId from `/cars/detail/{carId}`, `/car/detail/{carId}`, `?carid=`, last path segment
- `supabase/functions/analyze-car-link/validation.ts` — added 4 new ErrorCode union members:
  `ENCAR_API_UNAVAILABLE`, `ENCAR_API_NOT_FOUND`, `ENCAR_API_FORBIDDEN`, `ENCAR_API_INVALID_RESPONSE`
- `supabase/functions/analyze-car-link/index.ts` — pipeline update:
  1. Encar direct API (if carId + encar/youcar_encar source)
  2. HTML adapter
  3. Generic fetch
  4. Browser render
  5. listingText
  - Success response includes `carId` and `adapter` fields
  - Error metadata surfaces `adapterAttempted`, `adapterErrorCode`, `carId`

**Frontend**
- `src/services/aiLinkExtraction.ts` — added `adapter?: string` and `carId?: string` to `AnalyzeCarLinkSuccess` type
- `src/components/CalculatorScreen.tsx` — added `adapterLabels` constant, updated confirmation card to show `прямой источник Encar` when `adapter === 'encar_api'`, improved listingText placeholder and added `<details>/<summary>` hint
- `src/App.css` — CSS for `.calcHintDetails`, `.calcHintSummary`, `.calcHintList`

**Scripts and docs**
- `scripts/ai-extraction-pipeline-sanity.mjs` — added carId extraction tests + `buildEncarApiListingText` unit tests + adapter label constant check
- `scripts/ai-edge-live-check.mjs` — added 4 Encar API error codes to `controlledErrorCodes`, added `carId`, `adapter`, `adapterErrorCode`, `apiStatus` to summary
- `docs/supported-listing-sources.md` — pipeline order update, Encar direct API section, error taxonomy update, contract fields update
- `docs/ai-link-extraction-endpoint.md` — AI-5D notes, updated success response example, added ENCAR_API_* codes, updated live check summary fields
- `docs/ai-assisted-calculator-roadmap.md` — Phase AI-5D section added
- `docs/ai-edge-live-acceptance-runbook.md` — Encar direct URL curl test section, AI-5D acceptance criteria
- `docs/examples/ai-link-fem-encar-real-template.json` — NEW
- `docs/examples/ai-link-youcar-real-template.json` — NEW

## Key findings

- Encar API is the highest-reliability extraction path for Encar/YouCar URLs, but geo-blocking from US Supabase IPs is likely
- All Encar API failure codes are non-fatal — pipeline always falls through to HTML adapter and fetch
- 만원 normalization is critical: Encar `salesPrice: 4200` = 42,000,000 KRW, not 4,200 KRW

## Validation results

- lint: ✅ clean
- build: ✅ 495.62 kB main chunk (under 500 kB threshold)
- `npm run ai:pipeline`: ✅
- `npm run ai:edge`: ✅
- `npm run ai:link-ui`: ✅
- `npm run ai:contracts`: ✅
- `npm run ai:risk`: ✅
- `npm run calibration:sanity`: ✅
- `npm run admin:calibration`: ✅
- smoke:test, calc:sanity: require live dev server (Playwright) — not run in this session; expected

## Blockers

None. All code complete and validated.

## Next steps

- Deploy Edge Function: `supabase functions deploy analyze-car-link`
- Live test with a real Encar carId: `npm run ai:edge:live -- --payload docs/examples/ai-link-fem-encar-request.json --allow-controlled-error`
- Verify `carId` and `adapter` appear in live summary when Encar API responds
- If geo-blocked: `adapterErrorCode: ENCAR_API_FORBIDDEN` is expected; controlled error pass
- Next major phase: AI-7 (verified calculation workflow) or Screenshot/OCR if Encar geo-blocking persists
