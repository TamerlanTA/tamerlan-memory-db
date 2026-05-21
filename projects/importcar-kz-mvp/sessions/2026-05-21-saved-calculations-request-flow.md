# Session 2026-05-21 — Saved Calculations and Request Flow

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Implemented Phase 2 pre-auth UX: local saved calculations + local request mirror.
- Added `src/hooks/useSavedCalculations.ts` with resilient localStorage parsing, max 10 saved calculations, duplicate replacement by calculation fingerprint, remove/clear/latest helpers.
- Added `src/hooks/useLocalRequests.ts` with resilient localStorage parsing, max 10 local request mirrors, remove/latest helpers.
- Updated `CalculatorScreen.tsx`:
  - added "Сохранить расчёт" action after calculation result
  - saves JSON-serializable calculation snapshots locally
  - mirrors successful exact-calculation submissions into local requests after Supabase/mock success
  - success copy now says the calculation was saved and request passed to manager
- Rebuilt `RequestScreen.tsx` from placeholder into a real "Заявка" surface:
  - shows latest request when available
  - otherwise shows latest saved calculation
  - lists recent saved calculations with remove actions
  - includes WhatsApp support CTA
  - can switch back to Calculator via `onGoToCalculator`
- Added mobile-first request/saved-calculation styles in `App.css`.

## Key findings
- Existing tab architecture stayed state-based; no router/global state library needed.
- Supabase lead submission behavior was preserved; local request mirror is only saved after successful Supabase insert or existing mock mode success.
- Admin view snapshot metadata remains in the existing snake_case shape; local saved calculation uses camelCase for frontend UX.

## Blockers
- Supabase schema migration still must be run in dashboard before real calculator leads work in production.
- WhatsApp placeholder `77071234567` still exists and must be replaced before launch.

## Verification
- `npm run lint` — passed.
- `npm run build` — passed, output JS bundle about 470.06 kB.

## Next steps
- Complete remaining launch blockers in [[next-steps]]: Supabase migration, real WhatsApp number, deploy/test on iPhone.
