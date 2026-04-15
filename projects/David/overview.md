# Make-David — Overview

## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]

---

## Goal
Автоматизировать отправку WhatsApp шаблонных сообщений из Google Sheets через SellerChat + обработка входящих WhatsApp-сообщений AI-ботом для фотомульт (штрафов ПДД) в Колумбии.

## Client / Owner
**David** — клиент. Три пользователя системы: David, Lilia, Lyan.

## Business Context
- Юридическая/административная ниша (Колумбия, +57)
- Рабочий процесс: Когда в Google Sheets клетка становится "yes" → отправить WhatsApp-шаблон через SellerChat
- Параллельно: входящие WhatsApp-сообщения → AI-бот анализирует фотомульты, взаимодействует с Kommo CRM, хранит историю разговоров

## Architecture (high-level)
```
Google Sheets (onEdit trigger)
  → Apps Script webhook
    → Make.com scenario
      → SellerChat API (sends WhatsApp template)
        → Data Store (log success/failure)

WhatsApp incoming
  → n8n main workflow
    → Redis (buffer) + Supabase (persistence)
    → AI analysis (OpenAI/Claude)
    → Kommo CRM (contact lookup)
    → sub-scrape + sub-save (fotomultas)
    → Response via WhatsApp
```

## Tech Stack
| Layer | Technology |
|---|---|
| Spreadsheet trigger | Google Apps Script |
| Integration hub | Make.com (Integromat) |
| Bot orchestration | n8n |
| Messaging | WhatsApp API + SellerChat |
| CRM | Kommo |
| Cache / session | Redis |
| Database | Supabase (PostgreSQL) |
| AI | OpenAI / Claude |
| Data | Google Sheets |

## Files in Repo (`/Users/tamerlan/Desktop/PC/Make-David/`)
| File | Purpose | Status |
|---|---|---|
| `sellerchat_sheet_trigger.gs` | Google Apps Script — trigger onEdit, send webhook | ✅ Production-ready |
| `MAKE_SCENARIO.md` | Architecture blueprint for Make.com scenario | ✅ Designed, ⚠️ Not yet built in Make UI |
| `WhatsApp AI Bot - Fotomultas v3 con Buffer from scratch.json` | Main n8n workflow (128 nodes) | ✅ Built |
| `agendar-reminder.json` | Reminder scheduling workflow | ✅ Built |
| `sub-scrape.json` | Web scraping sub-workflow | ✅ Built |
| `sub-save.json` | Data persistence sub-workflow | ✅ Built (with some TODOs) |
| `kommo_export_leads_2026-03-19.csv` | CRM leads export (54k+ leads) | Data file |
| `template changing.mov` | Demo video | Reference |

## Users / Accounts
| Profile | SellerChat Account | Sheets mapped |
|---|---|---|
| David | davidreav@gmail.com | 8 spreadsheets |
| Lilia | liliarappi1@gmail.com | 1 spreadsheet |
| Lyan | lyancolombiasas@gmail.com | 1 spreadsheet |

## WhatsApp Templates (SellerChat)
- `listo_derecho_de_peticion_revisar_correo`
- `listo_radicado_revisar_correo`

## Trigger Columns per Profile
| Profile | Template 1 column | Template 2 column |
|---|---|---|
| David | S | T |
| Lilia | T | U |
| Lyan | Q | R |
