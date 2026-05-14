# 🔎 Pipeline C — Website Audit Generator

#flowops #pipeline #audit #outbound

> Находим бизнесы, анализируем их сайт и операции, отправляем персональный аудит с конкретными идеями.

---

## Build Status

**Status as of 2026-05-04:** Pipeline C v2 is operationally completed and working end-to-end in n8n.

- The system now finds sites automatically, scrapes and audits them, writes Airtable CRM records, sends Telegram approval cards, and sends Gmail email only after `Approve + Send`.
- User confirmed live operation is working after fixes to Firecrawl result normalization and Gmail sending.
- Main trigger mode is now Telegram command, not schedule:
  - `/pipeline_c`
  - `/audit_sites`
  - `запусти pipeline c`
  - `найди сайты для аудита`
- Prospecting no longer uses `Daily Schedule Trigger`; it uses `When Called by Telegram Command` plus Manual Trigger for n8n testing.
- WF-06 remains the only active Telegram Trigger and routes both `audit_*` callbacks and Pipeline C launch commands.

- Local workflow JSON: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-website-audit-generator-workflow.json`
- Local runbook: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-website-audit-generator-runbook.md`
- v1 workflow mode: legacy draft-only outbound. It creates Airtable `Leads`, `Audits`, `Messages`, `Automation Logs`, and sends a Telegram review item, but does not send cold email automatically.
- Do not continue v1 unless there is a specific reason; v2 supersedes it and is the completed operational version.

**Pipeline C v2 implementation files:**

- Prospecting: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-prospecting-workflow.json`
- Audit Queue: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-audit-queue-workflow.json`
- Approval Handler: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-approval-handler-workflow.json`
- WF-06 router patch: `/Users/tamerlan/Desktop/flowopsteamPipelines/WF-06 AI Command Center - Pipeline C v2 Router Patch.json`
- Runbook: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-runbook.md`
- Generator/source of truth for regenerating files: `/Users/tamerlan/Desktop/flowopsteamPipelines/build-pipeline-c-v2-workflows.js`
- v2 mode: Firecrawl Search rotates several niches, caps review queue at 10/run, creates CRM/audit/message/log records, sends Telegram cards with `Approve + Send`, `Reject`, `Edit Needed`, `Need Loom`, and sends Gmail only after approve.
- Important: WF-06 must remain the only active Telegram Trigger; the patched WF-06 export is intentionally inactive to avoid duplicate webhook registration.
- **v2.1 prospecting upgrade on 2026-05-04:** strengthened after live runs repeated the same 2 sites and produced too few Telegram cards. Prospecting now runs 24 randomized niche/city/intent queries per launch, requests 8 results/query, normalizes up to 120 unique domains, uses stronger Airtable dedupe by domain/company, caps scraping at up to 60 new websites, and sends up to 30 review candidates/run.

---

## Целевые ниши

- Property management companies
- Marketing agencies
- E-commerce stores
- Real estate agencies
- Local service businesses (plumbing, HVAC, cleaning)
- Clinics и медицинские практики
- Coaches и консультанты
- Recruiting agencies
- Law firms
- Home services

---

## Что анализируем

**На сайте:**
- Контактные формы — насколько легко оставить заявку?
- Booking flow — можно ли записаться автоматически?
- Live chat / chatbot — есть или нет?
- Lead capture механизмы — pop-up, формы, CTA

**Операции:**
- Как выглядит поддержка? (email, телефон, чат)
- Технологический стек (если виден: Shopify, HubSpot, Calendly)
- Отзывы — на что жалуются клиенты?
- Job posts — что ищут в команду (подсказывает ручные процессы)

---

## Что ищем (Pain Points)

- Форма есть, но нет мгновенного ответа → Speed-to-Lead
- Поддержка только по email/телефону → AI Chatbot
- Нет booking flow → Calendar automation
- Много одинаковых вопросов в отзывах → FAQ bot
- В вакансиях: "data entry", "CRM management" → Ops Sprint

---

## Структура записи в базе

| Поле | Описание |
|------|----------|
| Company | Название компании |
| Website | URL |
| Niche | Ниша |
| Bottleneck | Главная найденная проблема |
| Opportunity 1 | Идея автоматизации #1 |
| Opportunity 2 | Идея автоматизации #2 |
| Opportunity 3 | Идея автоматизации #3 |
| Estimated time saved | Сколько часов/неделю можно сэкономить |
| Loom script | Скрипт для видео-аудита |
| Cold email | Черновик email |
| LinkedIn message | Черновик DM |
| Follow-up | Следующий шаг |

---

## MVP workflow

1. Manual/weekly trigger.
2. Target website config list.
3. Airtable dedupe by `Website` or `Company`.
4. Firecrawl scrape of public website content.
5. OpenAI audit generation:
   - fit score;
   - bottleneck;
   - pain hypothesis;
   - 3 opportunities;
   - recommended offer/workflow;
   - Loom script;
   - cold email and follow-up drafts.
6. Quality gate: only `Fit Score >= 7` becomes a lead/audit draft.
7. Airtable writes:
   - `Leads` record;
   - `Audits` draft;
   - `Messages` cold email draft;
   - `Automation Logs` success/skipped record.
8. Telegram review message for manual Loom/email review.

---

## v2 automated workflow

