# AI Content Bot — Overview

## Related
- [[projects/ai-content-bot/current-state]]
- [[projects/ai-content-bot/decisions]]
- [[projects/ai-content-bot/risks]]
- [[projects/ai-content-bot/next-steps]]
- [[projects/linkedin-automation|LinkedIn Outreach (WF-00..WF-05)]]
- [[agent-memory]]

---

## Goal
Централизованный AI Telegram бот (@FlowOpstg_bot) для управления всей автоматизацией с телефона:
- Голосом / текстом запускать любой воркфлоу
- Topic Discovery из множества источников (RSS, Reddit, HN)
- AI генерация постов (LinkedIn + X + Threads) с изображениями через Gemini
- Ручное одобрение через Telegram inline кнопки перед публикацией
- Публикация через Buffer API
- Отчёты по всем таблицам
- Интеграция с LinkedIn Outreach (WF-00..WF-05)

---

## Stack

| Компонент | Значение |
|---|---|
| **Платформа** | n8n cloud — `tamerlantt.app.n8n.cloud` |
| **Telegram Bot** | @FlowOpstg_bot, credential ID: `P75Lp4hbDX3BOlkz` |
| **AI (текст)** | GPT-4O через n8n LangChain ноду, credential ID: `6Te8klWgg2iLJPap` |
| **AI (изображения)** | Gemini 3 Nano Banana Pro — `gemini-3-pro-image-preview` |
| **Google Sheets** | Spreadsheet ID: `1LT3amafjv1YleUqeNtUc4jKLHWy_QXvharH34gf6zzU`, credential: `vxM9FGPdxsweNDnl` |
| **Buffer** | API key: `90ofhUZVEdo_z5oOa60G3yd-CYTus7JQ8UZDIGr3b9W`, endpoint: `https://api.bufferapp.com/1/updates/create.json` |
| **Gemini API key** | `AIzaSyAwEtVjuIg5HkkcZ-TM9SpKDjmmgY_sC_o` (проект 1053960890982, Google AI Pro подписка) |
| **Telegram chat ID** | `405182031` |

---

## Архитектура

```
Telegram сообщение → WF-06 AI Agent (GPT-4O)
  ├─ IF: Is Callback? → True → Forward to WF-05 (callback_query)
  └─ False → Extract Message → AI Agent
       ├─ create_post          → WF-09 Content Generation
       ├─ manage_post          → WF-10 Post Approval
       ├─ run_topic_discovery  → WF-07 Topic Discovery
       ├─ get_daily_report     → WF-12 Stats Collection
       ├─ show_outreach_queue  → WF-05 Telegram Approval Queue
       └─ generate_outreach    → WF-01 Daily Outreach

Кнопки ✅/⏭️ (callback_query) → WF-06 → IF: Is Callback? → Forward to WF-05
  → WF-05 → Call WF-10 (action: approve/skip)

Автоматически по расписанию:
  07:00 → WF-07 Topic Discovery
  08:00 → WF-08 Morning Briefing
  09:00 → WF-01 Daily Outreach
  20:00 → WF-12 Stats Collection
  Пн 08:00 → WF-00 Lead Discovery
```

**Критическое ограничение n8n:** Только ОДИН активный Telegram Trigger на бота. WF-06 ловит ВСЕ типы обновлений (`message` + `callback_query`) и роутит внутри.

---

## Воркфлоу — ID и файлы

| WF | Название | Файл | n8n ID | Статус |
|---|---|---|---|---|
| WF-00 | Lead Discovery | `WF-00_Lead_Discovery.json` | неизвестен | ✅ работает |
| WF-01 | Daily Outreach | `WF-01_Daily_Outreach.json` | `NfNDnPPVsrMuG4Qs` | ✅ |
| WF-05 | Telegram Approval Queue | `WF-05 — Telegram Approval Queue.json` | `sgwBsMBN4eFvSh41` | ✅ |
| WF-06 | AI Command Center | `WF-06_AI_Command_Center.json` | неизвестен | ✅ (обновлён callback routing) |
| WF-07 | Topic Discovery | `WF-07_Topic_Discovery.json` | неизвестен | ✅ (RSS вместо Reddit HTTP) |
| WF-08 | Morning Briefing | `WF-08_Morning_Briefing.json` | неизвестен | ✅ |
| WF-09 | Content Generation | `WF-09 Content Generation.json` | `MfcnAfxzihlNKs42` | ✅ (Gemini image gen) |
| WF-10 | Post Approval | `WF-10_Post_Approval.json` | неизвестен | ⚠️ (кнопки добавлены, WF-11 ID нужен) |
| WF-11 | Publishing | `WF-11_Publishing.json` | **⏳ НУЖЕН** | ✅ (код готов) |
| WF-12 | Stats Collection | `WF-12_Stats_Collection.json` | неизвестен | ✅ |

Все файлы: `/Users/tamerlan/Desktop/linkedin automation/`

---

## Google Sheets структура

**Существующие:** `Leads` (gid=0), `Queue` (gid=766488070), `Stats` (gid=1974636481)

**Новые (нужно создать через Apps Script):**
- `Posts` — `post_id, date, topic, source, linkedin_text, twitter_text, threads_text, image_url, image_type, status, scheduled_at, published_at`
- `Topics` — `date, source, headline, url, score, status`
