# Session 2026-04-25 — WF-09 Gemini image gen, WF-10 кнопки, WF-06 callback routing

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

---

## Что было сделано

### WF-09 Content Generation — полный рерайт
- Переписан `Build Claude Prompt` — 4 вирусных контентных бакета (AI Basics Done Wrong, Real Implementation, AI Tools Breakdown, Contrarian Take)
- Добавлен `Prepare Gemini Body` Code нод — строит `gemini_body` JSON строку для HTTP Request
- `Generate Image Gemini` нод: `contentType: "raw"`, URL с Nano Banana Pro моделью
- `Extract Image Base64` — парсит `candidates[0].content.parts` Gemini ответа
- `Prepare Photo` + `Send Image Preview` — отправляет изображение в Telegram
- `Parse Response` — обновлён fallback цепочкой для LangChain v2.1 формата

### WF-06 AI Command Center — callback routing
- Telegram Trigger обновлён: `["message", "callback_query"]`
- Добавлен `IF: Is Callback?` нод (`$json.callback_query` is not empty)
- Добавлен `Forward to WF-05` executeWorkflow нод (workflowId: `sgwBsMBN4eFvSh41`)
- Флоу: Trigger → IF → (true: WF-05) / (false: Extract Message → AI Agent)

### WF-10 Post Approval — inline кнопки
- `Build Post Preview` теперь генерирует `reply_markup` с кнопками:
  - `✅ Publish` → callback_data: `approve_post_{post_id}`
  - `⏭️ Skip` → callback_data: `skip_post_{post_id}`
- `Send Post Preview` — добавлен `reply_markup` в additional fields
- Убран текст "Reply: approve post or skip post"

---

## Ключевые находки

- **n8n single webhook constraint**: только один активный Telegram Trigger на бота — WF-05 никогда не срабатывал сам по себе
- **LangChain v2.1**: ответ теперь в `$json.output[0].content[0].text`, не `$json.text`
- **Gemini `[invalid syntax]`**: нельзя использовать `JSON.stringify()` в `specifyBody: "json"` — нужен отдельный Code нод, передавать строку через переменную
- **Gemini API 429**: старый ключ не был привязан к AI Pro подписке. Новый ключ: `AIzaSyAwEtVjuIg5HkkcZ-TM9SpKDjmmgY_sC_o`
- **Модель Gemini**: `gemini-3-pro-image-preview` (Nano Banana Pro) — предыдущие версии `gemini-2.0-flash-*` устарели

---

## Blockers

- `REPLACE_WITH_WF11_ID` в WF-10 `Trigger WF-11 Publish` — публикация заблокирована
- WF-06 и WF-10 обновлены локально, но не импортированы в n8n

---

## Next Steps (из этой сессии)

1. Получить ID WF-11 из n8n UI → заменить в WF-10 → импортировать
2. Импортировать WF-06 (callback routing) и WF-10 (кнопки) в n8n
3. Создать Posts/Topics листы в Google Sheets
4. Тест полного флоу: create post → кнопки → approve → WF-11 → Buffer
