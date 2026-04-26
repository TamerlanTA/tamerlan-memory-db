# AI Content Bot — Risks & Blockers

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

---

## АКТИВНЫЕ БЛОКЕРЫ (2026-04-27)

### R-17: Outreach connection request не отправляется ⛔ accepted
**Симптом:** При approve в Telegram статус обновляется в таблицах, но connection request реально не уходит на LinkedIn.
**История:** Пробовали Sourcegeek (выдавал ошибки), затем Phantombuster через HTTP API. Phantom принимал launch (containerId возвращался) но не выполнялся даже вручную из Phantombuster UI. Видел лиды в Google Sheet, но не мог зайти в LinkedIn (Name/Headline пустые) — скорее всего невалидный/истёкший `li_at` cookie или Google Sheet недоступен.
**Решение:** Функция отправки полностью отключена. WF-05 идёт `Get Lead Approve → Set Approve Data` напрямую. Approve работает как "пометить отправленным" без реальной отправки.
**Что делать когда вернёмся:** обновить `li_at`, проверить sharing settings Google Sheet, или искать альтернативу (n8n LinkedIn community node, Apify, HeyReach API).

### R-18: TELEGRAM_BOT_TOKEN hardcoded в WF-09 ⚠️
**Симптом:** Для image-to-image fetch из Telegram нужен bot token, но n8n env vars — paid feature.
**Решение:** В `Prepare Gemini Body` Code ноде стоит placeholder `REPLACE_WITH_TELEGRAM_BOT_TOKEN`. После импорта нужно вручную заменить на токен от @BotFather.
**Что делать:** При апгрейде n8n плана перенести в env. Пока — hardcode.

---

## КРИТИЧЕСКИЕ БЛОКЕРЫ (обнаружены 2026-04-25)

### R-01: Inline кнопки подтверждения поста не появляются ✅ локально исправлено
**Симптом:** После показа поста бот не выводит кнопки ✅ Publish / ⏭️ Skip.
**Причина:** `Build Post Preview` создавал `reply_markup`, но Telegram node `Send Post Preview` его фактически не использовал. Аналогичная проблема была в WF-09 generated preview.
**Статус:** В локальных WF-09 и WF-10 Telegram nodes теперь используют inlineKeyboard с callback_data `approve_post_{post_id}` / `skip_post_{post_id}`.
**Что делать:** Импортировать WF-09/WF-10 и проверить кнопки в n8n.

---

### R-02: Промпт WF-09 статичен — всегда генерирует пост на первую выбранную тему ✅ локально исправлено
**Симптом:** При запросе "создай пост про X" — бот всегда берёт первую тему из первого запуска, не учитывает текущую тему.
**Статус:** Усилено после реального теста. WF-06 теперь напрямую извлекает `source_url` из Telegram текста до AI Agent, а WF-09 нормализует URL/headline и приоритетно матчится по source URL. Prompt явно запрещает generic n8n case study, если передан article/source URL.
**Что делать:** После импорта протестировать запросы вида `create post about <topic from briefing>`.

---

### R-03: Выбор темы из Morning Briefing не работает ✅ локально исправлено
**Симптом:** Бот присылает список топиков, но пользователь не может выбрать тему из него — бот не сравнивает написанное с Topics таблицей и создаёт пост только из текста запроса.
**Статус:** WF-08 теперь показывает top topics by `Topics.score`, а WF-09 понимает `создай пост 1/2/3` и выбирает тему по тому же score ranking.
**Что делать:** После импорта WF-06/WF-08/WF-09 протестировать: `Дай топ тем для постов` → `создай пост 1`.

### R-13: Запрос топ тем запускал discovery вместо briefing ✅ локально исправлено
**Симптом:** На `Дай мне топ тем для постов на сегодня` бот отвечал, что 30 тем сохранены, потому что AI Agent вызывал WF-07 discovery.
**Причина:** В WF-06 не было deterministic route для topic briefing, а AI tool `run_topic_discovery` был описан слишком широко.
**Статус:** WF-06 теперь напрямую распознаёт `топ тем / темы для постов / briefing` и вызывает WF-08. AI Agent получил отдельный tool `show_topic_briefing`; `run_topic_discovery` теперь предназначен только для явного refresh/discover новых тем.

