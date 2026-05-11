# Session 2026-05-11 — MOQ 1000 Branch-Drift Hotfix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated Benjamin's report that the `500 pcs` production quantity option returned in the quote/order flow.
- Confirmed current branch `milestone4-auth-completion` was at `a8a8e5a`, while the earlier MOQ 1000 fix lived on `claude/magical-mendel-0ac677` at commit `35faedc`.
- Re-applied the MOQ 1000 hotfix on the active branch without touching AI generation, favicon, Stripe, DB schema, or the order-flow architecture.
- Updated frontend domain constants, EN/FR order copy, order panel comment, shared order-intent validation, and tests.

## Key findings
- Root cause was branch/deployment drift: `milestone4-auth-completion` did not contain the earlier MOQ commit, so deploying or working from it reintroduced production `500`.
- Production quantity UI is derived from `client/src/domain/order.ts`; raising `PRODUCTION_MIN_QUANTITY` to `1_000` removes the `500` quick option and sets slider min/default behavior to 1000.
- Backend/shared intent validation previously accepted production quantity `500`; `orderIntentDraftPayloadSchema` now rejects production payloads below 1000 while sample payloads remain allowed.
- Remaining `500` search hits are intentional regression tests, `PRODUCTION_QUANTITY_STEP = 500`, HTTP status/error fixtures, CSS timing/weight classes, and unrelated image test dimensions.

## Blockers
- Live deployment still needs to be verified against the deployed commit; local code/tests/build are green.
- Local `git status` remains unreliable because of stale worktree metadata pointing at `.claude/worktrees/elated-engelbart`.

## Next steps
- Ensure the production deployment commit contains this hotfix, then hard-refresh the browser and verify `500` is absent, `1,000` minimum is visible, sample flow still works, and backend rejects a crafted production `500` payload.
- Keep branch selection explicit before future hotfixes: `milestone4-auth-completion` and `claude/magical-mendel-0ac677` have diverged around production stabilization fixes.
