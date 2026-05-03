# Session 2026-05-03 — Pipeline C Workflow Template

## Related
- [[../00 - Overview]]
- [[../../../current-focus]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]
- [[../06 - Priorities/What to Do First]]
- [[../08 - Выполненные задачи/Completed]]
- [[../05 - CRM Structure/Airtable CRM Build Spec]]
- [[../03 - Acquisition Pipelines/Pipeline D — Demo Library]]

## What was done
- Read FlowOps project memory and confirmed Pipeline C belongs to existing FlowOps Team project work.
- Created local n8n workflow JSON: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-website-audit-generator-workflow.json`.
- Created local runbook: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-website-audit-generator-runbook.md`.
- Updated Pipeline C memory, priorities, completed-work note, and current focus.

## Key findings
- Historical note: the original Pipeline C v1 template was draft-only at this stage.
- Superseded by Pipeline C v2 on 2026-05-04: v2 is operationally completed, runs from Telegram command, and sends Gmail only after Telegram `Approve + Send`.
- The workflow follows existing FlowOps CRM patterns: Airtable `Leads`, `Audits`, `Messages`, `Automation Logs`, plus Telegram review queue.
- The workflow uses Airtable base `apppMcDUQaQwijvIV` and known table IDs from Pipeline B for `Leads`, `Messages`, and `Automation Logs`; `Audits` is referenced by table name.

## Blockers
- Not imported into n8n yet.
- Credentials still need reconnect: Firecrawl, OpenAI, Airtable, Telegram.
- Target website list still needs real companies; workflow seed intentionally filters out `example.com`.
- First QA batch and Loom recording still pending.

## Next steps
- Import `pipeline-c-website-audit-generator-workflow.json` into n8n.
- Replace the config seed list with 10-15 real websites in one niche.
- Reconnect credentials and set `TELEGRAM_CHAT_ID`.
- Run manual QA and verify Airtable + Telegram outputs.
- Record first 10 audit Looms and send messages manually.