---

### R-04: Бот не различает несколько постов в очереди (post_id игнорируется) ⛔
**Симптом:** В Google Sheets несколько постов со статусом draft, но бот считает что всегда один. Не читает по post_id.
**Причина:** WF-10 `Read Draft Posts` возвращает все draft, но `Build Post Preview` берёт `items[0]` — первый найденный, без учёта навигации. Нет механизма "следующий пост".
**Что делать:** Добавить пагинацию или передавать явный post_id в запрос. Либо показывать по одному с кнопкой "следующий".

---

### R-05: Бот не обновляет статус поста при подтверждении ✅ локально исправлено, Buffer blocker остаётся
**Симптом:** После одобрения пост не меняет статус с `draft` на `approved`/`published` в таблице.
**Статус:** WF-10 теперь вызывает WF-11 `7WA4JJwkIGvbehYs`, читает пост по `post_id` и передаёт payload. WF-11 обновляет `Posts` на `published` или `error`.
**Осталось:** Buffer token/profile IDs должны быть рабочими.

---

### R-06: Бот не читает посты со статусом `approved` для публикации ✅ локально исправлено
**Симптом:** Посты одобрены, но не публикуются.
**Статус:** Убрана неверная фильтрация `status=approve`; WF-10 approve читает по `post_id`.
**Что делать:** После Buffer настройки протестировать WF-11 вручную с тестовыми данными.

---

### R-07: Вся логика approve/update/read статусов и публикации требует полного пересмотра ✅ локально пересобрано
**Симптом:** Комплексная проблема — несогласованность между WF-05, WF-10, WF-11 в обработке post_id, статусов, callback данных.
**Статус:** Локальные JSON приведены к схеме:
1. WF-06 routes post callbacks before AI Agent.
2. WF-05 remains fallback/callable for outreach and post callback pass-through.
3. WF-10 show: читать первый draft + кнопки с post_id
4. WF-05/WF-06 approve: получает post_id из callback → вызывает WF-10(approve, post_id)
5. WF-10 approve: читает пост по post_id → готовит payload → вызывает WF-11
6. WF-11: публикует → обновляет статус на `published` или `error`; если Buffer не настроен → `approved`
**Осталось:** show-flow всё ещё показывает первый draft, если не передан post_id; полноценная пагинация 1/3 не реализована.

---

### R-08: Генерация изображений не персонализирована под стиль ✅ финал 2026-04-27
**История:** Прошли через 3 итерации стиля — dark/neon → minimal dashboard-card → save-worthy infographic с muted accent → **vibrant viral edu-content**.
**Финал (2026-04-27):** White grid paper background, HUGE bold typography (40-50% площади), 2-3 vibrant accent colors (lime/coral/sky/yellow), filled highlight boxes за key words, 3D emoji-иконки, цветные pinned cards. Референсы: @organizeddashboard, techwith.ram. Личные посты получают quote-card/number-card стиль вместо infographic.
**Осталось:** Тестировать качество живой Gemini-генерации с новым промптом.

---

### R-09: `REPLACE_WITH_WF11_ID` в WF-10 ✅ решено локально
**Статус:** WF-10 теперь указывает на WF-11 ID `7WA4JJwkIGvbehYs`.

---

### R-10: WF-06, WF-10 локальные изменения не импортированы в n8n ⚠️
Файлы обновлены локально. Пока не переимпортированы — изменения не активны. После deterministic-router фикса нужно импортировать WF-06, WF-05, WF-09, WF-10, WF-11.

### R-19: Только educational/news посты — нет личных кейсов и историй ✅ исправлено 2026-04-27
**Симптом:** На запрос "уволил 4 человек, заработал $3350" бот генерил educational шаблон со списком "1. Efficiency Boost: 2. Focus Shift:". Не было поддержки личных постов.
**Решение:** WF-09 Build Claude Prompt переписан с STEP 1 — DETECT POST MODE (6 режимов: personal_case, personal_story, news_take, educational, contrarian, tool_breakdown), STEP 2 — WRITE according to mode. Personal-режимы получают voice "first person, raw, no corporate shape" + quote-card image style.

