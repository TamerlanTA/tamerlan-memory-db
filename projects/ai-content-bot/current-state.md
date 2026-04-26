# AI Content Bot — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Статус (2026-04-27)

### Последний аудит/фикс ✅
- **2026-04-27 outreach sending DROPPED**: после долгих попыток заменить Sourcegeek на Phantombuster (через HTTP `api.phantombuster.com/api/v2/agents/launch`, корректные имена аргументов `leadsSourceUrl`/`columnName`/`sessionCookie`/`userAgent`/`customizeInvite`/`numberOfAddsPerLaunch`) — phantom не запускался даже вручную из Phantombuster UI, видел лиды в Google Sheet но не мог зайти в LinkedIn (Name/Headline пустые). Решение: убрать отправку connection request полностью. WF-05 теперь идёт `Get Lead Approve → Set Approve Data` напрямую, без промежуточных Phantombuster нод. Approve флоу обновляет статус в Queue/Leads, шлёт "✅ Отправлено!" в Telegram, но реальный LinkedIn-запрос не отправляется.
- **2026-04-27 vibrant image style**: после анализа референсов (@organizeddashboard, techwith.ram, dark green workflow nodes) полностью переделан image prompt. Белый/off-white grid background, HUGE bold typography (40-50% площади), 2-3 vibrant accent colors вместо одного muted, filled highlight boxes за ключевыми словами, 3D emoji-иконки, цветные pinned cards. Промпт обновлён в двух местах: VISUAL STYLE REFERENCES внутри Build Claude Prompt и styleGuide в Prepare Gemini Body.
- **2026-04-27 adaptive post modes**: WF-09 теперь определяет один из 6 режимов автоматически: personal_case (реальный кейс с цифрами), personal_story (мысль/опыт), news_take, educational, contrarian, tool_breakdown. Промпт делает STEP 1 — DETECT POST MODE, STEP 2 — WRITE according to mode. Personal-режимы получают voice "first person, raw, no corporate shape" и quote-card/number-card image style. Editorial-режимы — sharp analysis + vibrant infographic. Решает проблему когда на личный кейс генерился educational шаблон "1. Efficiency Boost 2. Focus Shift".
- **2026-04-27 general assistant mode**: AI Agent system prompt в WF-06 переписан. Tool calls только когда запрос явно совпадает; на всё остальное (вопросы, брейнсторм, casual chat, follow-up) отвечает естественно как ChatGPT. Явно перечислено "When NOT to use tools".
- **2026-04-27 reference image input**: пользователь может прикрепить картинку + caption в Telegram. Route Telegram Update в WF-06 детектит `msg.photo` массив, захватывает `photo_file_id` (последний/самый большой размер) и автоматически роутит в `create_post`. Resolve Topic в WF-09 пробрасывает file_id, Prepare Gemini Body фетчит картинку через Telegram getFile + download, конвертирует в base64 и добавляет как `inlineData` в `parts` ПЕРЕД text — Gemini Nano Banana Pro поддерживает image-to-image, использует картинку как визуальный референс. Build Claude Prompt сообщает модели о референсе, она это учитывает в image_description. **Требует**: hardcode `TELEGRAM_BOT_TOKEN` в Code ноде Prepare Gemini Body после импорта (placeholder `REPLACE_WITH_TELEGRAM_BOT_TOKEN`), потому что n8n env variables — paid feature.

### Старые фиксы (2026-04-25/26) ✅
- **2026-04-25 deterministic router fix:**  после реального Telegram-теста обнаружено, что:
  - запрос с VentureBeat URL всё равно сгенерировал generic post про n8n/automation
  - нажатие `✅ Publish` привело к WF-10 `show`, а не `approve`
- Исправлено архитектурно:
  - **WF-06** теперь маршрутизирует `create post`, `show posts`, `approve_post_*`, `skip_post_*` обычными Code/Switch нодами до AI Agent.
  - **WF-09** теперь извлекает URL из текста, нормализует URL/headline и приоритетно матчится по source URL, а не по первой строке Topics.
  - **WF-10** получает `action/post_id/chat_id` напрямую из текущего JSON, добавлен `Prepare WF-11 Publish Payload`.
  - **WF-05** post callbacks теперь тоже проходят через `Prepare WF-10 Post Action`, без schema-dependent workflowInputs.
  - **WF-11** при отсутствии Buffer profile IDs ставит `Posts.status=approved` и объясняет setup blocker, вместо silent fail.
