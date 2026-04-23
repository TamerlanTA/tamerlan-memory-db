# Session 2026-04-23 — Product Photo Brand-Mark Interpretation Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Inspected the live generation path in `server/nanoBananaService.ts`, `server/label/buildGenerationPrompt.ts`, `server/label/variationProfiles.ts`, and the generation/pipeline tests.
- Verified the root cause: the uploaded image was always treated as logo artwork, the prompt explicitly asked Nano Banana to preserve the supplied logo geometry, and there was no product-photo-specific interpretation branch, crop, or masking layer.
- Added a shared source-image interpretation helper so prompts now tell the model to isolate the visible brand mark when the upload is a product/fashion photo and to ignore garment/person/product scene context.
- Applied the new rule to the full label prompt, compact API prompt, HD dark variant, HD motif refinement, HD cotton motif refinement, HD cotton single-pass fallback, and inline image payload labels.
- Added focused regression coverage for the new prompt wording and inline source-image labeling.

## Key findings
- The bug was prompt-driven, not a random provider mistake: the system consistently told the model the whole upload was “the logo” and to preserve its full geometry.
- There is still no real crop/detection pipeline for localized branding, so the safest durable fix in this batch was prompt hardening plus clearer source-image framing.
- The current fix keeps product-photo uploads allowed and does not add classifiers, blockers, or extra friction.

## Blockers
- None for local implementation.
- Live browser/provider QA is still needed to confirm the new prompt wording materially improves chest-logo and centered-branding cases.

## Next steps
- Run live generation QA with product photos containing small localized branding, including a chest logo and a centered branded detail.
- Watch for edge cases where the visible mark is extremely tiny, low-contrast, or heavily folded; consider a lightweight crop heuristic later only if prompt hardening is not enough.
