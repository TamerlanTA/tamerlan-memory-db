# Session 2026-04-27 — Image style + post modes + assistant mode

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done

### 1. Phantombuster outreach — DROPPED
- Заменили Sourcegeek на Phantombuster через HTTP Request к `api.phantombuster.com/api/v2/agents/launch`.
- Перепробовано несколько форматов аргументов: `spreadsheetUrl` массив → строка, корректные имена полей `leadsSourceUrl`, `columnName`, `sessionCookie`, `userAgent`, `customizeInvite`, `numberOfAddsPerLaunch`.
- API принимал launch (возвращал `containerId`), но phantom не запускался даже вручную — Phantombuster видел лиды в Google Sheet, но не мог зайти в LinkedIn (Name/Headline/Company пустые).
- Скорее всего невалидный/истёкший `li_at` cookie или sheet недоступен Phantombuster'у.
- **Решение**: убрать отправку connection request из бота. WF-05 теперь идёт `Get Lead Approve → Set Approve Data` напрямую, без `Prepare PB Body` и `Send connection request`. Approve флоу всё равно обновляет статус в Queue/Leads таблицах и шлёт "✅ Отправлено!" в Telegram, но реальный LinkedIn запрос не отправляется. Это осознанный компромисс пока не появится рабочий способ.

### 2. Image style overhaul (WF-09)
- Старый стиль: muted, "one accent color max", warm off-white, минимализм. Получались бледные пустые картинки.
- Новый стиль (после анализа референсов @organizeddashboard, techwith.ram, dark green workflow nodes):
  - Белый/off-white фон с **видимой grid pattern** (graph paper)
  - **HUGE bold black/deep-navy typography** — заголовок занимает 40-50% площади
  - **2-3 vibrant accent colors** (lime green #86EFAC, coral orange #F97316, sky blue #38BDF8, hot yellow #FDE047), а не один muted
  - **Filled color highlight boxes** за ключевыми словами (как text selection)
  - Цветные **pinned/sticky cards** с буллетами
  - **3D emoji-иконки** (✅ 🔥 ⚡ 📌 →) для энергии
  - "scroll-stopping, viral edu-content vibe"
- Промпт обновлён в двух местах: `Build Claude Prompt` (VISUAL STYLE REFERENCES) и `Prepare Gemini Body` (styleGuide).

### 3. Adaptive post modes (WF-09)
- Старый промпт жёстко ограничивал editorial/news. На запрос "уволил 4 человек, заработал $3350" бот всё равно генерил educational пост со списком "1. Efficiency Boost: 2. Focus Shift:".
- Новый промпт делает **STEP 1 — DETECT POST MODE**, выбирает один из 6 режимов:
  1. **personal_case** — реальный кейс с цифрами/результатами. Voice: первое лицо, raw, без educational shape, можно упоминать FlowOps как личный контекст.
  2. **personal_story** — мысль/опыт/наблюдение. Voice: разговорный, friendly, не preachy.
  3. **news_take** — комментарий к новости/URL.
  4. **educational** — объяснение/framework.
  5. **contrarian** — провокационная позиция.
  6. **tool_breakdown** — разбор инструмента.
- Каждому режиму соответствует свой voice и структура.
- `image_description` тоже адаптируется: для personal — quote-card / number-card стиль, для editorial — vibrant infographic.
- `Prepare Gemini Body` использует `post_mode` чтобы переключать первую строку styleGuide между "PERSONAL/QUOTE-STYLE" и "VIBRANT INFOGRAPHIC".

### 4. General assistant mode (WF-06)
- Старый system prompt был жёстко заточен на 7 tools, не понимал что делать вне их.
- Новый prompt разделяет работу на две категории: tool calls (когда явно совпадает) и general chat (на всё остальное — как ChatGPT).
- Явно перечислено "When NOT to use tools": general questions, brainstorming, casual conversation, follow-up на предыдущие темы.
- Теперь бот может полноценно общаться о чём угодно.

### 5. Reference image input (WF-06 + WF-09)
- В `Route Telegram Update` (WF-06) добавлено детектирование `msg.photo` массива и захват `photo_file_id` (последний/самый большой размер). Если фото присутствует — автоматически идёт в `create_post` с caption как topic.
- В `Resolve Topic` (WF-09) пробрасывается `photo_file_id`.
- В `Build Claude Prompt` (WF-09) добавлен `imageHint` — модель знает что есть референс и упоминает в `image_description`.
- В `Prepare Gemini Body` (WF-09) добавлен fetch:
  - HTTP GET `https://api.telegram.org/bot{TOKEN}/getFile?file_id=...` → получает `file_path`
  - HTTP GET `https://api.telegram.org/file/bot{TOKEN}/{file_path}` → бинарь картинки
  - `Buffer.from(buf).toString('base64')` → base64
  - Добавляется в `parts` как `inlineData` ПЕРЕД text — Gemini Nano Banana Pro поддерживает image-to-image.
- **Требует**: ручное заполнение `TELEGRAM_BOT_TOKEN` константы в Code ноде (placeholder `REPLACE_WITH_TELEGRAM_BOT_TOKEN`). Без env vars нет другого способа на n8n free tier.

## Key findings

- **Phantombuster API формат**: `id` должен быть строкой, не числом (validation error). `argument` может быть либо объектом либо JSON-строкой. `containerId` в ответе ≠ phantom реально запустился.
- **n8n environment variables** требуют платный план — для free tier credentials hardcode'ятся в Code/HTTP нодах.
- **Telegram Bot токен** напрямую недоступен из Code нод даже если используется в credentials — нужен hardcode.
- **Gemini Nano Banana Pro (gemini-3-pro-image-preview)** принимает image-to-image через `contents.parts[].inlineData` (mimeType + base64 data) до текстового prompt.

## Blockers

- ⚠️ User должен вручную заменить `REPLACE_WITH_TELEGRAM_BOT_TOKEN` в WF-09 после импорта.
- ⛔ Outreach отправка не работает — Phantombuster cookie/access блокеры не решены, функция отключена.

## Next steps

- Импорт WF-06 и WF-09 → замена token в `Prepare Gemini Body`.
- Тестирование 3 сценариев: (1) personal post с цифрами, (2) general chat, (3) photo + caption с референсом стиля.
- Если personal mode работает плохо — fine-tune промпт.
- Решить вопрос с outreach: либо найти рабочий способ (рабочий li_at + sheet access), либо считать "approve = mark as sent" финальным design'ом.
