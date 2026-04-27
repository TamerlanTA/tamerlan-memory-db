# Session 2026-04-27 — Vercel preview vs production status

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Verified local git state on `milestone4-auth-completion` and confirmed local `HEAD` is `d9762240467712f4994e663946b721a06982a6bc` (`Fix sample price card email rendering`).
- Confirmed GitHub remote branch `origin/milestone4-auth-completion` now also points to `d976224`.
- Queried Vercel deployments for both Griffes projects:
  - `griffes-vivienne-studio-3vop`
  - `griffes-vivienne-studio`

## Key findings
- Vercel has already created READY deployments for commit `d976224` on both Griffes projects.
- The user confusion came from looking at production: on `griffes-vivienne-studio-3vop`, the latest **production** deployment still points to `3040beb` (`Fix new label reset and prove generation credit safety`).
- Commit `d976224` exists in Vercel only as a READY preview deployment (`target: null`), not as the live production target.
- This means GitHub and Vercel are in sync; the missing piece is production promotion / production deployment selection, not another push.

## Blockers
- None on GitHub/Vercel sync itself.
- If the user expects to see the change on the live production domain, the current blocker is that `d976224` has not been promoted to production on `griffes-vivienne-studio-3vop`.

## Next steps
- If needed, inspect which domain the user is checking and confirm whether it points to `griffes-vivienne-studio-3vop` production or a preview alias.
- If the user wants the change live, trigger or promote a production deployment for `d976224` on `griffes-vivienne-studio-3vop`.
