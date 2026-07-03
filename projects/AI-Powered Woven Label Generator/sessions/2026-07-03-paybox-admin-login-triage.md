# Session 2026-07-03 — Paybox Admin Login Triage

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated Benjamin's report that `paybox@griffesvivienne.com` can no longer access admin.
- Reviewed auth/admin code paths: Clerk resolves user, local DB user is looked up by `openId`, then by email for first sign-in, and `adminProcedure` checks `user.role === "admin"`.
- Checked production DB row for `paybox@griffesvivienne.com`.

## Key findings
- `paybox@griffesvivienne.com` still exists in production DB with `role = admin`; it was not removed or demoted.
- The row's `lastSignedIn` had not updated today, implying the issue happens before backend admin authorization.
- Most likely cause is Clerk production instance/session transition: after live Clerk keys were added, Benjamin may need to sign in/create the production Clerk account for the same email, or Clerk may be blocking that login method.

## Blockers
- Exact user-facing Clerk error is unknown.
- Need the screenshot/error message from Benjamin or access to Clerk production user list to confirm whether `paybox@griffesvivienne.com` exists in the production Clerk instance.

## Next steps
- Ask Benjamin for the exact error screen/message.
- If he can sign in/sign up with the same email, the backend should relink by email and preserve admin role.
- If Clerk creates a different user but relink does not happen, manually link the new Clerk `user_...` id to the existing `paybox@griffesvivienne.com` DB user row.
