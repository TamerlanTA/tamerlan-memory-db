# Session 2026-06-16 — Document Render Dot-Path Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[technical-architecture]]

## What was done
- Investigated first real `/candidate_documents` output after Tamerlan reported the PDF was empty/unfilled.
- Verified `document_versions.structured_data` was populated correctly for candidate `ac3f8e19-790b-44df-a91b-8fe547d749c5`.
- Downloaded generated DOCX from private Supabase Storage and confirmed fields rendered as `undefined`.
- Identified root cause: Docxtemplater default parser did not resolve nested dot-path tags such as `{candidate.full_name}` and `{education.city}`.
- Added a dot-path parser in `apps/worker-documents/src/render.ts`.
- Added `apps/worker-documents/src/render.test.ts` regression coverage to assert rendered DOCX contains candidate data and no `undefined`.
- Redeployed `worker-documents` deployment `571f4438-ed3e-47aa-aa4f-229241b01926`.
- Re-enqueued document generation for the controlled candidate.
- Verified new document version `5c3ff2c0-54a1-4abc-8709-b91cdfad2749` is `pending_approval`.
- Verified generated DOCX contains name, email, phone, and role.
- Verified generated PDF text extraction contains the candidate CV content.

## Key findings
- Phase 3 data generation worked; the bug was isolated to DOCX template rendering.
- The latest valid PDF is storage key `ac3f8e19-790b-44df-a91b-8fe547d749c5/5c3ff2c0-54a1-4abc-8709-b91cdfad2749.pdf`.

## Blockers
- Manager approval callback still needs to be clicked/verified in Telegram.
- CV content quality is still basic and should be improved after the end-to-end approval path is confirmed.

## Next steps
- Open `/candidate_documents`, retrieve the latest pending CV, and approve it in Telegram.
- Confirm candidate status becomes `documents`.
- Then refine prompt/content quality and template wording.
