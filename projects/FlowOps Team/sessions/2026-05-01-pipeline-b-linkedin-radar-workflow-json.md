# Session 2026-05-01 — Pipeline B LinkedIn Radar Workflow JSON

## Related
- [[../00 - Overview]]
- [[../03 - Acquisition Pipelines/Pipeline B — LinkedIn Pain Radar]]
- [[../05 - CRM Structure/Airtable CRM Build Spec]]
- [[../07 - System Map/Full System Architecture]]

## What was done
- Created importable n8n workflow JSON at `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-b-linkedin-pain-radar-crm-workflow.json`.
- Workflow implements Pipeline B draft automation: scheduled/manual trigger -> Firecrawl `/v2/search` LinkedIn pain-signal queries -> normalize candidates -> OpenAI qualification -> score gate -> OpenAI LinkedIn DM draft -> Airtable CRM records -> Telegram review notification -> automation log.
- Used placeholders/env vars only: `FIRECRAWL_API_KEY`, `AIRTABLE_API_TOKEN`, `AIRTABLE_BASE_ID`, `TELEGRAM_CHAT_ID`, and placeholder OpenAI/Telegram credential IDs.

## Key findings
- FlowOps memory already defines Pipeline B as LinkedIn Pain Radar and Airtable as the CRM target, so this belongs to the existing FlowOps Team project.
- Firecrawl v2 search supports search plus optional markdown scraping, which fits the first working version without adding a separate LinkedIn-specific scraper provider.
- The workflow intentionally queues drafts for manual LinkedIn sending instead of auto-sending DMs.

## Blockers
- Not imported into a live n8n instance yet.
- Airtable base and field names must match `Airtable CRM Build Spec` before live run.
- n8n credentials/env vars need to be configured before activation.

## Next steps
- Import the JSON into n8n.
- Configure Firecrawl, OpenAI, Airtable, and Telegram credentials/placeholders.
- Run manually with low query limits and verify Airtable writes to `Leads`, `Messages`, and `Automation Logs`.
- If LinkedIn SERP quality is weak, swap the Firecrawl search node for a dedicated compliant LinkedIn/prospecting data provider while keeping downstream CRM nodes.
