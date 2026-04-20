# Session 2026-04-20 — Revert Moodboard Generation Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[2026-04-19-codex-moodboard-brand-leakage-fix]]

## What was done
- Reverted only the generation/moodboard part of commit `320262f` after owner reported severe HD / HD Cotton quality regression.
- Restored `server/moodboards.ts` exactly to the `8fe695c` version for active moodboard paths and prompt guidance.
- Deleted the six `*_material_safe_*` reference assets added by `320262f`.
- Preserved later client/mobile/white-logo/admin fixes; no broad rollback was performed.

## Key findings
- The `320262f` safe-reference approach removed too much structural conditioning for HD / HD Cotton.
- HD and HD Cotton depended heavily on the original full reference images for composition, support surface, label edge behavior, and motif integration realism.
- Cropped material-only references were safer against brand leakage but degraded material realism too much for production.

## Blockers
- Brand/reference leakage risk is reopened because the original ideal references contain readable competitor marks.
- Do not repeat the same crop-only safe-reference strategy without first validating HD / HD Cotton output quality.

## Next steps
- If anti-leak work is revisited, use a material-specific plan and preserve HD / HD Cotton structural conditioning.
- Consider adding text/logo-copy negative prompt safeguards before changing reference assets again.
- Verify HD and HD Cotton manually after redeploying this rollback.
