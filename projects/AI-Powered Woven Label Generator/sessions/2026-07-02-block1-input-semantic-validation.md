# Session 2026-07-02 — Block 1: Pre-provider semantic input validation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done
- Implemented Block 1 (input-side only): server classifies each uploaded image semantically with Gemini 2.5 Flash BEFORE asset storage, `generateLabel`, and any credit/free-trial commit.
- New module `server/label/inputSemanticValidation.ts` — `validateGenerationInputSemantics({logoBase64, logoMimeType})`, strict-JSON classifier prompt, typed result (accepted/rejected + reasonCode + detectedContent), injectable classifier for tests.
- New error code `INPUT_IMAGE_NOT_LOGO` in `shared/generationErrors.ts`, mapped to BAD_REQUEST server-side and to a "use another image" (new_image) CTA client-side. FR/EN copy added in `client/src/contexts/LanguageContext.tsx`.
- Gate wired into `server/routers.ts` label.generate: after `createGenerationRun` (so rejection persists in generationRuns diagnostics via existing failure handler — no DB migration), before `storeOriginalUploadAsset`.

## Key findings / decisions
- Safety policy: **fail open** when the validator is unavailable (missing key, provider error, 12s timeout, indeterminate response) with a logged warning; **hard reject only** on a clear "reject" verdict. Malformed-but-clearly-reject responses still reject (fallback reasonCode LOGO_NOT_ISOLATED).
- No migration needed: rejections land in generationRuns as status=failed, normalizedErrorCode=INPUT_IMAGE_NOT_LOGO, diagnosticStage=label.generate.inputSemantics.
- Vitest spyOn-on-module-namespace pattern works with the router's dynamic imports (same pattern as existing db mocks).

## Blockers
- None. Full suite green: 42 files / 259 tests, tsc clean.

## Next steps
- Block 2 (not started): output-side validation of generated label results.
- Follow-up (optional): dedicated generationRuns column for semantic-rejection reasonCode if analytics need it; currently only the normalized code is stored.
