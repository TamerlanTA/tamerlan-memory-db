# Session 2026-05-25 — AI-2 Secure Link Extraction

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

## What was done
- Implemented AI-2 backend infrastructure only.
- Added Supabase Edge Function folder `supabase/functions/analyze-car-link/`.
- Added separated function modules:
  - `index.ts` — POST endpoint, CORS, listing fetch fallback, response shaping
  - `provider.ts` — OpenAI-compatible provider abstraction and server-side secret access
  - `prompt.ts` — strict JSON extraction prompt that forbids import-cost calculation
  - `validation.ts` — request validation, mirrored extraction schema, normalization, confidence scoring
- Added `docs/ai-link-extraction-endpoint.md`.
- Added `scripts/ai-edge-contract-sanity.mjs` and npm script `ai:edge`.
- Updated `.env.example` with commented Supabase Edge Function secrets only; no `VITE_` AI secrets.
- Updated ESLint config with Deno globals for `supabase/functions/**/*.ts`.

## Key findings
- Supabase Edge Function docs confirm secrets are read server-side via environment variables and local serving uses `supabase functions serve`.
- Local workspace does not have `supabase` CLI or `deno` installed, so runtime/type verification for the Edge Function must be done manually with Supabase CLI/Deno.
- Frontend calculator behavior and app bundle remain unchanged.

## Validation
- `npm run ai:edge` — passed.
- `npm run ai:contracts` — passed.
- `npm run lint` — passed.
- `npm run build` — passed.

## Blockers
- Production activation still requires Supabase migration, Vercel env vars, deploy, and live acceptance.
- Edge Function needs manual Supabase CLI/Deno verification and deployment.
- Provider secrets must be set in Supabase before live use:
  - `AI_PROVIDER=openai`
  - `OPENAI_API_KEY`
  - `AI_MODEL`

## Next steps
- Run `supabase functions serve analyze-car-link --env-file ...` once Supabase CLI is available.
- Deploy the function and set Supabase Edge Function secrets.
- Next implementation phase: AI-3 user confirmation flow, where extracted/normalized data is shown for edit/confirm before deterministic calculation.
