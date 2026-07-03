# FlowOps SaaS — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

---

## Decision Log

### D-001 — Product Positioning
**Decision**: FlowOps OS позиционируется как AI Operations Platform, а не агентство автоматизаций.
**Why**: Агентства — commodity. Platform — IP и масштабируемый бизнес. Клиент покупает операционную систему, а не часы работы.
**Impact**: Все тексты, CTA, pricing и UX должны отражать platform-логику.

---

### D-002 — Hybrid Business Model (Setup + Subscription)
**Decision**: Гибридная модель: единоразовый setup fee + monthly subscription.
**Why**: Setup покрывает стоимость внедрения и создаёт commitment. Subscription = predictable revenue и long-term relationship.
**Impact**: Нужно объяснить клиенту ценность подписки — это не "поддержка", а living infrastructure.

---

### D-003 — Manual Delivery (Not Self-Serve) for MVP
**Decision**: MVP НЕ включает автодеплой pipeline-систем. Команда FlowOps делает это вручную.
**Why**: Self-serve деплой технически сложен. Для PMF важнее скорость запуска и качество первых клиентов.
**Impact**: Нужен чёткий internal delivery workflow. Клиент заполняет форму → команда deployes.

---

### D-004 — n8n скрыт от клиентов
**Decision**: n8n — внутренний engine. Клиент никогда не видит n8n интерфейс.
**Why**: n8n — не продукт для клиента. Клиент видит только результат (pipeline работает). Показ n8n разрушит премиум-восприятие.
**Impact**: Клиент видит статус, логи и результаты — но через собственный FlowOps UI.

---

### D-005 — Client Portal отложен
**Decision**: Полноценный client portal (login, dashboard, subscription management) — это Phase 3, не MVP.
**Why**: MVP нужен для валидации спроса. Portal — дорого строить до product-market fit.
**Impact**: В MVP клиент получает email-апдейты + ручную коммуникацию.

---

### D-006 — Stripe откладывается на Phase 2
**Decision**: В Phase 1 (MVP) оплата может быть через manual link или базовый Stripe Checkout.
**Why**: Полноценная Stripe-интеграция (subscriptions, invoices, webhooks) требует времени. MVP = validate demand first.
**Impact**: Первые клиенты могут платить через link (Stripe Checkout / PayPal / bank).

---

### D-007 — Design Direction: Premium Dark B2B
**Decision**: Дизайн — тёмный, графитовый, electric blue accents, Linear/Vercel/Stripe quality.
**Why**: Дешёвый дизайн = низкие цены в голове клиента. Premium UI = premium pricing.
**Impact**: Никаких ярких градиентов, никакого crypto-неона, никаких дешёвых карточек.

---

### D-008 — Loyalty через Stack Bundle + Tenure Rewards
**Decision**: Лучшая loyalty-модель — комбинация Stack Bundle Discount + Subscription Tenure Rewards.
**Why**: Bundle discount мотивирует покупать больше pipeline сразу. Tenure rewards удерживают долгосрочно.
**Impact**: 2+ pipelines = 10% discount на следующий setup; 3+ = 15%; 5+ = custom package.

---

### D-009 — Audit Form остаётся главной входной точкой
**Decision**: Free AI Operations Audit сохраняется и усиливается как главный CTA на сайте.
**Why**: Audit снижает барьер входа и создаёт персонализированный recommendation → natural upsell в конкретный pipeline.
**Impact**: После Audit → рекомендуем 2–3 pipeline-системы → ссылки на marketplace.

---

### D-010 — Supabase как единственная БД (MVP)
**Decision**: Supabase — primary database для MVP. Никаких других баз.
**Why**: Уже используется. PostgreSQL + realtime + auth in one. Избегаем overengineering.
**Impact**: Расширяем существующие таблицы, добавляем новые (pipelines, orders, subscriptions).

---

