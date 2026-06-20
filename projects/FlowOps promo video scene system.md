# FlowOps Promo Video Scene System

## Related
- [[agent-memory]]

## Current status
- 2026-06-17 retention pacing refinement: User said the video still forced viewers to wait because too many elements appeared one-by-one. Applied marketing-psychology framing: reduce waiting once the pattern is understood, group related elements, and make the peak/end stronger. Shortened active render to 18.00s, changed problem/effect elements to clustered entrances, varied motion types (`snap`, side slides, drops), moved solution beats earlier, and kept the centered final SVG logo/signature screen.
- 2026-06-17 snappy pacing refinement: User said the appearance animations felt too long and boring. Tightened the Remotion pacing across the active 1080x1350 composition: shorter fade/reveal windows, faster spring entrances, earlier scene beats, reduced total duration from 22.06s to 20.00s, and kept motion varied without adding heavy copy or sales language.
- 2026-06-17 logo refinement: User provided `/Users/tamerlan/Desktop/flowops_logo_enhanced_vector.svg` and requested replacing the final PNG logo with a clean backgroundless SVG. Copied it to `/Users/tamerlan/Desktop/videos-for-blog/public/flowops-logo-mark.svg`, updated the final brand screen to use that SVG via `staticFile`, removed card-like logo radius/shadow, verified still frame `outputs/qa/svg-logo-final.png`, and rerendered the active portrait MP4.
- 2026-06-17 dynamic portrait refinement: User requested larger scale for phone viewing, more varied/lively animation, and a separate final brand screen. Increased scene scale for 1080x1350, added subtle camera drift and floating element motion, extended duration to 22.06 seconds, faded the progress bar before the ending, and changed the final brand treatment into a centered full-screen column: logo -> `Tamerlan Togysbayev` -> `AI automation engineer`.
- 2026-06-17 portrait conversion: User requested non-Reels portrait format 1080x1350 and final personal branding. Changed Remotion composition dimensions to 1080x1350, scaled/compacted scene content for 4:5 layout, copied `flowopslogowhite.png` into `public/flowopslogowhite.png`, and added final signature: `Tamerlan Togysbayev / AI automation engineer`.
- New active portrait render: `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-problem-solution-effect-portrait.mp4` (18.00 seconds, H.264, 1080x1350, ~2.6 MB). QA contact sheet: `/Users/tamerlan/Desktop/videos-for-blog/outputs/qa/portrait-contact-sheet.png`.
- 2026-06-17 refinement: User flagged two workflow-path artifacts: a standalone dangling line in early solution frames and a blue dot peeking beside the final black `saves booking` pill. Fixed by delaying path draw, increasing SVG dash length so no repeated dash segment appears at zero progress, removing the moving blue dot, and realigning the path endpoint to land under the final pill. Also strengthened the final effect with a dark completion panel: `problem solved / lead handled end-to-end`.
- 2026-06-17 follow-up: User approved the white/minimal visual direction but said the 14s version was meaningless/unstructured. Revised the Remotion composition into an 18-second story with three explicit beats: problem (messages pile up / slot lost), solution (one workflow handles message -> AI reads -> checks slots -> writes reply -> saves booking), effect (booking confirmed / calendar updated / owner notified). Still no agency selling or FlowOps pitch.
- New active render: `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-problem-solution-effect-reel.mp4` (19.05 seconds, H.264, 1080x1920, ~2.1 MB). QA contact sheet: `/Users/tamerlan/Desktop/videos-for-blog/outputs/qa/problem-solution-effect-contact-sheet.png`.
- 2026-06-17: User rejected the prior generated video direction as too salesy/heavy. Revised `/Users/tamerlan/Desktop/videos-for-blog` into a 14-second white minimal organic workflow reel inspired by local references `Scene (8).mp4` and `Scene (9).mp4`: sparse words, white background, simple message → AI thinking → workflow → booked path, no agency selling or final FlowOps pitch.
- New render: `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-minimal-workflow-reel.mp4` (14.06 seconds, H.264, 1080x1920, ~1.7 MB). QA contact sheet: `/Users/tamerlan/Desktop/videos-for-blog/outputs/qa/minimal-contact-sheet.png`.
- 2026-06-14: Installed the reusable salon case-study Remotion project into `/Users/tamerlan/Desktop/videos-for-blog`, using the logo asset from that folder. This was the previous 40-second sales/case-study direction before the 2026-06-17 minimal organic revision.
- Fresh validation passed after upgrading Remotion packages to 4.0.477: `npm run lint`, `npm run build`, six representative still renders, full H.264 render, and production dependency audit with 0 high-severity findings.
- Current rendered Reel: `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-salon-automation-reel.mp4` (40.04 seconds, H.264, 1080x1920). QA contact sheet: `/Users/tamerlan/Desktop/videos-for-blog/outputs/qa/contact-sheet.png`.
- 2026-06-11: Built a reusable Remotion case-study Reel template in `/Users/tamerlan/Desktop/flowops-cartoon`.
- Added composition `FlowOpsSalonAutomation`: 1080x1920, 30 fps, 1200 frames / 40 seconds.
- Implemented six scenes for the salon speed-to-lead story: lost lead, fragmented follow-up, FlowOps reveal, simplified automation workflow, successful booking chat, and final brand screen.
- Scenario copy is centralized in `src/content.ts`; visual tokens and animation timing are centralized in `src/theme.ts`.
- Reusable components include `ChatBubble`, `WorkflowNode`, `AnimatedArrow`, `StatusBadge`, `LogoReveal`, `SectionTitle`, `PhoneFrame`, and `SceneBackground`.
- Used the local FlowOps logo from `/Users/tamerlan/Desktop/videos-for-blog/flowopslogo.png`, copied into the Remotion `public/` folder.
- Validation completed: `npm run lint`, `npm run build`, representative still renders, and full H.264 render all passed.
- Final rendered Reel: `/Users/tamerlan/Documents/Codex/2026-06-11/files-mentioned-by-the-user-you/outputs/flowops-salon-automation-reel.mp4`.
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
- 2026-04-20: User asked to do the animation fully. Created local Python/PIL renderer at `/Users/tamerlan/Desktop/flowopsVideopreviw/scripts/render_flowops_promo.py` and rendered silent 30s MP4 `/Users/tamerlan/Desktop/flowopsVideopreviw/exports/flowops_promo_1080x1920.mp4` plus contact sheet and SRT timing file.
- 2026-04-20: User clarified they do not need rendered video yet; they need separate blocks to assemble/animate manually. Created block export script `/Users/tamerlan/Desktop/flowopsVideopreviw/scripts/export_flowops_blocks.py` and exported full-canvas transparent PNG layer pack to `/Users/tamerlan/Desktop/flowopsVideopreviw/exports/capcut_blocks/` with per-scene folders, previews, contact sheet, and README.

