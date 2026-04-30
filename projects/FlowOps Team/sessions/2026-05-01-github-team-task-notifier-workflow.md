# Session 2026-05-01 — GitHub Team Task Notifier Workflow

## Related
- [[00 - Overview]]
- [[Team Task Automation]]
- [[n8n]]

## What was done
- Designed an importable n8n workflow JSON for polling GitHub-backed Obsidian team task folders every 5 minutes.
- Workflow checks Aslanbek, Adil, and Alexey active task folders, reads new markdown files, parses top task metadata, and sends a concise Telegram group notification.
- Added bootstrap mode logic so existing `.md` files can be marked processed without sending Telegram messages.

## Key findings
- Dedupe must be based on `file_path`, not GitHub `sha`, to prevent duplicate Telegram notifications after file edits.
- GitHub Contents API paths need URL encoding for spaces while preserving `/` path separators.
- Telegram send failure should not mark a file processed, so the next scheduled run can retry.

## Blockers
- None for the generated JSON.

## Next steps
- Import the workflow into n8n.
- Replace GitHub and Telegram placeholders.
- Run once with `BOOTSTRAP_MODE=true`, then switch to `false` for production polling.
