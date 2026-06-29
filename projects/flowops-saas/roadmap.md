# FlowOps SaaS — Full Roadmap

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[pipeline-catalog]]
- [[pricing]]
- [[technical-architecture]]

---

## Strategic Answer

**Самый умный путь**: не перестраивать всё с нуля, а добавить Marketplace layer поверх существующего сайта. Сначала 12 pipeline-карточек, ручная обработка заказов через расширенный internal workspace, Telegram как дешёвая notification система. Только после первых 5–10 платящих клиентов инвестировать в Stripe, client portal и AI layer.

**Ключевой принцип**: каждая фаза должна быть прибыльной или хотя бы окупаемой. Не строим для гипотетических клиентов.

---

## Current Stage — Phase 2A: Sales Readiness COMPLETE / Phase 2C–F: In Progress

**Status as of 2026-06-29**: All Phase 2A code tasks complete. Phase 2C catalog expansion done (25 systems + 7 coming soon + /internal/pipelines). Phase 2E bundle/stack pages live (3 stacks). Hero illustration redesigned via Figma. Phase 2F Trust Layer is now required before scaled owner-focused outreach, because business owners need proof of competence and risk reduction before trusting FlowOps with operations.

**Active objective**: add owner-trust/proof layer, then send first outreach batch to the 20-account seed list. Next code priority after trust layer: Stripe/Resend live keys OR Phase 3 planning.

### Verified Done (Phase 2A–C–E)
- [x] Production URL: `https://flowops-saas.vercel.app`
- [x] Vercel deployment smoke passed
- [x] Supabase remote migrations applied through 25-system catalog
- [x] Public marketplace/order flow works
- [x] Internal order workspace protected by `INTERNAL_ACCESS_KEY`
- [x] Telegram notifications verified
- [x] QA production order cleanup verified
- [x] `/os` search/filter interaction deployed
- [x] ROI/payback blocks deployed on pipeline detail pages
- [x] Post-submit thank-you/next-step flow deployed
- [x] First-client beta offer package prepared
- [x] Outreach seed list/message package prepared (20 accounts)
- [x] Delivery checklists for first 3 flagship pipelines prepared
- [x] Homepage/case-study sales copy polished and deployed
- [x] `/internal/audits` list + detail + status flow (June 23)
- [x] Audit request form (`#audit` section, POST `/api/audit-request`) (June 23)
- [x] Coming Soon cards on `/os` — 7 announced systems (June 23)
- [x] Site footer on all 4 public pages (June 23)
- [x] Rate limiting on `/api/pipeline-order` + `/api/audit-request` — Supabase-backed (June 23)
- [x] `/internal/pipelines` catalog management page (June 24)
- [x] Testimonials section on homepage — 3 placeholder cards (June 24; real data pending first clients)
- [x] `/stacks` overview page — 3 bundles with savings badges, system tags, pricing (June 25)
- [x] `/stacks/[slug]` detail pages — Sales Stack, Support Stack, Voice Operations (June 25)
- [x] Stacks link in SiteHeader + SiteFooter (June 25)
- [x] Homepage → "View system stacks — save up to 23%" link (June 25)
- [x] Pricing page bundle cards → link to `/stacks/[slug]` (June 25)
- [x] Hero illustration redesigned: Figma-sourced chaos → FlowOps → organized (post June-25 commits)
- [x] FlowOps SVG favicon replacing default Next.js icon

### Active Focus
- [ ] Add Phase 2F Trust Layer before scaled outreach
- [ ] Manual verification/enrichment of the 20-account seed list before sending
- [ ] Start first outreach batch

### Explicitly Deferred
- [ ] Stripe/Resend live verification until real keys or first payment moment
- [ ] Client portal until enough client demand exists
- [ ] Self-serve pipeline deployment

---

## Phase 0: Foundation Audit (Week 0) — COMPLETE

