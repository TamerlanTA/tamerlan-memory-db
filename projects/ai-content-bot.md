# AI Content & Command Center Bot (Telegram)

## Related
- [[agent-memory]]
- [[current-focus]]
- [[projects/linkedin-automation]]

---

## Goal
Централизованный AI Telegram бот для управления всей автоматизацией с телефона:
- Запуск любого воркфлоу голосом/текстом
- Topic Discovery из множества источников
- AI генерация постов + визуала
- Публикация на LinkedIn, X, Threads
- Отчёты по всем таблицам
- Интеграция с существующим LinkedIn Outreach (WF-00..WF-05)

---

## Stack

- **n8n cloud** — `tamerlantt.app.n8n.cloud`
- **Telegram Bot** — FlowOpsBot (@FlowOpstg_bot) — единственный UI
- **GPT-4O (OpenAI)** — генерация контента + AI Agent мозг
  - credential ID: `6Te8klWgg2iLJPap`, name: "OpenAI account"
- **Google Sheets** — база данных
  - Spreadsheet ID: `1LT3amafjv1YleUqeNtUc4jKLHWy_QXvharH34gf6zzU`
  - credential ID: `vxM9FGPdxsweNDnl`, name: "Google Sheets account"
  - Sheets: Leads, Queue, Stats (существующие) + Posts, Topics (новые)
- **Buffer** — публикация на LinkedIn + X + Threads
  - API key: `90ofhUZVEdo_z5oOa60G3yd-CYTus7JQ8UZDIGr3b9W`
  - Endpoint: `https://api.bufferapp.com/1/updates/create.json`
- **Unsplash API** — stock фото (нужен API ключ — placeholder в WF-09)
- **Telegram Bot** — credential ID: `P75Lp4hbDX3BOlkz`, name: "Telegram account"
- **Sourcegeek** — LinkedIn connection requests — credential ID: `zKALnECZoBSmtapY`

---

## Архитектура (финальная)

```
Telegram сообщение → WF-06 AI Agent (GPT-4O)
  ├─ create_post          → WF-09 Content Generation
  ├─ manage_post          → WF-10 Post Approval → WF-11 Publishing
  ├─ run_topic_discovery  → WF-07 Topic Discovery
  ├─ get_daily_report     → WF-12 Stats Collection
  ├─ show_outreach_queue  → WF-05 Telegram Approval Queue
  └─ generate_outreach    → WF-01 Daily Outreach

Кнопки ✅/⏭️ → callback_query → WF-05 Telegram Trigger (напрямую)

Автоматически по расписанию:
  07:00 → WF-07 Topic Discovery
  08:00 → WF-08 Morning Briefing (топ-5 тем в Telegram)
  09:00 → WF-01 Daily Outreach (генерация сообщений)
  20:00 → WF-12 Stats Collection (дневной отчёт)
  Пн 08:00 → WF-00 Lead Discovery (PhantomBuster)
```

---

## Воркфлоу — статус и ID

| WF | Название | Файл | n8n ID | Триггеры | Статус |
|---|---|---|---|---|---|
| WF-00 | Lead Discovery | `WF-00_Lead_Discovery.json` | неизвестен | Schedule Пн 08:00 | ✅ работает |
| WF-01 | Daily Outreach | `WF-01_Daily_Outreach.json` | `NfNDnPPVsrMuG4Qs` | Schedule 09:00 + executeWorkflow | ✅ обновлён |
| WF-02 | Followup | `WF-02_Followup.json` | неизвестен | — | не трогали |
| WF-03 | Reply Monitor | `WF-03_Reply_Monitor.json` | неизвестен | — | не трогали |
| WF-04 | Daily Stats | `WF-04_Daily_Stats.json` | неизвестен | — | не трогали |
| WF-05 | Telegram Approval Queue | `WF-05 — Telegram Approval Queue.json` | `sgwBsMBN4eFvSh41` | Telegram (callback_query только!) + executeWorkflow | ✅ обновлён |
| WF-06 | AI Command Center | `WF-06_AI_Command_Center.json` | неизвестен | Telegram (message) | ✅ перестроен как AI Agent |
| WF-07 | Topic Discovery | `WF-07_Topic_Discovery.json` | неизвестен | Schedule 07:00 + executeWorkflow | ✅ исправлен (RSS вместо HTTP) |
| WF-08 | Morning Briefing | `WF-08_Morning_Briefing.json` | неизвестен | Schedule 08:00 | ✅ построен |
| WF-09 | Content Generation | `WF-09 Content Generation.json` | `MfcnAfxzihlNKs42` | executeWorkflow | ✅ построен |
| WF-10 | Post Approval | `WF-10_Post_Approval.json` | неизвестен | executeWorkflow | ✅ построен |
| WF-11 | Publishing | `WF-11_Publishing.json` | неизвестен | executeWorkflow | ✅ построен |
| WF-12 | Stats Collection | `WF-12_Stats_Collection.json` | неизвестен | Schedule 20:00 + executeWorkflow | ✅ обновлён |

Все файлы: `/Users/tamerlan/Desktop/linkedin automation/`

---

## WF-06 — AI Agent детали

- **Тип агента:** `@n8n/n8n-nodes-langchain.agent` typeVersion 1.7
- **Chat Model:** `@n8n/n8n-nodes-langchain.lmChatOpenAi` v1.3, GPT-4O
- **Memory:** `@n8n/n8n-nodes-langchain.memoryBufferWindow` v1.3, sessionKey = chat_id
- **Tools:** `@n8n/n8n-nodes-langchain.toolWorkflow` v1.2

