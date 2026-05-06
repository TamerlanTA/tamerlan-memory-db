# AI Content Bot — Decisions

## Related
- [[projects/ai-content-bot/overview]]
- [[projects/ai-content-bot/current-state]]
- [[projects/ai-content-bot/risks]]
- [[projects/ai-content-bot/next-steps]]

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

## D-07: Промпт контента — 4 бакета [УСТАРЕЛО, см. D-08]

**Решение (старое):** WF-09 использовал 4 случайных бакета: AI Basics / Real Implementation / Tools Breakdown / Contrarian.

**Заменено на D-08 (2026-04-27).**

---

## D-08: Adaptive post modes (6 режимов, auto-detect)

**Решение:** WF-09 Build Claude Prompt делает STEP 1 — DETECT POST MODE из запроса пользователя. 6 режимов:
1. `personal_case` — реальный кейс с цифрами/результатами. Voice: первое лицо, raw, без educational shape.
2. `personal_story` — мысль/опыт/наблюдение. Voice: разговорный, не preachy.
3. `news_take` — комментарий к новости/URL.
4. `educational` — объяснение/framework.
5. `contrarian` — провокационная позиция.
6. `tool_breakdown` — разбор инструмента.

STEP 2 — WRITE согласно правилам режима. Personal-режимы получают voice "first person, raw, no corporate shape" и quote-card/number-card image style. Editorial-режимы — sharp analysis + vibrant infographic.

**Почему:** Старая система с 4 случайными бакетами + жёсткое правило "make it about the idea, not FlowOps" мешала писать личные посты с цифрами. На запрос "уволил 4 человек, заработал $3350" получался educational шаблон.

**Параметры:** post_mode возвращается моделью в JSON и пробрасывается через Parse Response → Prepare Gemini Body для адаптации image style.

---

## D-09: Tools опциональны, AI Agent — полноценный ассистент

**Решение:** WF-06 AI Agent system prompt разделяет работу на две категории:
1. **Automation & content tools** — когда запрос явно совпадает с одним из 7 tools.
2. **General assistant chat** — на всё остальное (вопросы, брейнсторм, casual chat, follow-up). Просто отвечает текстом без tool call.

System prompt явно перечисляет "When NOT to use tools": general questions about anything, brainstorming, casual conversation, help with non-bot work.

**Почему:** Старый prompt был жёстко заточен на 7 tools. Бот не понимал что делать вне их, отказывался отвечать на вопросы или пытался найти подходящий tool которого нет.

---

## D-10: Reference image input через Telegram getFile в WF-09

**Решение:** Пользователь прикрепляет картинку + caption в Telegram. Поток:
1. WF-06 Route Telegram Update детектит `msg.photo` (массив размеров) → захватывает `photo_file_id` последнего размера → автоматически роутит в `create_post` с file_id.
2. WF-09 Resolve Topic пробрасывает `photo_file_id` дальше.
3. WF-09 Prepare Gemini Body вызывает Telegram getFile API (`https://api.telegram.org/bot{TOKEN}/getFile?file_id=X`), получает file_path, скачивает картинку (`https://api.telegram.org/file/bot{TOKEN}/{file_path}`), конвертит в base64.
4. Base64 добавляется как `inlineData` в `parts` массив ПЕРЕД text-промптом → Gemini Nano Banana Pro использует это как visual style reference.

**Почему:** image-to-image даёт пользователю прямой контроль над style референсом — гораздо точнее чем описывать словами "as @organizeddashboard".

**Ограничение:** TELEGRAM_BOT_TOKEN hardcoded в Code ноде (placeholder `REPLACE_WITH_TELEGRAM_BOT_TOKEN`) — n8n env vars требуют paid план.

---

## D-11: Vibrant viral edu-content image style

**Решение:** Финальный image style для WF-09:
- Background: white или off-white **с видимой grid pattern** (graph paper)
- Typography: HUGE bold black/deep-navy headline, занимает 40-50% площади
- Accent colors: 2-3 vibrant (lime #86EFAC, coral #F97316, sky blue #38BDF8, hot yellow #FDE047), НЕ muted
- Decorations: filled highlight boxes за key words, цветные pinned cards с буллетами, 3D emoji-иконки (✅ 🔥 ⚡ 📌 →)
- Vibe: "scroll-stopping, viral edu-content, like @organizeddashboard"

**Adaptive:** для post_mode=personal_case|personal_story → quote-card/number-card стиль вместо infographic.

**Почему:** Прошлые итерации (dark/neon → minimal dashboard → muted infographic) давали слишком бледные пустые картинки. Референсы пользователя (@organizeddashboard, techwith.ram) — vibrant и energetic.

---

## D-12: Outreach connection request — отключён [accepted compromise]

**Решение:** WF-05 идёт `Get Lead Approve → Set Approve Data` напрямую. Реальный LinkedIn connection request НЕ отправляется. Approve флоу обновляет статус в Queue/Leads + шлёт "✅ Отправлено!" в Telegram, но это маркер только в таблицах.

**Почему:** Sourcegeek выдавал ошибки. Phantombuster через API принимал launch (containerId) но phantom не запускался даже вручную, не мог зайти в LinkedIn (li_at cookie или Sheet access проблема). Не нашли рабочего способа.

**Когда возвращаемся:** обновить li_at, проверить Google Sheet sharing, либо альтернативы — n8n LinkedIn community node, Apify LinkedIn actors, HeyReach API.

---

## D-13: Route Telegram Update — regex включает артикли между глаголом и "post"

**Решение:** `/^(create|write...)\s+(?:(?!post\b|пост\b)\w+\s+){0,2}(пост|post)(?:[.\s,!?]|$)/i` — допускает до 2 слов-заполнителей ("a", "me", "my", "the") между глаголом и словом "post".

**Почему:** "Create a post. [content]" раньше не распознавался как create_post route из-за "a" перед "post". Маршрутизировался в AI Agent, который терял контекст личной истории.

**Как применять:** При добавлении новых языков или вариаций глаголов — проверять что regex всё ещё распознаёт "create a post", "write me a post", "write us a post".

---

## D-14: toolWorkflow format unwrapping в WF-09 Resolve Topic

**Решение:** В начале Resolve Topic проверяется формат входных данных. Если `rawInput.query?.some_input` существует (n8n toolWorkflow format), парсится как JSON. Иначе используется как есть (прямой executeWorkflow вызов).

**Почему:** Когда WF-06 AI Agent вызывает WF-09 через toolWorkflow, данные приходят в формате `{ query: { some_input: '{"topic":"..."}' } }`. Прямой вызов через executeWorkflow приходит flat-объектом. Без unwrapping `input.text` и `input.topic` были undefined → personal narrative detection не срабатывала.

**Как применять:** При добавлении новых нод в WF-09 что читают `$('When Called by WF-06').first().json` — нужен тот же unwrapping.

---

## D-15: Tool: Create Post schema — поле `text` для полного текста пользователя

**Решение:** В схему инструмента добавлено поле `text`: "Full verbatim user message. CRITICAL: if user shared a personal story, case, money figures — copy ENTIRE message verbatim, do not summarize."

**Почему:** AI Agent получал личную историю ("уволил 4 человек, заработал $3350") и пересказывал её в topic как "automation case study". WF-09 получал безликий topic, генерировал generic educational пост.

**Как применять:** AI Agent prompt явно инструктирует передавать VERBATIM текст в поле text. Resolve Topic в WF-09 читает `input.text` как `rawText` → personal narrative detection срабатывает.