## Key decisions
- Use `public/flowops-logo-mark.svg` for the final logo mark; do not use the old PNG with white background on the final brand screen.
- Animation pacing preference from 2026-06-17: avoid slow, drawn-out entrances. Keep organic videos snappy and dynamic with short reveals, quick scene beats, varied motion, and no unnecessary waiting.
- Retention rule from 2026-06-17: once a viewer understands the pattern, do not make them wait for each element individually. Group related elements, use varied entrances, and move quickly to the next meaning beat.
- Dynamic treatment from 2026-06-17: portrait videos should be larger and more phone-readable, with subtle motion variety (camera drift, staggered/floating elements) while preserving the white minimalist style.
- Final brand treatment should be a separate centered screen in a vertical stack: logo, `Tamerlan Togysbayev`, `AI automation engineer`.
- Current publishing format from 2026-06-17: use 1080x1350 portrait, not 1080x1920 Reels, for this video variant.
- Final brand treatment: include personal signature with logo and `Tamerlan Togysbayev / AI automation engineer`, while still avoiding hard agency sales copy.
- Story requirement from 2026-06-17: white minimal style is good, but every organic workflow video still needs a clear structure: problem first, then solution, then effect/result. Avoid purely abstract “work path” visuals with no narrative stakes.
- New creative preference from 2026-06-17: for organic traffic videos, avoid agency promo language, dark premium pitch visuals, heavy copy, and “selling FlowOps.” Prefer bright white minimal scenes, very few words, clear process/path visuals, and a quiet “what I built” feeling.
- Treat this as a small project note, not a full project folder, unless the promo design evolves into a longer multi-session workstream.
- Use Remotion as the reusable production template for case-study videos; keep story copy and theme tokens separate so future scenarios can be changed without rebuilding scene components.
- Keep workflow visuals conceptual and owner-friendly rather than reproducing Make or n8n interfaces.
- Creative direction: premium AI explainer short, hybrid motion-design scenes, not generic website sections or app-only screens. Reference-informed style is warm/mint explainer with deep shadows and sparse central objects, adapted to FlowOps systems/automation positioning.
- System should use editable Figma layers, reusable components, consistent 1080x1920 scene frames, and CapCut-friendly layer grouping.
- If Figma MCP quota blocks canvas writes, use the local plugin route instead of waiting on MCP: import `figma-plugin/flowops-scene-system/manifest.json` in Figma Desktop and run `FlowOps Scene System Builder`.

## Blockers
- Figma Starter-plan MCP tool-call limit prevented direct creation of scene frames/components in Figma on both attempts.

## Next steps
- Review `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-problem-solution-effect-portrait.mp4`; this is now the active 1080x1350 output.
- Review `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-problem-solution-effect-reel.mp4`; if refining, preserve both constraints: white/minimal visual style and problem -> solution -> effect structure.
- Review `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-minimal-workflow-reel.mp4`; if refining, keep the white/minimal/organic direction and adjust only density, wording, pacing, or specific workflow labels.
- Keep `/Users/tamerlan/Desktop/videos-for-blog/outputs/flowops-salon-automation-reel.mp4` only as an older comparison point; the active direction is the minimal organic workflow reel.
- Add audio, voiceover, or sound effects only after the silent visual pacing is approved.
- Visually QA the generated Figma pages: `00 Design System + Components`, `01 Scenes - 1080x1920`, `02 Storyboard + Motion Notes`.
- Check that all six 1080x1920 scenes were created and that major text/cards/connectors are editable layers.
- If needed, refine composition based on screenshots from the generated Figma file.
- Rerun the local plugin after v2 update to replace old generated pages with the improved vertical scene stack.
- Use the CapCut animation guide to export Figma layers and animate the 30-second promo.
- Use `/Users/tamerlan/Desktop/flowopsVideopreviw/exports/capcut_blocks/` for manual CapCut assembly; import each scene folder's PNGs in README order.
