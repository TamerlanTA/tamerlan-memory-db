# Session 2026-07-03 — Clerk Sign-Up Route Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated owner report that clicking `Create an account` on `/sign-in` only reloaded the page.
- Found root cause: `ClerkProvider` had `signUpUrl="/sign-in"`, so Clerk's prebuilt sign-up link pointed back to the sign-in route.
- Added a dedicated `/sign-up` route/page using Clerk `<SignUp />`.
- Updated `signUpUrl` to `/sign-up` and added EN/FR page copy.
- Pushed commit `a99ee08` and deployed to Vercel Production.

## Key findings
- This was a routing configuration bug, not a Clerk account/database issue.
- Production deployment `dpl_7DDa4Hs6u9iAFJoAhGAh6P3ZCqxn` is READY and aliased to `https://methode.griffesvivienne.com`.

## Blockers
- None for this route fix.

## Next steps
- Browser-test `Create an account` from `/sign-in`; it should navigate to `/sign-up` and show the Clerk registration form.
- If the sign-up form itself rejects new accounts, check Clerk Dashboard production user/authentication settings.
