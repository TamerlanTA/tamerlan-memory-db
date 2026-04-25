# AI Content Bot — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Статус (2026-04-25)

### Последний аудит/фикс ✅
- Проведён полный локальный аудит всех JSON workflow-файлов:
  - JSON валиден
  - connections не указывают на отсутствующие ноды
  - старых `YOUR_*` / `REPLACE_WITH_*` плейсхолдеров в JSON не осталось
  - JS внутри Code-нод проходит синтаксическую проверку
- **WF-00**: upsert лидов теперь должен матчиться по `linkedin_url`.
- **WF-01**: исправлены `Build Prompt1`, лимит сообщения до 180 символов, и критическая ошибка обновления не того листа (`Stats` вместо `Leads`).
- **WF-02/WF-03/WF-04**: заменены плейсхолдеры Sheet/chat ID; WF-02 переведён с рискованных Set/spread/output-path выражений на Code-ноды.
- **WF-05**: удалён лишний Telegram Trigger из локального файла, export выставлен `active=false`, post callbacks передают в WF-10 явные `action/post_id/chat_id`.
- **WF-06**: callback detection усилен boolean-проверкой.
- **WF-09**: добавлен поиск темы в `Topics` через `Read Topics` → `Resolve Topic`, безопасная обработка пустого `source_url`, inline кнопки на preview.
- **WF-10**: inline кнопки реально подключены в Telegram node; approve читает по `post_id`; WF-11 получает явный payload.
- **WF-11**: Buffer body больше не пустой; публикация требует `profile_ids`/`BUFFER_PROFILE_IDS`; статус Posts обновляется в `published` или `error`.
- **create_sheets.gs**: добавлены `Posts`, `Topics`, и недостающие Queue columns.

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
- Импортировать обновлённые WF-05, WF-06, WF-09, WF-10, WF-11 в n8n (или обновить через n8n UI)
- Создать Posts и Topics листы в Google Sheets (запустить Apps Script)
- Настроить Buffer для WF-11: нужен valid direct API token + `profile_ids` / `$env.BUFFER_PROFILE_IDS`
- Протестировать полный флоу: create post → review → approve → publish

### Активированные воркфлоу в n8n
WF-06 — единственный активный Telegram Trigger. WF-05 должен быть callable-only через Execute Workflow, без активного Telegram Trigger. WF-09, WF-10, WF-11 могут быть сохранены/callable; отдельная активация Telegram Trigger для них не нужна.
