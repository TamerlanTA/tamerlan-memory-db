# FlowOps SaaS — Pipeline Catalog

## Related
- [[overview]]
- [[pricing]]
- [[technical-architecture]]
- [[automation-card-audit-brief]]

---

## Pipeline Categories

### 1. Lead & Sales (8 pipelines)
### 2. Support & Communication (6 pipelines)
### 3. Voice & Calls (5 pipelines)
### 4. Operations (6 pipelines)
### 5. CRM & Data (5 pipelines)
### 6. Reporting & Intelligence (5 pipelines)
### 7. Marketing & Content (5 pipelines)

**Total: 40 pipelines**

---

## Card Quality Standard (Added 2026-06-30)

Before scaled outreach, all live and coming-soon pipeline cards must be audited against [[automation-card-audit-brief]].

Each card should include or support:
- clear target buyer and best-fit verticals;
- concrete business pain;
- trigger → automation steps → result;
- richer 2–3 sentence description;
- typical integrations;
- setup scope;
- monthly monitoring/support scope;
- deploy time;
- setup and monthly price with rationale;
- realistic outcome/ROI logic;
- in-card illustration key/concept.

Descriptions that only say a workflow "routes requests", "answers questions", or "keeps response times tight" are too sparse for sales validation. Each card must make the buyer think: "this is my exact operational problem."

Visuals must follow the FlowOps workflow SVG style: light canvas, white rounded nodes, soft shadows, dotted connectors, small icons/status chips, and sky/mint/peach/amber accents. Reference files:
- `/Users/tamerlan/Downloads/flowops-custom-workflow.svg`
- `/Users/tamerlan/Downloads/flowops-request-to-proof-v2_1.svg`
- `/Users/tamerlan/Downloads/flowops-request-to-proof.svg`

---

## Category 1: Lead & Sales

### 1.1 LeadOS — Lead Research Pipeline
**Problem**: Команда тратит часы на ручной поиск и квалификацию лидов.
**What it does**: Автоматически ищет, обогащает и скорит потенциальных клиентов по заданным критериям. Создаёт карточки в CRM, уведомляет менеджера.
**Best for**: B2B продажи, агентства, SaaS
**Integrations**: Apollo/Hunter, LinkedIn, CRM (HubSpot/Pipedrive/Airtable), Slack/Telegram
**Setup**: $599 | **Monthly**: from $149
**Deploy time**: 3–5 days
**Related**: CRM Follow-up Pipeline, Cold Email Pipeline, CRMOS

---

### 1.2 CRM Follow-up Pipeline
**Problem**: Лиды падают в CRM и не получают вовремя follow-up. Сделки умирают.
**What it does**: Отслеживает статус лидов в CRM, триггерит автоматические follow-up по email/WhatsApp/SMS через нужные интервалы.
**Best for**: Sales teams, real estate, services
**Integrations**: HubSpot / Pipedrive / Airtable, WhatsApp, Gmail, Telegram
**Setup**: $549 | **Monthly**: from $149
**Deploy time**: 3–5 days

---

### 1.3 Cold Email Pipeline
**Problem**: Холодные email-кампании делаются вручную, нет персонализации.
**What it does**: Автоматически генерирует персонализированные cold email-последовательности, отправляет, трекает opens/replies, создаёт задачи в CRM.
**Best for**: B2B outreach, agencies, SaaS
**Integrations**: Apollo/Instantly/Lemlist, Gmail/SMTP, CRM
**Setup**: $699 | **Monthly**: from $149
**Deploy time**: 4–6 days

---

### 1.4 Pipeline Recovery Pipeline
**Problem**: Зависшие сделки в воронке теряются. Менеджеры забывают вернуться.
**What it does**: Сканирует CRM на "зависшие" сделки (no activity > N дней), создаёт задачи для менеджера, запускает re-engagement последовательность.
**Best for**: Real estate, services, B2B
**Integrations**: CRM, Slack/Telegram
**Setup**: $499 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 1.5 Proposal Automation Pipeline
**Problem**: Коммерческие предложения делаются вручную, занимают 1–2 часа каждое.
**What it does**: Собирает данные из CRM/формы, генерирует структурированное КП по шаблону (AI-assisted), отправляет клиенту, трекает статус.
**Best for**: Agencies, consultants, B2B services
**Integrations**: CRM, Google Docs/Notion, Gmail
**Setup**: $999 | **Monthly**: from $199
**Deploy time**: 5–7 days

