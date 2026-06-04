# Session 2026-05-28 — AI-5C.1 AI Output Validation Debug

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Implemented AI-5C.1 after live URL-only Browserless flow reached AI provider but failed with `AI_OUTPUT_INVALID`.
- Added safe validation diagnostics for AI provider schema failures: `validationIssues` include field path, expected message, received type, and capped preview.
- Changed `AI_OUTPUT_INVALID` from HTTP 502 to HTTP 422.
- Added conservative pre-validation normalization for common harmless provider variations: currency symbols/names, fuel labels, numeric strings, money strings, mileage strings, engine volume strings, country aliases, and missing arrays.
- Kept strict validation for unsafe values; confidence labels like `"medium"` still fail and are reported diagnostically.
- Hardened extraction prompt around JSON-only output, enum values, numeric confidence, numeric fields, and no import-cost calculation.
- Updated live check script to print validation issue summaries without secrets or raw provider output.
- Updated docs for endpoint behavior and live acceptance debugging.

## Key findings
- Browserless/source detection path is working; the current blocker moved from page rendering to provider-output schema compliance.
- Edge runtime should now return controlled 422 responses for invalid provider output, making live debugging more honest and less noisy.
- Pricing logic remains unchanged; deterministic calculator remains the final-price authority.

## Blockers
- AI-5C.1 still needs deployment to Supabase Edge runtime and live URL-only rerun.

## Next steps
- Deploy updated `supabase/functions/analyze-car-link`.
- Rerun URL-only live acceptance with `npm run ai:edge:live -- --payload docs/examples/ai-link-url-only-request.json --allow-controlled-error`.
- If output is still invalid, inspect safe `validationIssues` and adjust normalization/prompt only when the correction is conservative.