1. Telegram-command/manual multi-niche prospecting.
2. Firecrawl Search rotates across Home Services, Real Estate, Clinics, Agencies, E-commerce, and Coaches/Consultants.
3. Results are normalized, directory/social domains are filtered out, and Airtable dedupe runs before scraping.
4. Search produces a larger pool: 24 randomized queries x 8 results/query, then up to 120 unique domains are normalized.
5. Airtable dedupe checks domain/company before scraping; scrape work is capped at up to 60 new websites/run.
6. Top candidates are capped at 30/run before audit generation.
7. Audit Queue generates AI audit + teaser email, creates Airtable `Leads`, `Audits`, `Messages`, `Automation Logs`, then sends Telegram approval card.
8. Approval Handler receives `audit_*` callbacks through WF-06 and only sends Gmail after `Approve + Send`.
9. `Reject`, `Edit Needed`, and `Need Loom` update CRM/logs without sending email.
10. Duplicate approve and missing recipient email are blocked from sending.

## Operational Notes

- Pipeline C v2 should be treated as completed. Future work is optimization and campaign iteration, not initial build.
- **v3 scale/auto-send update on 2026-05-12:** local files `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Prospecting.json` and `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Audit Queue.json` were updated for scale mode. Prospecting now defaults to at least 100 review candidates/run, generates 40-80 Firecrawl Search queries, requests 8-10 results/query, normalizes up to 400 domains, scrapes up to 180, and caps review at 100 by default. Audit Queue now auto-sends via native Gmail node after Airtable records are created when a recipient email exists; Telegram approval cards are disconnected legacy fallback. After import, reconnect Gmail OAuth in `Gmail Auto Send Email`.
- **v3 batch gate update on 2026-05-13:** `Pipeline C v3 - Audit Queue.json` now paces the whole audit/send chain through `Assign Audit Queue Batch Delay` + `Wait Batch Window` before OpenAI/Airtable/Gmail. Default is 30 items per batch with a 5-minute gap; this can be overridden by incoming fields like `audit_batch_size` and `audit_batch_gap_minutes`. The first batch waits 1 second, batch 2 waits 5 minutes, batch 3 waits 10 minutes, etc.
- **v3 Airtable rate-limit fix on 2026-05-13:** after a live run hit `RATE_LIMIT_REACHED` at `Airtable Create Lead` item 40, the batch gate was strengthened with per-item staggering inside each batch. Default is now 30 per batch, 5-minute batch gap, and 3-second item gap. Airtable HTTP nodes in Prospecting/Audit Queue now have retry/backoff (`maxTries: 6`, `waitBetweenTries: 7000`) and Gmail auto-send has retry/backoff (`maxTries: 4`, `waitBetweenTries: 10000`).
- **v3 strict Airtable throttle on 2026-05-13:** after another `RATE_LIMIT_REACHED` at `Airtable Create Lead` item 35, throttling was moved directly before `Airtable Create Lead` via `Wait Before Airtable Create Lead`. Defaults are now more conservative: 10 per batch, 5-minute batch gap, 15-second Airtable item gap, 2-second OpenAI item gap. Airtable HTTP nodes now retry up to 10 times with 15s backoff and request batching where supported.
- **v3 mass personalized sender update on 2026-05-13:** Prospecting now defaults to 300 review/audit candidates, accepts `/pipeline_c 250` and `/pipeline_c 300`, normalizes up to 700 domains, and scrapes up to 360. Audit Queue was changed from quality-filter queue to mass outbound mode: score no longer blocks sending, OpenAI produces a personal email for each lead, parser falls back instead of failing, recipient selection uses discovered email first and then infers `info@domain`, and post-send Airtable updates are sequential instead of parallel.
- **FlowOps Opportunity Engine skill created on 2026-05-09:** `/Users/tamerlan/.codex/skills/flowops-opportunity-engine/`. Use it for trigger-based prospect diagnosis across website signals, reviews, company hiring pain, tech stack gaps, event/exhibitor triggers, scoring, outreach, Loom scripts, and compliance-safe B2B outbound. Do not use it for Upwork or other freelance marketplace lead search; Upwork is handled by a separate prepared pipeline.
- **Almaty Business Audit Proposal skill created on 2026-05-14:** `/Users/tamerlan/.codex/skills/almaty-business-audit-proposal/`. Use it when turning Almaty/Kazakhstan website and business evidence into a complete КП/commercial proposal, including audit findings, fit score, proposed automation system, scope, timeline, assumptions, risks, and next step. It complements `flowops-opportunity-engine` by focusing on local owner-facing proposals rather than general prospect radar.
- Use Telegram to start a batch: `/pipeline_c` or `/audit_sites`.
- Default batch is 30 review candidates/run; smaller runs can be requested with `/pipeline_c 20`, `/pipeline_c 15`, etc.
- For v3 scale mode, default batch is 100 review candidates/run; use `/pipeline_c 100`, `/pipeline_c 125`, `/pipeline_c 150`, `/pipeline_c 175`, or `/pipeline_c 200` when the router passes command text through.
- Email copy is teaser-style and must not claim a Loom exists unless a Loom URL exists.
- Gmail send uses native `n8n-nodes-base.gmail`, not HTTP Request with Gmail OAuth.
- `Normalize Search Results` uses manual URL parsing and supports Firecrawl `item.json.data.web`.

---

## Opener — Email / LinkedIn

> "Hey [Name], I took a quick look at [Company] and noticed 2–3 places where automation could save your team time or improve lead response time.
>
> Recorded a short 2-min audit video showing exactly what I found.
>
> Worth sending it over?"

---

## Opener — Если нет ответа (Follow-up)

> "Hey [Name], just following up on my previous message. I noticed [specific observation from the site]. Happy to share the 2-min video — no strings attached."

---

## Связанные страницы

- [[Speed-to-Lead System]] — главный оффер для этого пайплайна
- [[AI Chatbot & Voice Agent]] — второй частый оффер
- [[Pipeline D — Demo Library]] — демо для follow-up
- [[Sales Steps]] — что делать после ответа
- [[Message Templates]] — шаблоны

---

*#flowops #pipeline #audit #outbound*
