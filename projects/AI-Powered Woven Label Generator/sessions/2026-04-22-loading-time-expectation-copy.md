# Session 2026-04-22 — Loading Time Expectation Copy

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]

## What was done
- Added a truthful estimated-time line to the generation loading footer copy in FR/EN.
- Preserved the existing rotating microcopy and perceived progress architecture.
- Lightly refined one long-wait rotating message with a restrained weaving line:
  - EN: `Good weaving takes a moment.`
  - FR: `Un beau tissage prend un instant.`

## Key findings
- Loading messages live in `client/src/contexts/LanguageContext.tsx`.
- Rotation/timing is driven by `useGenerationLoadingSteps` using `MICROCOPY_KEYS`, `LONG_WAIT_KEYS`, and a 42-second long-wait threshold in `loadingConfig.ts`.
- The existing footer reassurance line was the cleanest place for the estimate, so no layout or generation logic changes were needed.

## Blockers
- None.

## Next steps
- Manual QA the Result loading screen in EN/FR on mobile and desktop to confirm the longer reassurance line wraps cleanly and keeps the premium tone.
