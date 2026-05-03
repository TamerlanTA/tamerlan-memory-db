# Airtable CRM Build Spec — FlowOps

#flowops #crm #airtable

## Related
- [[00 - Overview]]
- [[CRM Tables]]
- [[What to Do First]]
- [[Full System Architecture]]
- [[Pipeline A — Upwork Radar]]
- [[Pipeline B — LinkedIn Pain Radar]]
- [[Pipeline C — Website Audit Generator]]
- [[Pipeline D — Demo Library]]
- [[Pipeline E — Retainer Conversion]]

## Purpose

Подготовить FlowOps CRM в Airtable как операционную базу для продаж и будущих автоматизаций:
- собирать лиды из Upwork, LinkedIn, cold email, referrals и inbound;
- вести сделки от первого сигнала до Sprint / Retainer;
- хранить сообщения, демо, аудиты, предложения и клиентов;
- дать n8n/Make стабильную структуру для записи, обновления и follow-up логики.

## Build Status

**Status as of 2026-05-03:** FlowOps CRM system has been created.

- Earlier memory treated this note as an Airtable-ready spec only.
- Current project state: CRM is no longer just planned/prepared; it exists and should be treated as the operating CRM for FlowOps.
- Next CRM work should focus on validation, QA, automation wiring, data hygiene, and reporting rather than base creation.

## Base

**Base name:** `FlowOps CRM`

Рекомендуемые таблицы:
1. `Leads`
2. `Opportunities`
3. `Messages`
4. `Demos`
5. `Audits`
6. `Proposals`
7. `Clients`
8. `Retainers`
9. `Automation Logs`

## Table: Leads

Основная таблица. Одна запись = один потенциальный клиент или компания.

| Field                | Airtable type           | Options / notes                                                                                   |
| -------------------- | ----------------------- | ------------------------------------------------------------------------------------------------- |
| `Lead Name`          | Single line text        | Имя контакта или primary label                                                                    |
| `Company`            | Single line text        | Название компании                                                                                 |
| `Website`            | URL                     | Для аудита                                                                                        |
| `Source`             | Single select           | `Upwork`, `LinkedIn`, `Cold Email`, `Referral`, `Inbound`, `Manual`, `Other`                      |
| `Niche`              | Single select           | `Real Estate`, `Home Services`, `Agency`, `E-commerce`, `Clinic`, `SaaS`, `Coach`, `Other`        |
| `Pain Signal`        | Long text               | Что увидели или что клиент сказал                                                                 |
| `Likely Offer`       | Single select           | `Speed-to-Lead`, `Ops Sprint`, `AI Chatbot`, `Voice Agent`, `Audit`, `Retainer`                   |
| `Fit Score`          | Number                  | 0-10                                                                                              |
| `Budget Estimate`    | Single line text        | Например `$500-2k`, `$2k+`, unknown                                                               |
| `Status`             | Single select           | `New`, `Contacted`, `Replied`, `Call Booked`, `Called`, `Proposal Sent`, `Won`, `Lost`, `Nurture` |
| `Next Action`        | Single line text        | Следующий ручной шаг                                                                              |
| `First Contact Date` | Date                    | Первое касание                                                                                    |
| `Last Contacted`     | Date                    | Последнее касание                                                                                 |
| `Follow-up Date`     | Date                    | Когда написать снова                                                                              |
| `Last Activity`      | Last modified time      | Airtable system field                                                                             |
| `Contact URL`        | URL                     | LinkedIn / Upwork / profile                                                                       |
| `Email`              | Email                   | Если есть                                                                                         |
| `LinkedIn URL`       | URL                     | Если отдельно от Contact URL                                                                      |
| `Upwork Job URL`     | URL                     | Если источник Upwork                                                                              |
| `Opportunities`      | Link to `Opportunities` | Связанные сделки                                                                                  |
| `Messages`           | Link to `Messages`      | История сообщений                                                                                 |
| `Audits`             | Link to `Audits`        | Связанные аудиты                                                                                  |
| `Notes`              | Long text               | Контекст, research, conversation notes                                                            |

