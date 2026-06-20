# Session 2026-06-16 — Phase 3 Document Pipeline Foundation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[technical-architecture]]
- [[data-model]]

## What was done
- Confirmed Phase 2 is complete, including CodeRabbit remediation commit `e5ad6e4`.
- Implemented Phase 3 document pipeline foundation:
  - Supabase migration `202606160002_document_pipeline.sql`;
  - `document_templates`, `document_versions`, `generation_runs`;
  - private `candidate-documents` storage bucket;
  - `document_generate` PGMQ queue;
  - `apps/worker-documents`;
  - `Dockerfile.worker-documents`;
  - Telegram `/candidate_documents` command and approval callbacks.
- Added OpenAI Responses structured-output path for CV data, plus deterministic mode via `OPENAI_DOCUMENT_MODEL=deterministic`.
- Added DOCX rendering with Docxtemplater/PizZip and PDF rendering through Gotenberg.
- Added Gotenberg Railway service from `gotenberg/gotenberg:8`.
- Deployed:
  - `bot-api` deployment `036f2128-b596-4400-91d2-0429f7f75e3f`;
  - `worker-documents` deployment `2a6bb13a-cf38-4ee2-9fd6-a514713be301`;
  - `gotenberg` deployment `6e69edb9-6e87-4389-86de-8d20e1c1478b`.
- Refreshed Telegram webhook after bot deploy; pending updates were 0.

## Key findings
- Existing Railway service Dockerfiles must copy every workspace app package.json before `pnpm install`, because `pnpm build` builds all apps.
- `worker-documents` needs a direct `node apps/worker-documents/dist/main.js` CMD in its runtime layer; `pnpm --filter` fails without the root package manifest.
- Gotenberg private domain is `gotenberg.railway.internal`; worker uses `http://gotenberg.railway.internal:3000`.

## Blockers
- CV template and consent text still need business/legal approval.
- First production CV generation job has not yet been exercised with a controlled candidate.
- Configured OpenAI model must be verified by the first real job or changed to an available approved structured-output model.

## Verification
- `pnpm check` passed.
- `pnpm test` passed: 37 tests.
- `pnpm build` passed.
- `pnpm format:check` passed.
- Supabase migration list shows local and remote through `202606160002`.
- Railway status is SUCCESS for `bot-api`, `worker-documents`, and `gotenberg`.
- Production health endpoint returned database OK.

## Next steps
- Approve or revise the CV template and consent text.
- Run one complete test candidate through `/candidate_documents`.
- Inspect `document_versions`, `generation_runs`, private storage files, and worker logs.
- Approve the generated CV in Telegram and confirm candidate status becomes `documents`.
- Then refine CV content quality and begin employer catalog assembly.
