# Session 2026-06-22 — CV Profile Enrichment

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Implemented AMIGO Phase 3.5 CV enrichment from the attached production task.
- Added Supabase migration `202606220003_cv_profile_enrichment.sql`:
  - `candidate_photos`;
  - `candidate_work_experiences`;
  - `candidate_education`;
  - `candidate_cv_extras`;
  - private bucket MIME support for `image/jpeg`, `image/png`, and `image/webp`.
- Updated Drizzle schema exports for the new tables.
- Added Telegram manager flows:
  - `/candidate_photo`;
  - `/candidate_experience`;
  - `/candidate_education`;
  - `/candidate_extra`.
- Added parsers and tests for structured work experience, education, extras, and CV readiness warnings.
- Updated `/candidate_view` to show portrait photo status, CV work experience count, education count, extras count, and warnings.
- Updated `worker-documents` loading:
  - portrait photo status/path from `candidate_photos`;
  - real work experience from `candidate_work_experiences`;
  - structured education from `candidate_education`;
  - extras from `candidate_cv_extras`.
- Updated deterministic CV mapping and OpenAI grounding so CV sections map to new tables and unsupported extras/experience are stripped.
- Added `docs/cv-enrichment-runbook.md`.
- Applied migration to production Supabase, deployed `bot-api` and `worker-documents` to Railway, refreshed Telegram webhook, and pushed commit `3a7bd48`.

## Key findings
- The old worker SQL hard-coded `work_experience` as an empty JSON array; this was the direct cause of honest but empty EXPERIENCE sections.
- Supabase Storage bucket `candidate-documents` originally allowed only DOCX/PDF, so photo uploads needed an allowed MIME migration while keeping the bucket private.
- Actual DOCX portrait embedding is not implemented in this phase. The CV now records photo availability and renders `PHOTO UPLOADED - EMBEDDING PENDING` instead of pretending the image is embedded.

## Validation
- `pnpm check` passed.
- `pnpm test` passed: 52 tests.
- `pnpm build` passed.
- `pnpm format:check` passed.
- Production schema verification confirmed all four new tables exist.
- Production bucket verification confirmed `candidate-documents` is private and allows DOCX/PDF/JPEG/PNG/WebP.
- Railway status after deploy: `bot-api`, `worker-documents`, `worker-foundation`, and `gotenberg` all Online.
- Telegram webhook refresh returned `pending_update_count=0` and no last error.

## Blockers
- Manual Telegram photo upload and enriched CV regeneration were not exercised in-chat because no real candidate photo/form responses were supplied during the task.
- DOCX image embedding remains a future rendering improvement.

## Next steps
- Use `/candidate_photo`, `/candidate_experience`, `/candidate_education`, and `/candidate_extra` to enrich pilot candidates.
- Regenerate CVs through `/candidate_documents` and approve/reject them after visual review.
- Continue Phase 4 with the first read-only vacancy discovery connector.
