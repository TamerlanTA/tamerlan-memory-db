# Session 2026-04-29 — Architecture Validation Review

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Reviewed all 3 workflow JSON exports using n8n workflow testing and validation criteria.
- Checked JSON parseability, trigger presence, connected-node graph, dangling references, orphan execution nodes, node types, credential placeholders, StoreHouse URLs, removed mock references, and Google Sheets sheet usage.
- Confirmed WF1 tool nodes are connected to the agent via `ai_tool` connections, so the visually separate tool cluster is not disconnected execution flow.

## Key findings
- No orphan or dangling execution nodes were found in the 3 workflow exports.
- No `MOCK —` nodes, Code nodes, `mock_stock`, or `mock_documents` references remain.
- WF1 still has architecture risks: token-bearing Telegram image URL to OpenAI, SH tool calls without deterministic validation/error/log subflows, low-stock tool only reads thresholds, and numeric tool params are stringified.
- WF2 has a likely duplicate-alert runtime issue because the low-stock Set node runs once per `min_thresholds` input item.
- README still says each StoreHouse mock has a sticky note, which is stale after mock replacement.

## Blockers
- No live n8n instance validation or execution trace was available in this session.
- Target n8n version/tool-node compatibility still needs import testing.

## Next steps
- Convert WF1 StoreHouse agent tools into deterministic tool sub-workflows or current-version n8n tool nodes with explicit validation and clean return contracts.
- Fix WF2 aggregation so low-stock comparison emits one item per scheduled run.
- Change the photo branch to pass Telegram file binary or a token-safe temporary URL into OpenAI vision.
- Update README wording to match real WebAPI nodes rather than old mocks.
