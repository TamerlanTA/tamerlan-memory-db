# Session 2026-05-12 — Pipeline C v3 Auto-Send Scale

## Related
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C — Website Audit Generator]]
- [[../00 - Overview|FlowOps Team — overview]]

## What was done
- Updated `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Prospecting.json`.
- Updated `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Audit Queue.json`.
- Prospecting now defaults to at least 100 review candidates per run and builds a larger search pool:
  - 40-80 randomized Firecrawl Search queries per run.
  - 8-10 results per query.
  - normalized candidate cap raised to 400.
  - scrape cap raised up to 180.
  - review candidate cap defaults to 100 and can be requested as 100/125/150/175/200.
- Audit Queue now auto-sends cold emails after Airtable Lead/Audit/Message creation when a recipient email and email body exist.
- Added native Gmail send node plus Airtable updates for Message, Lead, Audit, and Automation Logs.
- Missing recipient/body now logs a skipped auto-send instead of waiting for Telegram approval.

## Key findings
- v3 should no longer depend on Telegram approval cards for normal send flow.
- Telegram approval nodes remain in the Audit Queue JSON as disconnected legacy fallback nodes.
- Native Gmail credential must be selected after import because exported JSON contains a placeholder Gmail OAuth credential id.

## Blockers
- Gmail OAuth credential must be reconnected in `Gmail Auto Send Email` after importing into n8n.
- Large auto-send batches may hit Gmail/n8n/provider rate limits; monitor first production runs.

## Next steps
- Import both v3 JSON files into n8n.
- Reconnect Gmail OAuth on `Gmail Auto Send Email`.
- Run one controlled batch and verify Airtable `Messages`, `Leads`, `Audits`, and `Automation Logs` update correctly.
