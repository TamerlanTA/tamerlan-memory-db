# AI Content Bot — Risks & Blockers

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

---

## R-01: WF-10 содержит `REPLACE_WITH_WF11_ID` ⚠️ АКТИВНЫЙ БЛОКЕР

**Риск:** WF-10 не может вызвать WF-11 для публикации — placeholder не заменён.

**Как исправить:** Открыть WF-11 в n8n → взять ID из URL → заменить `REPLACE_WITH_WF11_ID` в `WF-10_Post_Approval.json` нода `Trigger WF-11 Publish` → переимпортировать / обновить в n8n.

**Приоритет:** КРИТИЧЕСКИЙ — публикация полностью заблокирована без этого.

---

## R-02: Posts и Topics листы не созданы

**Риск:** WF-09 падает при попытке записать драфт в Posts лист.

**Как исправить:** Запустить Google Apps Script в таблице через Extensions → Apps Script → создать Posts и Topics листы.

**Приоритет:** Высокий.

---

## R-03: Gemini API — нестабильное имя модели

**Риск:** Имя модели `gemini-3-pro-image-preview` может измениться (уже менялось в ходе работы — использовались: `gemini-2.0-flash-preview-image-generation`, `gemini-2.0-flash-exp-image-generation`, `gemini-3.1-flash-image-preview`).

**Как исправить:** При ошибке 404 — проверить актуальное имя модели через Google AI Studio → Model → Image Generation.

**Приоритет:** Средний.

---

## R-04: WF-06, WF-10 — локальные файлы обновлены, но n8n импорт не подтверждён

**Риск:** Изменения в JSON файлах не применяются в n8n, пока не будут импортированы / обновлены вручную.

**Как исправить:** После каждого изменения файлов — импортировать воркфлоу в n8n (Settings → Import) или обновить через n8n MCP если доступен.

**Приоритет:** Средний.

---

## R-05: Unsplash API ключ не добавлен в WF-09

**Риск:** Нода `Fetch Unsplash Image` не работает — placeholder `REPLACE_WITH_UNSPLASH_ACCESS_KEY`.

**Как исправить:** Получить Access Key в unsplash.com/developers → вставить в WF-09.

**Статус:** Низкий приоритет (Gemini генерирует изображения, Unsplash — fallback).

---

## R-06: WF-06 плейсхолдеры для WF-07, WF-10, WF-12

**Риск:** WF-06 AI Agent инструменты `run_topic_discovery`, `manage_post`, `get_daily_report` содержат `REPLACE_WITH_WF07_ID`, `REPLACE_WITH_WF10_ID`, `REPLACE_WITH_WF12_ID`.

**Как исправить:** После импорта WF-07, WF-10, WF-12 в n8n — вставить реальные ID в WF-06.

**Приоритет:** Средний.

---

## R-07: Buffer API — публикация не тестировалась

**Риск:** WF-11 вызывает Buffer API для публикации на LinkedIn/X/Threads. Buffer аккаунт и связанные профили не проверялись.

**Как исправить:** Запустить WF-11 вручную с тестовыми данными → проверить публикацию в Buffer dashboard.

**Приоритет:** Средний (проверить после R-01 решён).
