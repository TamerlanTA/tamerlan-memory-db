# 🗃️ CRM Tables

#flowops #crm #structure

> Структура всех таблиц для отслеживания лидов, возможностей, сообщений и демо.

---

## Таблица 1 — Leads (Лиды)

Основная таблица. Каждый потенциальный клиент — отдельная запись.

| Поле | Тип | Описание |
|------|-----|----------|
| Lead name | Text | Имя контакта |
| Company | Text | Название компании |
| Website | URL | Сайт компании |
| Source | Select | Upwork / LinkedIn / Cold email / Referral / Inbound |
| Niche | Select | Real estate / Agency / E-commerce / Clinic / SaaS / Other |
| Pain signal | Text | Что именно сказали / написали о боли |
| Offer match | Select | Speed-to-Lead / Ops Sprint / AI Chatbot / Audit |
| Fit score | Number | 1–10 |
| Budget estimate | Text | Примерный бюджет |
| Contact URL | URL | Ссылка на профиль (LinkedIn / Upwork) |
| Email | Email | Email адрес |
| LinkedIn | URL | LinkedIn профиль |
| Status | Select | New → Contacted → Replied → Call Booked → Proposal Sent → Won → Lost |
| Next action | Text | Что нужно сделать следующим |
| Last contacted | Date | Дата последнего касания |
| Follow-up date | Date | Когда следующее касание |
| Notes | Long text | Любые заметки |

---

## Таблица 2 — Opportunities (Возможности)

Детальное описание автоматизации для каждого лида.

| Поле | Тип | Описание |
|------|-----|----------|
| Lead | Link | Связь с таблицей Leads |
| Automation opportunity | Text | Название идеи |
| Problem | Text | Конкретная проблема |
| Suggested workflow | Long text | Как будет работать автоматизация |
| Tools needed | Text | n8n, Make, OpenAI, HubSpot, etc. |
| Estimated value | Number | Сколько стоит проблема для клиента ($) |
| Build price | Number | Сколько мы берём за разработку |
| Retainer potential | Select | High / Medium / Low / None |

---

## Таблица 3 — Messages (Сообщения)

История всех коммуникаций с каждым лидом.

| Поле | Тип | Описание |
|------|-----|----------|
| Lead | Link | Связь с таблицей Leads |
| Channel | Select | Upwork / LinkedIn / Email / WhatsApp / Call |
| Message type | Select | Proposal / DM / Cold email / Follow-up / Retainer pitch |
| Draft | Long text | Текст сообщения |
| Sent? | Checkbox | Отправлено или нет |
| Response? | Select | No response / Replied / Interested / Not interested |
| Follow-up date | Date | Когда следующий контакт |

---

## Таблица 4 — Demos (Демо)

Библиотека демо-видео для использования в продажах.

| Поле | Тип | Описание |
|------|-----|----------|
| Demo name | Text | Название демо |
| Niche | Select | Для какой ниши |
| Problem solved | Text | Какую боль решает |
| Loom URL | URL | Ссылка на видео |
| Relevant offer | Link | Связь с оффером |
| When to use | Text | В каком контексте использовать |

---

## Статусы лидов (воронка)

```
New
  ↓
Contacted (отправили первое сообщение)
  ↓
Replied (ответил)
  ↓
Call Booked (записался на звонок)
  ↓
Proposal Sent (отправили предложение/скоп)
  ↓
Won ✅ / Lost ❌
```

---

## KPI для отслеживания

| Метрика | Цель |
|---------|------|
| Новых лидов в неделю | 50–100 |
| Conversion Contacted → Replied | > 10% |
| Conversion Replied → Call | > 30% |
| Conversion Call → Won | > 40% |
| MRR из ретейнеров | $5,000+ |

---

## Инструменты для CRM

- **Airtable** — лучший вариант для начала (гибкие таблицы + автоматизации)
- **Notion** — если уже используешь для заметок
- **HubSpot Free** — если нужен более "продажный" интерфейс

---

## Связанные страницы

- [[Sales Steps]] — статусы и шаги продаж
- [[Pipeline A — Upwork Radar]] — источник лидов
- [[Pipeline B — LinkedIn Pain Radar]] — источник лидов
- [[Pipeline D — Demo Library]] — таблица Demos
- [[What to Do First]] — приоритеты

---

*#flowops #crm #structure*
