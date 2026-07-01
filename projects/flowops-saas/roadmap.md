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
- [[automation-card-audit-brief]]

---

## Strategic Answer

**Самый умный путь**: не перестраивать всё с нуля, а добавить Marketplace layer поверх существующего сайта. Сначала 12 pipeline-карточек, ручная обработка заказов через расширенный internal workspace, Telegram как дешёвая notification система. Только после первых 5–10 платящих клиентов инвестировать в Stripe, client portal и AI layer.

**Ключевой принцип**: каждая фаза должна быть прибыльной или хотя бы окупаемой. Не строим для гипотетических клиентов.

---

## Current Stage — MVP Sales Validation: Portal / Chat / Deal Room Deferred

**Status as of 2026-06-30**: All Phase 2A code tasks complete. Phase 2C catalog expansion done (25 systems + 7 coming soon + /internal/pipelines). Phase 2E bundle/stack pages live. Phase 2F trust layer and priority pipeline before/after examples are complete. Phase 3 account/chat/deal-room work was explored and partially implemented, but the user reversed MVP scope on June 30, 2026.

**Active objective**: return the buyer-facing MVP to simple sales validation: public audit, public system request/order form, internal order workspace, manual follow-up, first outreach batch. Account system, chat, and deal room are required future platform features, but not part of the current MVP.

**Scope update**: Portal/auth/chat/deal-room code and docs should be preserved as future infrastructure, not deleted, unless the user explicitly requests removal.

**Latest preview**: `https://flowops-saas-pvoewrzoy-tamertt931-8560s-projects.vercel.app` (`dpl_92thMKzyip2qEvXBSi1MtV37EiKu`) contains the MVP scope reversal. Production `flowops.agency` still needs promotion if this preview is accepted.

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
- [x] Add Phase 2F Trust Layer before scaled outreach
- [x] Phase 3 portal/deal-room foundation explored and partially implemented; now deferred out of MVP
- [x] Restore public system-page ordering to `/api/pipeline-order` without requiring portal auth — preview deployed June 30
- [x] Remove Portal/deal-room from public navigation and buyer-facing CTA copy — preview deployed June 30
- [ ] Promote MVP scope-reversal preview to production if accepted
- [ ] Run [[automation-card-audit-brief]] before scaled outreach: verify every card's real buyer need, enrich descriptions, recheck pricing, and add unified in-card illustrations
- [ ] Manual verification/enrichment of the 20-account seed list before sending
- [ ] Start first outreach batch

### Explicitly Deferred
- [ ] Stripe/Resend live verification until real keys or first payment moment
- [x] Client accounts/deal room deferred out of MVP by user on June 30, 2026; keep as future platform layer
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

### Блок C2: Automation Card Audit & Upgrade (Before Scaled Outreach)
**Goal**: Make every automation card feel like a useful, credible, productized FlowOps system with clear demand, rich explanation, defensible pricing, and a consistent visual language.

Source of truth: [[automation-card-audit-brief]].

- [ ] Inventory all 25 live pipeline cards and 7 coming-soon cards from `src/lib/catalog.ts`.
- [ ] For every card, verify whether people actually need it:
  - [ ] target buyer and buyer role;
  - [ ] vertical fit;
  - [ ] urgency/frequency/cost of the pain;
  - [ ] keep/reposition/merge/move-to-coming-soon/remove recommendation.
- [ ] Expand every card description:
  - [ ] sharper tagline;
  - [ ] 2–3 sentence buyer-facing description;
  - [ ] trigger → automation steps → result;
  - [ ] setup scope;
  - [ ] monthly monitoring/support;
  - [ ] integrations;
  - [ ] deployment time;
  - [ ] realistic outcome/ROI logic.
- [ ] Recheck pricing card-by-card against current market references:
  - [ ] comparable custom automation/AI agency setup ranges;
  - [ ] FlowOps recommended setup/monthly;
  - [ ] productized discount target of about 30% below comparable custom builds where safe;
  - [ ] margin/delivery risk note;
  - [ ] update stack/bundle pricing after card price changes.
