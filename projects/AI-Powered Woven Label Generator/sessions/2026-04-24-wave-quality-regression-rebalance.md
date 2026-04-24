# Session 2026-04-24 — Wave quality regression rebalance

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated a new live-quality regression reported with real generated outputs: the whole scene, including the label ground and support surface, was covered with wavy / swirl-like artifacts.
- Audited the prompt changes added in `e12c8ba` and identified the likely cause: the generation layer was repeatedly using aggressive anti-distortion wording (`wave`, `ripple`, `warped`, `stretched`, `micro-variation`) across full prompts and runtime prompts.
- Replaced that language with calmer positive guidance focused on an orderly, premium, production-like weave.
- Added an explicit support-surface guardrail so the wood / marble / paper background stays smooth and non-textile instead of inheriting thread-like or swirl artifacts from the label prompt.
- Updated full-prompt and runtime-prompt tests to match the new wording.

## Key findings
- The quality drop was likely caused by prompt over-constraint, not by logo-reading logic.
- The previous anti-wave wording seems to have been interpreted too literally by the image model, contaminating the whole scene instead of quietly stabilizing the label ground.
- A positive, lower-anxiety wording style is a better fit here: constrain the label weave calmly and separately forbid textile contamination of the support surface.

## Blockers
- No code blockers.
- Live generation QA is still required to confirm the new wording restores the earlier clean luxury look on:
  - simple black typography on light cotton / HD labels
  - script logos
  - white / ivory labels on marble support surfaces

## Next steps
- Run live QA with the three failing examples provided by the user.
- Compare the new outputs directly against the wave-heavy examples before deciding whether to commit/deploy or continue tuning.