### Задачи
- [x] Стратегический roadmap создан (этот документ)
- [x] Аудит существующего кода (сайт + internal workspace)
- [x] Решить: нужен редизайн homepage + marketplace layer
- [x] Зафиксировать и реализовать первые pipeline-системы MVP
- [x] Проверить Supabase: текущие таблицы, data, доступы

**Deliverable**: Готовы начать Phase 1.

---

## Phase 1: Marketplace MVP (Weeks 1–4) — COMPLETE

**Цель**: Работающий marketplace с 12–15 pipeline-системами и возможностью принять заказ.

### Блок A: Database (Week 1)
- [x] Создать Supabase таблицы: `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [x] Добавить RLS policies (публичное чтение pipelines, запись только через API)
- [x] Seed data: 7 категорий + 15 pipeline-систем
- [x] API routes: GET /api/pipelines, GET /api/pipelines/[slug], POST /api/pipeline-order

### Блок B: Marketplace UI (Weeks 1–2)
- [x] `/os` — Marketplace main page
  - Hero: "Choose your operational system"
  - Category navigation (7 tabs/filters)
  - Pipeline cards grid (name, tagline, setup price, integrations icons, CTA)
  - Category navigation ready; interactive search/filter remains Phase 2A polish
- [x] `/os/[category]` — Category overview page
  - Category hero
  - Pipeline cards filtered by category
- [x] `/os/[slug]` — Pipeline detail page
  - Full pipeline info per [[pipeline-catalog]] standard
  - Visual workflow diagram (static SVG или Framer animation)
  - Pricing block (Setup + Monthly)
  - CTA: "Request Deployment" → order form

### Блок C: Order Flow (Week 2)
- [x] Order form modal/page (per pipeline)
  - Client info (name, email, company, website)
  - Current tools used
  - Business context
  - Specific requirements
  - Agree to pricing
- [x] POST /api/pipeline-order → Supabase pipeline_orders
- [x] Telegram notification → FlowOps team via direct Telegram env
- [ ] Thank-you page / polished post-submit next-step experience

### Блок D: Pricing Page (Week 2)
- [x] `/pricing` — Subscription tiers
  - Maintain / Scale / Operator / Enterprise cards
  - Feature comparison / value explanation
  - Bundle section (Sales Stack, Support Stack, etc.)
  - FAQ section optional polish
  - CTA: "Start with an audit" → Audit Form

### Блок E: Internal Orders Workspace (Week 3)
- [x] `/internal/orders` — Orders list
  - Список всех заказов с статусами
  - Filter by status, pipeline, date remains future internal polish
  - Quick actions
- [x] `/internal/orders/[id]` — Order detail
  - Полная информация о клиенте и заказе
  - Status management (New → Qualified → In Progress → Deployed → Active)
  - Internal notes
  - Status history timeline
  - Quick links: email client, Telegram

### Блок F: Homepage Update (Week 3–4)
- [x] Добавить Marketplace CTA на homepage
- [x] Обновить hero секцию под FlowOps OS marketplace
- [x] Добавить featured pipelines section
- [x] Обновить copy для platform positioning
- [x] Добавить proof/case-study section

### Phase 1 Success Criteria
- [x] Marketplace live с 12–15 pipeline-системами
- [x] Order form verified with production QA order
- [x] Internal workspace обрабатывает заказы
- [x] Production deploy completed

---

## Phase 2: First Revenue & Stripe (Weeks 5–10) — ACTIVE

**Цель**: Первые платящие клиенты. Stripe integration. Расширение каталога.

### Блок A: First Clients / Sales Readiness (Weeks 5–6) — CODE DONE / OUTREACH PENDING
- [x] Refine homepage and pipeline detail copy into final sales-ready language
- [x] Add search/filter interaction for `/os`
- [x] Add thank-you / next-step experience after public order submission
- [x] Prepare 5 flagship pipeline beta offers (first-client package)
- [x] Outreach seed list + message package prepared (20 целевых аккаунтов)
- [ ] Add owner-trust/proof layer before scaling outreach: risk-reduction copy, proof surfaces, implementation examples, and clear audit expectations
- [ ] Send first outreach batch (manually verify/enrich contacts first)
- [ ] Предложить beta pricing (20% скидка) для первых 5 клиентов
- [ ] Personal follow-up после каждого аудит-запроса
- [ ] Задеплоить первые 3 pipeline-системы вручную

### Блок B: Stripe Integration (Weeks 6–8) — CODE SCAFFOLD DONE / LIVE VERIFICATION DEFERRED
- [x] Stripe Checkout route для setup fee (one-time payment)
- [ ] Stripe Payment Link как альтернатива (быстрее запустить)
- [x] После оплаты → webhook scaffold can update order/payment state
- [x] Email confirmation hook через Resend scaffold
- [x] Stripe Subscriptions route для monthly
- [x] Stripe webhooks → update subscription status в Supabase scaffold
- [x] `/api/stripe/create-setup-checkout`
- [x] `/api/stripe/create-subscription-checkout`
- [x] `/api/stripe/webhook`
- [ ] Add real `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `RESEND_API_KEY`
- [ ] Complete live Stripe/Resend verification

