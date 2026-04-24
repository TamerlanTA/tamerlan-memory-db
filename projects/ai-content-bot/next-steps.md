# AI Content Bot — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

---

## Приоритет 1 — Разблокировать публикацию

1. **Получить ID WF-11** в n8n:
   - Открыть WF-11 в n8n → скопировать ID из URL
   - Заменить `REPLACE_WITH_WF11_ID` в `WF-10_Post_Approval.json` → нода `Trigger WF-11 Publish`
   - Переимпортировать WF-10 в n8n

2. **Импортировать / обновить WF-06 в n8n** (добавлен IF: Is Callback? + callback_query routing)

3. **Импортировать / обновить WF-10 в n8n** (добавлены inline keyboard кнопки)

---

## Приоритет 2 — Инфраструктура

4. **Создать Posts и Topics листы** в Google Sheets:
   - Открыть таблицу → Extensions → Apps Script → запустить скрипт

5. **Заменить оставшиеся плейсхолдеры в WF-06**:
   - После импорта WF-07, WF-10, WF-12 → вставить реальные ID
   - `REPLACE_WITH_WF07_ID`, `REPLACE_WITH_WF10_ID`, `REPLACE_WITH_WF12_ID`

---

## Приоритет 3 — Тест флоу

6. **Тестировать полный флоу:**
   - Написать боту "create post about AI automation"
   - Дождаться генерации → получить превью с кнопками
   - Нажать ✅ Publish → проверить что WF-05 → WF-10 (approve) → WF-11 отработали
   - Проверить публикацию в Buffer dashboard

7. **Протестировать Gemini изображения** с новым API ключом

8. **Проверить Buffer аккаунт** — связанные профили LinkedIn / X / Threads

---

## Приоритет 4 — Активация по расписанию

9. Активировать воркфлоу по расписанию:
   - WF-06 (Telegram trigger) ✅
   - WF-05 (callback_query) ✅
   - WF-07 (07:00 Topic Discovery)
   - WF-08 (08:00 Morning Briefing)
   - WF-01 (09:00 Outreach)
   - WF-12 (20:00 Stats)
   - WF-00 (Пн 08:00 Lead Discovery)

---

## Низкий приоритет

- Вставить Unsplash API ключ в WF-09 (`REPLACE_WITH_UNSPLASH_ACCESS_KEY`)
- Добавить Firecrawl credential в WF-07 (`REPLACE_WITH_FIRECRAWL_CREDENTIAL_ID`)
- Настроить WF-02 (Followup) и WF-03 (Reply Monitor)
