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
6. Replace mock StoreHouse HTTP Request nodes with real `POST /api/sh5exec` calls once WebAPI access is available.
7. Decide whether to initialize `/Users/tamerlan/Desktop/storehouse-n8n` as a git repository.