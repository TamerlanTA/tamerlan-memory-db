# Session 2026-04-24 — FlowOps Bot Complete Build

## Related
- [[projects/ai-content-bot]]
- [[current-focus]]

---

## What was done

### WF-06 — AI Agent Orchestrator (полная перестройка)
- Старый WF-06 был placeholder с ручным роутингом через Switch
- Перестроен как AI Agent: `@n8n/n8n-nodes-langchain.agent` v1.7
- Chat Model: GPT-4O (`@n8n/n8n-nodes-langchain.lmChatOpenAi` v1.3)
- Memory: `@n8n/n8n-nodes-langchain.memoryBufferWindow` v1.3, sessionKey = chat_id
- 6 инструментов через `toolWorkflow` v1.2:
  - `create_post` → WF-09 (`MfcnAfxzihlNKs42`)
  - `manage_post` → WF-10 (placeholder)
  - `run_topic_discovery` → WF-07 (placeholder)
  - `get_daily_report` → WF-12 (placeholder)
  - `show_outreach_queue` → WF-05 (`sgwBsMBN4eFvSh41`)
  - `generate_outreach` → WF-01 (`NfNDnPPVsrMuG4Qs`)
- Поток: Telegram Trigger → Extract Message (Code) → AI Agent → Send Response

### WF-05 — Gateway Pattern
- Telegram Trigger: убран `"message"`, остался только `"callback_query"`
- Route Request код обновлён: добавлена обработка `d.chat_id` (вызов от WF-06)
- Добавлен `executeWorkflowTrigger` как второй вход
- Файл: `WF-05 — Telegram Approval Queue.json` (пространство в имени!)

### executeWorkflowTrigger добавлен в:
- WF-01 (`NfNDnPPVsrMuG4Qs`) — рядом со Schedule 09:00, ведёт к Read Leads
- WF-07 — рядом со Schedule 07:00, ведёт ко всем 5 параллельным источникам
- WF-12 — рядом со Schedule 20:00, ведёт к Read Posts Sheet + Read Outreach Stats

### WF-07 — исправление Reddit 403
- Причина: Reddit блокирует n8n cloud IP при запросе JSON API
- Решение: заменены два HTTP Request на RSS Feed Read
- `Fetch Reddit r/artificial` → RSS: `https://www.reddit.com/r/artificial/top.rss?t=day&limit=10`
- `Fetch Reddit r/AINews` → RSS: `https://www.reddit.com/r/AINews/top.rss?t=day&limit=10`
- Normalize коды упрощены: читают `$json.title`, `$json.link` вместо `data.children[]`

### Google Apps Script
- Написан скрипт для создания листов Posts и Topics без удаления существующих данных
- Функция `ensureHeaders()` добавляет только отсутствующие колонки
- Запускать через Extensions → Apps Script в Google Sheets

---

## Key findings

- **n8n cloud IP блокируется Reddit JSON API** — использовать RSS вместо JSON для Reddit
- **toolWorkflow** требует реальный workflow ID, не имя — заменять плейсхолдеры после импорта
- **WF-05 Telegram Trigger** нужен для callback_query даже после введения WF-06 — кнопки идут напрямую
- **executeWorkflowTrigger** не требует активации sub-workflow — он только должен быть сохранён
- **WF-05 имеет пробел в имени файла** — `WF-05 — Telegram Approval Queue.json`

---

## Known IDs

| WF | n8n ID |
|---|---|
| WF-01 | `NfNDnPPVsrMuG4Qs` |
| WF-05 | `sgwBsMBN4eFvSh41` |
| WF-09 | `MfcnAfxzihlNKs42` |

---

## Remaining placeholders in WF-06

- `REPLACE_WITH_WF07_ID`
- `REPLACE_WITH_WF10_ID`
- `REPLACE_WITH_WF12_ID`

In WF-10: `REPLACE_WITH_WF11_ID`
In WF-09: `REPLACE_WITH_UNSPLASH_ACCESS_KEY`

---

## Next steps

1. Запустить Google Apps Script → Posts + Topics листы
2. Переимпортировать WF-05, WF-06, WF-07, WF-01, WF-12 в n8n
3. Скопировать ID WF-07, WF-10, WF-11, WF-12 → вставить в WF-06 и WF-10
4. Вставить Unsplash ключ в WF-09
5. Активировать WF-06, WF-05 в n8n
6. Тест: find topics → create post → approve/skip → отправка → stats
