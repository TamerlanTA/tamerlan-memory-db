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
- `WF-01_Daily_Outreach.json` — генерация сообщений через Claude (09:00 daily)
- `WF-02_Followup.json` — follow-up для лидов без ответа 3+ дня (09:30 daily)
- `WF-03_Reply_Monitor.json` — мониторинг ответов каждые 2 часа
- `WF-04_Daily_Stats.json` — дневная статистика (20:00 daily)
- `WF-05_Telegram_Approval.json` — интерактивное одобрение через Telegram
- `create_sheets.gs` — Google Apps Script для создания таблицы

## Google Sheets структура
**Leads**: linkedin_url, first_name, last_name, company, title, industry, pain_point, status, replied, sent_date, followup_sent, tg_notified, updated_at
**Queue**: linkedin_url, full_name, company, title, message, type, queue_status, generated_at
**Stats**: date, total, sent, replied, followup_sent, converted, queued, new, reply_rate, conversion_rate

## WF-05 Telegram Approval — логика
- Пишешь "отправка" → бот показывает ПЕРВЫЙ pending лид с кнопками
- Нажал ✅ Отправить → Sourcegeek отправляет LinkedIn сообщение → обновляет Queue (sent) + Leads (sent) → автоматически показывает следующий лид
- Нажал ⏭️ Пропустить → обновляет Queue (skip) → автоматически показывает следующий лид
- Очередь пуста → "🎉 Очередь пуста!"
- callback_data: `a` (approve) или `s` (skip) — без индекса, всегда берёт первый pending лид

## Ключевые технические решения
- Anthropic нода output path: `$json.output[0].content[0].text` (не `$json.content[0].text`)
- Set нода: spread operator `...($json)` не работает → использовать "Include Other Input Fields"
- Google Sheets update: `matchingColumns: ["linkedin_url"]` обязательно
- Telegram parse_mode HTML безопаснее Markdown (сообщения содержат спецсимволы)
- Apify возвращает `linkedinUrl`, `currentPositions[0].companyName/title`
- Sourcegeek нода: `operation: sendMessage`, поля `linkedinUrl` + `message`

## Статус (2026-04-23)
- WF-01 — WF-04 работают ✅
- WF-05 переработан: одна карточка за раз + автоцикл после каждого действия ✅
- Sourcegeek подключён ✅
- Лиды тестировались на реальных данных (Matt Silk, COY Creator)

## Next Steps
1. Импортировать обновлённый WF-05 (цикличный режим) и протестировать
2. Убедиться что Sourcegeek реально отправляет сообщения в LinkedIn
3. Настроить Apify actor для WF-00 (заменить YOUR_APIFY_ACTOR_ID)
4. Запустить в production режиме (активировать все воркфлоу)