| Tool | WF ID | Статус |
|---|---|---|
| create_post | `MfcnAfxzihlNKs42` | ✅ реальный ID |
| manage_post | `REPLACE_WITH_WF10_ID` | ⏳ заменить после импорта |
| run_topic_discovery | `REPLACE_WITH_WF07_ID` | ⏳ заменить после импорта |
| get_daily_report | `REPLACE_WITH_WF12_ID` | ⏳ заменить после импорта |
| show_outreach_queue | `sgwBsMBN4eFvSh41` | ✅ реальный ID |
| generate_outreach | `NfNDnPPVsrMuG4Qs` | ✅ реальный ID |

---

## WF-05 — важные изменения

- Telegram Trigger изменён: `["message", "callback_query"]` → `["callback_query"]` только
- Route Request код обновлён: текстовые сообщения убраны, добавлена обработка вызова от WF-06 через `d.chat_id`
- Добавлен `executeWorkflowTrigger` как второй вход
- **Причина:** WF-06 теперь единственный вход для текстовых сообщений. WF-05 нужен только для кнопок.

---

## WF-07 — исправление Reddit

- **Проблема:** Reddit блокирует HTTP Request с n8n cloud IP (403 Forbidden)
- **Решение:** Заменены `Fetch Reddit r/artificial` и `Fetch Reddit r/AINews` с `httpRequest` на `rssFeedRead`
- URLs: `https://www.reddit.com/r/artificial/top.rss?t=day&limit=10`
- Normalize коды упрощены под RSS формат (title, link вместо data.children)

---

## Плейсхолдеры — что нужно заменить после импорта

| Файл | Плейсхолдер | Что вставить |
|---|---|---|
| WF-06_AI_Command_Center.json | `REPLACE_WITH_WF07_ID` | ID WF-07 после импорта |
| WF-06_AI_Command_Center.json | `REPLACE_WITH_WF10_ID` | ID WF-10 после импорта |
| WF-06_AI_Command_Center.json | `REPLACE_WITH_WF12_ID` | ID WF-12 после импорта |
| WF-09 Content Generation.json | `REPLACE_WITH_UNSPLASH_ACCESS_KEY` | Unsplash API ключ |
| WF-10_Post_Approval.json | `REPLACE_WITH_WF11_ID` | ID WF-11 после импорта |
| WF-07_Topic_Discovery.json | `REPLACE_WITH_FIRECRAWL_CREDENTIAL_ID` | ID credential Firecrawl API в n8n (оба Reddit узла) |

---

## Google Sheets — структура

**Существующие (не трогать):**
- `Leads` (gid=0) — LinkedIn лиды
- `Queue` (gid=766488070) — очередь отправки
- `Stats` (gid=1974636481) — outreach статистика

**Новые (создать скриптом):**
- `Posts` — `post_id, date, topic, source, linkedin_text, twitter_text, threads_text, image_url, image_type, status, scheduled_at, published_at`
- `Topics` — `date, source, headline, url, score, status`

Google Apps Script для создания листов написан — запустить через Extensions → Apps Script в таблице.

---

## Что нужно активировать в n8n (Published = ON)

| WF | Причина |
|---|---|
| WF-06 | Telegram trigger — главный вход |
| WF-05 | Telegram trigger — callback_query кнопки |
| WF-00 | Schedule |
| WF-01 | Schedule |
| WF-07 | Schedule |
| WF-08 | Schedule |
| WF-12 | Schedule |

WF-09, WF-10, WF-11 — только сохранить, активировать не нужно.

---

## Параметры контента

- **Язык:** английский
- **Тон:** живой, личный, от первого лица (Tamerlan)
- **Ниша:** AI автоматизация бизнеса, n8n, продуктивность
- **Платформы:** LinkedIn + Twitter/X + Threads
- **Одобрение:** всегда ручное перед публикацией

---

## Статус (2026-04-24)

**Завершено:**
- ✅ WF-06 перестроен как AI Agent с 6 инструментами (GPT-4O + Memory + toolWorkflow)
- ✅ WF-05 обновлён: убран текстовый trigger, добавлен executeWorkflowTrigger
- ✅ WF-01, WF-07, WF-12 получили executeWorkflowTrigger
- ✅ WF-07 исправлен: Reddit JSON API → RSS Feed
- ✅ Google Apps Script для создания листов Posts и Topics написан
- ✅ Все реальные workflow IDs вставлены в WF-06 где известны

**Ожидает:**
- ⏳ Импорт WF-06..WF-12 в n8n и замена оставшихся плейсхолдеров
- ⏳ Вставить Unsplash API ключ в WF-09
- ⏳ Запустить Google Apps Script для создания листов
- ✅ WF-07 Score Topics (эвристический скоринг по нише)
- ✅ WF-07 Clear Topics Sheet (очистка перед каждым запуском)
- ✅ WF-09 Mark Topic Used (статус → used при создании поста)
- ⏳ Тестирование всех функций бота
- ⏳ Активировать нужные воркфлоу в n8n

---

## Next Steps

1. Запустить Google Apps Script → создать Posts и Topics листы
2. Импортировать обновлённые файлы WF-05, WF-06, WF-07, WF-01, WF-12 в n8n
3. После импорта — скопировать реальные ID WF-07, WF-10, WF-11, WF-12 и заменить плейсхолдеры в WF-06 и WF-10
4. Добавить Unsplash API ключ в WF-09 (нода Fetch Unsplash Image)
5. Активировать WF-06 и WF-05 в n8n
6. Протестировать по чеклисту: find topics → create post → show post → skip → отправка → stats
