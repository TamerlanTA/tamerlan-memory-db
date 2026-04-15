# Make-David — Prompts & Patterns

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

---

## Полезные контекстные подсказки для работы с проектом

### При работе с Apps Script
Файл: `/Users/tamerlan/Desktop/PC/Make-David/sellerchat_sheet_trigger.gs`
- Профили и их spreadsheet ID захардкожены в `SPREADSHEET_PROFILE_OVERRIDES` (начало файла)
- Добавить новый sheet → добавить его ID в этот объект с нужным профилем
- Trigger columns: David=(S,T), Lilia=(T,U), Lyan=(Q,R)
- Webhook URL Make.com: `https://hook.us2.make.com/pqms2w8hd1jyvwxbwj66w4gv37gefzu9`

### При создании Make.com сценария
- Следовать MAKE_SCENARIO.md строго
- SellerChat connections: по одному на каждый аккаунт (david, lilia, lyan)
- Data Store ключ дедупликации: `{account}|{record_key}|{template_name}`
- Sequential processing = ON

### При отладке n8n workflow
- Workflow: `WhatsApp AI Bot - Fotomultas v3 con Buffer from scratch.json`
- Redis debounce = 15 секунд
- Supabase table: `conversations`
- Kommo contact lookup — множество дублирующих nodes (разные индексы поиска)

### При добавлении нового профиля (нового пользователя)
1. Добавить их spreadsheet IDs в `SPREADSHEET_PROFILE_OVERRIDES` в Apps Script
2. Определить trigger columns (какие колонки = "yes")
3. Добавить в Make.com 2 новых route (один на шаблон)
4. Подключить SellerChat account в Make.com
5. Протестировать
