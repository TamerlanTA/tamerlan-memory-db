# Pipeline A — Upwork Radar

## Related
- [[00 - Overview]]
- [[n8n]]

## Current status
- Workflow file lives at `/Users/tamerlan/Desktop/flowopsteamPipelines/upwork-radar-workflow.json`.
- On 2026-04-30, import trouble was investigated: original JSON is syntactically valid and has 14 nodes / 13 connections, but includes instance-specific workflow metadata and credential IDs.
- Created clean import variant: `/Users/tamerlan/Desktop/flowopsteamPipelines/upwork-radar-workflow.clean-import.json`.

## Key findings
- Original export references credentials from the existing n8n instance: Gmail, Google Sheets, Firecrawl, OpenAI, Telegram.
- Workflow depends on community/custom node `@mendable/n8n-nodes-firecrawl.firecrawl`; target n8n must have this package installed or import/execution may fail.
- Trigger is Gmail Trigger and workflow is inactive by default, so importing alone will not run anything.

## Next steps
- Import `upwork-radar-workflow.clean-import.json`.
- Reconnect credentials in n8n for Gmail, Google Sheets, Firecrawl, OpenAI, and Telegram.
- Ensure Firecrawl community node package is installed or replace it with built-in HTTP Request.
- Activate the workflow and test with a matching Gmail alert email.
