# Make-David — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Status: Pre-production / Staging

### ✅ Done
- **Google Apps Script** (`sellerchat_sheet_trigger.gs`) — 553 строки, production-ready
  - onEdit trigger, multi-profile (David/Lilia/Lyan), нормализация номеров, retry logic
  - 10 spreadsheets сконфигурированы (8 David, 1 Lilia, 1 Lyan)
- **n8n Main Workflow** (128 nodes) — WhatsApp AI-бот обработки фотомульт
  - Redis-буфер, Supabase persistence, AI analysis, Kommo integration
- **n8n Sub-workflows** — sub-scrape (веб-скрапинг), sub-save (сохранение данных)
- **Reminder workflow** — планирование напоминаний через Supabase + hourly schedule
- **Architecture design** — Make.com сценарий полностью задокументирован в MAKE_SCENARIO.md

### ⚠️ Pending / Incomplete
- **Make.com сценарий** — НЕ создан в Make UI. Только документация есть.
  - Нужно вручную создать ~20+ модулей (webhook, router, 6 SellerChat routes, data stores)
- **sub-save.json** — есть несколько TODO sticky notes, некоторые edge cases не закрыты
- **SellerChat template mapping** — переменные шаблонов не полностью задокументированы
- **Тестирование** — нет тест-кейсов, только видео-демо

### 🔧 Known Issues / TODOs
- Hardcoded API keys / URLs в workflows (нет разделения на env variables)
- Profile overrides захардкожены в Apps Script (сложно поддерживать)
- Debounce logic в n8n workflow может иметь edge cases
- Нет мониторинга / дашборда для tracking sent/failed messages

## Data
- Kommo leads export: 54k+ записей (kommo_export_leads_2026-03-19.csv)

## Last Updated
2026-04-15
