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

---

## FlowOps SaaS — AI Operations Platform (добавлен 2026-06-10)

**Статус**: PLANNING — стратегический роадмап создан. Готов к Phase 1 разработке.

**Что это**: SaaS/Platform с marketplace из 40 готовых AI/automation pipeline-систем для бизнеса. Гибридная модель: setup fee + monthly subscription. Premium B2B positioning (Linear/Vercel quality).

**Phase 1 цель (4 недели)**:
- Supabase: pipeline_categories + pipelines + pipeline_orders таблицы
- `/os` marketplace + `/os/[slug]` detail pages
- Order request form + Telegram notifications
- `/pricing` страница
- `/internal/orders` workspace
- Seed: 12–15 pipeline-систем

**Следующий шаг**: Аудит существующего кода → создать DB схему → начать `/os` страницу

**Память**: [[projects/flowops-saas/overview]] | [[projects/flowops-saas/roadmap]] | [[projects/flowops-saas/pipeline-catalog]] | [[projects/flowops-saas/pricing]]

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
