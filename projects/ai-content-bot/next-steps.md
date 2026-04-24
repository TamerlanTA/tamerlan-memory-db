# AI Content Bot — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

---

## Задачи на 2026-04-26 (завтра)

### Блок 1 — Инфраструктура (разблокировать всё остальное)

**Задача 1.1 — Получить ID WF-11 и заменить плейсхолдер**
- Открыть WF-11 в n8n → ID из URL
- Заменить `REPLACE_WITH_WF11_ID` в `WF-10_Post_Approval.json` → нода `Trigger WF-11 Publish`
- Импортировать WF-10 в n8n

**Задача 1.2 — Импортировать WF-06 и WF-10 в n8n**
- WF-06: добавлен IF: Is Callback? + Forward to WF-05
- WF-10: добавлены inline кнопки + reply_markup
- Проверить что Telegram шлёт сообщение с кнопками

**Задача 1.3 — Создать Posts и Topics листы в Google Sheets**
- Extensions → Apps Script → запустить скрипт
- Проверить колонки: `post_id, date, topic, source, linkedin_text, twitter_text, threads_text, image_url, status`

---

### Блок 2 — Полный пересмотр approve/publish флоу (ГЛАВНАЯ ЗАДАЧА)

Текущая архитектура WF-05 → WF-10 → WF-11 несогласована по post_id и статусам. Нужна полная переработка.

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

**Конкретные изменения в воркфлоу:**

- **WF-09**: добавить шаг `Search Topic in Sheet` — поиск по ключевому слову в Topics таблице перед генерацией
- **WF-10 (show)**: убрать `items[0]` — показывать конкретный post_id или первый draft с явным post_id в кнопках
- **WF-10 (approve)**: читать по `post_id` → вызывать WF-11 → обновлять статус на `approved`
- **WF-11**: после публикации → обновить Posts статус на `published` → подтверждение в Telegram
- **WF-05**: убедиться что передаёт post_id корректно в WF-10

---

### Блок 3 — Персонализация изображений

**Задача 3.1 — Разработать визуальный стиль**
Определить:
- Основные цвета (пример: тёмный фон #0D0D0D, акценты: электрик синий #00F0FF, неоново-зелёный #00FF88)
- Визуальные элементы (circuit lines, floating UI fragments, minimal geometric shapes)
- Атмосфера (tech-noir, corporate cyberpunk, minimalist AI)
- Формат: 16:9 photorealistic, no text, no logos

**Задача 3.2 — Обновить system prompt в WF-09 `Build Claude Prompt`**
Заменить шаблон image_description на:
```
"MINIMALISTIC PERSONAL BRAND STYLE: Ultra dark background (#0D0D0D), 
electric blue and neon green accent elements, [specific visual metaphor for post topic], 
thin geometric lines/grids, cinematic lighting, photorealistic 16:9, 
NO text, NO logos, NO people faces, depth of field blur"
```

---

### Блок 4 — Замена оставшихся плейсхолдеров в WF-06

После импорта WF-07, WF-10, WF-12 в n8n:
- `REPLACE_WITH_WF07_ID` → ID WF-07
- `REPLACE_WITH_WF10_ID` → ID WF-10
- `REPLACE_WITH_WF12_ID` → ID WF-12

---

### Низкий приоритет (отложить)
- Unsplash API ключ в WF-09
- Firecrawl credential в WF-07
- WF-02 Followup и WF-03 Reply Monitor
- Активация всех воркфлоу по расписанию

---

## Порядок работы завтра

1. Инфраструктура (Блок 1) — 20 минут
2. Пересмотр approve/publish флоу (Блок 2) — основная работа
3. Персонализация изображений (Блок 3) — если останется время
