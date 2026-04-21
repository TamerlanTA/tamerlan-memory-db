# Session 2026-04-21 — Generation Error Taxonomy

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Implemented a narrow UX/error-handling stabilization fix for generation failures.
- Added a typed shared generation error taxonomy with presentation metadata for retry vs new-image actions.
- Added server-side generation error normalization near the Nano Banana / Gemini service boundary.
- `label.generate` now throws typed app-level tRPC errors instead of surfacing misleading raw provider messages to the client.
- Result page now maps normalized error codes to calm FR/EN copy and dynamic CTA behavior.
- React `ErrorBoundary` no longer blames the uploaded image for generic runtime crashes.

## Key findings
- The misleading message came from both layers:
  - server returned raw generation/provider failure text
  - Result UI always showed the same image-blaming error copy
- Free trial / credit consumption remains success-only in the audited path: failed generation errors occur before `createFreeTrialGenerationWithCommit` / paid spend bookkeeping.

## Verification
- `pnpm check`: PASS
- Focused tests: PASS — `server/label/generationErrors.test.ts`, `client/src/domain/generationErrorPresentation.test.ts`, `server/generation.test.ts`, `client/src/domain/resultFlow.test.ts`, `client/src/lib/trpcTransport.test.ts` (31 tests)
- `git diff --check`: PASS

## Blockers
- Live provider behavior still needs smoke verification with real 503/overload/timeout/rate-limit conditions.

## Next steps
- Deploy or preview-test a forced/upstream unavailable generation path and confirm the user sees service-temporary copy, not image-invalid copy.
- Continue live QA for generation quality, mobile upload, large payload, order/email, account downloads, and admin metrics.