---

### 1.6 Sales Call Summary Pipeline
**Problem**: После созвонов нет структурированных записей. Инсайты теряются.
**What it does**: Транскрибирует звонок, генерирует summary (проблема / решение / следующий шаг), создаёт задачи в CRM, уведомляет менеджера.
**Best for**: Sales teams, consultants
**Integrations**: Zoom/Google Meet/Fireflies, CRM, Slack
**Setup**: $899 | **Monthly**: from $199
**Deploy time**: 4–5 days

---

### 1.7 Lead Qualification Pipeline
**Problem**: SDR тратят время на неквалифицированных лидов.
**What it does**: Автоматически скорит входящих лидов по ICP-критериям, маршрутизирует к нужному менеджеру, отправляет приветственное сообщение.
**Best for**: B2B с высоким объёмом входящих
**Integrations**: Website forms, CRM, Slack/Telegram
**Setup**: $599 | **Monthly**: from $149
**Deploy time**: 3–5 days

---

### 1.8 Referral Tracking Pipeline
**Problem**: Реферальные клиенты не отслеживаются системно.
**What it does**: Создаёт уникальные реферальные ссылки, трекает конверсии, начисляет бонусы, уведомляет рефераллов.
**Best for**: Services, SaaS, real estate
**Integrations**: Website, CRM, Email
**Setup**: $699 | **Monthly**: from $149
**Deploy time**: 4–6 days

---

## Category 2: Support & Communication

### 2.1 InboxOS — Support Inbox Automation
**Problem**: Входящие запросы клиентов обрабатываются медленно и непоследовательно.
**What it does**: Классифицирует входящие сообщения (email/chat), маршрутизирует к нужному агенту, создаёт тикеты, отправляет автоответ клиенту.
**Best for**: E-commerce, SaaS, services с высоким объёмом support
**Integrations**: Gmail/Help Scout/Intercom, Slack/Telegram, CRM
**Setup**: $649 | **Monthly**: from $149
**Deploy time**: 3–5 days

---

### 2.2 AI Customer Support Assistant
**Problem**: Поддержка отвечает на одни и те же вопросы часами.
**What it does**: AI-агент отвечает на FAQ автоматически, эскалирует сложные случаи человеку, учится на предыдущих ответах.
**Best for**: E-commerce, SaaS, clinics
**Integrations**: Email/Chat widget/Telegram, Knowledge base
**Setup**: $1,099 | **Monthly**: from $199
**Deploy time**: 5–7 days

---

### 2.3 WhatsApp Lead Reply Pipeline
**Problem**: Входящие WhatsApp-запросы от лидов остаются без ответа часами.
**What it does**: Автоматически отвечает на входящие WhatsApp-сообщения, квалифицирует лида, записывает в CRM, уведомляет менеджера.
**Best for**: Real estate, clinics, local services
**Integrations**: WhatsApp Business API, CRM, Telegram
**Setup**: $499 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 2.4 Telegram Bot Intake Pipeline
**Problem**: Нет удобного канала для входящих запросов от клиентов.
**What it does**: Telegram-бот принимает заявки, квалифицирует по скрипту, создаёт лида в CRM, уведомляет команду.
**Best for**: Local businesses, services, clinics
**Integrations**: Telegram Bot API, CRM, Airtable
**Setup**: $499 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 2.5 FAQ Automation Pipeline
**Problem**: Одни и те же вопросы забивают поддержку.
**What it does**: Автоматически отвечает на частые вопросы через email/chat/Telegram, перенаправляет сложные случаи.
**Best for**: Any business с высоким FAQ-объёмом
**Integrations**: Email / Telegram / Chat widget
**Setup**: $299 | **Monthly**: from $99
**Deploy time**: 1–2 days

---

