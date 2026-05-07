# Session 2026-05-08 — 25x25 Square Format Generation Hotfix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated owner screenshots where selected `25x25` generated as a long horizontal woven label.
- Confirmed UI/order state was correct: result and quote panel both carried `25x25`; the problem was in generation prompt control.
- Fixed prompt/domain instructions so `25x25` is treated as a physical square label body, not merely a label code.
- Removed the worst conflicting instruction for HD Cotton runtime prompts: `One long horizontal woven cotton label only` now resolves dynamically from the requested format.
- Added square-format locks for compact runtime prompts, full prompt view instructions, quality guardrails, validation prompt, and retry feedback.
- Added regression tests for `25x25` HD and HD Cotton prompts to ensure they include square/1:1 instructions and do not include the long-horizontal cotton hardcode.

## Key findings
- Root cause for HD Cotton: runtime prompt explicitly told Gemini to render a long horizontal woven cotton label even when `config.size` was `25x25`.
- Root cause for HD/other paths: `25x25` existed in config, but prompt language was too soft; reference images and generic label defaults could overpower the requested physical aspect ratio.
- The fix is prompt-level/validator-level, not UI-level.

## Blockers
- `git diff --check` still fails because the local workspace has stale/conflicting git worktree metadata pointing at `/Users/tamerlan/.git/worktrees/elated-engelbart`.

## Verification
- `pnpm exec vitest run server/nanoBananaService.helpers.test.ts server/generation.test.ts` PASS — 49 tests.
- `pnpm check` PASS.
- `pnpm build` PASS with existing analytics env and bundle-size warnings.

## Next steps
- Run a live generation for `25x25` HD beige/black and `25x25` HD Cotton beige/black after deploying this patch.
- If Gemini still drifts, add image post-validation retry feedback specifically saying `FORMAT=NO because 25x25 must be square, not long horizontal`.
