# Current Focus

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[projects/flowops-saas/overview|FlowOps SaaS — overview]]
- [[projects/flowops-saas/roadmap|FlowOps SaaS — roadmap]]
- [[projects/PromAlp/overview|PromAlp — overview]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team — overview]]
- [[Linear/Linear Ops Automation System/overview|Linear Ops Automation System]]
- [[projects/AI-Powered Woven Label Generator/current-state|AI-Powered Woven Label Generator — current state]]
- [[projects/importcar-kz-mvp/overview|ImportCar.kz — overview]]
- [[projects/importcar-kz-mvp/roadmap|ImportCar.kz — roadmap]]
- [[projects/amigo-mvp/overview|AMIGO MVP — overview]]
- [[projects/amigo-mvp/roadmap|AMIGO MVP — roadmap]]
- [[projects/tg-finance-agent/overview|TG Finance Agent — overview]]

---

## TG Finance Agent (добавлен 2026-06-17)

**Статус**: memory initialized. Local workspace: `/Users/tamerlan/Desktop/tg-finance-agent`. At initialization the workspace was empty and not a git repository.

**Следующее**: define product scope and initialize/inspect the app workspace.

**Память**: [[projects/tg-finance-agent/overview]] | [[projects/tg-finance-agent/current-state]] | [[projects/tg-finance-agent/next-steps]]

---

## AMIGO MVP — International Hospitality Job Applications (обновлён 2026-06-30)

**Статус**: Active, health Yellow. Phase 1–5 are functionally implemented/deployed through matching and approval. Phase 6 safe manual-action slice is deployed: DB migrations applied, `bot-api` and `worker-applications` live, controlled handoff created 4 manual-action application jobs. Remaining acceptance is Telegram manual resolution/evidence.

**Цель**:
- controlled pilot for 10 candidates by 2026-07-05;
- immediate post-launch capacity for 30 candidates from the waitlist;
- 5–10 manager-approved application attempts per active candidate per day when enough suitable vacancies exist.

**Что готово**:
- `/candidate_new`, `/candidate_find`, `/candidate_view`, `/candidate_edit`, `/candidate_close` — все работают
- Языки (CEFR), согласие, аудит-события, profile completeness check — реализованы
- `/candidate_documents` — выбор кандидата, queue generation, signed PDF link, approve/reject callbacks
- `worker-documents` + Gotenberg deployed on Railway
- CV template quality upgrade deployed in commit `a11145b`; latest controlled candidate CV version `9219995e-fed0-407c-a27f-f5ee3493cd71` is `pending_approval`
- Telegram approval callback verified on 2026-06-22; CV version `9219995e-fed0-407c-a27f-f5ee3493cd71` is approved and candidate status is `documents`
- Partner-approved CV correction deployed on 2026-06-22; latest corrected sample `c20ddaa5-15a7-4aa9-9314-8db68adec1ab` is pending approval and verified by PDF text + PNG render
- Employer catalog foundation committed in `91bc7b0`; production has 25 employers and 25 career sources
- Vacancy discovery schema committed in `b1f1411`; production has empty `source_runs` and `vacancies` tables ready for first connector
- Phase 3.5 CV enrichment committed in `3a7bd48`: production tables for candidate photos/work experience/education/extras, Telegram commands `/candidate_photo`, `/candidate_experience`, `/candidate_education`, `/candidate_extra`, `/candidate_view` readiness warnings, worker-documents structured loading
- Unified `/candidate_new` onboarding deployed in `8145245`: durable resume, experience/education/extras/photo/final review, optional WhatsApp, standalone enrichment commands preserved
- Compact two-column CV header deployed in `63d9637`; production sample `689f61c4-ff82-426b-97fe-b44a7072939d` passed PDF/PNG verification
- Phase 4/5 production state: 31 discovery sources active in scheduler, 533 total vacancies / 388 active after manual activation; `/candidate_batch` approved a strict 6/10 shortage batch; `/approved_vacancies` deployed for pre-Phase-6 duplicate audit
- Phase 6 production safe slice is accepted for manual deep-link mode: migrations `202606300001` and `202607010001` applied; application tables, queues, unique open manual-action guard, and queue depth verified. Production DB on 2026-07-02 shows 8 `applied` applications, 8 resolved manual actions with `resolution_note = applied`, and 8 `manual_confirmation` evidence rows. Two manual actions remain open for Тамерлан Тог.
- Candidate supply expansion on 2026-07-02 is deployed: location backfill reduced active null-country vacancies from 275 to 224; `phase5-v2` tiered matching plus `/candidate_supply` gives production-like local supply of Юля 6 primary + 7 reserve and Жанибек 5 primary + 4 reserve. Full validation passed. `bot-api` and `worker-vacancy-discovery` are online after Railway deploy; `/health` OK, Telegram commands include `/candidate_supply`, webhook pending updates 0.