### 2.6 Complaint Routing Pipeline
**Problem**: Жалобы клиентов теряются или обрабатываются медленно.
**What it does**: Детектирует негативные обращения, маршрутизирует к старшему агенту, трекает статус и SLA.
**Best for**: E-commerce, services, hospitality
**Integrations**: Email/Chat, CRM, Slack
**Setup**: $549 | **Monthly**: from $149
**Deploy time**: 3–4 days

---

## Category 3: Voice & Calls

### 3.1 VoiceOS — AI Phone Receptionist
**Problem**: Бизнес теряет входящие звонки или платит за call center.
**What it does**: AI-голосовой агент принимает входящие звонки, квалифицирует, записывает на приём, передаёт менеджеру сложные случаи.
**Best for**: Clinics, real estate, services, restaurants
**Integrations**: Telephony (Twilio/SIP), CRM, Calendar
**Setup**: $1,199 | **Monthly**: from $299
**Deploy time**: 7–10 days

---

### 3.2 Missed Call Recovery Pipeline
**Problem**: Пропущенные звонки = потерянные клиенты.
**What it does**: Детектирует пропущенный звонок, создаёт лида, немедленно отправляет SMS/WhatsApp с "Мы скоро перезвоним", уведомляет менеджера, запускает follow-up.
**Best for**: Clinics, real estate, auto, local services
**Integrations**: Telephony, WhatsApp/SMS, CRM, Telegram
**Setup**: $349 | **Monthly**: from $99
**Deploy time**: 2–3 days
**ROI**: 1 вернувшийся клиент окупает 3+ месяца подписки

---

### 3.3 Call Summary Pipeline
**Problem**: После звонков нет структурированных заметок. Контекст теряется.
**What it does**: Транскрибирует звонок, генерирует структурированное summary, сохраняет в CRM, создаёт follow-up задачи.
**Best for**: Sales, support, consulting
**Integrations**: Telephony/Zoom, CRM, Notion/Slack
**Setup**: $499 | **Monthly**: from $99
**Deploy time**: 3–4 days

---

### 3.4 Appointment Booking Voice Agent
**Problem**: Запись на приём занимает время администратора.
**What it does**: AI-агент принимает звонки и записывает клиентов в календарь, подтверждает, отправляет напоминания.
**Best for**: Clinics, beauty, services
**Integrations**: Telephony, Google Calendar/Calendly, CRM
**Setup**: $1,099 | **Monthly**: from $249
**Deploy time**: 7–10 days

---

### 3.5 Lead Qualification Voice Agent
**Problem**: SDR тратят время на первичную квалификацию по телефону.
**What it does**: AI-голосовой агент проводит первичный скрининг входящих лидов по скрипту, скорит, передаёт горячих людям.
**Best for**: B2B, real estate, insurance
**Integrations**: Telephony, CRM, Slack
**Setup**: $1,199 | **Monthly**: from $299
**Deploy time**: 7–10 days

---

## Category 4: Operations

### 4.1 OpsOS — Internal Workflow Automation
**Problem**: Внутренние процессы (согласования, задачи, документы) хаотичны.
**What it does**: Комплексная операционная система: маршрутизация задач, уведомления команды, статусы, эскалации.
**Best for**: Teams 5–50, operations-heavy businesses
**Integrations**: Slack/Telegram, Notion/Linear, CRM, email
**Setup**: $1,499 | **Monthly**: from $299
**Deploy time**: 7–10 days

---

### 4.2 Task Routing Pipeline
**Problem**: Входящие задачи/запросы распределяются вручную или теряются.
**What it does**: Автоматически классифицирует входящие задачи и направляет нужному исполнителю с дедлайном.
**Best for**: Agencies, operations teams
**Integrations**: Email/Forms, Notion/Linear/Trello, Slack
**Setup**: $549 | **Monthly**: from $149
**Deploy time**: 3–5 days

---

### 4.3 Document Processing Pipeline
**Problem**: Входящие документы (заявки, договора) обрабатываются вручную.
**What it does**: Извлекает данные из документов (PDF/email), структурирует, создаёт записи в системе, уведомляет ответственных.
**Best for**: Legal, finance, real estate, logistics
**Integrations**: Gmail, Google Drive, Airtable/Notion, Telegram
**Setup**: $699 | **Monthly**: from $149
**Deploy time**: 4–6 days

