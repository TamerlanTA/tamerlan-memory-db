# AI Content Bot — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

---

## Задачи на 2026-04-26 (завтра)

### Блок 1 — Инфраструктура (разблокировать всё остальное)

**Задача 1.1 — Импортировать обновлённые локальные workflows**
- Импортировать WF-05, WF-06, WF-09, WF-10, WF-11 из `/Users/tamerlan/Desktop/linkedin automation/`
- Важно: WF-06 — единственный активный Telegram Trigger
- WF-05 должен оставаться callable-only через Execute Workflow

**Задача 1.2 — Создать/обновить Google Sheets структуру**
- Запустить обновлённый `create_sheets.gs` или вручную добавить:
  - `Posts`
  - `Topics`
  - Queue columns: `subject`, `followup_subject`, `followup_message`

**Задача 1.3 — Разблокировать Buffer**
- Получить valid direct API token/credential для Buffer
- Получить Buffer `profile_ids`
- Указать `BUFFER_PROFILE_IDS` в n8n env или передавать `profile_ids` в WF-11
- Текущий токен при прямом API тесте вернул `401 OIDC tokens are not accepted for direct API access`

---

### Блок 2 — Проверка approve/publish флоу (ГЛАВНАЯ ЗАДАЧА)

Локальная архитектура WF-05 → WF-10 → WF-11 пересобрана по `post_id` и статусам. Теперь нужна проверка после импорта.

**Требования к новому флоу:**

```
Пользователь пишет "create post about X"
  → WF-09 ищет тему X в Topics таблице (match by keyword)
  → Если найдена → берёт url/headline из топика
  → Если нет → генерирует на основе текста запроса
  → Генерирует пост → сохраняет в Posts (status=draft, уникальный post_id)
  → Отправляет превью с кнопками ✅ Publish / ⏭️ Skip

Пользователь нажимает ✅ Publish (callback: approve_post_{post_id})
  → WF-06 → IF: Is Callback? → WF-05
  → WF-05 парсит post_id из callback_data
  → Вызывает WF-10 {action: approve, post_id: XXX, chat_id: YYY}
  → WF-10 читает пост по post_id из Posts
  → Вызывает WF-11 {post_id, linkedin_text, twitter_text, threads_text, image_url}
  → WF-11 публикует в Buffer → обновляет статус в Posts на published
  → Отправляет подтверждение в Telegram

Пользователь пишет "show pending posts"
  → WF-10 (action=show) читает ВСЕ draft посты
  → Показывает по одному с кнопками + пост 1/3 индикатором
  → Кнопка "следующий" показывает следующий (по post_id)
```

**Проверить после импорта:**
- `Дай мне топ тем для постов на сегодня` → WF-06 должен вызвать WF-08, не WF-07; Telegram должен показать top 5+ pending topics sorted by `Topics.score`
- `создай пост 1` после briefing → WF-09 должен взять topic #1 by score, not first arbitrary row
- New post preview buttons show channel options: `All`, `LinkedIn`, `X`, `Threads`, `LI+X`, `LI+Threads`, `X+Threads`, `Skip`
- Clicking `LinkedIn` publishes only LinkedIn; clicking `LI+X` publishes only LinkedIn and X
- Generated post should be editorial/traffic-focused, not agency ad; no `At FlowOps, we...` unless user explicitly asks for conversion/sales
- New post should save `Posts.image_url` as a Cloudinary `secure_url`
- Buffer publish should show `Image: attached` and create posts with the generated image
- `Создай пост <VentureBeat URL>` → WF-06 должен напрямую вызвать WF-09 с `source_url`; WF-09 должен сгенерировать пост по этой статье, не generic n8n case study
- Telegram preview содержит кнопки
- `approve_post_{post_id}` → WF-06 → WF-10 approve → WF-11; WF-10 не должен получать `show`
- outreach callbacks `a`/`s` → WF-06 → WF-05
- WF-11 с валидным Buffer config обновляет `Posts.status=published`
- Если Buffer profile IDs отсутствуют: `Posts.status=approved`, Telegram получает понятное сообщение о Buffer setup
- При ошибке Buffer API: `Posts.status=error`, Telegram получает понятное сообщение

---

### Блок 3 — Персонализация изображений

**Задача 3.1 — Проверить новый FlowOps image style после импорта WF-09**
- Новый стиль уже записан локально в WF-09:
  - 4:5 vertical Threads/LinkedIn infographic poster
  - warm off-white / subtle grid paper background
  - bold black/deep-navy typography
  - one muted accent color only
  - headline + 3-5 useful short labels/bullets/framework elements
  - clean cards/arrows/tags/checklist/stack layouts
  - no neon/robots/rockets/fake metrics/logos
- После импорта создать тестовый пост и оценить:
  - есть ли сильный visual hook
  - есть ли полезная структура, которую хочется сохранить
  - нет ли misspelled/unreadable text

**Задача 3.2 — Проверить Cloudinary hosting для изображений**
- WF-09 уже добавляет upload step после Gemini:
  - `Extract Image Base64`
  - `Prepare Cloudinary Upload`
  - `Upload Image to Cloudinary`
  - `Finalize Record`
- Проверить, что `Posts.image_url` заполняется `https://res.cloudinary.com/...`
- После успешного теста перенести Cloudinary secret из JSON в безопасное место.

---

### Блок 4 — Низкоуровневая проверка после импорта
- Убедиться, что WF-06 tool workflow IDs указывают на актуальные импортированные workflow IDs
- Проверить, что в JSON нет старых `YOUR_*` / `REPLACE_WITH_*`
- Проверить, что в n8n UI Telegram nodes действительно показывают inlineKeyboard

---

### Низкий приоритет (отложить)
- Firecrawl credential в WF-07
- WF-02 Followup и WF-03 Reply Monitor
- Активация всех воркфлоу по расписанию

---

## Порядок работы завтра

1. Инфраструктура + импорт (Блок 1) — 20 минут
2. Проверка approve/publish флоу (Блок 2) — основная работа
3. Персонализация изображений (Блок 3) — если останется время
