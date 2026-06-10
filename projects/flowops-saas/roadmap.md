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

## Phase 0: Foundation Audit (Week 0) — CURRENT

**Цель**: Зафиксировать текущее состояние и подготовиться к Phase 1.

### Задачи
- [x] Стратегический roadmap создан (этот документ)
- [ ] Аудит существующего кода (сайт + internal workspace)
- [ ] Решить: нужен ли редизайн homepage или только добавить marketplace?
- [ ] Зафиксировать: какие pipeline-системы делаем первыми (12 MVP)
- [ ] Проверить Supabase: текущие таблицы, data, доступы

**Deliverable**: Готовы начать Phase 1.

---

## Phase 1: Marketplace MVP (Weeks 1–4)

**Цель**: Работающий marketplace с 12–15 pipeline-системами и возможностью принять заказ.

### Блок A: Database (Week 1)
- [ ] Создать Supabase таблицы: `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [ ] Добавить RLS policies (публичное чтение pipelines, запись только через API)
- [ ] Seed data: 7 категорий + 12 pipeline-систем
- [ ] API routes: GET /api/pipelines, GET /api/pipelines/[slug], POST /api/pipeline-order

### Блок B: Marketplace UI (Weeks 1–2)
- [ ] `/os` — Marketplace main page
  - Hero: "Choose your operational system"
  - Category navigation (7 tabs/filters)
  - Pipeline cards grid (name, tagline, setup price, integrations icons, CTA)
  - Search/filter by category
- [ ] `/os/[category]` — Category overview page
  - Category hero
  - Pipeline cards filtered by category
- [ ] `/os/[slug]` — Pipeline detail page
  - Full pipeline info per [[pipeline-catalog]] standard
  - Visual workflow diagram (static SVG или Framer animation)
  - Pricing block (Setup + Monthly)
  - CTA: "Request Deployment" → order form

### Блок C: Order Flow (Week 2)
- [ ] Order form modal/page (per pipeline)
  - Client info (name, email, company, website)
  - Current tools used
  - Business context
  - Specific requirements
  - Agree to pricing
- [ ] POST /api/pipeline-order → Supabase pipeline_orders
- [ ] Telegram notification → FlowOps team via n8n
- [ ] Thank you page / email confirmation (простой, без Resend — можно Supabase email)

### Блок D: Pricing Page (Week 2)
- [ ] `/pricing` — Subscription tiers
  - Maintain / Scale / Operator / Enterprise cards
  - Feature comparison table
  - Bundle section (Sales Stack, Support Stack, etc.)
  - FAQ section
  - CTA: "Start with an audit" → Audit Form

### Блок E: Internal Orders Workspace (Week 3)
- [ ] `/internal/orders` — Orders list
  - Список всех заказов с статусами
  - Filter by status, pipeline, date
  - Quick actions
- [ ] `/internal/orders/[id]` — Order detail
  - Полная информация о клиенте и заказе
  - Status management (New → Qualified → In Progress → Deployed → Active)
  - Internal notes
  - Status history timeline
  - Quick links: email client, Telegram

### Блок F: Homepage Update (Week 3–4)
- [ ] Добавить Marketplace CTA на homepage
- [ ] Обновить hero секцию (упомянуть "40+ operational systems")
- [ ] Добавить featured pipelines section (3–5 карточек)
- [ ] Обновить copy для platform positioning

### Phase 1 Success Criteria
- Marketplace live с 12–15 pipeline-системами
- Первые 3 заказа приняты через форму
- Internal workspace обрабатывает заказы
- Время деплоя MVP: 3–4 недели

---

## Phase 2: First Revenue & Stripe (Weeks 5–10)

**Цель**: Первые платящие клиенты. Stripe integration. Расширение каталога.

### Блок A: First Clients (Weeks 5–6)
- [ ] Direct outreach к 20 целевым бизнесам
- [ ] Предложить beta pricing (20% скидка) для первых 5 клиентов
- [ ] Personal follow-up после каждого аудит-запроса
- [ ] Задеплоить первые 3 pipeline-системы вручную

### Блок B: Stripe Integration (Weeks 6–8)
- [ ] Stripe Checkout для setup fee (one-time payment)
- [ ] Stripe Payment Link как альтернатива (быстрее запустить)
- [ ] После оплаты → автоматически обновляется статус заказа
- [ ] Email confirmation через Resend (настроить)
- [ ] Stripe Subscriptions для monthly (после первой оплаты)
- [ ] Stripe webhooks → update subscription status в Supabase
- [ ] /api/stripe/create-checkout
- [ ] /api/stripe/create-subscription
- [ ] /api/stripe/webhooks

### Блок C: Pipeline Catalog Expansion (Weeks 7–9)
- [ ] Добавить pipeline-системы до 20–25 (приоритет: популярные категории)
- [ ] `/internal/pipelines` — управление каталогом
- [ ] Добавить "Coming Soon" карточки для объявленных pipeline
- [ ] Добавить testimonials / результаты первых клиентов

### Блок D: Email Automation (Week 8)
- [ ] Resend: transactional emails (order confirmation, status updates)
- [ ] n8n workflow WF-02: Status update → email клиенту
- [ ] n8n workflow WF-03: Deployment complete → welcome email
- [ ] n8n workflow WF-05: Subscription renewal reminder

### Блок E: Loyalty Mechanics (Week 9)
- [ ] Stack Bundle Discount logic (2nd pipeline = 10% off setup)
- [ ] Loyalty badge на сайте ("Stack & Save")
- [ ] Bundle pages: Sales Stack, Support Stack, Voice Stack, Full Ops Stack

### Phase 2 Success Criteria
- 5+ платящих клиентов (setup fee received)
- 3+ активных подписок
- MRR > $500/month
- Stripe Checkout работает
- 20+ pipeline в каталоге

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
WEEK 1:
  1. Supabase: создать pipeline_categories + pipelines + pipeline_orders таблицы
  2. API: GET /api/pipelines, GET /api/pipelines/[slug]
  3. Seed: 7 категорий + 12 pipeline-систем
  4. API: POST /api/pipeline-order с rate limiting

WEEK 2:
  5. /os страница (marketplace main) с категориями и card grid
  6. /os/[slug] pipeline detail page
  7. Order form + POST /api/pipeline-order
  8. Telegram notification via n8n при новом заказе
  9. /pricing страница с тарифами

WEEK 3:
  10. /internal/orders list page
  11. /internal/orders/[id] detail + status management
  12. Status history timeline
  13. Homepage обновление (добавить marketplace CTA + featured pipelines)

WEEK 4:
  14. /os/[category] category pages
  15. Mobile responsive polish
  16. SEO: meta tags для всех новых страниц
  17. QA + E2E test критических flows
  18. Production deploy

WEEK 5–6:
  19. Первый outreach + первые клиенты
  20. Stripe Payment Link (быстрее чем full integration)

WEEK 7–8:
  21. Full Stripe Checkout integration
  22. Stripe Subscriptions
  23. Email via Resend

WEEK 9–10:
  24. Каталог расширить до 20–25 pipelines
  25. Bundle pages
  26. Loyalty mechanics

WEEKS 11+:
  27. Supabase Auth
  28. Client portal MVP
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

**Запускать Phase 1 немедленно.**

Не ждать идеального дизайна — сделать достаточно хорошо за 3–4 недели.  
Первые 5 клиентов важнее идеального UI.  
Деньги от первых клиентов инвестировать в дизайн Phase 2.

Самый большой риск — потратить 2 месяца на "идеальный" marketplace и не получить ни одного клиента.  
Самый быстрый путь к валидации — 12 pipeline-карточек + рабочая форма заказа + личный outreach к 20 бизнесам.

**Через 30 дней** у FlowOps должны быть первые 2–3 заказа.  
**Через 60 дней** — первые 3–5 платящих клиентов.  
**Через 90 дней** — MRR > $1,000 и понимание, какие pipeline-системы продаются лучше всего.

Тогда Phase 2–3 строятся на реальных данных, а не гипотезах.
