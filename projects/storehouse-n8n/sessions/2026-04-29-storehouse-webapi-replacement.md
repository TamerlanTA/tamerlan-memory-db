# Session 2026-04-29 — StoreHouse WebAPI Replacement

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Replaced all `MOCK —` StoreHouse nodes with real HTTP Request nodes targeting `/api/sh5exec`.
- Removed old mock sticky notes and added on-site configuration sticky notes.
- Replaced StoreHouse-data Google Sheets reads for `mock_stock` and `mock_documents` with SH WebAPI calls.
- Kept Google Sheets usage for `automation_log` and `min_thresholds`.
- Updated `README.md` and `generate-workflows.mjs`.
- After visual review in n8n, removed an unused dangling suspicious-activity generic error branch from WF3.
- After a second visual review, corrected WF1 agent tools: StoreHouse tools now use dedicated `toolHttpRequest` nodes connected to the agent via `ai_tool`, instead of ordinary HTTP Request nodes with misleading main-flow branches.

## Key findings
- Current workflow files now contain zero node names starting with `MOCK —`.
- StoreHouse calls use n8n variables for host, port, credentials, and procedure placeholders.
- Each StoreHouse HTTP Request node has a `VALIDATE — SH Response OK...` IF node plus StoreHouse connection and response-error branches.

## Validation
- `node --check generate-workflows.mjs`
- Regenerated all 3 workflow JSON files.
- Parsed all generated workflow JSON files with `JSON.parse`.
- Checked unique node names, valid connection references, zero `MOCK —` nodes, zero Code nodes, `/api/sh5exec` URLs, validation branches, and error branches.
- Confirmed Google Sheets nodes only target `automation_log` and `min_thresholds`.
- Rechecked dangling nodes: WF1 has no dangling non-tool nodes, and its five tool sources connect to the agent via `ai_tool`.

## Blockers
- Real StoreHouse host, port, user, password, and procedure names are still placeholders.
- Exact response shapes must be verified against the client server.
- Workflows still need import and live smoke testing in n8n.

## Next steps
- Configure SH variables on-site.
- Discover procedures via `/api/sh5` and `/api/sh5struct`.
- Run live StoreHouse smoke tests and adjust response parsing if needed.
