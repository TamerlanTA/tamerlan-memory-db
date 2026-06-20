# Session 2026-06-16 — CV Template Quality Upgrade

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Used the provided Google Doc resume reference as direction for a warmer hospitality CV structure.
- Updated `packages/document-templates/templates/hospitality-cv-en-v1.docx` via `scripts/generate_cv_template.py`.
- Updated `apps/worker-documents/src/cv-data.ts` to:
  - add `candidate.profile_line`;
  - translate common Russian hospitality roles/countries to English;
  - transliterate Cyrillic names and cities for English CV output;
  - replace internal placeholder phrases with candidate-facing wording.
- Updated OpenAI structured schema/prompt to require `profile_line` and avoid placeholder language.
- Added regression tests for Cyrillic formatting and new render expectations.
- Deployed `worker-documents` to Railway and regenerated controlled candidate CV.
- Committed and pushed `a11145b` (`improve hospitality CV template quality`) to `main`.

## Key findings
- The previous generated CV was technically filled but not employer-ready: it exposed internal phrases like `pending manager enrichment`, Cyrillic values in an English CV, and weak placeholder sections.
- Final generated PDF text for candidate `ac3f8e19-790b-44df-a91b-8fe547d749c5` verifies:
  - `Tamerlan Tog`;
  - `Waiter`;
  - `Almaty, Kazakhstan`;
  - `Hospitality readiness profile`;
  - no old `pending manager enrichment` or `provided on request` text.
- Latest document version: `9219995e-fed0-407c-a27f-f5ee3493cd71`, status `pending_approval`, validation errors `[]`.

## Blockers
- Telegram approval callback and candidate status transition still need a real manager click test.
- CV quality is now acceptable for a sparse profile, but strong real CVs require collecting actual employers, dates, duties, and achievements instead of relying on boolean experience signals.

## Next steps
- In Telegram, run `/candidate_documents`, select the controlled candidate, and approve or reject latest CV version `9219995e-fed0-407c-a27f-f5ee3493cd71`.
- Verify approved CV status and candidate status transition.
- Decide which structured experience fields to add to intake before scaling beyond the pilot.