---

### 4.4 Approval Workflow Pipeline
**Problem**: Согласования тормозят операции: счета, договора, запросы.
**What it does**: Структурированный workflow согласований с уведомлениями, дедлайнами, историей решений.
**Best for**: Finance, operations, HR
**Integrations**: Slack/Telegram, Email, Google Drive/Notion
**Setup**: $699 | **Monthly**: from $149
**Deploy time**: 4–5 days

---

### 4.5 Employee Onboarding Pipeline
**Problem**: Онбординг новых сотрудников хаотичен и непоследователен.
**What it does**: Автоматически запускает onboarding-последовательность: задачи, документы, доступы, приветствия, чеклисты.
**Best for**: Companies with regular hiring
**Integrations**: HR tools, Gmail, Slack, Google Drive
**Setup**: $699 | **Monthly**: from $149
**Deploy time**: 4–6 days

---

### 4.6 Daily Operations Report Pipeline
**Problem**: Ежедневные отчёты по операциям делаются вручную или не делаются.
**What it does**: Каждое утро собирает ключевые метрики из всех источников и отправляет структурированный дейли-репорт команде.
**Best for**: Operations managers, founders
**Integrations**: CRM, Airtable, Slack/Telegram/Email
**Setup**: $349 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

## Category 5: CRM & Data

### 5.1 CRMOS — CRM Automation Suite
**Problem**: CRM захламлён, дубли, устаревшие данные, нет автоматизаций.
**What it does**: Комплексная система: очистка CRM, дедупликация, автоматические статусы, enrichment, регулярный аудит данных.
**Best for**: Sales-driven businesses с CRM
**Integrations**: HubSpot / Pipedrive / Airtable + enrichment tools
**Setup**: $1,299 | **Monthly**: from $249
**Deploy time**: 7–10 days

---

### 5.2 Contact Enrichment Pipeline
**Problem**: Контакты в CRM неполные: нет email, телефона, компании.
**What it does**: Автоматически обогащает контакты данными из открытых источников (Apollo, Hunter, Clearbit).
**Best for**: B2B sales, agencies
**Integrations**: Apollo/Hunter/Clearbit, CRM
**Setup**: $399 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 5.3 Duplicate Detection Pipeline
**Problem**: В CRM тысячи дублирующихся контактов и сделок.
**What it does**: Регулярно сканирует CRM, находит дубли, мёрджит или флагует для ручной проверки.
**Best for**: Any CRM user with large database
**Integrations**: HubSpot / Pipedrive / Airtable
**Setup**: $349 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 5.4 Deal Stage Automation Pipeline
**Problem**: Менеджеры не двигают сделки по воронке. Стадии устаревают.
**What it does**: Автоматически двигает сделки по стадиям на основе триггеров (email sent, call logged, etc.), уведомляет менеджеров.
**Best for**: Sales teams
**Integrations**: CRM
**Setup**: $599 | **Monthly**: from $149
**Deploy time**: 3–4 days

---

### 5.5 Client Database Sync Pipeline
**Problem**: Данные о клиентах разбросаны по разным системам (CRM, таблицы, billing).
**What it does**: Синхронизирует клиентские данные между системами в реальном времени. Single source of truth.
**Best for**: Businesses with multiple tools
**Integrations**: CRM + Google Sheets / Airtable / Billing tools
**Setup**: $599 | **Monthly**: from $149
**Deploy time**: 3–5 days

---

## Category 6: Reporting & Intelligence

### 6.1 ReportOS — Operational Dashboard
**Problem**: Нет единой картины операционных метрик.
**What it does**: Создаёт автоматически обновляемый операционный дашборд из всех источников данных.
**Best for**: Founders, operations directors
**Integrations**: CRM, Airtable, Google Analytics, ads platforms, billing
**Setup**: $1,199 | **Monthly**: from $249
**Deploy time**: 7–10 days

---

### 6.2 Weekly KPI Report Pipeline
**Problem**: KPI-отчёты делаются вручную каждую неделю.
**What it does**: Каждую пятницу автоматически собирает KPI и отправляет структурированный отчёт с динамикой.
**Best for**: Any business with KPIs
**Integrations**: CRM, Airtable/Google Sheets, Slack/Email
**Setup**: $599 | **Monthly**: from $149
**Deploy time**: 3–5 days