**Текущая фаза**: Phase 6 — local readiness complete; next is explicit production migration/deploy/acceptance checkpoint.

**Блокеры**:
- Consent text v1-ru-2026-06 still needs business/legal approval before pilot scale
- Need managers to collect real CV enrichment data for pilot candidates; JPEG/PNG/WebP/HEIC/HEIF uploads are accepted, with HEIC/HEIF converted privately to JPEG before CV rendering
- Need one full live Telegram acceptance pass of unified `/candidate_new`; one production session is safely waiting at `awaiting_form`
- `/approved_vacancies` still needs manual Telegram verification before Phase 6 handoff
- Phase 6 manual evidence acceptance is complete; next is pilot operating loop, source expansion, and certified email/adapter planning
- Railway token shared in chat must be rotated
- Need production/manual Telegram acceptance before any auto-submit path
- Need Telegram manual verification of `/candidate_supply` and `/candidate_batch` after candidate supply expansion deploy
- Нет production-enabled certified ATS/application adapter; `manual-deep-link-v1` never submits and `email-apply-v1` exists locally with dry-run default, but no real sender/source-level production enable is wired

**ВАЖНО для деплоя**: Railway НЕ подключён к GitHub. После каждого push делать `railway up --service bot-api` из `/Users/tamerlan/Documents/amigo-mvp`

**Память**: [[projects/amigo-mvp/overview]] | [[projects/amigo-mvp/current-state]] | [[projects/amigo-mvp/next-steps]] | [[projects/amigo-mvp/technical-architecture]]

---

## FlowOps SaaS — AI Operations Platform (обновлён 2026-06-30)

**Статус**: MVP Sales Validation. Account/chat/deal-room deferred out of MVP on 2026-06-30; future layer preserved.

**Что это**: SaaS/Platform с marketplace из 40 готовых AI/automation pipeline-систем для бизнеса. Гибридная модель: setup fee + monthly subscription. Premium B2B positioning (Linear/Vercel quality).

**Что готово**:
- Production site live: `https://flowops.agency` / `https://flowops-saas.vercel.app`
- Latest MVP scope-reversal preview: `https://flowops-saas-pvoewrzoy-tamertt931-8560s-projects.vercel.app` (`dpl_92thMKzyip2qEvXBSi1MtV37EiKu`) — public order flow restored to `/api/pipeline-order`, Portal removed from public nav/CTA, `/portal/*` gated unless `ENABLE_CLIENT_PORTAL=true`
- 25 live pipeline systems + `/os`, `/os/[slug]`, `/pricing`, homepage audit CTA
- Supabase-backed `pipeline_orders`, `audit_requests`, internal order/audit workspaces
- Telegram notifications for orders and audit requests
- Protected `/internal/*` routes with working `src/middleware.ts`
- Stripe/Resend scaffolds exist, but live verification is deferred
- Durable Supabase-backed rate limiting added for `/api/pipeline-order` and `/api/audit-request`
- Phase 3 account/chat/deal-room foundation was explored and partially implemented, but is deferred out of MVP; keep as future infrastructure, not current buyer flow

**Следующий шаг**: if preview is accepted, promote MVP scope-reversal preview to production; then run the FlowOps automation-card audit before scaled outreach: verify every card's real buyer need, expand sparse descriptions, recheck pricing against market/custom-build references with productized ~30%-below-market logic where safe, add unified in-card SVG-style illustrations, then manually verify/enrich the 20-account seed list and start first outreach batch.

**Память**: [[projects/flowops-saas/overview]] | [[projects/flowops-saas/current-state]] | [[projects/flowops-saas/next-steps]] | [[projects/flowops-saas/roadmap]] | [[projects/flowops-saas/pipeline-catalog]] | [[projects/flowops-saas/pricing]] | [[projects/flowops-saas/automation-card-audit-brief]]

---

## PromAlp (добавлен 2026-06-02)