- [ ] Add a small illustration for every live automation card:
  - [ ] consistent with `/Users/tamerlan/Downloads/flowops-custom-workflow.svg`;
  - [ ] consistent with `/Users/tamerlan/Downloads/flowops-request-to-proof-v2_1.svg`;
  - [ ] consistent with `/Users/tamerlan/Downloads/flowops-request-to-proof.svg`;
  - [ ] pale blue/white canvas, soft shadows, rounded nodes, dotted connectors, status chips, sky/mint/peach/amber accents;
  - [ ] illustration must show the actual workflow concept, not decoration.
- [ ] Update UI/schema only after the audit table is reviewed or clearly aligned with the brief.
- [ ] QA desktop/mobile on `/os`, `/os/[slug]`, `/pricing`, and `/stacks`.

### Automation Card Audit Success Criteria
- [ ] Every live card has clear buyer need, pain, workflow, outcome, price rationale, and illustration.
- [ ] No card reads like a generic automation service or Fiverr-style listing.
- [ ] Pricing is credible, internally consistent, and reflects productized deployment economics.
- [ ] Copy does not overpromise ROI or imply unsupported guarantees.
- [ ] Visuals match the existing FlowOps SVG/product style.
- [ ] First outreach batch points prospects to a marketplace that feels complete and premium.

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

## Future Phase 3: Client Accounts + Deal Room — DEFERRED OUT OF MVP

**Цель будущей фазы**: Клиент может создать аккаунт, заказать/предложить автоматизацию внутри сайта, вести обсуждение с FlowOps в одном workspace, затем видеть активные системы, статусы, поддержку и billing. Portal is the canonical source of truth; email/Telegram are notifications only.

**June 30, 2026 MVP decision**: account system, chat, and deal room are not needed for the current MVP. Keep this section as the future product target, but do not treat it as active MVP scope. Current MVP returns to unauthenticated public audit + public system request/order form + internal order workspace + manual follow-up.

Execution source of truth:
`/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-client-accounts-deal-room-plan.md`

Quality target:
`/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md`

### Future Phase 3 Foundation — Built/Explored, Now Deferred
- [x] Supabase Auth UI direction changed to email/password + Google OAuth, not magic-link-first
- [x] Phase 3 migration applied: `clients`, `client_pipeline_instances`, `automation_requests`, `request_messages`, `request_status_history`
- [x] RLS policies for client-owned data and internal-note hiding
- [x] Portal routes:
  - [x] `/portal`
  - [x] `/portal/dashboard`
  - [x] `/portal/new-request`
  - [x] `/portal/requests`
  - [x] `/portal/requests/[id]`
  - [x] `/portal/pipelines/[id]`
  - [x] `/portal/billing`
  - [x] `/portal/support`
- [x] Portal APIs:
  - [x] `GET /api/portal/me`
  - [x] `GET /api/portal/dashboard`
  - [x] `POST /api/portal/requests`
  - [x] `GET /api/portal/requests`
  - [x] `GET /api/portal/requests/[id]`
  - [x] `POST /api/portal/requests/[id]/messages`
  - [x] `GET /api/portal/pipelines/[id]`
- [x] Internal request workspace:
  - [x] `/internal/requests`
  - [x] `/internal/requests/[id]`
  - [x] request status update
  - [x] assignment
  - [x] client-visible FlowOps replies
  - [x] internal-only notes
  - [x] request-to-order conversion
- [x] Internal APIs protected by `INTERNAL_ACCESS_KEY`
- [x] Public system detail pages created portal deal-room requests in the June 29/30 build; superseded by June 30 MVP reversal, public system pages should now use `/api/pipeline-order` again
- [x] Notifications added for new requests, client messages, FlowOps replies, and status updates through existing Telegram/webhook/Resend paths when configured

### Future Phase 3 Acceptance / Production Setup — Deferred
- [ ] Configure Supabase email/password confirmation behavior when portal is reactivated
- [ ] Configure Supabase Auth redirect URLs for `/portal/dashboard`
- [x] Configure Google OAuth provider for production domain (user reported Google auth works)
- [ ] Create one test auth user + client account when portal is reactivated
- [ ] Run authenticated browser acceptance when portal is reactivated:
  - email/password signup
  - email/password sign-in
  - Google sign-in
  - profile setup
  - create request
  - request list/detail
  - client message
  - FlowOps internal reply/status/note
  - convert to order
  - verify `/internal/orders/[id]`
