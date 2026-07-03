# Session 2026-07-02 — Block 1 Review And Block 2 Prompt

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[prompts]]

## What was done
- Reviewed Claude's Block 1 implementation for pre-provider semantic input validation.
- Inspected changed files in `server/label/inputSemanticValidation.ts`, `server/routers.ts`, `shared/generationErrors.ts`, client translation/error presentation files, and credit-safety tests.
- Verified locally with focused tests, full Vitest suite, and TypeScript.

## Key findings
- Block 1 is acceptable to continue from: semantic input validation runs after entitlement/run creation but before original upload storage, expensive label generation, result storage, and paid/free-trial commit.
- Clear non-logo/image-scene rejections produce `INPUT_IMAGE_NOT_LOGO`, `BAD_REQUEST`, and client "use another image" UX.
- Paid credit and guest free-trial commit remain protected on semantic rejection.
- Full verification passed: `npx vitest run` passed 42 files / 259 tests; `npx tsc --noEmit` passed.
- Nuance: the semantic gate still uses a small Gemini Flash classifier call, so it prevents expensive image-generation spend, not all provider/token usage.

## Blockers
- Block 1 is not committed/deployed.
- Block 2 output validation is still required to prevent bad generated images from being shown to customers.

## Next steps
- Give Claude the Block 2 prompt: add post-generation output safety validation before result asset storage/bookkeeping.
- Block 2 must catch people/faces/photo-scene output, unrelated brand/text leakage, and non-label compositions; rejected output should not be shown or charged.
- After Block 2, run smoke tests with photo/person inputs and normal logo inputs.