### Блок C: Pipeline Catalog Expansion (Weeks 7–9)
- [x] Добавить pipeline-системы до 20–25 (приоритет: популярные категории)
- [x] `/internal/pipelines` — управление каталогом (June 24, 2026)
- [x] Добавить "Coming Soon" карточки для объявленных pipeline — 7 systems (June 23, 2026)
- [x] Добавить proof/case-study section
- [x] Testimonials section — 3 placeholder cards на homepage (June 24, 2026; реальные данные появятся после первых клиентов)
- [ ] Заменить placeholder testimonials реальными результатами клиентов

### Блок F: Trust Layer / Proof of Work (Before Scaled Outreach)
**Goal**: Make business owners feel FlowOps is competent, careful, and safe to trust with real operations before they book an audit or request a deployment.

- [ ] Add homepage section: "Built for business owners, not automation hobbyists"
  - Emphasize operational discipline, business-process understanding, and owner-level clarity
  - Avoid generic AI hype; frame FlowOps as risk-aware operations infrastructure
- [ ] Add homepage section: "Our deployment process protects your operations"
  - Audit/process review
  - Workflow map
  - Owner approval before deployment
  - Test run / manual QA
  - Monitoring and support after launch
- [ ] Add homepage section: "Proof of work"
  - Use implementation examples and mini-case studies, not fake outcome claims
  - Show actual or mock-safe product surfaces: audit workspace, pipeline/order dashboard, Telegram/status notification, workflow diagram
  - Include concrete business scenarios such as missed-call recovery, dental lead follow-up, real estate inquiry routing, support inbox triage
- [ ] Add trust badges/signals where relevant
  - Manual QA before deployment
  - Private business data handling
  - Owner-approved workflow map
  - Rollback/monitoring plan
  - Monthly monitoring included
  - n8n/internal automation engine hidden from clients
- [ ] Add "What happens after you request an audit" near the audit CTA
  - 15-minute business process review
  - 2–3 practical automation opportunities
  - Simple implementation map
  - No deployment until owner approval
- [ ] Add before/after operational examples to priority pipeline detail pages
  - Before: manual follow-up, missed WhatsApp/phone leads, status confusion, owner chasing updates
  - After: automated response, routing, reminders, escalation, reporting
- [ ] Replace or clearly reframe placeholder testimonials
  - Until real clients exist, prefer "implementation examples" over fictional testimonials
  - After first 3 clients, convert real outcomes into case studies with permission
- [ ] Add founder/operator credibility block
  - Explain FlowOps experience through built systems, workflow count, CRM/Telegram/AI/n8n/Supabase implementation capability, and delivery discipline
  - Avoid overclaiming enterprise credentials until proven

