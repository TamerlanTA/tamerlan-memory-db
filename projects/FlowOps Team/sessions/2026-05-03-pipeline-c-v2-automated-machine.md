# Session 2026-05-03 — Pipeline C v2 Automated Machine

## Related
- [[../00 - Overview]]
- [[../../../current-focus]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]
- [[../06 - Priorities/What to Do First]]
- [[../08 - Выполненные задачи/Completed]]
- [[../05 - CRM Structure/Airtable CRM Build Spec]]

## What was done
- Implemented Pipeline C v2 as local import-ready n8n workflow templates.
- Created generator/source file: `/Users/tamerlan/Desktop/flowopsteamPipelines/build-pipeline-c-v2-workflows.js`.
- Generated:
  - `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-prospecting-workflow.json`
  - `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-audit-queue-workflow.json`
  - `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-approval-handler-workflow.json`
  - `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-wf06-router-patch.json`
  - `/Users/tamerlan/Desktop/flowopsteamPipelines/WF-06 AI Command Center - Pipeline C v2 Router Patch.json`
  - `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-runbook.md`
- Validated all generated JSON files parse correctly and all Code node JavaScript compiles.

## Key findings
- The best v2 architecture is split into Prospecting, Audit Queue, and Approval Handler workflows.
- Prospecting uses Firecrawl Search across multiple niche packs and caps review candidates at 10/day.
- Audit Queue creates Airtable `Leads`, `Audits`, `Messages`, `Automation Logs`, then sends Telegram approval cards.
- Approval Handler is callable via WF-06 and sends Gmail only after `Approve + Send`.
- WF-06 must remain the only active Telegram Trigger. The patched WF-06 export is intentionally `active=false` to avoid duplicate webhook registration on import.

## Blockers
- Workflows are not imported into n8n yet.
- Placeholder credentials/workflow IDs must be replaced after import.
- Gmail OAuth send path must be live-tested in n8n.
- WF-06 router patch must be applied carefully to the active command-center workflow.

## Next steps
- Import Audit Queue, Approval Handler, then Prospecting.
- Replace `REPLACE_WITH_PIPELINE_C_V2_AUDIT_QUEUE_WORKFLOW_ID`.
- Patch WF-06 with `audit_*` routing and replace `REPLACE_WITH_PIPELINE_C_V2_APPROVAL_HANDLER_WORKFLOW_ID`.
- Reconnect Firecrawl, OpenAI, Airtable, Telegram, and Gmail credentials.
- Run one manual 10-candidate QA batch and test all Telegram buttons before activating the daily schedule.
