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

## Resolved risks

- Initial project scope clarified enough to generate mock n8n workflow exports.
- Empty workspace risk resolved by adding workflow JSON exports and a generator script.
- Old 6-file workflow output was replaced by the requested 3-file AI Agent architecture.
- StoreHouse mock nodes removed; generated workflow files now contain zero `MOCK —` nodes.
