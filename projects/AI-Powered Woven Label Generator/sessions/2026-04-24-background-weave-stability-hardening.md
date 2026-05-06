# Session 2026-04-24 — Background weave stability hardening

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Investigated the new post-rebalance failure class where logo/text reading was closer to correct but the woven label background itself became wavy, stretched, or uneven.
- Confirmed the problem was prompt-level background-field freedom rather than logo-interpretation logic: prompts described weave density and material character, but did not explicitly lock even field structure, regular thread spacing, stable tension, or anti-ripple behavior.
- Added a small shared helper `server/label/backgroundFieldStability.ts` with common and material-specific background-field stability language.
- Applied the new stability rules to:
  - full prompt builder
  - compact runtime color/background prompt path
  - HD dark prompt
  - HD refinement prompt
  - HD Cotton Stage A / Stage B / single-pass prompts
  - taffeta single-pass prompt
- Added anti-wave / anti-warp wording to the full negative instructions and a self-check line for even background-field structure.
- Updated focused tests for full prompt and runtime prompt parity.

## Key findings
- The instability was strongest in clean luxury-label cases because the system already constrained motif behavior well, but left the background fabric field too stylistically free.
- Taffeta already had the strongest regular-grid language; HD, cotton, and satin needed more explicit “even field / no ripple / no stretched rows” wording.
- The safest fix was to constrain field regularity while still allowing micro textile variation, so the output stays woven and realistic rather than flat or dead.

## Blockers
- No code blockers.
- Manual/live generation QA is still needed to confirm:
  - beige/light backgrounds look calmer
  - black wordmarks retain good typography
  - the field no longer shows wave-like drift

## Next steps
- Run live QA on:
  - clean black text on beige/light label
  - HD and HD cotton minimal text labels
  - satin minimal luxury text label
  - taffeta dark/gold case
- Confirm product-photo protection still holds after the weave-field hardening.
