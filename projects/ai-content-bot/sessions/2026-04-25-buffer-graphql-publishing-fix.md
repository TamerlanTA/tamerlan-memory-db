# Session 2026-04-25 — Buffer GraphQL Publishing Fix

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- User reported WF-11 skipped Buffer because `IF: Buffer Configured` returned false, then sent a misleading approval message.
- Root cause: old REST Buffer API path required `profile_ids`, but the current token is a Buffer GraphQL API key, not a REST `api.bufferapp.com` token.
- Verified current Buffer token works against GraphQL `https://api.buffer.com`.
- Retrieved Buffer organization/channel IDs:
  - Organization: `69eb400172fa1a46db847fd7`
  - Threads: `69eb4061031bfa423c3a81bf`
  - LinkedIn: `69eb419a031bfa423c3a88d2`
  - Twitter/X: `69eb4550031bfa423c3a984e`
- Reworked WF-11:
  - `Validate Input` now emits one item per channel with the correct text and `channel_id`.
  - `Publish via Buffer` now uses Buffer GraphQL `createPost` mutation at `https://api.buffer.com`.
  - Added `Aggregate Buffer Results`.
  - Updates `Posts.status` to `published`, `partial_error`, or `error`.
  - Telegram message now reflects actual publish result, not “approved” fallback.
- `IF: Buffer Configured` and `Prepare Buffer Missing Result` are disconnected/orphaned from active path.
- Updated `create_sheets.gs` post status validation to include `partial_error`.

## Key findings
- Current Buffer key is valid for GraphQL but rejected by old REST API with `OIDC tokens are not accepted for direct API access`.
- Buffer GraphQL uses `channelId`, not REST `profile_ids`.
- GraphQL `createPost` creates one post per channel, so WF-11 fans out LinkedIn/Twitter/Threads then aggregates the result.

## Blockers
- Need to re-import WF-11 and test live publishing.
- If any channel rejects a post due text length/platform limits, workflow will mark `partial_error` or `error` and include failed service messages.

## Next steps
- Re-import WF-11.
- Approve a post and verify Buffer dashboard receives posts on LinkedIn, X/Twitter, and Threads.
- If live post should be queued instead of immediate, change GraphQL `mode: now` to `mode: addToQueue`.
