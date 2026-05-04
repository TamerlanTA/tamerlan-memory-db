# Session 2026-05-04 — Pipeline B Dedupe Fix

## Related
- [[../00 - Overview]]
- [[../03 - Acquisition Pipelines/Pipeline B — LinkedIn Pain Radar]]
- [[../05 - CRM Structure/CRM Automation Plan]]
- [[../05 - CRM Structure/Airtable CRM Build Spec]]
- [[../08 - Выполненные задачи/Completed]]

## What was done
- Investigated why Pipeline B repeatedly returned the same 5 LinkedIn accounts and sent duplicate Telegram notifications.
- Found root cause in the local n8n workflow JSON: fixed search queries with `results_per_query: 5`, no persistent Airtable duplicate check between runs, and Telegram notification happening after every qualified result.
- Updated `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-b-linkedin-pain-radar-crm-workflow.json`.
- Added Airtable lookup before lead creation using `Contact URL`, `LinkedIn URL`, and `Unique key:` stored in `Notes`.
- Added `Only New Leads` gate and `Build Duplicate Skip Log` branch.
- Increased search depth to 20 results per query and up to 80 normalized candidates per run.
- Added `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-b-linkedin-pain-radar-dedupe-runbook.md`.
- Hotfixed n8n import/runtime issue: `Airtable Find Existing Lead` had invalid inline expression syntax in the URL field. Moved Airtable formula URL construction into `Prepare Airtable Records` as `airtable_find_url`; the HTTP node now uses `={{ $json.airtable_find_url }}`.

## Key findings
- The old workflow deduped only inside a single run via an in-memory `Set`; it forgot seen leads on the next run.
- The generated `unique_key` existed only in prepared data/notes and was not used to block duplicate creates.
- Better freshness requires searching more candidates and filtering out already-seen records before notification.

## Blockers
- The updated JSON still needs to be imported/replaced in the live n8n workflow.
- Live validation requires configured Firecrawl, OpenAI, Airtable, and Telegram credentials in n8n.
- If Firecrawl/search keeps returning the same source URLs, dedupe will stop spam but may produce fewer new Telegram alerts until search query rotation or a better prospecting source is added.
- If the live n8n workflow was already imported before this hotfix, re-import the JSON or manually update `Prepare Airtable Records` plus `Airtable Find Existing Lead` URL.

## Next steps
- Import updated Pipeline B JSON into n8n.
- Run manually twice: first run should create/notify new leads; second run should log repeated records as `Skipped` without Telegram spam.
- If duplicate Telegram messages still occur, check whether existing Airtable records have matching `Contact URL`, `LinkedIn URL`, or `Unique key:` in `Notes`.
- Later improvement: move duplicate lookup earlier before OpenAI DM drafting to save tokens, and add query/time-window rotation for fresher leads.
