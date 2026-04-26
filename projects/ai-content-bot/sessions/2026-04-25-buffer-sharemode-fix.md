# Session 2026-04-25 — Buffer ShareMode Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- User reported Buffer GraphQL error: `Value "now" does not exist in "ShareMode" enum`.
- Introspected Buffer GraphQL schema for `ShareMode`.
- Valid enum values:
  - `addToQueue`
  - `shareNow`
  - `shareNext`
  - `customScheduled`
  - `recommendedTime`
- Updated WF-11 `Publish via Buffer` GraphQL mutation from `mode: now` to `mode: shareNow`.

## Key findings
- Buffer docs mention “Post now” conceptually, but the actual enum is `shareNow`.

## Next steps
- Re-import WF-11.
- Approve a post again; `Publish via Buffer` should pass GraphQL validation.