### D-011 — Local-first order API fallback
**Decision**: В Phase 1 `/api/pipeline-order` валидирует запрос и возвращает success payload без persistence, если Supabase env keys не настроены.
**Why**: Это позволяет тестировать UI/order flow локально до подключения реального Supabase проекта, не блокируя frontend build.
**Impact**: Перед production обязательно настроить `.env.local`, применить migration и проверить, что заказы реально пишутся в `pipeline_orders`.

---

### D-012 — Light Bright Product Direction
**Decision**: Текущее визуальное направление FlowOps OS изменено с premium dark на светлый, яркий, технологичный стиль: warm off-white base, strong blue/cyan, пастельные system cards, большие выразительные заголовки, animated workflow diagrams.
**Why**: Пользователь принёс sketch и reference juanmora.co; нужен более запоминающийся, живой и современный продуктовый интерфейс, не сухой dark SaaS.
**Impact**: Дизайн страниц `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders` должен сохранять light/bright direction. D-007 считается историческим решением, заменённым для текущей реализации.

### D-013 — Trust Layer Before Scaling Outreach
**Decision**: Before scaling owner-focused outreach, FlowOps site needs a deliberate trust/proof layer across the homepage, marketplace, audit flow, and pipeline detail pages.
**Why**: Primary buyers are business owners. They do not buy "AI automation" first; they buy reduced operational risk, proof of competence, and confidence that FlowOps will not break their business processes.
**Impact**:
- Do not rely on generic testimonials alone, especially while real client proof is still limited.
- Add risk-reduction proof: deployment process, manual QA, owner approval before deployment, rollback/monitoring language, privacy/data-handling signals.
- Add proof-of-work surfaces: implementation examples, audit workspace/product screenshots, workflow diagrams, Telegram/status notifications, internal pipeline/order surfaces where appropriate.
- Use mini-case studies and implementation examples without falsely claiming client outcomes until real results exist.
- Replace placeholder testimonials with real proof as soon as first clients produce credible outcomes.

### D-014 — Client Accounts Should Become a Deal Room, Not Only a Dashboard
**Decision**: Phase 3 client accounts should include an in-site order/proposal/chat workspace ("deal room"), not only post-deployment dashboard, billing, and support.
**Why**: The stronger product experience is: client creates an account, submits an automation request/offer inside the site, FlowOps discusses scope in the same workspace, then the request becomes an order/deployment. This reduces reliance on email, keeps context durable, and makes FlowOps feel like a platform instead of a contact form.
**Status**: Future-only after D-018. This remains the target for a later SaaS maturity layer, not the current MVP.
**Impact**:
- Portal scope must expand from passive dashboard to active client workspace.
- Add authenticated conversations, request/proposal threads, attachments/context, status timeline, team replies, and internal assignment.
- Keep MVP manual-delivery: chat helps qualification and scope, but does not imply self-serve automation deployment.
- Email/Telegram can remain notifications, but the canonical client conversation should live in FlowOps.

### D-015 — Phase 3 Execution Reprioritized By User
**Decision**: On June 29, 2026, the user explicitly moved FlowOps SaaS execution into Phase 3 Client Accounts + Deal Room.
**Why**: The user wants to proceed with client accounts and deal-room implementation now, rather than keep it deferred behind outreach/first-client validation.
**Status**: Superseded by D-018 on June 30, 2026.
**Impact**:
- Treat the older roadmap warning "do not go into Phase 3 before first clients" as a risk note, not a blocker.
- All Phase 3 implementation must follow `docs/phase-3-client-accounts-deal-room-plan.md`.
- The MVP remains scoped: accounts, automation request intake, request-specific discussion, internal request management, and request-to-order conversion.
- Still do not build self-serve deployment, multi-user workspaces, file uploads, realtime logs, or AI reports unless explicitly reprioritized.

### D-016 — Portal Auth Uses Email/Password + Google, Not Magic-Link-First
**Decision**: Phase 3 portal auth should use conventional SaaS auth: email/password sign-in, email/password account creation, and Google OAuth when configured.
**Why**: The user rejected the magic-link-first MVP experience as not normal enough for the product.
**Impact**:
- Do not reintroduce magic link as the primary portal login UX.
- Keep Supabase Auth as the auth provider and keep RLS/API bearer-token model.
- Production readiness must include Supabase email/password provider, Google provider, anon key, and redirect URL setup.
- Authenticated acceptance should test password signup/login and Google OAuth, not magic-link login.

