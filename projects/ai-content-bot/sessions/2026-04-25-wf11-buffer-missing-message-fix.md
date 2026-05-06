# Session 2026-04-25 — WF11 Buffer Missing Message Fix

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- User reported WF-11 correctly had `buffer_ready=false`, but Telegram still sent `Publishing failed`.
- Root cause: `Prepare Buffer Missing Result` set `pending_buffer=true`, but Google Sheets `Update Post Status` output dropped transient fields before `Build Result Msg`.
- Updated WF-11 `Build Result Msg`:
  - treats `pending_buffer=true`, `status=approved`, or `buffer_ready=false` as the approved-but-waiting-for-Buffer path.
  - sends “Post approved / Buffer is not configured yet” instead of publishing failure.

## Key findings
- After Google Sheets update nodes, do not rely on transient fields unless they are mapped into the sheet/output. Build messages should also infer state from durable fields like `status`.

## Next steps
- Re-import WF-11.
- Approve another post without Buffer profile IDs. Expected Telegram message: `Post approved`, not `Publishing failed`.
