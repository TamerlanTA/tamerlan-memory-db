# Session 2026-07-02 — Telegram Duplicate Response Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated why `/candidate_batch` and `/application_handoff` replies were sent about four times.
- Checked Railway `bot-api` logs and found multiple Telegram webhook requests returning `500 Request timed out after 10000 ms`.
- Added in-memory Telegram `update_id` dedupe in `bot-api` so retries of the same update are ignored.
- Increased grammY webhook timeout from 10 seconds to 30 seconds.
- Deployed `bot-api` to Railway with the temporary token.

## Key findings
- Repeated messages were not caused by matching creating multiple batches; they were caused by Telegram retrying the same update after webhook timeout.
- Handoff returned `duplicate_application: 8` because application rows already existed from the first successful handoff; repeated retries hit duplicate prevention.

## Validation
- `pnpm --filter @amigo/bot-api check`
- `pnpm --filter @amigo/bot-api test`
- `pnpm --filter @amigo/bot-api build`
- Railway `bot-api` online after deploy.
- `/health` returns `status=ok` and `database=ok`.
- Telegram webhook pending updates are 0.

## Next steps
- Re-test `/candidate_batch` and `/application_handoff` from Telegram.
- Rotate the temporary Railway token shared in chat.