---

### 6.3 Lead Source Attribution Pipeline
**Problem**: Непонятно, откуда приходят лиды. Маркетинг-бюджет тратится вслепую.
**What it does**: Трекает источник каждого лида, строит attribution report, помогает оптимизировать каналы.
**Best for**: Marketing-driven businesses
**Integrations**: Website, CRM, Google Analytics, ads
**Setup**: $699 | **Monthly**: from $149
**Deploy time**: 4–6 days

---

### 6.4 Team Performance Dashboard
**Problem**: Нет прозрачности в работе команды.
**What it does**: Автоматически собирает метрики активности команды (tasks, calls, emails) в еженедельный дашборд.
**Best for**: Team leads, sales managers
**Integrations**: CRM, task manager, Slack/Telegram
**Setup**: $599 | **Monthly**: from $149
**Deploy time**: 4–5 days

---

### 6.5 Revenue Operations Dashboard
**Problem**: MRR, churn, LTV считаются вручную или не считаются.
**What it does**: Автоматически собирает и отображает ключевые revenue metrics в реальном времени.
**Best for**: SaaS, subscription businesses
**Integrations**: Stripe, CRM, billing tools
**Setup**: $1,399 | **Monthly**: from $299
**Deploy time**: 7–10 days

---

## Category 7: Marketing & Content

### 7.1 Content Calendar Pipeline
**Problem**: Контент-план ведётся в таблицах вручную. Хаос и дедлайны срываются.
**What it does**: Автоматически генерирует идеи контента, заполняет календарь, ставит задачи, напоминает дедлайны.
**Best for**: Marketing teams, agencies
**Integrations**: Notion/Airtable, Slack/Telegram
**Setup**: $399 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 7.2 AI Social Post Generator
**Problem**: Написание постов для соцсетей занимает много времени.
**What it does**: По brief или теме генерирует несколько вариантов постов, форматирует под платформы (LinkedIn, Instagram, Telegram).
**Best for**: Marketing teams, founders, agencies
**Integrations**: Notion/Airtable, Buffer/publish APIs
**Setup**: $499 | **Monthly**: from $99
**Deploy time**: 2–4 days

---

### 7.3 Video Brief Generator
**Problem**: Создание брифов для видео-контента занимает часы.
**What it does**: По теме/продукту автоматически генерирует структурированный видео-бриф с hook, сценарием, CTA.
**Best for**: Content creators, video agencies
**Integrations**: Notion, Telegram/Slack
**Setup**: $399 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 7.4 Campaign Reporting Pipeline
**Problem**: Отчёты по рекламным кампаниям делаются вручную.
**What it does**: Автоматически собирает данные из рекламных платформ, строит сводный отчёт, отправляет клиенту/команде.
**Best for**: Marketing agencies, in-house marketing
**Integrations**: Google Ads, Meta Ads, Airtable/Google Sheets
**Setup**: $349 | **Monthly**: from $99
**Deploy time**: 2–3 days

---

### 7.5 Review Collection Pipeline
**Problem**: Клиенты не оставляют отзывы. Репутация не растёт.
**What it does**: После завершения сервиса автоматически просит отзыв (email/WhatsApp), направляет довольных на Google/Yelp/платформы, негативные — внутрь.
**Best for**: Local services, clinics, hospitality
**Integrations**: Gmail/WhatsApp, CRM
**Setup**: $299 | **Monthly**: from $99
**Deploy time**: 1–2 days

---

## Pipeline Card Standard Structure

Каждая pipeline detail page должна содержать:

```
1. Name + tagline
2. Problem statement (1 sentence)
3. What it does (2-3 sentences)
4. Best for (industry tags)
5. Integrations (icons)
6. Setup price + Monthly price
7. Deployment time
8. What you get (bullet list)
9. Example workflow (visual step diagram)
10. Expected outcomes (metrics/results)
11. Requirements (что нужно от клиента)
12. Support level included
13. Related pipelines
14. CTA: "Request Deployment"
```
