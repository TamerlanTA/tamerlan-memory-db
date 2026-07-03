# Session 2026-07-02 — Semantic gate observability + error semantics

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done
- Monitoring-focused review of Blocks 1+2 + recovery. Gap: recovery successes and fail-open windows were invisible in `generationRuns` (log-only); input rejections lost the classifier reason code; `OUTPUT_IMAGE_REJECTED` surfaced as HTTP 500 and `console.error`, making expected quality rejections look like crashes.
- Added a compact per-gate audit trail persisted into EXISTING `generationRuns` fields — no migration:
  - `validatorReason` now carries `input=ok|unavailable|rejected:CODE (summary); output=...; recovery=ok|unavailable|rejected:CODE|generation-failed`, plus ` | woven=<status>: <reason>` for the internal validator on success rows.
  - `validatorStatus` = `"recovered"` on success rows whose stored image came from the automatic recovery generation; `"fail"` on semantic rejections (input and output).
  - Helper `describeSemanticGateOutcome()` in `server/routers.ts`.
- Error semantics: `OUTPUT_IMAGE_REJECTED` now maps to tRPC `UNPROCESSABLE_CONTENT` (422, not 500); inner+outer catch logs downgrade to `console.warn` for `INPUT_IMAGE_NOT_LOGO`/`OUTPUT_IMAGE_REJECTED` via `isExpectedQualityRejectionCode()`.
- Admin `/admin/stats` recent-runs table shows the new strings automatically (already renders validatorStatus/validatorReason/normalizedErrorCode).

## Key findings / decisions
- All seven root-cause questions (input gate used? output gate used? first image rejected? recovery ran? recovery outcome? reason code? final image source?) now answerable from a single generationRuns row.
- Client-side retry presentation unaffected (keyed on error message = code).

## Blockers
- None. Focused tests PASS, full `vitest run` PASS (44 files, 276 tests), `tsc --noEmit` PASS, `npm run build` PASS. NOT committed / NOT deployed.

## Next steps
- The full local batch (Blocks 1, 2, seed/recovery, observability) is release-ready pending commit/deploy authorization.
- After deploy: query `generationRuns` for `validatorStatus='recovered'` rate and `validatorReason LIKE '%unavailable%'` for fail-open windows.
