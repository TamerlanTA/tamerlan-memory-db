# Session 2026-04-26 — Save-Worthy Infographic Prompt

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]
- [[projects/David/prompts]]

## What was done
- Updated WF-09 image generation prompt after user feedback that images were cleaner but too empty and not engaging.
- Shifted image strategy from decorative minimal dashboard cards to save-worthy social infographic posters.
- New image requirements:
  - 4:5 vertical Threads/LinkedIn format
  - strong headline
  - 3-5 short useful labels/bullets
  - layout type such as cover/checklist/framework/stack/before-after
  - warm off-white/grid paper style
  - bold black/deep-navy type
  - one muted accent color
  - no neon, robots, rockets, fake metrics, third-party logos, copied social handles, or dense AI-looking filler

## Key findings
- The previous minimal prompt reduced obvious AI artifacts but lost informational value.
- The desired direction is closer to educational carousel covers and structured visual notes, not generic SaaS dashboard art.

## Blockers
- AI image text rendering may still need real-output iteration; Gemini may misspell if too much text is requested.

## Next steps
- Import WF-09.
- Generate 2-3 test posts and compare image readability/informativeness.
- If text rendering is weak, reduce image text to headline + 3 labels max.
