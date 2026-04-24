# LinkedIn Outreach Automation (n8n)

## Related
- [[agent-memory]]
- [[current-focus]]

---

## Goal
Полная автоматизация LinkedIn outreach: поиск лидов → генерация персонализированных сообщений через Claude → ручное одобрение в Telegram → отправка через Sourcegeek → follow-up → мониторинг ответов → ежедневная статистика.

## Stack
- **n8n** (cloud: tamerlantt.app.n8n.cloud) — оркестратор всех воркфлоу
- **Google Sheets** — база данных (Leads, Queue, Stats)
- **Anthropic Claude** (claude-haiku) — генерация персонализированных сообщений
- **Sourcegeek** — отправка LinkedIn сообщений (заменил PhantomBuster)
- **Telegram Bot** — FlowOpsBot (@FlowOpstg_bot) — интерфейс одобрения
- **Apify** — скрапинг LinkedIn профилей (заменил PhantomBuster для поиска)

## Credentials (в n8n)
- Google Sheets: `vxM9FGPdxsweNDnl` — "Google Sheets account"
- Telegram: `P75Lp4hbDX3BOlkz` — "Telegram account"
- Sourcegeek: `zKALnECZoBSmtapY` — "Sourcegeek Credentials account"
- Google Sheet ID: `1LT3amafjv1YleUqeNtUc4jKLHWy_QXvharH34gf6zzU`
- Telegram chat ID: `405182031`
- Queue sheet gid: `766488070`

## Файлы
Все JSON воркфлоу лежат в `/Users/tamerlan/Desktop/linkedin automation/`
- `WF-00_Lead_Discovery.json` — Apify скрапинг лидов (понедельник 08:00)
- `WF-01_Daily_Outreach.json` — генерация сообщений + подготовка Queue (09:00 daily)
- `WF-02_Followup.json` — follow-up после принятия connection request (09:30 daily)
- `WF-03_Reply_Monitor.json` — мониторинг ответов каждые 2 часа
- `WF-04_Daily_Stats.json` — дневная статистика (20:00 daily)
- `WF-05_Telegram_Approval.json` — интерактивное одобрение через Telegram
- `create_sheets.gs` — Google Apps Script для создания таблицы

## Google Sheets структура
**Leads**: linkedin_url, first_name, last_name, company, title, industry, pain_point, status, replied, sent_date, followup_sent, tg_notified, updated_at
**Queue**: linkedin_url, full_name, company, title, message, type, queue_status, generated_at, subject, followup_subject, followup_message
**Stats**: date, total, sent, replied, followup_sent, converted, queued, new, reply_rate, conversion_rate

⚠️ **Queue нужно добавить 3 колонки**: `subject`, `followup_subject`, `followup_message` — ещё не добавлены

## WF-05 Telegram Approval — логика
- Пишешь "отправка" → бот показывает ПЕРВЫЙ pending лид с кнопками
- Нажал ✅ Отправить → Sourcegeek **Send Connection Request** → обновляет Queue (sent) + Leads (sent) → автоматически показывает следующий лид
- Нажал ⏭️ Пропустить → обновляет Queue (skip) → автоматически показывает следующий лид
- Очередь пуста → "🎉 Очередь пуста!"
- callback_data: `a` (approve) или `s` (skip) — без индекса, всегда берёт первый pending лид

## WF-01 — что генерируется
Промпт генерирует JSON с 4 полями:
```json
{
  "message": "connection request note, MAX 180 chars, mention company, hint automation, sign as Tamerlan",
  "followup_message": "follow-up after acceptance, max 80 words",
  "subject": "",
  "followup_subject": ""
}
```
Нода `Prepare Queue Row` — тип **Code** (не Set), парсит JSON с fallback на plain text.

## Ключевые технические решения
- Anthropic нода output path: `$json.output[0].content[0].text` (не `$json.content[0].text`)
- Set нода: spread operator `...($json)` не работает → использовать "Include Other Input Fields"
- Google Sheets update: `matchingColumns: ["linkedin_url"]` обязательно
- Telegram parse_mode: **HTML** (не Markdown — сообщения содержат спецсимволы)
- Apify возвращает `linkedinUrl`, `currentPositions[0].companyName/title`
- Sourcegeek: **Send Connection Request** (не sendMessage, не Recruiter InMail)
  - sendMessage — только 1st degree connections
  - Recruiter InMail — требует LinkedIn Recruiter (enterprise)
  - Connection Request — работает для всех, лимит 180 символов
- Answer Callback нода: должна вызываться ДО медленных операций (Sourcegeek + Sheets), иначе "query too old" (30 сек таймаут)
- `callbackQueryId` берётся из `$('Route Request').first().json.callbackQueryId` (не из дочерних нод)
- После каждого действия (approve/skip): re-read Queue → берём первый pending → показываем следующую карточку

## Статус (2026-04-24)
- WF-01: обновлён промпт (сообщение MAX 180 символов, 4 поля JSON), нода `Prepare Queue Row` переделана в Code ✅ (нужно импортировать в n8n)
- WF-05: переработан (цикличный режим, одна карточка, Sourcegeek = sendConnectionRequest) ✅ (нужно импортировать в n8n)
- WF-02 — WF-04: не трогались
- Sourcegeek: подключён по API, но аккаунт показывает ~20% setup → нужно завершить настройку (рабочие часы, кампания)

## Next Steps (приоритет)
1. **Импортировать WF-05** из `/Users/tamerlan/Desktop/linkedin automation/WF-05_Telegram_Approval.json` → деактивировать старый → активировать новый
2. **Импортировать WF-01** из `/Users/tamerlan/Desktop/linkedin automation/WF-01_Daily_Outreach.json` → деактивировать старый → активировать новый
3. **Добавить 3 колонки в Queue** (Google Sheets): `subject`, `followup_subject`, `followup_message`
4. **Завершить настройку Sourcegeek**: выставить рабочие часы → аккаунт станет активным
5. **Протестировать end-to-end**: WF-01 генерирует → Queue заполнена → WF-05 отправляет connection request через Sourcegeek
6. Настроить Apify actor для WF-00 (заменить `YOUR_APIFY_ACTOR_ID`)
7. Запустить в production (активировать все воркфлоу по расписанию)
