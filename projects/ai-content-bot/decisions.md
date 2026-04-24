# AI Content Bot — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

---

## D-01: Один Telegram Trigger на всю систему (WF-06)

**Решение:** WF-06 — единственный активный Telegram Trigger. Он слушает `message` + `callback_query` и роутит внутри.

**Почему:** n8n допускает только ОДИН активный вебхук на бота. Если WF-05 тоже активен с Telegram Trigger, он никогда не срабатывает — n8n регистрирует только последний вебхук.

**Как применять:** Никогда не активировать Telegram Trigger в WF-05, WF-07, WF-08 или других воркфлоу. Только WF-06.

---

## D-02: callback_query роутится через WF-06 → WF-05

**Решение:** WF-06 содержит `IF: Is Callback?` нод. Если `$json.callback_query` не пустой → Forward to WF-05 через executeWorkflow.

**Почему:** WF-05 обрабатывает логику approve/skip, но не может иметь собственный Telegram Trigger (см. D-01).

**Как применять:** При добавлении новых типов кнопок — добавить роутинг в WF-05, не в WF-06.

---

## D-03: Gemini для генерации изображений

**Решение:** `gemini-3-pro-image-preview` (Nano Banana Pro), API key от AI Studio проекта, привязанного к Google AI Pro подписке.

**Почему:** Google AI Pro подписка включает AI Studio с высокими лимитами для Gemini. Старый ключ `AIzaSyBW5obrOKfkKpZcq9CLMGB37K28wWk86BA` был привязан к другому проекту без подписки → 429.

**Текущий ключ:** `AIzaSyAwEtVjuIg5HkkcZ-TM9SpKDjmmgY_sC_o` (проект 1053960890982)

**Как применять:** Если снова 429 — проверить, что ключ от проекта в AI Studio, а не из Google Cloud Console отдельного проекта.

---

## D-04: HTTP Request с raw body для Gemini

**Решение:** В ноде `Generate Image Gemini`: `contentType: "raw"`, `rawContentType: "application/json"`, body = `={{ $json.gemini_body }}`.

**Почему:** n8n выдаёт `[invalid syntax]` если использовать `specifyBody: "json"` с `JSON.stringify()` в expressions, или если передавать объект напрямую с вложенными arrays. Предварительно строить JSON строку в Code ноде (`Prepare Gemini Body`) и передавать как строку — единственный надёжный способ.

**Как применять:** Любой сложный JSON для внешних API строить в Code ноде, передавать через переменную как строку.

---

## D-05: OpenAI LangChain нода v2.1 — путь к тексту изменился

**Решение:** `$json.output[0].content[0].text` (не `$json.text` как раньше).

**Почему:** LangChain нода обновилась. `$json.text` больше не возвращается. Parse Response в WF-09 проверяет оба варианта через fallback цепочку.

**Как применять:** В `Parse Response` и любом коде, читающем выход LangChain ноды:
```js
const raw = j.text || j.output?.[0]?.content?.[0]?.text || j.message?.content || '{}';
```

---

## D-06: Inline keyboard вместо текстовых инструкций в WF-10

**Решение:** WF-10 `Build Post Preview` генерирует `reply_markup` JSON с кнопками `✅ Publish` (callback: `approve_post_{id}`) и `⏭️ Skip` (callback: `skip_post_{id}`).

**Почему:** Без кнопок пользователь писал текст "Публикуй", AI agent интерпретировал как action=show вместо approve, публикация не происходила.

**Как применять:** callback_data в WF-10 должен совпадать с паттернами в WF-05 Route Request (проверить что WF-05 обрабатывает `approve_post_` и `skip_post_` префиксы).

---

## D-07: Промпт контента — 4 бакета

**Решение:** WF-09 использует 4 контентных бакета случайно:
1. AI Basics Done Wrong — разрушение мифов
2. Real Implementation — конкретный процесс
3. AI Tools Breakdown — инструменты/стек
4. Contrarian Take — неудобная правда

**Почему:** Разнообразие повышает engagement на LinkedIn. Монотонный контент = падение охвата.

**Параметры:** Английский язык, тон — живой, первое лицо (Tamerlan), ниша — AI автоматизация бизнеса / n8n.
