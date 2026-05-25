# Session 2026-05-25 — AI-1 Contracts and Schemas

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

## What was done
- Implemented AI-1 as infrastructure only.
- Added isolated `src/domain/aiCalculator/` module with types, schemas, normalization, confidence scoring, snapshot extension, and barrel exports.
- Added `zod` for runtime validation.
- Added `scripts/ai-contracts-sanity.mjs` and npm script `ai:contracts`.
- Updated `docs/ai-assisted-calculator-roadmap.md` with AI-1 implementation notes.

## Key findings
- Node v26 can run TypeScript modules directly, so the sanity script can import the new domain module without adding a test framework.
- Build still outputs the same app bundle size because the new AI domain module is not imported by the UI.
- Calculator behavior is unchanged.

## Validation
- `npm run ai:contracts` — passed.
- `npm run build` — passed.
- `npm run lint` — passed.

## Blockers
- Production activation still requires Supabase migration, Vercel env vars, deploy, and live acceptance.
- AI-2 is not implemented yet; no AI provider, Edge Function, or backend endpoint exists.

## Next steps
- Run final lint/build validation.
- Next implementation phase: AI-2 secure backend extraction endpoint with server-side provider key, strict input/output validation, and fallback behavior.
