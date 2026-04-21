# Session 2026-04-21 — Input Guidance Softening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Softened upload and pre-generation guidance copy for the post-Milestone-5 polish batch.
- Preserved the product principle that reliable inputs are logos, monograms, graphic symbols, and existing label visuals.
- Added restrained EN/FR copy that explicitly allows unusual or experimental visuals and frames them as less predictable rather than wrong.
- Kept technical validation unchanged: unsupported formats are still blocked, but no category/image-content restrictions were added.
- Scope stayed limited to `Home.tsx`, `Prepare.tsx`, and `LanguageContext.tsx`.

## Key findings
- Upload guidance is rendered in `Home.tsx` and sourced from `LanguageContext.tsx`.
- Prepare previously had no soft input guidance beyond “logo is ready.”
- The old “Avoid: full garment photos...” wording felt too prescriptive for the client preference to preserve creative happy accidents.
- The frontend validator only checks technical upload format support; no content/category blocking was present or introduced.

## Verification
- `pnpm check`: PASS
- `pnpm build`: PASS with known analytics env and bundle-size warnings
- `git diff --check`: PASS

## Blockers
- None.

## Next steps
- Browser QA EN and FR on Home and Prepare.
- Confirm a supported unusual image can still proceed from upload to Prepare and generation start.
- Confirm unsupported technical files still show the technical unsupported-format message.