## Table: Opportunities

Одна запись = конкретная сделка / автоматизация, которую можно продать.

| Field                    | Airtable type               | Options / notes                                                                                                                  |
| ------------------------ | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `Opportunity Name`       | Formula or single line text | Например `{Company} & " — " & {Offer}`                                                                                           |
| `Lead`                   | Link to `Leads`             | Required                                                                                                                         |
| `Offer`                  | Single select               | `Speed-to-Lead`, `Ops Sprint`, `AI Chatbot`, `Voice Agent`, `Audit`, `Retainer`                                                  |
| `Automation Opportunity` | Single line text            | Короткое название идеи                                                                                                           |
| `Problem`                | Long text                   | Конкретная проблема клиента                                                                                                      |
| `Suggested Workflow`     | Long text                   | Как будет работать автоматизация                                                                                                 |
| `Tools Needed`           | Multiple select             | `n8n`, `Make`, `OpenAI`, `Airtable`, `HubSpot`, `GoHighLevel`, `Slack`, `Email`, `Calendly`, `Twilio`, `Vapi`, `Retell`, `Other` |
| `Stage`                  | Single select               | `Discovery`, `Proposal Draft`, `Proposal Sent`, `Negotiating`, `Won`, `Lost`, `Nurture`                                          |
| `Proposed Value`         | Currency                    | Ценность/размер сделки                                                                                                           |
| `Build Price`            | Currency                    | Цена разработки                                                                                                                  |
| `Estimated Client Value` | Currency                    | Сколько проблема стоит клиенту                                                                                                   |
| `Retainer Potential`     | Single select               | `High`, `Medium`, `Low`, `None`                                                                                                  |
| `Close Probability %`    | Percent                     | Оценка вероятности                                                                                                               |
| `Discovery Call Date`    | Date                        | Если был звонок                                                                                                                  |
| `Proposal Sent Date`     | Date                        | Если отправлено предложение                                                                                                      |
| `Decision Date`          | Date                        | Плановая/фактическая дата решения                                                                                                |
| `Pain Summary`           | Long text                   | Итог discovery                                                                                                                   |
| `ROI Presented`          | Long text                   | Как объясняли ROI                                                                                                                |
| `Decision Maker`         | Single line text            | Кто решает                                                                                                                       |
| `Objections Raised`      | Long text                   | Возражения                                                                                                                       |
| `Won/Lost Reason`        | Long text                   | Причина результата                                                                                                               |
| `Proposal`               | Link to `Proposals`         | Если есть                                                                                                                        |
| `Client`                 | Link to `Clients`           | Если won                                                                                                                         |
| `Notes`                  | Long text                   | Follow-up/context                                                                                                                |

## Table: Messages

История касаний и база для follow-up автоматизаций.

| Field             | Airtable type           | Options / notes                                                                                                    |
| ----------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `Message ID`      | Autonumber              | Primary field can be formula `MSG-{Message ID}`                                                                    |
| `Lead`            | Link to `Leads`         | Required                                                                                                           |
| `Opportunity`     | Link to `Opportunities` | Optional                                                                                                           |
| `Channel`         | Single select           | `Upwork`, `LinkedIn`, `Email`, `WhatsApp`, `Call`, `Referral`                                                      |
| `Message Type`    | Single select           | `Proposal`, `DM`, `Cold Email`, `Follow-up`, `Retainer Pitch`, `Call Note`, `Manual Note`                          |
| `Template Used`   | Single select           | `Upwork Proposal`, `LinkedIn Opener`, `Cold Audit Email`, `Follow-up 1`, `Follow-up 2`, `Retainer Pitch`, `Custom` |
| `Draft`           | Long text               | Текст до отправки                                                                                                  |
| `Message Text`    | Long text               | Фактически отправленный текст                                                                                      |
| `Sent?`           | Checkbox                | Отправлено                                                                                                         |
| `Date Sent`       | Date/time               | Когда отправлено                                                                                                   |
| `Opened?`         | Checkbox                | Если отслеживается                                                                                                 |
| `Response`        | Single select           | `No Response`, `Replied`, `Interested`, `Not Interested`, `Call Booked`, `Nurture`                                 |
| `Reply Sentiment` | Single select           | `Positive`, `Neutral`, `Negative`, `No Reply`                                                                      |
| `Follow-up Date`  | Date                    | Следующий контакт                                                                                                  |
| `Outcome`         | Single select           | `Call Booked`, `Not Interested`, `No Reply`, `Nurture`, `Won`, `Lost`                                              |
| `Notes`           | Long text               | Любой контекст                                                                                                     |