### R-20: Бот не общается на общие темы — только tool calls ✅ исправлено 2026-04-27
**Симптом:** AI Agent system prompt в WF-06 был жёстко заточен на 7 tools, не понимал что делать вне их.
**Решение:** System prompt переписан. Tool calls только когда явно совпадает; на всё остальное — отвечает естественно как ChatGPT. Явно перечислено "When NOT to use tools".

### R-21: Нет поддержки картинки-референса при генерации поста ✅ исправлено 2026-04-27
**Симптом:** Пользователь хотел прикрепить картинку + caption и чтобы бот использовал картинку как визуальный референс для image generation.
**Решение:** WF-06 Route Telegram Update детектит `msg.photo` массив, захватывает `photo_file_id` и роутит в `create_post`. WF-09 Resolve Topic пробрасывает file_id, Prepare Gemini Body фетчит из Telegram (getFile + download), конвертит в base64, добавляет как `inlineData` в Gemini contents ПЕРЕД text — Gemini Nano Banana Pro поддерживает image-to-image. См. R-18 про token hardcode.

### R-11: Buffer REST token/profile IDs ✅ решено заменой на GraphQL
**Симптом:** WF-11 не публиковал, потому что old REST path требовал `profile_ids`, а текущий токен давал `401 OIDC tokens are not accepted for direct API access`.
**Статус:** WF-11 переведён на Buffer GraphQL API `https://api.buffer.com`, где используются `channelId`, а не `profile_ids`.
**Каналы:** LinkedIn `69eb419a031bfa423c3a88d2`, Twitter/X `69eb4550031bfa423c3a984e`, Threads `69eb4061031bfa423c3a81bf`.
**Осталось:** Реально протестировать live publish после импорта WF-11.

### R-12: Фото не прикрепляется к Buffer без публичного image_url ✅ локально исправлено
**Симптом:** Telegram получает Gemini image preview, но Buffer публикует текст без изображения.
**Причина:** Buffer GraphQL `createPost` принимает `assets.images[].url`; текущий WF-09 хранит `image_url: ''`, потому что Gemini отдаёт base64/binary, а не публичный URL.
**Статус:** WF-09 теперь делает signed upload в Cloudinary и сохраняет `secure_url` как `image_url`; WF-11 использует этот URL в Buffer `assets.images[].url`.
**Осталось:** После импорта протестировать live generation → Cloudinary upload → Buffer publish. Security cleanup: перенести Cloudinary secret из JSON в n8n credentials/env.

### R-14: Контент слишком рекламирует агентство ✅ локально исправлено
**Симптом:** Даже news/trend posts превращались в pitch FlowOps/agency вместо traffic/reach content.
**Статус:** WF-09 prompt теперь default editorial reach mode: анализ темы/новости, no agency pitch, no `At FlowOps, we...`, no service CTA, no hype wording. Conversion/sales должен быть отдельным явным режимом/запросом.

### R-15: Выбор соцсети для публикации отсутствовал ✅ локально исправлено
**Симптом:** Approve публиковал во все каналы.
**Статус:** WF-09/WF-10 preview buttons теперь позволяют выбрать channel set; WF-06/WF-10 parse callback suffix `|linkedin,twitter`; WF-11 фильтрует Buffer mutation по `target_channels`.

### R-16: Cloudinary секрет временно хранится в workflow JSON ⚠️
**Симптом:** Для быстрого signed upload Cloudinary `api_secret` добавлен прямо в WF-09 Code node.
**Риск:** JSON export содержит секрет.
**Что делать:** Когда флоу подтвердится live-тестом, перенести Cloudinary auth в n8n credentials/env или заменить на unsigned upload preset.

---

## Решённые

- ~~Reddit HTTP 403~~ → заменён на RSS Feed в WF-07
- ~~LangChain v2.1 response format~~ → добавлен fallback в Parse Response
- ~~Gemini `[invalid syntax]`~~ → Prepare Gemini Body Code нод
- ~~Gemini 429~~ → новый API ключ от AI Pro подписки
- ~~Один webhook на бота~~ → WF-06 ловит все, роутит через IF: Is Callback?
