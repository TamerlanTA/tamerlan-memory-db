# Session 2026-04-27 — Mock n8n Workflows

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- Generated mock-version n8n workflow JSON exports for StoreHouse Telegram Bot automation.
- Created 6 workflow files under `/Users/tamerlan/Desktop/storehouse-n8n/workflows/`:
  - `workflow-1-invoice-photo-recognition.json`
  - `workflow-2-stock-movement.json`
  - `workflow-3a-low-stock-alert.json`
  - `workflow-3b-suspicious-activity-alert.json`
  - `workflow-4-stock-report.json`
  - `workflow-5-expense-report.json`
- Added `generate-workflows.mjs` to regenerate the exports.
- Added `README.md` with required variables and import notes.

## Key findings
- The user requested 5 modules, but Module 3 has two explicit sub-workflows; generated 6 import files to match the requested output labels.
- All StoreHouse mock nodes are HTTP Request nodes and have nearby sticky notes with the replacement instruction.
- Telegram, Anthropic, StoreHouse, and Google Sheets values are referenced through n8n variables/placeholders rather than hardcoded secrets.

## Validation
- `node --check generate-workflows.mjs`
- Generated all workflow JSON files with `node generate-workflows.mjs`.
- Parsed every generated JSON file with `JSON.parse`.
- Checked unique node names, valid connection references, node-name prefixes, and that all `MOCK — SH API` nodes are HTTP Request nodes.

## Blockers
- Workflows have not yet been imported into a live n8n instance.
- Actual n8n credential names and Google Sheets node compatibility may need final adjustment in the target environment.
- Real StoreHouse WebAPI is not yet available.

## Next steps
- Import workflows into n8n and run smoke tests.
- Configure variables/credentials in n8n.
- Replace mock StoreHouse nodes with real `POST /api/sh5exec` calls when API access is available.

