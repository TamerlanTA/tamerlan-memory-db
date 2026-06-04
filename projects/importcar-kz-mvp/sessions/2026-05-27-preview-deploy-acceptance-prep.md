# Session 2026-05-27 — Preview Deploy Acceptance Prep

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Prepared the project for Vercel preview deploy acceptance.
- Added `docs/vercel-preview-acceptance-checklist.md`.
- Updated `README.md` with a current release candidate section.
- Verified docs separate Vercel frontend env vars, Supabase Edge Function secrets, and Supabase DB migration steps.
- Ran full local validation set.

## Key findings
- AI provider secrets are documented as Supabase Edge Function secrets only, not as frontend `VITE_` variables.
- Vercel frontend env docs include only public frontend values.
- Supabase DB migration and RLS checks remain documented in production activation docs.
- All requested local validation commands pass.

## Blockers
- Folder is not a git repository, so git status/diff is unavailable.
- Real-device acceptance still needs to be run against a fresh Vercel preview URL.

## Next steps
- Deploy the current build to Vercel preview.
- Run `docs/vercel-preview-acceptance-checklist.md` on desktop and real mobile device.
- Promote to production only after preview acceptance passes.
