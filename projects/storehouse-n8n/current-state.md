# Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Content
Status as of 2026-04-27:

- Project memory skeleton created.
- Local workspace path: `/Users/tamerlan/Desktop/storehouse-n8n`.
- Rebuilt StoreHouse Telegram Bot automation into a 3-file AI Agent architecture and replaced StoreHouse mocks with real WebAPI HTTP Request nodes.
- Local workspace is not currently a git repository.
- Current generated files:
  - `README.md`
  - `generate-workflows.mjs`
  - `workflows/workflow-1-main-ai-agent-photo-recognition.json`
  - `workflows/workflow-2-low-stock-alert.json`
  - `workflows/workflow-3-suspicious-activity-alert.json`
- JSON syntax validation passed for all 3 workflow exports.
- Node-name, connection, no-Code-node, and node-type sanity checks passed for all 3 workflow exports.
- Workflow 1 now uses `AGENT — Main Warehouse Brain` with GPT-4o and 5 connected `ai_tool` nodes.
- Telegram actions use native Telegram nodes; OpenAI uses native OpenAI/LangChain nodes; Google Sheets uses native Google Sheets nodes.
- HTTP Request is used only for StoreHouse WebAPI calls to `/api/sh5exec`.
- Zero nodes named `MOCK — ...` remain in generated workflow files.
- StoreHouse data reads now use SH WebAPI for stock balances and recent documents; Google Sheets remains only for `automation_log` and `min_thresholds`.
- Cleaned up a dangling unused WF3 suspicious-activity error branch after visual review in n8n.

## Working assumptions
- Treat this as an ongoing project because the user explicitly requested a project skeleton in memory.
- Current architecture uses 3 workflows: main AI Agent/photo recognition, low stock scheduled alert, suspicious activity scheduled alert.
- StoreHouse calls use placeholder n8n variables for host/port/login/password/proc names until on-site procedure discovery is complete.
- In WF1, StoreHouse tool nodes may appear visually separate because they are connected to the AI Agent through `ai_tool` connections rather than normal main-flow lines.