### Phase 2F Success Criteria
- [ ] Homepage trust layer shipped and responsive
- [ ] Audit CTA explains next steps clearly
- [ ] At least 3 mini-case/implementation examples visible
- [ ] At least 3 real product/proof surfaces visible
- [ ] Placeholder testimonials removed, reframed, or clearly separated from real client claims
- [ ] Priority pipeline pages include before/after owner-facing examples
- [ ] First outreach batch points prospects to a page that feels credible for business owners

### Блок D: Email Automation (Week 8)
- [x] Resend: transactional email helper scaffold
- [ ] Resend: live transactional emails (order confirmation, status updates)
- [ ] n8n workflow WF-02: Status update → email клиенту
- [ ] n8n workflow WF-03: Deployment complete → welcome email
- [ ] n8n workflow WF-05: Subscription renewal reminder

### Блок E: Loyalty Mechanics (Week 9) — PARTIALLY DONE
- [ ] Stack Bundle Discount logic (2nd pipeline = 10% off setup) — не реализовано, только статические страницы
- [x] Loyalty badge на сайте — "Save X%" badge на /stacks страницах (June 25, 2026)
- [x] Bundle pages: Sales Stack, Support Stack, Voice Operations — 3 из 4 (June 25, 2026)
- [ ] Full Ops Stack bundle page — не реализовано

### Phase 2 Success Criteria
- [ ] 5+ платящих клиентов (setup fee received)
- [ ] 3+ активных подписок
- [ ] MRR > $500/month
- [ ] Stripe Checkout live verification passed
- [x] 20+ pipeline в каталоге

---

## Phase 3: Client Portal (Weeks 11–20)

**Цель**: Клиент видит свои активные системы, может управлять подпиской.

### Блок A: Auth Layer (Weeks 11–12)
- [ ] Supabase Auth (email magic link или password)
- [ ] Создать client accounts после первого деплоя
- [ ] Link клиент → его pipeline_orders
- [ ] RLS policies для клиентских данных

### Блок B: Client Portal MVP (Weeks 12–16)
- [ ] `/portal` — Login page
- [ ] `/portal/dashboard` — Active pipeline systems
  - Список активных pipeline с статусом (Active/Maintenance/Issue)
  - Health score per pipeline
  - Last activity timestamp
  - Quick: "Request support", "View details"
- [ ] `/portal/pipelines/[id]` — Pipeline instance detail
  - Status + logs (simplified)
  - Deployment date, next check date
  - Support history
- [ ] `/portal/billing` — Subscription management
  - Current plan
  - Invoice history
  - Next billing date
  - Upgrade/downgrade plan
- [ ] `/portal/support` — Support ticket creation

### Блок C: Operations Monitoring (Weeks 16–18)
- [ ] n8n workflow WF-04: Weekly health check → update pipeline health scores
- [ ] Alert system: если pipeline не работает → notify FlowOps team immediately
- [ ] Client visible status updates (через Supabase realtime)

### Блок D: AI Audit Reports (Weeks 18–20)
- [ ] После завершения аудита → AI генерирует report с рекомендациями
- [ ] Рекомендации = конкретные pipeline-системы с расчётом ROI
- [ ] Report доступен в portal

### Phase 3 Success Criteria
- 10+ активных клиентов с доступом к portal
- MRR > $2,000/month
- Client churn < 10%
- NPS > 7

---

## Phase 4: SaaS Maturity (Months 6–12)

**Цель**: Настоящий SaaS-продукт с масштабируемой delivery системой.

### Блок A: Pipeline Catalog — Full 40
- [ ] Каталог расширить до 35–40 pipeline-систем
- [ ] Все категории заполнены
- [ ] "Trending" и "Popular" метки
- [ ] Pipeline roadmap (публичный)

### Блок B: Delivery Automation
- [ ] Стандартизированные n8n templates для каждого pipeline типа
- [ ] Semi-automated onboarding: клиент заполняет tech form → автоматически генерируется plan
- [ ] Deployment checklist per pipeline (internal)
- [ ] Automated testing после деплоя

