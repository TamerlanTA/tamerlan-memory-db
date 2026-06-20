# TG Finance Agent — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

## Content
## 2026-06-17 — Project Memory Location
Decision: Track this workstream as a full project folder at `projects/tg-finance-agent/`.

Why: Tamerlan explicitly requested a new project memory skeleton and said all memory for the upcoming work should be recorded there.

## 2026-06-17 — Initial Scope
Decision: Start with core domain model, modular TypeScript structure, documentation, and sample categorization rules only.

Why: Tamerlan explicitly requested not to build the Telegram bot or n8n workflows yet. The first useful foundation is a reliable domain model for Kaspi statement parsing, conservative income classification, and a future user review loop.

## 2026-06-17 — Parser Boundary
Decision: Implement Kaspi parsing as a raw extraction layer with `KaspiStatementTransaction`, separate from the categorized domain `Transaction`.

Why: The parser should extract facts from PDF statements without deciding whether an inflow is real income, internal transfer, refund, or debt return. Categorization belongs to the next layer.

## 2026-06-17 — Conservative Categorization
Decision: If an incoming transaction is not confidently matched by a trusted rule, categorize it as `Needs Review` with `isRealIncome: false`.

Why: Kaspi incoming transfers include internal transfers, debt returns, refunds, family/friend movements, and freelance income. Counting all inflows as real income would make monthly reports misleading.

## 2026-06-17 — Learning Rules Storage
Decision: Store learned user answers as JSON rules in the existing rule files, starting with `people_rules.json` for `add-rule` defaults.

Why: JSON rules keep the prototype auditable and easy to inspect before choosing a database backend.

Update: On Railway, learned rules must be written to runtime `BOT_DATA_DIR=/data`, not the app repository folder. The categorizer now merges repository base rules with runtime learned rules so user learning persists across deploys and restarts.

## 2026-06-17 — Report Output Formats
Decision: Generate monthly reports in JSON, Markdown, Telegram text, HTML, and PNG chart outputs.

Why: JSON supports downstream automation, Markdown/HTML support review and sharing, Telegram text supports the bot UX, and PNG charts can later be sent directly in Telegram.

## 2026-06-17 — Telegram Storage Mode
Decision: Implement the first Telegram bot version with local JSON storage and an abstract `BotStorage` interface.

Why: Local JSON is enough for single-user prototyping and keeps all learned rules/report artifacts inspectable. The interface leaves room for Supabase or Google Sheets later.

## 2026-06-17 — Reminder Orchestration
Decision: Implement reminder state and logic inside the app, with n8n acting as the scheduler/orchestrator.

Why: The finance app should remain the source of truth for whether a statement was received or a report was generated. n8n only needs to call `reminder:check` or future webhook endpoints and send Telegram messages when instructed.

## 2026-06-17 — User-Facing Month Result
Decision: In Telegram/AI responses, use statement opening and closing balances as the primary "month result" when available.

Why: Users interpret month outcome as whether the account balance grew or shrank. The deterministic `realIncome - realExpenses` calculation remains useful for analytics, but can be misleading before all income/expense rules are trained.
