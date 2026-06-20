# Session 2026-06-17 — n8n Monthly Reminders

## Related
- [[../overview|overview]]
- [[../current-state|current-state]]
- [[../next-steps|next-steps]]
- [[../decisions|decisions]]
- [[../risks|risks]]

## What was done
- Added reminder state model and logic under `/Users/tamerlan/Desktop/tg-finance-agent/src/reminders/`.
- Added persistent local JSON reminder storage under `data/reminders/`.
- Added CLI command: `npm run reminder:check`.
- Added webhook payload contracts and reusable `ReminderWebhookHandlers` for future HTTP endpoints.
- Integrated Telegram bot PDF success path with reminder completion: statement received + report generated stop reminders.
- Added docs at `/Users/tamerlan/Desktop/tg-finance-agent/docs/n8n-workflow.md`.
- Added sample n8n workflow JSON at `/Users/tamerlan/Desktop/tg-finance-agent/n8n/monthly-reminder-workflow.json`.
- Added `REMINDER_DAY_OF_MONTH` to `.env.example`.

## Key findings
- `npm run typecheck` passes.
- `npm run reminder:check -- --chatId 999002 --now 2026-07-03T04:00:00.000Z --day 3` correctly creates June reminder state and returns a Russian reminder message.
- Repeated checks before `nextReminderAt` correctly return `shouldSend=false`.

## Decisions made
- Keep app-side reminder state as source of truth; n8n is only the scheduler/message orchestrator.
- Use Execute Command in the sample n8n workflow for local MVP, while documenting future webhook contracts.

## Blockers
- n8n workflow has not been imported/tested with live Telegram credentials.
- No actual HTTP server mounts webhook handlers yet.

## Next steps
- Import sample workflow into n8n and configure Telegram credentials.
- Live-test monthly reminder delivery to the user's Telegram chat.
- Decide whether reminders should stay local JSON or move to Supabase/SQLite before deployment.