- [ ] Verify RLS and API boundaries when portal is reactivated:
  - unauthenticated portal API returns 401
  - client A cannot read client B request
  - client cannot read internal notes
  - internal API without key returns 401
  - service-role key not exposed to client bundle

### Future Quality Bar — Account System
- [ ] Account page with personal profile, company profile, notification preferences, security, connected context, and privacy/data-handling summary
- [ ] Profile fields: contact name, work email, company, role/title, website, business type, country/time zone, preferred contact channel
- [ ] Optional account context: phone/WhatsApp, CRM used, current tools, team size, lead volume, main bottleneck, urgency
- [ ] Auth states: signup, login, Google OAuth, password reset, missing confirmation, expired session, provider disabled, network failure
- [ ] Account UX should keep setup short before first request and ask deeper operational questions inside request intake

### Future Quality Bar — Dashboard
- [ ] Dashboard answers five questions immediately:
  - what is active?
  - what needs client action?
  - what did FlowOps update recently?
  - what is being scoped/deployed?
  - where does the client start a new request?
- [ ] Modules: action-required queue, active systems summary, open deal rooms, recent activity, upcoming milestones, billing summary, support shortcut
- [ ] States: new account, no requests, request awaiting FlowOps, request awaiting client, multiple open requests, active client, billing pending/overdue, auth/session error

### Future Quality Bar — Request Intake
- [ ] Request types: existing pipeline, custom automation, support, upgrade/additional system, audit follow-up
- [ ] Required request fields: title, type, desired outcome, current process, tools involved, trigger/event, current manual steps, output recipient, urgency, success criteria
- [ ] Optional fields: volume, examples, links, constraints, launch date, budget comfort range
- [ ] Future pipeline detail CTA can prefill pipeline slug/context and redirect directly into the deal room after submit; not for current MVP

### Future Quality Bar — Deal Room
- [ ] Deal room layout: header, conversation/activity, scope side panel, next action, timeline, proposal state, key links
- [ ] Header: request number, title, status, last update, assigned FlowOps owner, current next action
- [ ] Side panel: request type, selected pipeline, desired outcome, tools, urgency, current stage, next milestone, proposal/payment state when available
- [ ] Client-visible statuses: New, Reviewing, Scoping, Proposal ready, Approved, Deploying, Live, Needs input, Paused, Closed
- [ ] Every open deal room has one clear next action: waiting for FlowOps, waiting for client, proposal approval, payment, build, QA, launch confirmation, monitoring
- [ ] Scope section: problem, desired outcome, included workflow, excluded workflow, tools, inputs, outputs, approval gates, edge cases, data access needed, launch criteria
- [ ] Proposal section: recommended system, setup fee, monthly plan, included/excluded scope, timeline, required access, risk notes, approval CTA
- [ ] Delivery section after approval: access collection, build, internal QA, client review, launch, monitoring, active
- [ ] Decision log/system events: scope approved, price approved, access provided, launch date confirmed, workflow exclusions accepted, change requests accepted/rejected

### Future Quality Bar — Chat
- [ ] Chat is structured around requests, not a generic messenger
- [ ] Message types:
  - client message
  - FlowOps message
  - system status update
  - proposal sent
  - approval recorded
  - access requested
  - launch update
  - internal note
  - assignment change
  - risk flag
- [ ] Message behavior: sender labels, chronological order, internal note separation, loading/error/retry states, duplicate-send prevention, body validation, line breaks, preserved draft on failure
- [ ] Client composer: clear response expectation and suggested context prompts when helpful
- [ ] Internal composer: client-visible/internal-note toggle, warning before client-visible reply, recent client context visible while replying
- [ ] Notifications: new request, new client message, FlowOps reply, status change, proposal sent, approval needed, support update, billing action
- [ ] Email links must deep-link back to the exact deal room

### Future Quality Bar — Internal Operations
- [ ] Internal inbox filters: status, owner, waiting state, last activity, unread client messages, overdue requests, company/request search
- [ ] Internal request detail: client profile, request scope, client messages, internal notes, status controls, assignment, proposal state, convert-to-order, related order/system links, activity history
- [ ] Internal safety: internal notes never returned by portal APIs; service-role only server-side; internal routes and APIs protected