## Table: Demos

Библиотека демо для продаж.

| Field                | Airtable type    | Options / notes                                                        |
| -------------------- | ---------------- | ---------------------------------------------------------------------- |
| `Demo Name`          | Single line text | Например `Speed-to-Lead — Real Estate`                                 |
| `Offer`              | Single select    | `Speed-to-Lead`, `Ops Sprint`, `AI Chatbot`, `Voice Agent`, `Retainer` |
| `Niche`              | Single select    | Same as Leads.Niche                                                    |
| `Problem Solved`     | Long text        | Какую боль решает                                                      |
| `Loom URL`           | URL              | Ссылка на видео                                                        |
| `Date Created`       | Date             | Когда создано                                                          |
| `Status`             | Single select    | `Idea`, `Scripted`, `Recorded`, `Live`, `Needs Update`                 |
| `When to Use`        | Long text        | В каком контексте отправлять                                           |
| `Times Sent`         | Number           | Можно обновлять автоматизацией                                         |
| `Views`              | Number           | Если данные доступны из Loom/ручного ввода                             |
| `Replies After Demo` | Number           | Ручной или автоматический счетчик                                      |
| `Calls Booked`       | Number           | Атрибуция                                                              |
| `Deals Closed`       | Number           | Атрибуция                                                              |
| `Close Rate %`       | Formula          | `IF({Times Sent}=0,0,{Deals Closed}/{Times Sent})`                     |
| `Notes`              | Long text        | Что улучшить                                                           |

## Table: Audits

Для Website Audit Generator и персонализированных cold outreach.

| Field                  | Airtable type               | Options / notes                                                               |
| ---------------------- | --------------------------- | ----------------------------------------------------------------------------- |
| `Audit Name`           | Formula or single line text | `{Company} & " — Website Audit"`                                              |
| `Lead`                 | Link to `Leads`             | Required                                                                      |
| `Website`              | Lookup from Leads           | Or URL if independent                                                         |
| `Audit Type`           | Single select               | `Website`, `Speed-to-Lead`, `CRM/Ops`, `Booking Flow`, `Chatbot Opportunity`  |
| `Findings`             | Long text                   | Конкретные находки                                                            |
| `Pain Hypothesis`      | Long text                   | Предположение о боли                                                          |
| `Recommended Offer`    | Single select               | Same as `Likely Offer`                                                        |
| `Recommended Workflow` | Long text                   | Что предложить                                                                |
| `Audit Loom URL`       | URL                         | Если записан Loom                                                             |
| `Audit Status`         | Single select               | `Queued`, `Researching`, `Drafted`, `Recorded`, `Sent`, `Replied`, `Archived` |
| `Created Date`         | Created time                | Airtable system field                                                         |
| `Sent Date`            | Date                        | Когда отправили                                                               |
| `Notes`                | Long text                   | Дополнительный контекст                                                       |

## Table: Proposals

Коммерческие предложения и scope.

