# Session 2026-06-30 — Generation Platform Health Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Audited production Vercel deployment, production env presence, recent production logs, production DB generation/asset tables, local build/typecheck/tests, and generation/error-handling code paths.
- Checked live domain `https://methode.griffesvivienne.com`, Vercel deployment `dpl_FsiZLHuxjxBREUzZrTmkpCVKYbQH`, production env names, recent `label.generate` logs, `generationRuns`, `generations`, and `assets`.
- Inspected `server/nanoBananaService.ts`, `server/routers.ts`, `server/label/generationErrors.ts`, `shared/generationErrors.ts`, and client Result error presentation.
- Implemented local step-1 stabilization: fail-closed validation behavior, provider `INVALID_ARGUMENT` normalization, explicit entitlement errors, Result premium-lock handling, and stale test expectation updates.
- Repaired release tooling: removed accidental tracked `.claude/worktrees/*` gitlink entries from the index, added ignores for `.claude/worktrees/` and `.vercel/`, replaced the broken `.vercel` temp symlink with a stable local `.vercel/project.json`, and verified Vercel CLI can inspect the linked production project.
- Created local release commit `d25e7b1` (`Stabilize generation failure handling`) and deployed it directly to Vercel Production as `dpl_HkE8JkNdaiQkDiCLkBgB5EE5pMuv`; GitHub push failed because local HTTPS credentials are not configured.

## Key findings
- Platform is live, not fully down. Production responds 200 and deployment is READY.
- Generation is degraded: DB shows 204 successful generations, 20 failed, and 5 old `started` runs; checked 2026-06-30 window had 7 successes and 1 failed run.
- Recent failures are provider/request failures: Gemini returned `400 INVALID_ARGUMENT`; current normalization maps this to `GENERATION_FAILED_UNKNOWN` / HTTP 500.
- R2 is working in production now; recent original, derivative, and generation result assets have R2-backed storage keys.
- Production Clerk configuration is unsafe for launch: live deployment uses Clerk test keys (`pk_test` / `sk_test`) with `NODE_ENV=production`.
- Local validation: TypeScript and build pass, but full Vitest still fails 10 generation/texture tests.
- Main generation quality risk is deliberate best-effort behavior in `server/nanoBananaService.ts`: non-pass validation and protocol errors are logged but still returned as `success: true`.
- Guest free-trial exhaustion and similar entitlement errors can appear as generic 500s instead of clear paywall/account states.
- ~~Release operations remain fragile because `git status` fails from stale worktree metadata and local `.vercel` is a broken temp symlink.~~ Repaired later in the same work block.
- After local fixes, quality gates are green: `vitest run` PASS (41 files, 241 tests), `tsc --noEmit` PASS, Vite/esbuild build PASS. Build still warns only about the known large client chunk.
- After release-tooling repair, `git status --short --branch` works again. Vercel CLI identifies project `griffes-vivienne-studio-3vop` (`prj_LkPZqybEyxElduycv9y1O1qu6G4j`) and lists Production env vars successfully.
- Production alias `https://methode.griffesvivienne.com` now serves bundle `assets/index-DCe4fzhf.js`; the bundle contains `GUEST_FREE_TRIAL_EXHAUSTED` and `INSUFFICIENT_CREDITS`, confirming the client-side entitlement handling is live.
- The same live bundle still contains Clerk `pk_test_YWJsZS1jaGVldGFoLTcuY2xlcmsuYWNjb3VudHMuZGV2JA`, so Clerk live-key replacement remains the top production-readiness blocker.

## Blockers
- ~~Production deploy is still pending; local fixes are not live yet.~~ Resolved by direct Vercel production deploy `dpl_HkE8JkNdaiQkDiCLkBgB5EE5pMuv`.
- Production Clerk live-key replacement requires dashboard/env access and redeploy.
- Production still uses Clerk test keys until `CLERK_PUBLISHABLE_KEY`, `VITE_CLERK_PUBLISHABLE_KEY`, and `CLERK_SECRET_KEY` are replaced with live values.
- GitHub remote push remains blocked locally until HTTPS credentials or another authenticated remote method is configured.

## Next steps
- Push commit `d25e7b1` to GitHub once local GitHub credentials are available, so repository history matches the already-deployed Vercel production hotfix.
- Replace production Clerk test keys with live keys before or alongside the deploy.
- Add persistent observability for upstream error status/code, model, attempts, and validator reason.
- Re-run production generation matrix after fixes and record results in [[current-state]].
