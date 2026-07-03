# Session 2026-07-02 — Block 2: post-generation output safety validation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done
- Implemented Block 2 (output side): after `generateLabel()` returns an image, the router classifies the generated result with Gemini 2.5 Flash BEFORE `storeGenerationResultAsset` and before any paid-credit / free-trial / basic bookkeeping commit.
- New module `server/label/outputSemanticValidation.ts` — mirrors Block 1's structure (strict JSON, temperature 0, 12s timeout, injectable classifier). The classifier receives BOTH the generated image and the customer's source logo so it can distinguish the customer's own text from unrelated brands (the "American Vintage" complaint case).
- New retryable error code `OUTPUT_IMAGE_REJECTED` (shared taxonomy → retry CTA client-side, FR/EN copy says image and credit are untouched, please retry).
- Rejection reason codes: PEOPLE_OR_FACES, PHOTO_SCENE, UNRELATED_TEXT_OR_BRAND, MULTIPLE_OBJECTS_OR_COLLAGE, NOT_A_WOVEN_LABEL, PRINT_OR_POSTER_NOT_TEXTILE.

## Key findings / decisions
- Same fail-open policy as Block 1: hard reject only on a clear classifier "reject"; validator outage/timeout/malformed-indeterminate response fails open with a logged warning.
- Diagnostics: before throwing, the router writes `validatorStatus: "fail"` + `validatorReason` (reasonCode + summary) to the run row; the existing catch then adds `status: failed`, `normalizedErrorCode: OUTPUT_IMAGE_REJECTED`, `diagnosticStage: label.generate.outputSemantics`. `updateGenerationRun` does partial updates so both writes coexist — no migration.
- This gate coexists with the internal nanoBananaService woven/fidelity validator (which returns warnings, never blocks); the new gate is the only output-side hard stop and it protects credits because it fires before all bookkeeping.

## Blockers
- None. Full suite green: 43 files / 270 tests, tsc clean. NOT committed and NOT deployed per instruction.

## Next steps
- Commit + deploy Blocks 1 and 2 together with the other pending local commits once authorized.
- Watch production `generationRuns` for OUTPUT_IMAGE_REJECTED frequency; if the classifier over-rejects legitimate labels, soften the prompt or add config text hints.