| Field            | Airtable type           | Options / notes                                                        |
| ---------------- | ----------------------- | ---------------------------------------------------------------------- |
| `Proposal Name`  | Single line text        | Название предложения                                                   |
| `Lead`           | Link to `Leads`         | Required                                                               |
| `Opportunity`    | Link to `Opportunities` | Required                                                               |
| `Offer`          | Single select           | Same as Opportunities.Offer                                            |
| `Scope Summary`  | Long text               | Что входит                                                             |
| `Deliverables`   | Long text               | Конкретные deliverables                                                |
| `Price`          | Currency                | Цена                                                                   |
| `Timeline`       | Single line text        | Например `5-7 days`                                                    |
| `Status`         | Single select           | `Draft`, `Sent`, `Follow-up Needed`, `Accepted`, `Rejected`, `Expired` |
| `Proposal URL`   | URL                     | Google Doc / PDF / Upwork proposal                                     |
| `Sent Date`      | Date                    | Когда отправлено                                                       |
| `Follow-up Date` | Date                    | Когда напомнить                                                        |
| `Accepted Date`  | Date                    | Если принято                                                           |
| `Notes`          | Long text               | Контекст и изменения                                                   |

## Table: Clients

Клиенты после won.

| Field                | Airtable type           | Options / notes                                                                                       |
| -------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------- |
| `Client Name`        | Single line text        | Company or person                                                                                     |
| `Lead`               | Link to `Leads`         | Источник                                                                                              |
| `Opportunity`        | Link to `Opportunities` | Won deal                                                                                              |
| `Primary Contact`    | Single line text        | Имя                                                                                                   |
| `Email`              | Email                   | Контакт                                                                                               |
| `Website`            | URL                     | Сайт                                                                                                  |
| `Client Status`      | Single select           | `Onboarding`, `Active Sprint`, `Delivered`, `Retainer Offered`, `Retainer Active`, `Paused`, `Closed` |
| `Project Start Date` | Date                    | Старт                                                                                                 |
| `Project End Date`   | Date                    | План/факт завершения                                                                                  |
| `Total Revenue`      | Currency                | Можно rollup из proposals/retainers                                                                   |
| `Retainer`           | Link to `Retainers`     | Если есть                                                                                             |
| `Handoff URL`        | URL                     | Loom/doc handoff                                                                                      |
| `Notes`              | Long text               | Контекст клиента                                                                                      |

## Table: Retainers

MRR и пост-проектная конверсия.

| Field                | Airtable type     | Options / notes                                                                        |
| -------------------- | ----------------- | -------------------------------------------------------------------------------------- |
| `Retainer Name`      | Single line text  | Например `{Client} — Growth`                                                           |
| `Client`             | Link to `Clients` | Required                                                                               |
| `Tier`               | Single select     | `Starter`, `Growth`, `Partner`, `Custom`                                               |
| `Monthly Fee`        | Currency          | MRR                                                                                    |
| `Status`             | Single select     | `Pitch Planned`, `Pitched`, `Negotiating`, `Active`, `Paused`, `Cancelled`, `Declined` |
| `Pitch Date`         | Date              | 7-14 дней после delivery                                                               |
| `Start Date`         | Date              | Если active                                                                            |
| `Renewal Date`       | Date              | Следующее продление                                                                    |
| `Included Work`      | Long text         | Что входит                                                                             |
| `Monthly Report URL` | URL               | Отчет                                                                                  |
| `Notes`              | Long text         | Контекст                                                                               |

## Table: Automation Logs

Служебная таблица для n8n/Make.

| Field                 | Airtable type           | Options / notes                                                           |
| --------------------- | ----------------------- | ------------------------------------------------------------------------- |
| `Log ID`              | Autonumber              | Primary can be formula `LOG-{Log ID}`                                     |
| `Workflow Name`       | Single line text        | Например `Upwork Radar`                                                   |
| `Source`              | Single select           | `Upwork`, `LinkedIn`, `Website Audit`, `CRM Follow-up`, `Manual`, `Other` |
| `Related Lead`        | Link to `Leads`         | Optional                                                                  |
| `Related Opportunity` | Link to `Opportunities` | Optional                                                                  |
| `Execution Status`    | Single select           | `Success`, `Skipped`, `Warning`, `Failed`, `Retried`                      |
| `Action Taken`        | Single line text        | Что сделал workflow                                                       |
| `Input Snapshot`      | Long text               | Sanitized JSON only, no secrets                                           |
| `Error Message`       | Long text               | Если ошибка                                                               |
| `Run URL`             | URL                     | n8n execution URL if useful                                               |
| `Created At`          | Created time            | Airtable system field                                                     |