### D-017 — Account, Chat, and Deal Room Quality Bar
**Decision**: The target Phase 3 portal quality bar is a full operational workspace: account system, structured request intake, request-specific chat, deal-room scope/proposal/status/decision history, active systems, support, billing context, and internal request operations.
**Why**: A premium FlowOps client should never wonder what is happening, who owns the next step, what has been agreed, or where to discuss a request. The portal must make FlowOps feel like a managed AI operations platform, not a prettier contact form.
**Status**: Future quality target after D-018. Preserve the spec; do not expose it in MVP.
**Impact**:
- Use `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md` as the Phase 3 quality target.
- Deal rooms must show status, next action, scope summary, timeline, chat, proposal/approval state later, and conversion/order/system links.
- Chat is not a generic messenger; it is a structured business workflow conversation tied to requests, proposals, decisions, delivery, support, and internal-only notes.
- Portal dashboard should emphasize action-required, open deal rooms, active systems, recent updates, billing/support shortcuts, and what needs the client or FlowOps next.
- Keep manual delivery and keep n8n hidden from clients.
- Do not build file uploads, multi-user client workspaces, realtime logs, self-serve workflow builder, or AI-generated proposals until real usage proves need.

### D-018 — Client Accounts, Chat, and Deal Room Deferred Out of MVP
**Decision**: On June 30, 2026, the user reversed the MVP scope: account system, chat, and deal room are not needed for the current MVP and must be removed from the buyer-facing MVP flow for now.
**Why**: For the current MVP, the priority is sales validation and simple manual delivery: public audit, public system request/order form, internal order workspace, and direct follow-up. Account/chat/deal-room is valuable, but it adds product surface area before there is enough client usage to justify it.
**Impact**:
- Do not expose account/chat/deal-room as the primary public order flow in the MVP.
- Public system pages should use the earlier `/api/pipeline-order` request flow without requiring portal auth.
- Remove Portal from public navigation/CTA surfaces for MVP.
- Keep the existing Phase 3 portal/deal-room code, database schema, docs, and quality spec as future infrastructure unless the user explicitly asks to delete it.
- Treat account/chat/deal-room as a required future SaaS maturity layer after first client/sales validation, not as abandoned work.
- The future quality bar remains `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md`.

### D-019 — Bundle Discount Computed By Email Lookup, Not an Account System
**Decision**: The Stack Bundle Discount (D-008: 2nd active pipeline = 10% off setup, 3rd+ = 15%) is computed server-side at order time in `POST /api/pipeline-order` by counting a client's prior distinct `pipeline_slug` values in `pipeline_orders` matched by `client_email` (case-insensitive), excluding cancelled orders and the pipeline being ordered. It does not depend on the deferred (D-018) client account/portal system.
**Why**: Implementing this via email lookup against the existing unauthenticated order flow makes the loyalty pricing real now, without requiring the account system that D-018 explicitly deferred out of MVP. Email-based matching is an approximation (a client could use a different email per order) but is good enough for the current manual-follow-up sales model, where FlowOps staff can also apply/adjust the discount manually if the automatic match misses a known repeat client.
**Impact**:
- `pipeline_orders` has `original_setup_price`, `discount_percent`, `discount_reason` columns (migration `20260703091233_bundle_discount.sql`). `agreed_setup_price` is now the post-discount price; `original_setup_price` preserves the base catalog price.
- Discount logic lives in `src/lib/loyalty.ts` (`bundleDiscountForPriorCount`, `getBundleDiscountForClient`, `applyDiscount`) so the tier numbers stay in one place if D-008 pricing changes.
- If/when the account system (D-018) is reactivated, this same logic should key off `clients.id` instead of raw email for a more reliable match — revisit at that time.
- Discount is only applied automatically up to the 15% (3rd+) tier; D-008's "5+ = custom package" remains a manual sales conversation, not automatic.
