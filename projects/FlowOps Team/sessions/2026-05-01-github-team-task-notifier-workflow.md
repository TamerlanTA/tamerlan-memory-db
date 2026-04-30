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
- Created corrected workflow file at `/Users/tamerlan/Desktop/flowopsteamPipelines/flowops-team-github-task-notifier-static-fixed-paths.json`.
- Created newer corrected workflow file at `/Users/tamerlan/Desktop/flowopsteamPipelines/flowops-team-github-task-notifier-telegram-node-fixed-normalize.json`.
- Created current corrected workflow file at `/Users/tamerlan/Desktop/flowopsteamPipelines/flowops-team-github-task-notifier-telegram-node-v2.json`.

## Key findings
- Dedupe must be based on `file_path`, not GitHub `sha`, to prevent duplicate Telegram notifications after file edits.
- GitHub Contents API paths need URL encoding for spaces while preserving `/` path separators.
- Telegram send failure should not mark a file processed, so the next scheduled run can retry.
- Static workflow data fallback stores records in `processedTeamTaskFiles[file_path]`; this persists inside the workflow but does not transfer automatically to a separately imported duplicate workflow.
- The GitHub web URL `https://github.com/TamerlanTA/tamerlan-memory-db/tree/main/My-Team/Aslanbek/tasks/active-tasks` maps to GitHub Contents API path `My-Team/Aslanbek/tasks/active-tasks`; the repo root already represents the vault root.
- `Filter Only Markdown Files` returned nothing because `Normalize GitHub Folder Response` expected an array, while n8n had already split the GitHub folder response into individual file-object items. The newer normalize code accepts both shapes.
- Official Telegram node is now used for sending. The only Code node after Telegram is the static processed-state save gate, needed so failed Telegram sends do not mark files processed.
- Fixed IF nodes to use explicit Boolean `Equal` comparisons: `is_processed Equal false` and `BOOTSTRAP_MODE Equal true`.
- Removed `$items(...)` cross-node references from Code nodes because n8n import suffixes such as `Config / Settings1` can break exact-name references.

## Blockers
- Data Store node is unavailable in the user's n8n instance; use static workflow data fallback unless Data Store/Data Table is later enabled.

## Next steps
- Import the workflow into n8n.
- Replace GitHub and Telegram placeholders.
- Run once with `BOOTSTRAP_MODE=true`, then switch to `false` for production polling.
- Rotate exposed GitHub and Telegram tokens because they appeared in the n8n screenshot.
