# Session 2026-05-25 — AI-Assisted Calculator Roadmap

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

## What was done
- Updated project memory and repo docs for the new AI-assisted calculator direction.
- Clarified that ImportCar.kz is becoming an AI-assisted import calculator, not an AI-only calculator.
- Documented that AI extracts, normalizes, enriches, explains, and flags risks.
- Documented that deterministic pricing engine remains the source of truth for final totals.
- Added repo doc `docs/ai-assisted-calculator-roadmap.md`.
- Updated README with product direction and safe public positioning.
- Added scope notes to production activation/live acceptance docs to keep current deploy separate from future AI work.

## Key findings
- Current app state remains Production Calculator v1 + Phase 3B deploy prep.
- Existing Supabase lead metadata migration is still the immediate production blocker.
- The previous next strategic item was Auth; priority is now AI-assisted calculator architecture/contracts before Auth, Payments, Subscriptions, or App Store packaging.
- Public docs should not promise 5-7% accuracy until real estimate-vs-final data validates it.

## Decisions
- AI is not the final price authority.
- AI output for vehicle extraction must be strict JSON and validated, preferably with Zod.
- User must confirm/edit extracted vehicle data before deterministic calculation.
- AI API calls must not happen from the frontend; future implementation should use Supabase Edge Function or another secure backend endpoint.

## Blockers
- Production activation still requires Supabase migration, Vercel env vars, deploy, and live acceptance.
- AI implementation is intentionally not started yet.

## Next steps
- Complete production activation.
- Then implement Phase AI-1 only: contracts, schemas, snapshot extension types, and confidence logic design with no real AI API.
