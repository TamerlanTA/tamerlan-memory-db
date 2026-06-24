# Session 2026-06-24 — CV Photo Fallback Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Audited the existing portrait embedding implementation against the full production task.
- Extracted private Supabase Storage portrait loading and format detection into a tested module.
- Kept JPEG/PNG embedding and added explicit safe fallback text `PHOTO UPLOADED - EMBEDDING FAILED` for download or unsupported-format failures.
- Removed private storage paths from warning logs.
- Made missing DOCX image parts/placeholders and Gotenberg rendering failures explicit `validation_failed` document outcomes.
- Added tests for JPEG loading, format detection, failed download, unsupported WebP, successful embedding, and missing-photo fallback.
- Ran `pnpm check`, `pnpm test`, `pnpm build`, and `pnpm format:check`.
- Committed and pushed `f3e4c9d`, then deployed only `worker-documents` to Railway.

## Key findings
- Official Supabase JavaScript behavior still supports server-side `.storage.from(bucket).download(path)` for private buckets.
- Production document version `84e1f6bf-fe95-40c8-b294-4e6e9588d3a8` completed as `pending_approval` with no validation errors.
- PDF text extraction contains no `PHOTO`, `PENDING`, or `FAILED` placeholder text.
- `pdfimages -list` reports one 1024x1024 JPEG image object.
- PNG visual review confirms the portrait is visible, About Me is below the header, and Experience remains grounded.
- One manual queue test message was accidentally sent as a JSON string, rejected by schema validation, deleted, and replaced with a correct JSON object. The final queue depth is zero.

## Blockers
- WebP conversion is not implemented; managers must re-upload WebP portraits as JPEG or PNG.
- Final portrait crop and overall CV presentation still require manager review before approval.

## Next steps
- Approve or reject document version `84e1f6bf-fe95-40c8-b294-4e6e9588d3a8` through `/candidate_documents`.
- Continue Phase 4 with the first read-only vacancy discovery connector.
