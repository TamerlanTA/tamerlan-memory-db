# Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Content
Immediate next steps:

1. Import all 3 JSON files from `/Users/tamerlan/Desktop/storehouse-n8n/workflows/` into the target n8n instance.
2. Configure required n8n credentials/variables: `TELEGRAM_BOT_CREDENTIAL`, `OPENAI_CREDENTIAL`, `GOOGLE_SHEETS_CREDENTIAL`, `TELEGRAM_CHAT_ID`, and `GOOGLE_SHEETS_ID`.
3. Smoke-test Workflow 1 with text and photo Telegram payloads.
4. Confirm the AI Agent can call all 5 connected tools in the target n8n version.
5. Smoke-test scheduled low-stock and suspicious-activity workflows.
6. On-site: configure `SH_HOST`, `SH_PORT`, `SH_USER`, `SH_PASSWORD`, and all `SH_PROC_*` variables.
7. On-site: discover exact procedure names and payload schemas via `/api/sh5` and `/api/sh5struct`.
8. Run live StoreHouse smoke tests for stock balances, incoming invoice, stock movement, expense report, and recent documents.
9. Adjust response parsing if real SH payload fields differ from assumed `data` / `rows` / `items` / `documents` shapes.
10. Decide whether to initialize `/Users/tamerlan/Desktop/storehouse-n8n` as a git repository.
