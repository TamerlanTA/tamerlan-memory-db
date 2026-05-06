# Session 2026-04-27 — AI Agent Rebuild

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- Rebuilt StoreHouse Telegram Bot workflow exports from the prior module-split architecture into a central AI Agent architecture.
- Replaced generated workflow output with 3 files:
  - `workflow-1-main-ai-agent-photo-recognition.json`
  - `workflow-2-low-stock-alert.json`
  - `workflow-3-suspicious-activity-alert.json`
- Updated `README.md`.
- Rewrote `generate-workflows.mjs` to regenerate the new architecture.

## Key findings
- Official n8n AI Agent architecture uses `@n8n/n8n-nodes-langchain.agent` with `ai_languageModel`, `ai_memory`, and `ai_tool` connections.
- The main workflow uses GPT-4o via native n8n OpenAI/LangChain nodes.
- Telegram actions are native Telegram nodes; Google Sheets operations are native Google Sheets nodes.
- StoreHouse mock calls are the only HTTP Request nodes and have exact sticky-note replacement text.

## Validation
- `node --check generate-workflows.mjs`
- Regenerated all 3 workflow JSON files.
- Parsed all generated JSON with `JSON.parse`.
- Checked unique names and valid connection references.
- Checked generated workflows contain 0 Code nodes.
- Checked HTTP Request nodes are not used for OpenAI or Telegram.
- Checked Workflow 1 has 5 `ai_tool` connections.

## Blockers
- Workflows still need import and smoke testing inside a live n8n instance.
- Tool execution behavior should be verified against the exact target n8n version.
- Real StoreHouse WebAPI access is still unavailable.

## Next steps
- Import the 3 workflow files into n8n.
- Bind credentials and variables.
- Test text-agent, photo-invoice, scheduled low-stock, and scheduled suspicious-activity paths.

