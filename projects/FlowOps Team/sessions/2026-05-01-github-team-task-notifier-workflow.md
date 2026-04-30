# Session 2026-05-01 — GitHub Team Task Notifier Workflow

## Related
- [[00 - Overview]]
- [[Team Task Automation]]
- [[n8n]]

## What was done
- Designed an importable n8n workflow JSON for polling GitHub-backed Obsidian team task folders every 5 minutes.
- Workflow checks Aslanbek, Adil, and Alexey active task folders, reads new markdown files, parses top task metadata, and sends a concise Telegram group notification.
- Added bootstrap mode logic so existing `.md` files can be marked processed without sending Telegram messages.
- Revised the workflow after import/runtime issue: user's n8n instance does not recognize `n8n-nodes-base.dataStore`, so the corrected version uses Code node static workflow data.

## Key findings
- Dedupe must be based on `file_path`, not GitHub `sha`, to prevent duplicate Telegram notifications after file edits.
- GitHub Contents API paths need URL encoding for spaces while preserving `/` path separators.
- Telegram send failure should not mark a file processed, so the next scheduled run can retry.
- Static workflow data fallback stores records in `processedTeamTaskFiles[file_path]`; this persists inside the workflow but does not transfer automatically to a separately imported duplicate workflow.

## Blockers
- Data Store node is unavailable in the user's n8n instance; use static workflow data fallback unless Data Store/Data Table is later enabled.

## Next steps
- Import the workflow into n8n.
- Replace GitHub and Telegram placeholders.
- Run once with `BOOTSTRAP_MODE=true`, then switch to `false` for production polling.
