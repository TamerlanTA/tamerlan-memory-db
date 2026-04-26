# Session 2026-04-25 — WF11 Env Access Denied Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- User reported WF-11 `Validate Input` fails in n8n Cloud with `access to env vars denied`.
- Removed all `$env` references from WF-11 JSON, including comments.
- WF-11 now reads Buffer profile IDs only from:
  - input `profile_ids`
  - input `buffer_profile_ids`
  - local constant `HARDCODED_BUFFER_PROFILE_IDS` inside `Validate Input`
- If no profile IDs are available, WF-11 follows the existing non-publish path and marks the post `approved` instead of crashing.

## Key findings
- n8n Cloud can throw even when checking `typeof $env`; do not reference `$env` at all in Code nodes.

## Next steps
- Re-import WF-11.
- Approve a post again; without profile IDs, expected result is `Posts.status=approved` and Telegram message explaining Buffer setup is pending.
- Later, add Buffer profile IDs either by passing them into WF-11 or hardcoding them in `HARDCODED_BUFFER_PROFILE_IDS`.
