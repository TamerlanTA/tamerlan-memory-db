# AI Content Bot — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Статус (2026-04-25)

### Завершено ✅
- **WF-09 Content Generation** — полностью переписан:
  - Вирусные промпты по 4 контентным бакетам (AI Basics Done Wrong / Real Implementation / AI Tools Breakdown / Contrarian Take)
  - Gemini 3 Nano Banana Pro (`gemini-3-pro-image-preview`) для генерации изображений
  - Новый нод `Prepare Gemini Body` (Code) — строит JSON строку, избегая `[invalid syntax]` в HTTP Request
  - `Parse Response` обрабатывает оба формата: `$json.text` и `$json.output[0].content[0].text` (LangChain v2.1)
  - Сохраняет драфт в Google Sheets Posts + отправляет превью + изображение в Telegram

- **WF-06 AI Command Center** — обновлён:
  - Telegram Trigger слушает `["message", "callback_query"]` (оба типа)
  - Добавлен `IF: Is Callback?` нод — роутит callback_query → WF-05
  - Добавлен `Forward to WF-05` executeWorkflow нод (workflowId: `sgwBsMBN4eFvSh41`)

- **WF-05 Telegram Approval Queue** — обновлён ранее:
  - Только `callback_query` триггер (текстовые сообщения убраны)
  - Добавлен `executeWorkflowTrigger` как второй вход
  - Обрабатывает `approve_post_{id}` и `skip_post_{id}` callback_data

- **WF-10 Post Approval** — частично обновлён:
  - `Build Post Preview` теперь генерирует `reply_markup` с inline keyboard кнопками `✅ Publish` и `⏭️ Skip`
  - `Send Post Preview` добавлен `reply_markup` в additional fields
  - ❌ `REPLACE_WITH_WF11_ID` placeholder ещё не заменён

### Ожидает ⏳
- Получить реальный n8n ID WF-11 (из URL после импорта) → заменить в WF-10
- Импортировать обновлённые WF-06, WF-10 в n8n (или обновить через n8n UI)
- Создать Posts и Topics листы в Google Sheets (запустить Apps Script)
- Вставить Unsplash API ключ в WF-09 (placeholder `REPLACE_WITH_UNSPLASH_ACCESS_KEY`)
- Протестировать полный флоу: create post → review → approve → publish

### Активированные воркфлоу в n8n
WF-06 и WF-05 должны быть активны (Telegram triggers). WF-09, WF-10, WF-11 — только сохранены, не активированы.
