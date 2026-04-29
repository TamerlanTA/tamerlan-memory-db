# Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

## Content
## Open risks

- No git repository exists yet, so change history and rollback strategy are not established.
- Workflow JSON files have passed static JSON/name/connection/no-Code-node checks but have not yet been imported and smoke-tested inside a live n8n instance.
- Google Sheets node parameter compatibility may need minor adjustment depending on the target n8n version and credential naming.
- Telegram Trigger setup and credential binding must be confirmed in the target n8n instance.
- StoreHouse HTTP Request nodes now point to `/api/sh5exec`, but real host/port/credentials/procedure names must be configured on-site.
- Exact StoreHouse procedure names and response payload shapes remain unknown until `/api/sh5`, `/api/sh5struct`, and live tests are run on the client server.
- The main Agent tools are connected as n8n AI tools, but end-to-end behavior must be verified in n8n because tool execution details vary by n8n version.
- WF1 photo branch currently builds a Telegram file URL using the bot token inside the OpenAI vision image URL; this should be replaced with binary image handoff or a token-safe temporary URL.
- WF1 StoreHouse agent tool calls use `toolHttpRequest` directly, so they do not have deterministic `VALIDATE — SH Response OK` / Telegram / log branches inside the tool execution path.
- WF2 low-stock scheduled workflow may duplicate alerts because the comparison Set node runs once per `min_thresholds` row after Google Sheets read.
- WF1 `check_low_stock` agent tool only returns threshold rows and relies on the agent to combine them with stock balances, rather than returning deterministic low-stock results.
- WF1 tool HTTP placeholders send numeric parameters such as `quantity` and `limit` as strings.

## Resolved risks

- Initial project scope clarified enough to generate mock n8n workflow exports.
- Empty workspace risk resolved by adding workflow JSON exports and a generator script.
- Old 6-file workflow output was replaced by the requested 3-file AI Agent architecture.
- StoreHouse mock nodes removed; generated workflow files now contain zero `MOCK —` nodes.