### Future Quality Bar — Active Systems, Support, Billing
- [ ] Active systems page: system name, status, health, last check, monthly plan, owner, related deal room/order, support shortcut
- [ ] System detail: what the system does, connected tools, status, last meaningful activity, monitoring summary, known limitations, support history, change request CTA
- [ ] Support: issue type, affected system, severity, affected workflow, since when, examples, expected response time
- [ ] Billing MVP: manual billing status, plan name if known, setup/payment status if known, open billing support
- [ ] Full billing later: invoices, receipts, subscription plan, payment method, renewal date, upgrade/downgrade, failed payment state

### Future Phase 3 Quality Upgrade Batches
1. **MVP acceptance and auth hardening**
   - Supabase auth config, authenticated browser pass, RLS/API boundary checks.
2. **Portal dashboard + deal-room usability**
   - Action-required dashboard, open deal rooms, next-action model, clearer deal-room layout, scope summary, timeline, proposal placeholder.
3. **Chat reliability + internal inbox**
   - Better message composer states, duplicate-send prevention, preserved drafts, internal visible/private toggle clarity, unread/waiting/owner filters.
4. **Proposal and approval layer**
   - Structured proposal fields, proposal status, client approval action, approval system events, manual payment/billing handoff.
5. **Active systems + support**
   - Useful client system detail, support request types, severity, related system/deal-room history.
6. **Hardening**
   - Rate limits for request/message creation, API tests, RLS verification, notification deep links, production monitoring.

### Future Phase 3 Success Criteria
- Authenticated account flow works reliably with email/password and Google
- At least 5 client requests created inside the portal instead of email-only
- Client/FlowOps conversation history stored in portal deal rooms
- Every open deal room has status, next action, scope summary, and latest activity
- Internal team can filter, reply, note, assign, update status, and convert to order without leaking private notes
- Client can see active systems/support/billing context without false automation claims
- Security acceptance passes for auth, RLS, internal notes, and internal APIs
- MRR target remains $2,000+/month once sales catches up to product readiness

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
  24. Promote MVP scope-reversal preview to production if accepted
  25. Run Automation Card Audit & Upgrade: demand check, richer descriptions, pricing recheck, unified illustrations
  26. Manually verify/enrich the 20-account seed list
  27. Send first outreach batch

NEXT AFTER FIRST PAYMENT / KEYS:
  28. Stripe Payment Link or live Checkout verification
  29. Resend live transactional emails
  30. Subscription verification

LATER:
  30. Stack Bundle Discount logic (2nd pipeline = 10% off setup)
  31. Real testimonials (replace placeholders after first clients)
  32. Future client accounts + deal room after sales validation
  33. Proposal/approval layer in future deal rooms
  34. Active systems/support hardening after portal is reactivated
  35. File uploads only after storage/RLS design
```

---

## What NOT To Build (Yet)

- ❌ Self-serve automated pipeline deployment
- ❌ Full self-serve workflow builder inside client portal
- ❌ Complex AI layer before product-market fit
- ❌ White-label version
- ❌ Mobile app
- ❌ External marketplace for 3rd party pipeline providers
- ❌ Usage-based billing (too complex for MVP)
- ❌ Raw n8n / real-time execution logs exposed to clients
- ❌ Multi-user workspace per client (Phase 4)
- ❌ API access for clients
- ❌ AI-generated proposals without human review
- ❌ File uploads before storage/RLS/security design

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

**Текущая рекомендация: убрать account/chat/deal-room из MVP и вернуться к sales validation.**

Marketplace, trust layer, pipeline pages, audit form, and internal order workspace are enough for the current MVP. Account/chat/deal-room has a strong future spec and partial implementation, but it is now intentionally deferred.

Fastest path:
1. promote the MVP scope-reversal preview to production if accepted;
2. manually verify/enrich the 20-account outreach list;
3. start outreach with audit/order flows and manual FlowOps follow-up;
4. only reactivate portal/deal-room after real client conversations show what the account workspace must support.

**Следующие 7 дней**: production promotion if accepted + first outreach batch.  
**Следующие 30 дней**: 2–3 qualified requests through audit/order/manual follow-up.  
**Следующие 60 дней**: 3–5 paying clients, real proof/case studies, then decide when to reactivate account/deal-room.
