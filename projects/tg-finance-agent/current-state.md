# TG Finance Agent — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Content
Status: Railway-deployed Telegram MVP with improved real-PDF parsing, AI report UX, and review learning UX on 2026-06-17.

Known state:
- Project memory folder exists at `projects/tg-finance-agent/`.
- Local workspace exists at `/Users/tamerlan/Desktop/tg-finance-agent`.
- Initial Node.js + TypeScript project files were created.
- Core domain types were added for transactions, statement periods, balances, category/person/merchant rules, summaries, and uncategorized review items.
- Category taxonomy covers income, transfers, refunds/debt returns, business categories, core expense groups, and review buckets.
- Documentation exists for architecture and category system.
- Starter JSON rule files exist in `data/`.
- `npm run typecheck` passes.
- Kaspi PDF parser exists under `src/statements/kaspi/`.
- CLI exists: `npm run parse -- ./path/to/kaspi_statement.pdf`.
- Synthetic parser smoke script exists: `npm run parse:sample`.
- Latest synthetic sample output is saved at `/Users/tamerlan/Desktop/tg-finance-agent/data/sample_outputs/parsed_statement.json`.
- Categorization engine exists under `src/categorization/`.
- Rule files exist: `data/merchant_rules.json`, `data/people_rules.json`, `data/category_rules.json`, `data/income_rules.json`.
- CLI exists: `npm run categorize -- ./data/sample_outputs/parsed_statement.json`.
- CLI exists: `npm run review -- ./data/sample_outputs/categorized_statement.json`.
- CLI exists: `npm run add-rule -- --match "Ivan S." --category "Debt" --financeArea "personal" --incomeType "not_income"`.
- Latest categorized sample output is saved at `/Users/tamerlan/Desktop/tg-finance-agent/data/sample_outputs/categorized_statement.json`.
- Latest review queue sample output is saved at `/Users/tamerlan/Desktop/tg-finance-agent/data/sample_outputs/review_queue.json`.
- Monthly reporting layer exists under `src/reports/`.
- CLI exists: `npm run report -- ./data/sample_outputs/categorized_statement.json`.
- Report outputs exist: `monthly_summary.json`, `monthly_report.md`, `telegram_report.txt`, `monthly_report.html`, and PNG charts under `data/sample_outputs/charts/`.
- Telegram bot layer exists under `src/bot/`.
- CLI exists: `npm run bot`.
- `.env.example` exists with `TELEGRAM_BOT_TOKEN`, optional `OPENAI_API_KEY`, and `STORAGE_MODE=local`.
- Local JSON bot storage exists under `src/storage/local-json-storage.ts`.
- Bot docs exist at `/Users/tamerlan/Desktop/tg-finance-agent/docs/telegram-bot.md`.
- Reminder module exists under `src/reminders/`.
- CLI exists: `npm run reminder:check`.
- Reminder docs exist at `/Users/tamerlan/Desktop/tg-finance-agent/docs/n8n-workflow.md`.
- Sample n8n workflow exists at `/Users/tamerlan/Desktop/tg-finance-agent/n8n/monthly-reminder-workflow.json`.
- Reminder state persists in local JSON under `data/reminders/`.
- Git repository initialized and pushed to private GitHub repo `TamerlanTA/tg-finance-agent`.
- Railway project `tg-finance-agent` exists in workspace `tamerlanta's Projects`.
- Railway service `bot` is deployed and running from deployment `8045b000-03d8-4380-99dc-bce1c328ef6d`.
- Latest Railway deployment after review-learning UX fixes is `2cb1e8ed-abb6-4e1f-946e-9057118b080e` and logs show `Finance Telegram bot is running.`
- Railway volume `bot-volume` is mounted at `/data`.
- Telegram bot token was set in Railway variables; do not store it in memory or repo.
- Telegram API `getMe` verified bot username `@tgFinanceAgentbot`.
- Real Kaspi PDF `/Users/tamerlan/Downloads/gold_statement.pdf` was retested locally after parser fixes: parser extracts period 2026-05-17..2026-06-17, 136 transactions, total card inflow `965,676.66 KZT`, expenses `911,973.75 KZT`, opening balance `14,825.92 KZT`, closing balance `68,528.83 KZT`, balance movement `+53,702.91 KZT`.
- n8n has been made optional for MVP; bot now has internal monthly reminder scheduler.
- AI finance analysis and Q&A code exists under `src/ai/`; it is enabled only when `OPENAI_API_KEY` is set.
- Railway has `OPENAI_API_KEY` and `OPENAI_MODEL=gpt-4.1-mini`; OpenAI smoke test via `railway run` returned `OK`.
- Bot now supports `/ask`, `/questions`, `/learn`, `/storage`, `/history`, `/forgetme`, AI report generation after PDF upload, chart sending after reports, and expanded review category buttons.
- Parser no longer treats `Доступно на ...` balance lines as transactions.
- AI report prompt now favors a user-friendly Telegram-style report, separates card inflow from real income, highlights probable PayPal/Upwork income, uses balance movement as the user-facing month result when balances exist, and hides internal labels like `Needs Review`.
- Learned rules now persist under runtime `BOT_DATA_DIR` (`/data` on Railway), and categorization merges repository base rules with runtime learned rules.
- `/forgetme` deletes current chat run data/goals/reminders and resets runtime learned rules back to repository base rules.
- Review questions are now Russian, show a batch of up to 8, remove Custom, and offer broader category buttons such as groceries, cafes, transport, parking, fuel, subscriptions, education, health/sport, family, friends, debt, business income/expense, internal transfer, not income, and other.
- After answering a review category, the bot saves the rule and re-runs categorization without re-sending the entire review batch.
- Persistent database storage is intentionally not implemented yet; AI model calls are now wired and smoke-tested.
- n8n workflow JSON is generated but has not been imported/tested in n8n with real credentials.
- Telegram bot has been used by Tamerlan, but the newly deployed parser/AI/storage fixes still need one live Telegram PDF re-upload validation.
- Parser has been tested on one real PDF but still needs quality review of extracted rows/categories.

## Latest Session
- [[sessions/2026-06-17-n8n-monthly-reminders]]
- [[sessions/2026-06-17-telegram-bot-interface]]
- [[sessions/2026-06-17-monthly-reporting-system]]
- [[sessions/2026-06-17-categorization-learning-system]]
- [[sessions/2026-06-17-kaspi-pdf-parser]]
- [[sessions/2026-06-17-initial-typescript-domain-skeleton]]
- [[sessions/2026-06-17-project-memory-initialization]]