### Блок C: AI Operations Layer
- [ ] AI-powered audit recommendations (Claude API)
- [ ] Pipeline health anomaly detection
- [ ] Proactive improvement suggestions
- [ ] AI assistant в client portal ("What should I automate next?")

### Блок D: Analytics & Intelligence
- [ ] Internal analytics: какие pipeline продаются лучше
- [ ] Client retention dashboard
- [ ] Revenue analytics (MRR, churn, LTV)
- [ ] Pipeline performance benchmarks

### Блок E: Enterprise Tier
- [ ] Enterprise pricing ($2,000+ setup, custom subscription)
- [ ] Dedicated account manager
- [ ] Custom SLA
- [ ] White-label option (v2)
- [ ] Multi-team workspace

### Phase 4 Success Criteria
- MRR > $10,000/month
- 30+ active clients
- 40 pipeline-систем в каталоге
- < 5% monthly churn
- Average client lifespan > 12 months

---

## Phase 5: Platform Expansion (Year 2)

**Цель**: Настоящая платформа. Возможно — внешние поставщики pipeline.

- Marketplace для внешних разработчиков pipeline (ecosystem)
- API access для клиентов (build on top of FlowOps)
- Mobile app (iOS/Android) для мониторинга
- Integrations directory
- Community / FlowOps Academy
- Partnerships с CRM vendors, software companies

---

## UX / Page Architecture

