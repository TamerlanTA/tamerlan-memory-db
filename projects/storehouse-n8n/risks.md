# Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

## Content
## Open risks

- No git repository exists yet, so change history and rollback strategy are not established.
- Workflow JSON files have passed static JSON/name/connection checks but have not yet been imported and smoke-tested inside a live n8n instance.
- Google Sheets node parameter compatibility may need minor adjustment depending on the target n8n version and credential naming.
- Telegram webhook setup is external to the workflow exports; Telegram must be configured to POST group updates to the generated webhook URLs.
- Mock StoreHouse HTTP Request nodes currently point at `https://httpbin.org/anything`; production must replace them with `POST /api/sh5exec`.
- Real StoreHouse credentials, API availability, and exact procName payload contracts remain unknown.

## Resolved risks

- Initial project scope clarified enough to generate mock n8n workflow exports.
- Empty workspace risk resolved by adding workflow JSON exports and a generator script.
