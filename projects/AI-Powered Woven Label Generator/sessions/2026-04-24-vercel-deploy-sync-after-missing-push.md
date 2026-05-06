# Session 2026-04-24 — Vercel deploy sync after missing push

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Investigated why the user could not see the latest generation-stability commit in Vercel.
- Compared local git, `origin/milestone4-auth-completion`, and the active Vercel projects.
- Confirmed the real issue was not Vercel: local `HEAD` was `e12c8ba`, while `origin/milestone4-auth-completion` and the latest Vercel deployment were still on `1b00e96`.
- Pushed `milestone4-auth-completion` to GitHub.
- Rechecked Vercel and confirmed it detected commit `e12c8ba` (`Stabilize woven background field prompts`) and created a new queued deployment on `griffes-vivienne-studio-3vop`.

## Key findings
- The missing deployment was caused by a missed push, not by a broken Vercel integration.
- The likely active production-facing project is `griffes-vivienne-studio-3vop`; `griffes-vivienne-studio` continues to receive preview-style deployments.
- After the push, Vercel immediately registered the new SHA, so the repo-to-Vercel webhook path appears healthy.

## Blockers
- Deployment was still `QUEUED` at the time of verification, so live runtime validation of `e12c8ba` still depends on that build finishing successfully.

## Next steps
- Verify the queued Vercel deployment for `e12c8ba` reaches `READY`.
- Once ready, run the planned manual QA for background weave stability on the live deployment.
