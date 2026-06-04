# Session 2026-05-28 — AI-5C.2 Post-Extraction Quality Gate

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented AI-5C.2 after live URL-only Browserless flow returned schema-valid `ok: true` output with all key vehicle fields missing.
- Added `assessExtractionCompleteness(extractedVehicle)` in the Edge Function validation layer.
- Required calculator handoff fields are now `year`, `price`, `currency`, `engineVolumeCc`, and `fuelType`.
- Recommended fields are tracked separately: `brand`, `model`, `mileageKm`, `transmission`, `trim`, and `vin`.
- Added controlled `EXTRACTION_INSUFFICIENT_DATA` error with HTTP 422, source/method context, missing required/recommended fields, warnings, and optional small `partialVehiclePreview`.
- Updated frontend error mapping with Russian fallback copy and missing-field labels.
- Updated live check script and docs.

## Key findings
- Schema validity is not enough for product success; page-not-found/no-vehicle output must be blocked before the confirmation card.
- `currency: UNKNOWN` and `fuelType: unknown` do not count as usable calculator handoff data.
- Deterministic pricing logic remains unchanged.

## Blockers
- AI-5C.2 still needs deployment to Supabase Edge runtime and live URL-only rerun.

## Next steps
- Deploy updated `supabase/functions/analyze-car-link`.
- Rerun URL-only live acceptance with `npm run ai:edge:live -- --payload docs/examples/ai-link-url-only-request.json --allow-controlled-error`.
- Confirm the current page-not-found/no-data case returns HTTP 422 `EXTRACTION_INSUFFICIENT_DATA` instead of HTTP 200 `ok: true`.
