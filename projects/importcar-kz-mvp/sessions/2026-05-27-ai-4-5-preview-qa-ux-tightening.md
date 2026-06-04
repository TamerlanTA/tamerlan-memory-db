# Session 2026-05-27 — AI-4.5 Preview QA and UX Tightening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Reviewed AI-4 result UI structure for overload after adding risk and explanation sections.
- Made "Пояснение к расчёту" collapsible by default.
- Capped visible risk cards to the top 3 and sorted risks by severity while preserving the full snapshot.
- Added `docs/ai-4-preview-qa-checklist.md`.
- Ran mobile Playwright QA at 375px, 390px, and 412px.
- Ran mocked AI-link success QA and old snapshot compatibility QA.

## Key findings
- Result order remains conversion-friendly: total first, breakdown second, risk/explanation after.
- Manual mode remains default and saves `riskReview` / `groundedExplanation`.
- Link mode remains editable and deterministic after confirmation.
- Old saved calculations/local requests without AI-4 fields still render in the request flow.
- Build remains under Vite's default chunk warning threshold at about 494.35 kB.

## Blockers
- Browser plugin was not available, so rendered QA used Playwright fallback.
- Folder is not a git repository, so git status/diff is unavailable.

## Next steps
- Review the tightened AI-4 result UI on the Vercel preview.
- Deploy/promote when approved.
- Proceed to AI-5 Accuracy Calibration only after preview/production review.