**Статус**: Инициализация. Зонтичный проект (сайт + видео + маркетинг) для бригады промышленных альпинистов в Алматы.
- Сайт: в разработке → [[projects/promalp-site/overview|promalp-site]]
- Видео: сырьё собрано (37 iPhone + 67 DJI), монтаж не начат → [[projects/PromAlp/video-tz|ТЗ на видео]]
- Маркетинг: не начат
- Видеопапка: `/Users/tamerlan/Desktop/видео альпинисты/`

**Следующее**: разложить файлы по папкам → отбор → монтаж Reels 30–45 сек.

---

## ImportCar.kz / imcar.kz (добавлен 2026-05-21)

**Статус**: **PRODUCTION LIVE ✅** (2026-06-08). Все фазы AI-1..AI-6.6 завершены и задеплоены. Обе Supabase-миграции применены. `analyze-car-link` (AI-5C.2) + `admin-calibrations` (AI-6.5) live в продакшне. `vercel deploy --prod` выполнен, live acceptance + real iPhone test пройдены.

**Следующее**: AI-7 Verified Calculation Workflow (подтверждение менеджером, статус verified quote) + сбор реальных данных для AI-5 Accuracy Calibration.

Детали: [[projects/importcar-kz-mvp/next-steps]]

---

## Active project (as of 2026-05-04)

**FlowOps Team** — agency operating system + Linear execution layer

### Status
FlowOps is now the active operating focus. The CRM system exists, Pipeline B / LinkedIn Pain Radar is complete, and Linear has been populated with detailed FlowOps execution issues.

### What was last completed
- FlowOps Linear projects, labels, and issues were created and rewritten with detailed context and acceptance criteria.
- Linear Ops Automation System was specified in Obsidian memory and linked from [[My-tasks]].
- FlowOps CRM is treated as created; future work starts from QA, validation, data hygiene, and production-safe automation wiring.
- Pipeline B / LinkedIn Pain Radar is treated as complete; future work is operational QA and iteration, not initial build.
- Pipeline C v2 / Website Audit Generator is completed operationally end-to-end. v2.1 Prospecting was strengthened on 2026-05-04 for lead volume: Telegram command starts 24 randomized search queries, Firecrawl finds/scrapes sites, Airtable records are created, Telegram approve cards work, and Gmail sends only after `Approve + Send`.
- FlowOps Opportunity Engine skill was created on 2026-05-09 at `/Users/tamerlan/.codex/skills/flowops-opportunity-engine/` to guide trigger-based prospect diagnosis, scoring, outreach, Loom scripts, and compliance-safe B2B outbound. It explicitly excludes Upwork and freelance marketplaces because Upwork already has its own prepared pipeline.

### Immediate blockers / next actions
1. Build or prototype the Linear Ops Automation System from [[Linear/Linear Ops Automation System/implementation-plan]].
2. Run CRM QA / automation-readiness review before scaling n8n/Make workflows.
3. Build the first 5 Demo Library Loom assets.
4. Continue Upwork Radar from the prepared workflow state: import, reconnect credentials, test, then operationalize.
5. Use Website Audit Generator v2.1 operationally after re-import/patch: trigger `/pipeline_c` or `/audit_sites` in Telegram, review/approve cards, monitor replies, and iterate niche/query rotation and teaser copy.
6. Resolve FlowOps duplicate note structure before deleting old folders.

---

## Secondary / watch
- **AI-Powered Woven Label Generator** — client: Griffes Vivienne. Product-flow work is functionally complete through Milestone 5, but remaining risk notes still mention production env / QA / credential rotation. См. [[projects/AI-Powered Woven Label Generator/current-state]] and [[projects/AI-Powered Woven Label Generator/risks]].
- **AI Content Bot** — Telegram бот (@FlowOpstg_bot) для генерации и публикации контента (WF-06..WF-12). Статус: WF-09 Gemini image gen ✅, WF-06 callback routing ✅, WF-10 inline кнопки ✅. Блокер: WF-11 ID нужен для финального флоу. См. [[projects/ai-content-bot/overview]]
- **LinkedIn Outreach Automation** — n8n воркфлоу для личного LinkedIn (WF-00..WF-05). Статус: WF-05 переработан. См. [[projects/linkedin-automation]]
- Upwork freelance work (automation / integrations — episodic)
- Knowledge building: Firecrawl, n8n patterns (see `knowledge/`)