- **2026-04-25 WF-06 callback payload hotfix:** в n8n UI обнаружено, что WF-10 `Parse Action` получает `{ ok: true, result: true }`, потому что Telegram `Answer Post Callback` стоял перед `Call WF-10 Post Action`. Исправлено: `Answer Post Callback` теперь отдельная side branch, а WF-10 получает payload через новый `Prepare WF-10 Post Action`.
- **2026-04-25 WF-10 show-default guard:** так как approve/skip всё ещё приводил к `show`, WF-06 перестроен ещё жёстче: `Switch post_action → Prepare WF-10 Post Action → [Answer Callback + Call WF-10]`. WF-10 `Parse Action` теперь бросает ошибку, если получает `{ok,result}` или boolean `result` без `action/post_id`, вместо молчаливого fallback в `show`.
- **2026-04-25 remove post answer callback:** после guard error в n8n `Answer Post Callback` полностью отключён от post approve/skip ветки. Текущий путь: `Switch post_action → Prepare WF-10 Post Action → Call WF-10 Post Action`. Это исключает попадание Telegram `{ok,result}` в WF-10.
- **2026-04-25 Buffer GraphQL publishing fix:** выяснено, что текущий Buffer token работает с новым GraphQL API `https://api.buffer.com`, но не со старым REST `api.bufferapp.com`. WF-11 переведён на GraphQL `createPost` и реальные channel IDs:
  - LinkedIn `69eb419a031bfa423c3a88d2`
  - Twitter/X `69eb4550031bfa423c3a984e`
  - Threads `69eb4061031bfa423c3a81bf`
  `IF: Buffer Configured` больше не участвует в активном пути; публикация идёт напрямую в Buffer и агрегируется в `published` / `partial_error` / `error`.
- **2026-04-25 multi-channel Buffer fix + FlowOps image style:** после live test Buffer публиковал LinkedIn отдельно и затем присылал второй failure из-за multi-item fan-out. WF-11 теперь строит один GraphQL mutation с alias для `linkedin/twitter/threads`, парсит ответ по каналам и отправляет одно Telegram-сообщение. Добавлена поддержка `assets.images[].url`, если в `image_url` появится публичная ссылка. WF-09 image prompt переведён на референсный FlowOps стиль: light frosted/ice-blue background, deep navy panels/type, cyan/aqua accents, SaaS operation-board cards, pill labels, square composition.
- **2026-04-25 top topics routing fix:** команда вроде `Дай мне топ тем для постов на сегодня` больше не должна запускать WF-07 discovery/save. WF-06 теперь deterministic routes such requests to WF-08 `Topic Briefing`; WF-08 callable через `executeWorkflowTrigger`, читает `Topics`, сортирует pending темы по `score` и показывает top 5+ (default 7). WF-09 теперь поддерживает numeric selection from briefing: `создай пост 1`, `создай пост 2` выбирают темы по тому же score ranking.
- **2026-04-25 channel selection + editorial content fix:** посты больше не обязаны публиковаться во все соцсети. Preview buttons теперь дают выбор: `All`, `LinkedIn`, `X`, `Threads`, `LI+X`, `LI+Threads`, `X+Threads`, `Skip`; WF-06/WF-10/WF-11 передают `target_channels` до Buffer. WF-09 prompt переведён в default reach/traffic editorial mode: не рекламировать FlowOps в каждом посте, не превращать новости в агентский кейс, не использовать hype вроде `revolution/game-changer/race car`. Image prompt ужесточён до minimal editorial SaaS style: off-white, deep navy, muted blue, whitespace, almost no glow, no rockets/robots/neon/fake metrics.
- **2026-04-26 Cloudinary image hosting fix:** WF-09 теперь загружает Gemini image base64 в Cloudinary (`drzrljg9t`) через signed upload (`Prepare Cloudinary Upload` → `Upload Image to Cloudinary`) и сохраняет `secure_url` в `Posts.image_url`. WF-11 уже прикрепляет `image_url` к Buffer через `assets.images[].url`, поэтому после импорта WF-09 + WF-11 новые посты должны публиковаться с изображениями.
- **2026-04-26 save-worthy infographic prompt:** после теста первые изображения стали чище, но слишком пустыми/малоинформативными. WF-09 image prompt обновлён: теперь модель должна генерировать 4:5 vertical Threads/LinkedIn infographic poster, not decorative image. В `image_description` требуется exact headline + 3-5 short labels/bullets + layout type (`cover/checklist/framework/stack/before-after`). Стиль: warm off-white/grid paper, bold black/deep-navy type, one muted accent color, useful cards/arrows/tags, no neon/robots/rockets/fake metrics/logos.
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
