# Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Content
Immediate next steps (as of 2026-04-30, all requested workflow JSON fixes are complete):

1. **Import all 3 JSON files** from `/Users/tamerlan/Desktop/storehouse-n8n/workflows/` into the target n8n instance.
2. **Set credentials**: `TELEGRAM_BOT_CREDENTIAL`, `OPENAI_CREDENTIAL`, `GOOGLE_SHEETS_CREDENTIAL`.
3. **Set variables**: `TELEGRAM_CHAT_ID`, `GOOGLE_SHEETS_ID`.
4. **Smoke-test WF1** with text and photo Telegram payloads; verify dynamic chatId, binary file download without HTTP auth, OpenAI vision parse, and SH tool failure alert user/chat context.
5. **Smoke-test WF2 and WF3** scheduled flows with an empty `automation_cursors` sheet; verify 15-minute cold-start fallback and no duplicate alert sends.
6. **On-site**: set `SH_HOST`, `SH_PORT`, `SH_USER`, `SH_PASSWORD`, all `SH_PROC_*` variables.
7. **Discover exact procedure names + schemas** via `/api/sh5` and `/api/sh5struct`.
8. **Adjust response parsing** if real SH payload fields differ from assumed `data`/`rows`/`items`/`documents` shapes.
9. Decide whether to initialize `/Users/tamerlan/Desktop/storehouse-n8n` as a git repository.
