# FlowOps Promo Video Scene System

## Related
- [[agent-memory]]

## Current status
- 2026-04-20: Created new Figma design file for the FlowOps 30-second vertical promo scene system: https://www.figma.com/design/jXPSBkTyDPvGK92nI85Jd8
- Figma MCP canvas write was blocked by the Starter-plan tool-call limit immediately after file creation.
- Wrote the complete Figma-ready build specification in `/Users/tamerlan/Desktop/flowopsVideopreviw/docs/flowops-figma-scene-system.md`.
- 2026-04-20: User provided visual reference `/Users/tamerlan/Downloads/Claude Code Clearly Explained.mp4`. Extracted reference frames locally and revised the spec toward a soft warm/mint premium AI explainer style: central mint objects, deep shadows, sparse kinetic type, dust/depth, dark UI fragments only where useful.
- Tried Figma MCP canvas write again after reference review; still blocked by Starter-plan MCP tool-call limit.
- 2026-04-20: Built local Figma plugin workaround at `/Users/tamerlan/Desktop/flowopsVideopreviw/figma-plugin/flowops-scene-system/`. Fixed Figma runtime syntax issue by replacing `??` with older-compatible conditional logic. User confirmed the fix was applied/run.
- 2026-04-20: After user saw the generated file, clarified that the first version placed scenes in a wide 3x2 canvas and Scene 1 was too sparse. Updated plugin v2 to stack all six scenes vertically on `01 Scenes - 1080x1920`, add a page guide, and make Scene 1 a fuller hook with a disconnected-tools dark panel plus large `better systems` mint capsule.
- 2026-04-20: User showed that v2 still only produced Scene 1 plus labels for scenes 2-6. Diagnosis: scene labels were created before frame creation, then runtime stopped after Scene 1. Updated plugin v3 so all six 1080x1920 scene frames are prepared first before any scene is decorated.
- 2026-04-20: Runtime error `failed at scene 1 content: not a function` was caused by `chip()` creating a pill as a Rectangle and then trying to append text into it. Fixed by changing `capsule()` to create a Frame with fills/strokes/cornerRadius, so chip labels can be editable child text layers.
- 2026-04-20: User provided FlowOps landing screenshot and noted overlapping elements. Updated plugin v4 to use brand-aligned dark navy/cyan/violet palette, dark glass panels, soft cyan-violet cards, and revised Scene 4 spacing so panel text, progress bars, and metric chips no longer collide.
- 2026-04-20: Added CapCut animation guide at `/Users/tamerlan/Desktop/flowopsVideopreviw/docs/flowops-capcut-animation-guide.md` with export-layer setup, 30s timing, per-scene animation plan, transitions, and quality checklist.

## Key decisions
- Treat this as a small project note, not a full project folder, unless the promo design evolves into a longer multi-session workstream.
- Creative direction: premium AI explainer short, hybrid motion-design scenes, not generic website sections or app-only screens. Reference-informed style is warm/mint explainer with deep shadows and sparse central objects, adapted to FlowOps systems/automation positioning.
- System should use editable Figma layers, reusable components, consistent 1080x1920 scene frames, and CapCut-friendly layer grouping.
- If Figma MCP quota blocks canvas writes, use the local plugin route instead of waiting on MCP: import `figma-plugin/flowops-scene-system/manifest.json` in Figma Desktop and run `FlowOps Scene System Builder`.

## Blockers
- Figma Starter-plan MCP tool-call limit prevented direct creation of scene frames/components in Figma on both attempts.

## Next steps
- Visually QA the generated Figma pages: `00 Design System + Components`, `01 Scenes - 1080x1920`, `02 Storyboard + Motion Notes`.
- Check that all six 1080x1920 scenes were created and that major text/cards/connectors are editable layers.
- If needed, refine composition based on screenshots from the generated Figma file.
- Rerun the local plugin after v2 update to replace old generated pages with the improved vertical scene stack.
- Use the CapCut animation guide to export Figma layers and animate the 30-second promo.