## Views

### Leads
- `New Leads` — Status = `New`
- `Follow-up Today` — Follow-up Date is today or before, Status not `Won/Lost`
- `Hot Leads` — Fit Score >= 8
- `Upwork Leads` — Source = `Upwork`
- `LinkedIn Leads` — Source = `LinkedIn`
- `Nurture` — Status = `Nurture`
- `Lost` — Status = `Lost`

### Opportunities
- `Active Pipeline` — Stage not `Won/Lost`
- `Proposal Follow-up` — Stage = `Proposal Sent` or `Negotiating`
- `Won Deals` — Stage = `Won`
- `Retainer Candidates` — Retainer Potential = `High` or `Medium`

### Messages
- `Drafts to Send` — Sent? unchecked
- `No Reply Follow-ups` — Response = `No Response`, Follow-up Date due
- `Positive Replies` — Reply Sentiment = `Positive`

### Demos
- `Live Demos` — Status = `Live`
- `Needs Recording` — Status = `Idea` or `Scripted`
- `Best Performing` — sort by Close Rate %

### Audits
- `Audit Queue` — Audit Status = `Queued`
- `Drafted Audits` — Audit Status = `Drafted`
- `Sent Audits` — Audit Status = `Sent`

### Proposals
- `Draft Proposals`
- `Sent Proposals`
- `Follow-up Needed`
- `Accepted`

### Retainers
- `Pitch Planned`
- `Active MRR`
- `Renewals This Month`

## Initial records to create

### Demos
1. `Speed-to-Lead — Real Estate`
2. `AI Lead Qualification Chatbot — Clinic`
3. `Ops Automation — Agency Client Onboarding`
4. `Jotform → CRM + Slack Notification`
5. `Appointment + Reminder System`

### Offers/select consistency
Use the same offer names everywhere:
- `Speed-to-Lead`
- `Ops Sprint`
- `AI Chatbot`
- `Voice Agent`
- `Audit`
- `Retainer`

## Automation-ready rules

Use these rules before building n8n/Make:
- Deduplicate leads by `Website`, `Email`, `LinkedIn URL`, or `Upwork Job URL`.
- Never overwrite human notes automatically; append automation context to `Automation Logs`.
- AI-generated fields should be stored as draft/suggestion until manually approved.
- Every workflow should write one `Automation Logs` record with status, action, and sanitized input.
- Follow-up automation should only create message drafts first; sending can be manual until copy is proven.

## First automations to build after Airtable

1. **Upwork Radar → Leads**
   - Trigger: scheduled Upwork search/RSS/manual import.
   - Output: new `Leads` record, fit score, pain signal, proposal draft in `Messages`, log record.

2. **CRM Follow-up Queue**
   - Trigger: daily schedule.
   - Output: list of due follow-ups, draft messages, optional Telegram/Slack alert.

3. **Website Audit Generator**
   - Trigger: new lead with website and source `Cold Email` or manual audit request.
   - Output: `Audits` record with findings, recommended workflow, outreach draft.

4. **Proposal/Retainer Reminder**
   - Trigger: proposal sent or client delivered.
   - Output: follow-up task/date and retainer pitch reminder.

## Airtable setup checklist

- [ ] Create base `FlowOps CRM`.
- [ ] Create all tables above.
- [ ] Add linked record fields after both linked tables exist.
- [ ] Configure select options exactly as listed.
- [ ] Create views for daily work.
- [ ] Add initial 5 demo records.
- [ ] Add test lead and run one manual lead -> message -> opportunity path.
- [ ] Only after manual path works, connect n8n/Make automation.
