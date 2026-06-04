# Session 2026-05-27 — AI-4 Risk Review and Explanation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Implemented deterministic AI-4 Risk Reviewer + Grounded Explanation Layer.
- Added `src/domain/aiCalculator/riskReview.ts`.
- Added `src/domain/aiCalculator/explanation.ts`.
- Extended AI calculator types with `CalculationRiskReview`, `CalculationRiskItem`, and `GroundedCalculationExplanation`.
- Integrated "Надёжность расчёта" and "Пояснение к расчёту" sections into calculator results.
- Stored JSON-safe `riskReview` and `groundedExplanation` in saved calculations and lead metadata snapshots.
- Added minimal AdminLeads risk context display.
- Added `scripts/ai-risk-sanity.mjs` and `npm run ai:risk`.
- Updated AI docs.

## Key findings
- AI-4 does not call AI APIs and does not calculate/change final totals.
- Manual calculation remains default and shows "Ориентировочный" risk context.
- Mocked AI-link calculation with missing `productionDate`/`vin` shows medium risk, includes VIN/date risks, and saves risk/explanation metadata.
- User reported live Edge Function acceptance passed before AI-4: HTTP 200, `ok: true`, confidence `medium`, missing fields `productionDate` and `vin`, warnings `[]`.
- Build remains under Vite's default chunk warning threshold at about 493.93 kB main JS.

## Blockers
- Folder is not a git repository, so git status/diff is unavailable.
- Production activation still depends on environment/migration/live QA steps outside this code change.

## Next steps
- Review AI-4 UI on preview/production.
- Proceed to AI-5 Accuracy Calibration when ready.
