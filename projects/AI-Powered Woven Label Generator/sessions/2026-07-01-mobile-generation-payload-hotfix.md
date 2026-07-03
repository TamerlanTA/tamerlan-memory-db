# Session 2026-07-01 — Mobile Generation Payload Hotfix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated a mobile Safari screenshot showing `Service temporarily unavailable` during generation while desktop generation mostly worked.
- Vercel CLI logs returned no request logs for the active deployment/domain, so the investigation followed the client upload and generation payload path.
- Hardened `client/src/domain/logoAssets.ts`: lowered generation canvas max dimension from `1280` to `960` and excluded heavy original uploads above `750_000` chars from the generation request.
- Added regression coverage in `client/src/domain/logoAssets.test.ts` for the new default dimension cap and heavy-mobile-original exclusion.
- Created local commit `883ca3c` (`Harden mobile logo generation payloads`).
- Deployed directly to Vercel Production as `dpl_iP1YJvhGLkZmQcs9eh3vvzKBUtVh`, READY and aliased to `https://methode.griffesvivienne.com`.

## Key findings
- The screenshot corresponds to the app's `TEMPORARY_UPSTREAM_UNAVAILABLE` presentation, not the previous validator-final failure screen.
- The likely mobile-specific risk is heavier iPhone image payload behavior: the client could send a large original upload along with the generation-ready image, and the 1280px canvas could still produce a heavy PNG on mobile.
- The hotfix reduces request weight and makes mobile generation input more predictable without changing server credit/storage safety.

## Blockers
- No real mobile generation smoke has been run by Codex in this session.
- Vercel request logs were unavailable through CLI, so the root cause is inferred rather than proven from a live stack trace.
- GitHub push is still blocked locally by missing HTTPS credentials; branch is ahead of `origin/milestone4-auth-completion` by 3 commits (`d25e7b1`, `69751ed`, `883ca3c`).

## Next steps
- Test one real mobile Safari generation with a phone image/logo on production deployment `dpl_iP1YJvhGLkZmQcs9eh3vvzKBUtVh`.
- If the error remains, add temporary production-safe metadata logging around generation input sizes and original-inclusion decisions.
- Push local commits to GitHub after credentials are fixed.
