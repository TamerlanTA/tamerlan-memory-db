# Session 2026-07-02 — Demo-stability audit + retry entropy & output-rejection recovery

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Senior end-to-end audit of the generation reliability surface after Blocks 1+2 (both still local/uncommitted).
- Audit verdict: credit/free-trial ordering, admin diagnostics (recentRuns already shows normalizedErrorCode/validatorStatus/validatorReason), stale-run cleanup, and client error CTA wiring are all sound. Two real gaps found and fixed:
- **Gap 1 — deterministic retry loop:** `generateSeed()` is a pure hash of the config and the prompt tells the model to keep visual consistency with that seed. A retry after `OUTPUT_IMAGE_REJECTED` rebuilt the identical prompt+seed, steering the model to reproduce the same bad output. Fixed with `deriveGenerationSeed(config, variation)` (`server/utils/generationSeed.ts`), `seedVariation` on `GenerateLabelInput`, optional `attempt` on the router input, and Result.tsx sending its existing retry counter. Attempt 0 keeps the historical seed (consistency preserved).
- **Gap 2 — customer-visible output rejections:** the router now performs ONE automatic recovery generation (seedVariation 1000+attempt) when the output gate rejects, re-validates the new image, and only surfaces `OUTPUT_IMAGE_REJECTED` if recovery also fails. Recovery errors fall back to the original rejection, never a worse error.

## Key findings / decisions
- Recovery seed offset base 1000 so it never collides with manual retry counters (capped at 100 in the schema).
- Worst case per request is now 2 generations + 3 flash validations — within the same envelope as nanoBananaService's existing internal 3-attempt retries.
- No vercel.json maxDuration change: current production already sustains multi-attempt runs; flagged for monitoring instead.

## Blockers
- None. Verification: focused tests PASS, full `vitest run` PASS (44 files, 276 tests), `tsc --noEmit` PASS, `npm run build` PASS. NOT committed / NOT deployed per instruction.

## Next steps
- Commit + deploy the whole local batch (Blocks 1, 2, this stabilization) when authorized.
- Post-deploy monitoring: recovery log lines (`output.semanticValidation.recovery.*`), OUTPUT_IMAGE_REJECTED/INPUT_IMAGE_NOT_LOGO frequency in generationRuns, request duration vs platform timeout on recovery paths.
