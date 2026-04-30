# Team Task Automation

## Related
- [[00 - Overview]]
- [[Pipeline A — Upwork Radar]]
- [[n8n]]

## Current status
- On 2026-04-30, converted `/Users/tamerlan/Desktop/flowopsteamPipelines/team-tasks-import.json` from a custom data import file into a real n8n workflow export.
- Ready n8n workflow file: `/Users/tamerlan/Desktop/flowopsteamPipelines/team-task-n8n-workflow.json`.
- Workflow name: `FlowOps Team Task - Create Aslanbek Pricing Task`.

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
