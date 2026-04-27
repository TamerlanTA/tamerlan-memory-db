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
