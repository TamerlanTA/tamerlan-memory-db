# Session 2026-06-23 — CV Photo Embedding Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated why an uploaded candidate portrait did not appear in generated PDF `5e8a5b44-25dc-4e47-962f-6512c5796a17.pdf`.
- Confirmed the PDF contained `PHOTO UPLOADED - EMBEDDING PENDING`, meaning photo upload/storage worked but DOCX/PDF image embedding was not implemented.
- Implemented portrait embedding in `worker-documents`:
  - downloads JPEG/PNG portrait from private Supabase Storage;
  - injects image relationship/media into DOCX;
  - replaces the photo placeholder run with OOXML drawing markup;
  - preserves placeholder fallback for missing/unsupported images.
- Added regression test for DOCX image embedding.
- Updated CV enrichment runbook.
- Deployed `worker-documents` to Railway.
- Regenerated the controlled candidate CV.
- Pushed commit `04dda5d` (`embed candidate portrait in generated CV`).

## Key findings
- The uploaded portrait existed in production:
  - candidate `ac3f8e19-790b-44df-a91b-8fe547d749c5`;
  - storage path `ac3f8e19-790b-44df-a91b-8fe547d749c5/photos/f5936f61-979b-4122-a7f4-6504c4102320-portrait.jpg`;
  - MIME type `image/jpeg`.
- The previous Phase 3.5 implementation intentionally stored photo status/path but did not embed the image; this was visible in the generated PDF as `PHOTO UPLOADED - EMBEDDING PENDING`.
- Production verification for new document version `0fb3b92b-2397-4ca6-bff5-d7db4072a6bb`:
  - placeholder text is gone from PDF text extraction;
  - `pdfimages -list` shows one JPEG image object on page 1.

## Validation
- `pnpm check` passed.
- `pnpm test` passed: 53 tests.
- `pnpm build` passed.
- `pnpm format:check` passed.
- Local LibreOffice conversion succeeded with the real uploaded portrait.
- Railway status after deploy: all AMIGO services Online.

## Blockers
- WebP is still not embedded; managers should upload/re-upload portraits as JPEG or PNG for final CVs.

## Next steps
- Review the new generated PDF visually in Telegram or via signed URL.
- Approve or reject document version `0fb3b92b-2397-4ca6-bff5-d7db4072a6bb`.
