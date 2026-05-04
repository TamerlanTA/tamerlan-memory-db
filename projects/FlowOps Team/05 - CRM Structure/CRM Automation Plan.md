# CRM Automation Plan

#flowops #crm #automation #n8n #airtable

## Related
- [[Airtable CRM Build Spec]]
- [[CRM Tables]]
- [[Pipeline A — Upwork Radar]]
- [[Pipeline B — LinkedIn Pain Radar]]
- [[Pipeline C — Website Audit Generator]]
- [[Pipeline D — Demo Library]]
- [[Pipeline E — Retainer Conversion]]
- [[Sales Steps]]
- [[Message Templates]]

## Goal

Build automations around `FlowOps CRM` after the Airtable base exists, using Airtable as the source of truth and n8n/Make as the execution layer.

## Current status

**Status as of 2026-05-03:** CRM system is created, and Pipeline B is complete.

- The previous blocker "confirm/create Airtable base" is resolved from project-memory perspective.
- Next automation work should assume the CRM exists and start with validation, QA, and production-safe wiring.
- Pipeline B should be treated as completed and ready for operational review/refinement.

**Pipeline B dedupe update as of 2026-05-04:**
- Updated local workflow JSON at `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-b-linkedin-pain-radar-crm-workflow.json`.
- Pipeline B now checks Airtable before creating a lead or sending Telegram.
- Duplicate LinkedIn leads are logged as `Skipped` in `Automation Logs` and should not create new CRM records or Telegram notifications.
- Search depth increased from 5 to 20 results per query and up to 80 normalized candidates per run.
- Runbook: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-b-linkedin-pain-radar-dedupe-runbook.md`.

## Build order

### 1. CRM core setup validation
- Validate that required Airtable tables, fields, select values, links, and views exist in the created CRM.
- Create initial demo records.
- Write a test `Automation Logs` record.
- Required before enabling/expanding production automation.

### 2. Upwork Radar to CRM
- Trigger: scheduled Upwork search, RSS/manual import, or scraped jobs.
- Actions: deduplicate by `Upwork Job URL`, `Website`, `Email`, `LinkedIn URL`; create/update `Leads`; estimate `Fit Score`; extract `Pain Signal`; suggest `Likely Offer`.
- Output: `Leads`, draft proposal/message in `Messages`, `Automation Logs`.

### 3. LinkedIn Pain Radar to CRM
- Trigger: manual list, saved search, or scraped LinkedIn/company data.
- Actions: deduplicate lead/company; classify niche; detect pain/opportunity; create `Leads`; draft opener.
- Output: `Leads`, `Messages`, `Automation Logs`.

### 4. Website audit generator
- Status: Pipeline C v2 completed operationally on 2026-05-04.
- Trigger: Telegram command via WF-06 (`/pipeline_c`, `/audit_sites`) or manual status/action.
- Actions: Firecrawl Search finds websites automatically, dedupes domains, scrapes sites, summarizes conversion/ops gaps, generates `Pain Hypothesis`, `Recommended Offer`, and teaser email.
- Output: `Leads`, `Audits`, `Messages`, `Automation Logs`, Telegram approval cards, and Gmail send only after `Approve + Send`.

### 5. Outreach draft generator
- Trigger: new qualified lead, audit completed, or manual request.
- Actions: create channel-specific message draft using `Message Templates`; personalize with pain, niche, offer, and demo.
- Output: unsent draft in `Messages`.
- Rule: do not auto-send until copy is proven.

### 6. Follow-up queue
- Trigger: daily schedule.
- Actions: find due `Leads`, `Messages`, `Proposals`; create follow-up drafts; update `Next Action`; send Telegram/Slack summary.
- Output: `Messages`, updated dates/statuses, `Automation Logs`.

### 7. Reply and status intake
- Trigger: manual update, email/LinkedIn/Upwork reply webhook if available.
- Actions: classify reply sentiment; update lead status; create opportunity when interested or call booked.
- Output: updated `Leads`, `Messages`, optional `Opportunities`.

### 8. Opportunity and proposal builder
- Trigger: call booked, discovery notes added, or opportunity stage change.
- Actions: convert discovery notes into problem, workflow, ROI, scope, price, timeline; create proposal draft.
- Output: `Opportunities`, `Proposals`, `Automation Logs`.

### 9. Demo recommendation and tracking
- Trigger: message/proposal draft or lead offer match.
- Actions: recommend the best demo by offer/niche; increment `Times Sent` after demo is sent; update performance metrics manually or via available tracking.
- Output: updated `Demos`, `Messages`, `Automation Logs`.

### 10. Won deal to client handoff
- Trigger: opportunity stage becomes `Won`.
- Actions: create `Clients`; link won opportunity/proposal; set onboarding status; generate handoff checklist; schedule delivery milestones.
- Output: `Clients`, updated `Opportunities`, `Automation Logs`.

### 11. Retainer conversion
- Trigger: client delivered or project end date approaching.
- Actions: create/pitch retainer opportunity; schedule pitch follow-up; generate retainer pitch draft and monthly report placeholders.
- Output: `Retainers`, `Messages`, updated `Clients`, `Automation Logs`.

### 12. Weekly CRM health report
- Trigger: weekly schedule.
- Actions: calculate new leads, messages sent, reply rate, calls booked, proposals sent, won deals, retainer MRR.
- Output: Telegram/Slack summary and optional `Automation Logs`.

## Safety rules

- Airtable remains the source of truth.
- Every workflow writes to `Automation Logs`.
- Deduplicate before creating records.
- Never overwrite human notes; append context or create logs.
- AI-generated copy, audits, proposals, and scores are drafts unless explicitly approved.
- Store sanitized snapshots only; never store API keys, cookies, tokens, or private credentials.

## First implementation batch

1. CRM core setup validation.
2. Upwork Radar to CRM.
3. Follow-up queue.
4. Outreach draft generator.
