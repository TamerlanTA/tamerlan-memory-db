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
- Hotfixed `Normalize Search Results` after live n8n step showed Firecrawl returning `item.json.data.web` results but the node returning no candidates. The normalizer now prioritizes `item.json.data.web`, supports `data.results`, `data.links`, array `data`, object/string URL inputs, logs per-input counts, and returns `status: error_no_candidates` instead of throwing. Prospecting now has a branch to log that skip to Airtable.
- Second normalization fix after Airtable logs showed `web_results_found: 4` for each query but 0 usable candidates. Normalizer now records sample URLs and rejection reasons, uses hard-block only for social/Google domains, and keeps soft-blocked directory domains as fallback only when no direct business domains are found.
- Third normalization fix after Airtable debug showed every valid URL returning `invalid_url`. Root cause was n8n escaping around regex protocol detection causing valid `https://...` values to be treated as invalid/prefixed incorrectly. `normalizeUrl` now uses `startsWith('https://') || startsWith('http://')` and avoids regex protocol detection.
- Fourth normalization fix after repeated live failure: removed `new URL()` from `Normalize Search Results` entirely and replaced it with manual host parsing. This makes the normalizer robust against n8n runtime/parser oddities and accepts valid Firecrawl `item.json.data.web[].url` strings like `https://soflochiro.com/`.
- Expanded soft directory blocking to include `clutch`, `upcity`, `designrush`, `goodfirms`, `sortlist`, `themanifest`, `g2`, `capterra`, `softwareadvice`, `expertise`, and `threebestrated`; these only pass as fallback if no direct business domains are found.
- Audited all generated workflows after the fix: 24 Code nodes compile with 0 syntax errors; all workflow graph edges resolve; `Normalize Search Results` smoke test against the failing Firecrawl payload returns real `candidate_found` domains; WF-06 `audit_approve_rec...` routing, Approval Handler callback parsing, and Gmail MIME body generation pass local smoke tests.
- Fixed live Telegram `Approve + Send` failure where Gmail OAuth credentials rejected use from an HTTP Request node (`This credential is configured to prevent use within an HTTP Request node`). Approval Handler now uses native `n8n-nodes-base.gmail` message send node with `sendTo`, `subject`, `emailType: text`, `message`, and `appendAttribution: false`.
- Converted Pipeline C v2 Prospecting from schedule-driven to Telegram-command-driven. Prospecting no longer has `Daily Schedule Trigger`; it now has `When Called by Telegram Command` (`executeWorkflowTrigger`) plus Manual Trigger for n8n testing.
- Updated WF-06 patch to route `/pipeline_c`, `/audit_sites`, `запусти pipeline c`, and `найди сайты для аудита` to `pipeline_c_prospecting`, send a Telegram start confirmation, then call Pipeline C v2 Prospecting via `REPLACE_WITH_PIPELINE_C_V2_PROSPECTING_WORKFLOW_ID`.
- User confirmed Pipeline C is now working well end-to-end. As of 2026-05-04, mark Pipeline C v2 as completed operationally, not merely prepared.

## Key findings
- The best v2 architecture is split into Prospecting, Audit Queue, and Approval Handler workflows.
- Prospecting uses Firecrawl Search across multiple niche packs and caps review candidates at 10/run.
- Local sample validation confirmed `soflochiro.com`, `miami-chiropractors.com`, and `miamispineclinic.com` pass normalization from the same `data.web` shape shown in n8n.
- Local fallback validation confirmed normal business domains are preferred, while Yelp/BBB only pass as `soft_blocked_source: true` if no better candidates exist.
- Local validation with the exact failing domains (`soflochiro.com`, `miami-chiropractors.com`, `miamispineclinic.com`, `chiropractic-clinics.com`, `charlottesinc.com`) now returns all as usable candidates.
- Current generated Prospecting JSON no longer contains `new URL()` inside `Normalize Search Results`; if n8n still shows `invalid_url`, the imported workflow is stale and must be re-imported or the node code replaced from the regenerated JSON.
- Audit Queue creates Airtable `Leads`, `Audits`, `Messages`, `Automation Logs`, then sends Telegram approval cards.
- Approval Handler is callable via WF-06 and sends Gmail only after `Approve + Send`.
- Approval Handler must be re-imported or patched in n8n after the Gmail-node fix; old imports still have the invalid Gmail HTTP Request node.
- WF-06 must remain the only active Telegram Trigger. The patched WF-06 export is intentionally `active=false` to avoid duplicate webhook registration on import.
- Telegram menu commands to expose through BotFather: `/pipeline_c` and `/audit_sites`.
- Completion status: Pipeline C v2 is done. Future work is campaign operation, QA, copy/filter iteration, and reply-rate optimization.

## Blockers
- No active build blockers for Pipeline C v2 after live confirmation.
- Residual operational risks: monitor duplicate behavior, deliverability, Gmail/API failures, Firecrawl result quality, and Airtable field drift.

## Next steps
- Run Pipeline C from Telegram using `/pipeline_c` or `/audit_sites`.
- Review Telegram cards, approve good candidates, reject/edit/Need Loom as appropriate.
- Track replies and delivery quality; iterate niche rotation, city/query list, fit scoring, and teaser copy.
- Use Loom selectively for high-fit prospects or `Need Loom`, not as a required step for every email.
