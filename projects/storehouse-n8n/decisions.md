# Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

## Content
## 2026-04-27 — Create full project memory skeleton

Decision: create a canonical project folder for Storehouse n8n instead of a single-file project note.

Reason:
- The user explicitly asked to create a project skeleton in memory for this project.
- The project appears intended to continue across future sessions.
- n8n/automation work benefits from tracking current state, decisions, risks, next steps, prompts, and session handoffs separately.

## 2026-04-27 — Generate 6 workflow exports for 5 modules

Decision: generate 6 n8n workflow JSON files because Module 3 explicitly contains two schedule-based sub-workflows: Low Stock Alert and Suspicious Activity Alert.

Decision: use HTTP Request nodes for StoreHouse mock calls and place sticky notes next to each mock with the replacement instruction:

`REPLACE WITH REAL SH API: POST /api/sh5exec, procName: [name]`

Decision: use n8n variables/placeholders for sensitive values (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `GOOGLE_SHEETS_ID`, `ANTHROPIC_API_KEY`, `SH_USER`, `SH_PASSWORD`) and avoid hardcoded secrets.

## 2026-04-27 — Rebuild into AI Agent architecture

Decision: replace the prior 6-workflow Claude/HTTP architecture with 3 workflow exports:

- Main AI Agent + photo recognition
- Low Stock Alert scheduled workflow
- Suspicious Activity Alert scheduled workflow

Decision: use official n8n nodes for Telegram, OpenAI/GPT-4o, AI Agent, and Google Sheets. HTTP Request is reserved only for StoreHouse mock calls.

Decision: avoid Code nodes entirely in generated workflows. Use Set/If node expressions for parsing, comparisons, and message formatting.

Decision: represent the agent's 5 capabilities as connected `ai_tool` nodes. StoreHouse-backed tools use `MOCK — SH API` HTTP Request nodes so they satisfy the mock-node naming and sticky-note requirements.

## 2026-04-29 — Replace StoreHouse mocks with WebAPI calls

Decision: replace all StoreHouse mock nodes with real HTTP Request nodes calling:

`http://{{SH_HOST}}:{{SH_PORT}}/api/sh5exec`

In n8n JSON this is expressed through `$vars.SH_HOST`, `$vars.SH_PORT`, `$vars.SH_USER`, `$vars.SH_PASSWORD`, and procedure placeholders:

- `$vars.SH_PROC_STOCK_BALANCES`
- `$vars.SH_PROC_INCOMING_INVOICE`
- `$vars.SH_PROC_STOCK_MOVEMENT`
- `$vars.SH_PROC_EXPENSE_REPORT`
- `$vars.SH_PROC_DOCUMENT_LOG`

Decision: remove all `MOCK —` node names and old mock sticky notes. Add on-site configuration sticky notes instead.

Decision: keep Google Sheets for `automation_log` and `min_thresholds`, because these are system-owned data, not StoreHouse data. Replace previous StoreHouse-data sheet reads (`mock_stock`, `mock_documents`) with WebAPI calls.
