# Session 2026-04-30 - Upwork Radar n8n Workflow JSON

## Related
- [[../00 - Overview]]
- [[../03 - Pipelines/Pipeline A — Upwork Radar]]
- [[../03 - Acquisition Pipelines/Pipeline A — Upwork Radar]]
- [[../05 - CRM Structure/CRM Tables]]

## What was done
- Created importable n8n workflow JSON at `/Users/tamerlan/Desktop/flowopsteamPipelines/upwork-radar-workflow.json`.
- Workflow implements Gmail Upwork `New job alert` trigger -> URL extraction -> Google Sheets dedup -> Firecrawl scrape -> OpenAI scoring -> OpenAI proposal generation -> proposal validation -> Telegram send -> Google Sheets append.
- Added placeholders only: Gmail, Firecrawl, OpenAI HTTP Header Auth, Telegram, Google Sheets, Sheet ID, Telegram chat ID.

## Key findings
- The local workspace folder was empty before this workflow file was created.
- Existing memory already defined this as FlowOps Team Pipeline A - Upwork Radar, so no new project folder was created.
- Firecrawl community node is used as requested: `@mendable/n8n-nodes-firecrawl.firecrawl`.
- OpenAI is called through n8n HTTP Request nodes with an OpenAI header-auth credential placeholder for predictable import behavior.

## Blockers
- Workflow was JSON-validated locally, but not imported into a live n8n instance yet.
- User must configure credentials, `REPLACE_WITH_GOOGLE_SHEET_ID`, `REPLACE_WITH_TELEGRAM_CHAT_ID`, and create the `Upwork Radar` sheet columns.
- If n8n does not have the Firecrawl community node installed, replace it with HTTP Request `POST https://api.firecrawl.dev/v2/scrape`.

## Next steps
- Import `upwork-radar-workflow.json` into n8n.
- Set credentials and placeholders.
- Run manual test with a real Upwork Gmail alert.
- Confirm Google Sheets dedup and append behavior.
- Confirm proposal validation does not reject good drafts too aggressively.
