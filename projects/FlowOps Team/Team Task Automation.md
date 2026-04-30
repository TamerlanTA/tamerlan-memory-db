# Team Task Automation

## Related
- [[00 - Overview]]
- [[Pipeline A — Upwork Radar]]
- [[n8n]]

## Current status
- On 2026-04-30, converted `/Users/tamerlan/Desktop/flowopsteamPipelines/team-tasks-import.json` from a custom data import file into a real n8n workflow export.
- Ready n8n workflow file: `/Users/tamerlan/Desktop/flowopsteamPipelines/team-task-n8n-workflow.json`.
- Workflow name: `FlowOps Team Task - Create Aslanbek Pricing Task`.
- On 2026-05-01, designed an importable n8n workflow JSON for polling GitHub-backed Obsidian team task folders every 5 minutes and notifying Telegram only for new `.md` task files.
- Same day correction: user's n8n instance rejected `n8n-nodes-base.dataStore`; use static workflow data fallback instead for processed-file storage.

## What it does
- Supports Manual Trigger and POST Webhook trigger.
- Builds the Aslanbek pricing-section task from the original JSON data.
- Validates required task fields, priority/status enums, and array fields.
- Builds an HTML Telegram task card.
- Sends the task card to Telegram chat `405182031`.
- Returns JSON success/error response when triggered through webhook.

## Setup notes
- Import `team-task-n8n-workflow.json` into n8n, not `team-tasks-import.json`.
- Reconnect Telegram credentials after import.
- Activate workflow for production webhook use.
- The workflow intentionally has no hardcoded n8n credential IDs.
- For the GitHub polling task-notifier workflow, dedupe must use `file_path` as the primary key; GitHub `sha` is metadata only because it changes when a markdown file is edited.
- Static workflow data fallback stores processed records under `processedTeamTaskFiles[file_path]` inside the workflow's global static data. This state is per workflow copy.