### Design Principles
- Dark, deep, graphite base (#0A0A0B, #111114)
- Electric blue accents (#2563EB, #3B82F6)
- Amber operational highlights (#F59E0B) для статусов и alerts
- Typography: Inter / Geist — clean, technical
- Motion: subtle, purposeful (no decorative spin animations)
- Density: information-rich без перегруженности
- Feel: Linear + Vercel + Stripe Dashboard качество

### Marketplace UI Principles
- Pipeline cards: dark bordered cards с иконкой категории, ценой, integration badges
- Hover state: subtle glow / border highlight
- Category nav: horizontal tabs или left sidebar (зависит от viewport)
- Detail pages: два колонки (info left, CTA/pricing sticky right)
- Mobile: полностью responsive, cards стек

### Animation Principles
- Page transitions: subtle fade/slide (Framer Motion)
- Scroll: Lenis smooth scroll
- Cards: subtle scale on hover (1.02)
- Pipeline workflow diagram: sequential reveal
- NO: spinning loaders, excessive particle effects, crypto animations

---

## Internal Operations Workflow

### Когда приходит новый заказ:

```
1. Клиент заполняет форму на /os/[slug]
2. POST /api/pipeline-order → Supabase pipeline_orders (status: 'new')
3. n8n WF-01: Telegram уведомление команде FlowOps
4. [Manual] Команда проверяет заказ в /internal/orders/[id]
5. [Manual] Первичный звонок/сообщение клиенту (квалификация)
6. [Manual] Статус: new → qualified
7. [Manual] Согласовать детали (инструменты клиента, доступы)
8. [Manual] Статус: qualified → in_progress
9. [Manual] Деплой pipeline в n8n (по шаблону)
10. [Manual] Тестирование workflow
11. [Manual] Статус: in_progress → deployed
12. n8n WF-03: Email клиенту "Your pipeline is live"
13. [Manual/Auto] Создать subscription запись
14. [Phase 2] Stripe subscription активируется
15. Статус: deployed → active
16. [Ongoing] Monthly health checks, обновления, поддержка
```

### Delivery Time Targets
- Entry pipeline (Tier 1): 1–3 дня
- Standard pipeline (Tier 2): 3–5 дней
- Complex pipeline (Tier 3): 7–10 дней
- Enterprise: по договорённости

---

## Prioritized Implementation Order

```
DONE:
  1.  Supabase: pipeline_categories + pipelines + pipeline_orders + order_status_history
  2.  API: GET /api/pipelines, GET /api/pipelines/[slug], POST /api/pipeline-order
  3.  Catalog: 25 systems live in code and Supabase
  4.  /os marketplace, /os/[slug] details, /pricing
  5.  /internal/orders list/detail + status management
  6.  Telegram notifications for new orders
  7.  Homepage redesign + marketplace CTA + proof section
  8.  Internal access hardening
  9.  Vercel production deploy + smoke test
  10. Stripe/Resend code scaffolds
  11. Search/filter interaction on /os + ROI/payback blocks + thank-you flow
  12. First-client beta package + outreach seed list (20 accounts) + delivery checklists
  13. Homepage sales copy polish
  14. /internal/audits list + detail + status flow + audit_requests Supabase migration
  15. Audit request form (#audit section) + POST /api/audit-request
  16. Coming Soon cards on /os (7 announced systems)
  17. Site footer on all public pages
  18. Rate limiting (Supabase-backed, 3 req/hr per IP+email)
  19. /internal/pipelines catalog management page
  20. Testimonials section on homepage (3 placeholder cards)
  21. /stacks overview + /stacks/[slug] detail pages (3 bundles, savings badges)
  22. Stacks nav links in SiteHeader + SiteFooter
  23. Hero illustration redesigned (Figma-sourced) + FlowOps SVG favicon

NOW:
  24. Send first outreach batch (manually verify/enrich the 20-account seed list first)

NEXT AFTER FIRST PAYMENT / KEYS:
  25. Stripe Payment Link or live Checkout verification
  26. Resend live transactional emails
  27. Subscription verification

LATER:
  28. Full Ops Stack bundle page (4th stack)
  29. Stack Bundle Discount logic (2nd pipeline = 10% off setup)
  30. Real testimonials (replace placeholders after first clients)
  31. Supabase Auth
  32. Client portal MVP
```

---

## What NOT To Build (Yet)

- ❌ Self-serve automated pipeline deployment
- ❌ Full client portal before 10 paying clients
- ❌ Complex AI layer before product-market fit
- ❌ White-label version
- ❌ Mobile app
- ❌ External marketplace for 3rd party pipeline providers
- ❌ Usage-based billing (too complex for MVP)
- ❌ Real-time pipeline logs in client portal (Phase 3 only)
- ❌ Multi-user workspace per client (Phase 4)
- ❌ API access for clients

---

## Success Metrics by Phase

| Metric | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|--------|---------|---------|---------|---------|
| Pipelines in catalog | 12–15 | 20–25 | 30–35 | 40 |
| Paying clients | 1–3 | 5–10 | 10–20 | 30+ |
| Active subscriptions | 0–2 | 3–8 | 10–20 | 30+ |
| MRR | $0–$500 | $500–$2K | $2K–$8K | $10K+ |
| Avg deploy time | <7 days | <5 days | <4 days | <3 days |
| Client churn (monthly) | N/A | <20% | <10% | <5% |

---

## Risks Summary (Top 5)

1. **Slow first sales** → Mitigate: direct outreach, beta pricing для первых 5
2. **Pricing too high** → Mitigate: entry-level pipelines от $299, ROI calculator
3. **Delivery bottleneck** → Mitigate: стандартизация workflows, ограничить capacity
4. **Cheap agency perception** → Mitigate: premium design, platform copy, case studies
5. **Subscription churn** → Mitigate: monthly value delivery, proactive improvements

---

## Final Recommendation

**Текущая рекомендация: не уходить в Phase 3 portal. Дожать Phase 2A: sales readiness + первые клиенты.**

Marketplace уже live, поэтому главный риск сместился с разработки на спрос.  
Самый быстрый путь к валидации теперь: conversion-ready сайт + 5 flagship offers + direct outreach к 20 бизнесам + ручной delivery первых pipeline.

**Следующие 7 дней**: привести live сайт к sales-ready состоянию и подготовить outreach package.  
**Следующие 30 дней**: получить первые 2–3 заказа через форму/личный outreach.  
**Следующие 60 дней**: закрыть 3–5 платящих клиентов, после чего Stripe/Resend/client portal получают реальные требования, а не строятся на гипотезах.
