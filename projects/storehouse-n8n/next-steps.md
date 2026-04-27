# Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Content
Immediate next steps:

1. Import all 6 JSON files from `/Users/tamerlan/Desktop/storehouse-n8n/workflows/` into the target n8n instance.
2. Configure required n8n variables/credentials: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `GOOGLE_SHEETS_ID`, `ANTHROPIC_API_KEY`, `SH_USER`, `SH_PASSWORD`, and Google Sheets OAuth2 credential `GOOGLE_SHEETS_OAUTH2`.
3. Smoke-test each workflow with sample Telegram payloads or manual executions.
4. Confirm Google Sheets read/append mappings against the real spreadsheet structure.
5. Replace mock StoreHouse HTTP Request nodes with real `POST /api/sh5exec` calls once WebAPI access is available.
6. Decide whether to initialize `/Users/tamerlan/Desktop/storehouse-n8n` as a git repository.
