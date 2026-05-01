# Session 2026-05-01 — FlowOps Airtable CRM Prep

## Related
- [[00 - Overview]]
- [[What to Do First]]
- [[CRM Tables]]
- [[Airtable CRM Build Spec]]
- [[Full System Architecture]]

## What was done
- Read existing FlowOps memory for CRM, priorities, acquisition pipelines, sales process, and system architecture.
- Consolidated the two existing CRM table notes into one Airtable-ready implementation spec.
- Created `05 - CRM Structure/Airtable CRM Build Spec.md` with tables, fields, select options, links, views, seed demo records, automation rules, and first automation candidates.
- Linked the new Airtable spec from `05 - CRM Structure/CRM Tables.md`.

## Key findings
- Existing FlowOps plan already expects Airtable/Notion as CRM and project management layer.
- CRM needs more than the original four tables before automation: `Audits`, `Proposals`, `Clients`, `Retainers`, and `Automation Logs` are needed for clean n8n/Make workflows.
- First useful automations after Airtable setup should be Upwork Radar, CRM follow-up queue, Website Audit Generator, and proposal/retainer reminders.

## Blockers
- No direct Airtable base was created from this environment.
- Airtable API credentials/base ID are not available and should not be stored in memory.

## Next steps
- Create the `FlowOps CRM` base in Airtable using [[Airtable CRM Build Spec]].
- Add the initial five demo records.
- Add one test lead and manually walk it through lead -> message -> opportunity before automating.
- After Airtable structure is confirmed, build the first automation: Upwork Radar -> Leads -> proposal draft -> log.
