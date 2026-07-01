# Session 2026-06-29 — Homepage Custom Workflow Section Refinement

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done
- Reworked the homepage `We can build / custom workflow` section to match the newer bright/editorial canvas direction.
- Removed the old two-row block grid of workflow cards.
- Replaced it with an open process-map composition: trigger surface, map copy, build surface, approval surface, connector paths, color fields, and lightweight works/breaks fallback logic.
- Added `.custom-workflow-piece` pointer-only hover polish using transform/box-shadow transitions.
- Removed now-unused `workflowSteps` constant after the old grid was replaced.
- Verified desktop/mobile screenshots and no horizontal overflow.
- Ran `npm run lint` and `npm run build` successfully.

## Key findings
- The previous section broke visual continuity after the integrated `How it works` and marketplace sections because it reverted to equal-weight blocks.
- Absolute desktop compositions need an explicit inner scene height when using `bottom-*` positioning; otherwise bottom-positioned nodes can calculate from zero-height parents and clip upward.
- Decision logic works better as a compact annotation than as another large headline in the scene.

## Blockers
- None.

## Next steps
- Continue transforming the next homepage sections with the same open-canvas language.
- If shipping immediately, deploy the homepage changes to Vercel preview or production as requested.
