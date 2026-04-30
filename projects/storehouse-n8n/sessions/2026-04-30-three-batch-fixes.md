# Session 2026-04-30 — Three-Batch Fix Run

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done

### Batch 1 — WF1: 7 fixes
1. **Binary file handoff**: Replaced broken `$credentials`-based Telegram file URL with a new `ACTION — Download Invoice File Binary` HTTP Request node using `predefinedCredentialType: telegramApi`, passing binary to OpenAI via `binaryPropertyName: "data"`.
2. **Tool error handling**: Added `onError: continueErrorOutput` to all 4 `toolHttpRequest` AI tool nodes; added shared `ERROR — SH Tool Failure Alert` node (isolated — toolHttpRequest nodes cannot have main-flow error branches).
3. **Dynamic chatId**: Replaced static `$vars.TELEGRAM_CHAT_ID` with `$('TRIGGER — Telegram group message').item.json.message.chat.id` on both user-facing Telegram send nodes.
4. **qty int cast**: Added `parseInt(i.qty) || 0` to items map in `ACTION — SH API: Create Incoming Invoice`.
5. **Invoice file error branch**: Connected `ACTION — Telegram get invoice file` error output → `ERROR — Telegram invoice failure alert`.
6. **Robust JSON parsing**: Rewrote `VALIDATE — Parse invoice JSON` with `indexOf('{')` / `lastIndexOf('}')` extraction; throws on missing JSON object.
7. **Lean SET node**: Stripped `SET — Extract photo file id` to 5 fields only: `messageId`, `chatId`, `text`, `fileId`, `username`.

### Batch 2 — WF2: 2 fixes
1. **Dedup Telegram sends**: Inserted `AGGREGATE — Collect All Thresholds` (`aggregateAllItemData`) after Google Sheets read → collapses N rows to 1 item, preventing N Telegram sends.
2. **Cursor-based deduplication**: Added `GET — Last Processed Timestamp` (Google Sheets read of `automation_cursors`, filter `wf2-low-stock`) + `LOG — Update Last Processed Timestamp` (upsert). SH API now sends `since` cursor param with 30-min fallback. Both cursor read outputs connect to SH API for first-run resilience.

### Batch 3 — WF3 + WF1 coordinated: 3 fixes
1. **Source tagging (WF1)**: Added `source: 'telegram_bot'` to params of `ACTION — SH API: Create Incoming Invoice` and `create_stock_movement` toolHttpRequest.
2. **Source filter (WF3)**: Updated `SET — Build suspicious activity alert` filter to `r.source && r.source !== 'telegram_bot'`; built multi-op alert message with numbered lines (documentType, itemName, quantity, userName); `ACTION — Telegram send suspicious alert` reads `$json.alertMessage`.
3. **Cursor pattern (WF3)**: Same pattern as WF2 but `wf3-suspicious-monitor` key and 15-min fallback. Both cursor read outputs connect to SH API.

## Validation
- WF1 after Batch 1: 11/11 checks passed (automated script).
- WF2 after Batch 2: 17/17 checks passed (automated script).
- WF1 + WF3 after Batch 3: 14/14 checks passed (automated script).

## Key findings
- `toolHttpRequest` nodes in n8n LangChain agent flows only support `ai_tool` connections — they cannot have main-flow VALIDATE IF or ERROR branches. `onError: continueErrorOutput` + a shared ERROR alert node is the correct pattern.
- When `automation_cursors` sheet is empty (first run), Google Sheets returns 0 items and the chain would break. Fix: connect both `main[0]` and `main[1]` of the cursor read node to the SH API call.
- WF3 original had two nodes at identical canvas position (780, 520); moved `ERROR — Telegram SH response alert suspicious` to (780, 420) to fix overlap.

## Blockers (unchanged from prior sessions)
- Real StoreHouse host, port, credentials, and procedure names still need on-site configuration.
- `automation_cursors` Google Sheet must be pre-seeded with one row per workflow (`wf2-low-stock`, `wf3-suspicious-monitor`) before first run, or the cursor read error-path fallback must be accepted.
- No live smoke tests done.

## Next steps
1. Pre-seed `automation_cursors` sheet: two rows, columns `workflowName` | `last_processed_at`.
2. Import all 3 JSON files into target n8n instance.
3. Set credentials: `TELEGRAM_BOT_CREDENTIAL`, `OPENAI_CREDENTIAL`, `GOOGLE_SHEETS_CREDENTIAL`.
4. Set variables: `TELEGRAM_CHAT_ID`, `GOOGLE_SHEETS_ID`.
5. On-site: set `SH_HOST`, `SH_PORT`, `SH_USER`, `SH_PASSWORD`, all `SH_PROC_*` variables.
6. Smoke-test WF1 with text and photo Telegram payloads.
7. Verify SH response shapes (`data`/`rows`/`items`/`documents`) and adjust parsing if needed.
