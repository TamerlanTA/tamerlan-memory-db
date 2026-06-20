# TG Finance Agent — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Content
Immediate next steps:
- Use `/forgetme` in Telegram to clear the prior test state, then re-upload `/Users/tamerlan/Downloads/gold_statement.pdf` and confirm the new report says card inflow is about `965,676.66 KZT` and balance grew by about `53,702.91 KZT`.
- Use `/learn`, `/storage`, and `/history` in Telegram to verify the bot explains learning/storage and shows historical stats clearly.
- Confirm expanded review buttons in Telegram: e.g. classify `Перевод Mahmajabor H.` as `Продукты`, `OBSIDIAN` as `Подписки`, and verify the bot saves rules and re-runs categorization.
- Add/confirm rule `PAYPAL это доход` if PayPal/Upwork inflows should count as real freelance/business income.
- Inspect the bot's review questions and answer enough rules to reduce the remaining real-PDF review items.
- Refine parser rules against real Kaspi extracted text, especially multiline rows and statement summary labels.
- Keep validating parser totals against real PDF summary lines whenever a new Kaspi layout appears.
- If Railway bot flow works, treat n8n as optional and keep internal reminders enabled.
- n8n is optional for now; prefer internal reminder scheduler unless Tamerlan explicitly returns to n8n.
- Decide whether to expose reminder webhook handlers via Express/Fastify or keep n8n on Execute Command for local MVP.
- Consider moving storage from Railway volume/local JSON to Supabase after MVP validation.
- Test the learning loop with an unknown person transfer using `npm run add-rule`, then re-run categorization.
- Test natural-language Telegram rules like `Ivan S. это долг`, `PAYPAL это бизнес доход`, `Mahmajabor H. это продукты`, and `С карты другого банка это внутренний перевод`.
- Decide first storage backend: JSON for prototype, SQLite for local persistence, or Postgres/Supabase for production.
- Add automated tests for income safety rules: internal transfers are not real income, PAYPAL/UPWORK are business income with confirmation, unknown people transfers are Needs Review.
- Add automated tests for monthly summary calculations and report renderers.
- Add automated tests before the next major refactor/deployment cycle.
