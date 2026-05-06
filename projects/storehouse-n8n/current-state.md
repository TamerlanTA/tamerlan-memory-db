# Current State

## Related
- [[projects/storehouse-n8n/overview]]
- [[projects/storehouse-n8n/decisions]]
- [[projects/storehouse-n8n/risks]]
- [[projects/storehouse-n8n/next-steps]]

## Content
Status as of 2026-04-30:

- All 3 workflow JSON files fully built, fixed across review sessions, and validated.
- Local workspace path: `/Users/tamerlan/Desktop/storehouse-n8n`.
- Local workspace is not currently a git repository.
- Current generated files:
  - `README.md`
  - `generate-workflows.mjs`
  - `workflows/workflow-1-main-ai-agent-photo-recognition.json`
  - `workflows/workflow-2-low-stock-alert.json`
  - `workflows/workflow-3-suspicious-activity-alert.json`

### WF1 — main AI Agent / photo recognition (40 nodes)
- Binary file handoff via `ACTION — Download Invoice File Binary`; HTTP Request authentication was removed because Telegram file download uses token-in-URL rather than n8n HTTP credential auth.
- Dynamic chat ID from trigger node on all Telegram send nodes.
- `ERROR — SH Tool Failure Alert` includes the triggering Telegram user's first name and chat ID.
- All 4 `toolHttpRequest` AI tool nodes have `onError: continueErrorOutput`.
- `VALIDATE — Parse invoice JSON` uses indexOf/lastIndexOf robust extraction.
- `SET — Extract photo file id` outputs 5 lean fields only.
- All SH write nodes include `source: 'telegram_bot'` in params.

### WF2 — low stock scheduled alert (20 nodes)
- `AGGREGATE — Collect All Thresholds` node prevents duplicate Telegram sends.
- Cursor-based deduplication via `automation_cursors` Google Sheet (`wf2-low-stock` row).
- `GET — Last Processed Timestamp` has exactly one outgoing connection.
- SH API uses `since` cursor param with safe cold-start fallback to 15 minutes ago.

### WF3 — suspicious activity scheduled alert (15 nodes)
- Source filter excludes `telegram_bot` writes from suspicious activity detection.
- Multi-op alert message with numbered lines (documentType, itemName, quantity, userName).
- Cursor-based deduplication via `automation_cursors` Google Sheet (`wf3-suspicious-monitor` row).
- `GET — Last Processed Timestamp` has exactly one outgoing connection.
- SH API uses `since` cursor param with safe cold-start fallback to 15 minutes ago.

### Validation scores
- WF1: 11/11 (Batch 1) + 2/2 (Batch 3 WF1 changes)
- WF2: 17/17
- WF3 + WF1 Batch 3: 14/14

## Working assumptions
- StoreHouse calls use placeholder n8n variables for host/port/login/password/proc names until on-site procedure discovery.
- `automation_cursors` sheet no longer needs pre-seeded rows for first run; WF2/WF3 default to checking the last 15 minutes when no cursor row is found.
- On-site StoreHouse WebAPI endpoint `http://10.0.23.2:9797/api/sh5` is reachable and returns SH5WAPI2 v1.12, but browser GET returns `errorCode: 1`, `errMessage: JSON is absent`; procedure discovery must be done with JSON POST/auth payload via PowerShell/Postman/n8n HTTP Request, not plain browser GET.
- On-site n8n HTTP Request tests against `/api/sh5exec` with guessed procedure names reached StoreHouse but returned `procedure not found` from `SDBCLI.DLL`; this indicates guessed names are invalid and exact SH5 procedure names must be obtained from SH5 WebAPI templates/test utility/docs/integrator, not inferred from `/api/sh5exec`.
- On-site TEMPLATE scan found real procedures and `sh5struct` confirmed `errorCode: 0` for `GRemns`, `GDocs`, `InsGDoc0`, and `InsGDoc1`; tentative mapping is stock balances `GRemns`, document log `GDocs`, incoming document create `InsGDoc0`, movement/other document create `InsGDoc1` pending full field-structure review.
- Official SH5 WebAPI II execution uses `Input` arrays with table `head`, `original` field IDs, and `values`; existing generated workflow bodies using a generic `params` object will need adjustment for real StoreHouse execution.
