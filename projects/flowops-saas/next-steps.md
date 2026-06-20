# FlowOps SaaS — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

---

## Immediate Next Actions (Phase 1 — MVP)

### Priority 1 — Database Schema Extension
- [x] Создать migration для Supabase таблиц: `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [ ] `pipeline_subscriptions` оставить на Phase 2/Stripe или добавить позже, когда subscription workflow станет реальным
- [x] Добавить seed данные для первых 8 pipeline-систем
- [ ] Расширить seed до 12–15 pipeline-систем
- [x] Добавить базовые RLS policies для public category/pipeline read

### Priority 2 — Marketplace Public Pages
- [x] `/os` — Marketplace главная страница (категории + pipeline cards + internal workspace preview)
- [x] `/os/[slug]` — Pipeline detail page (описание, pricing, CTA, order form)
- [ ] `/os/[category]` — Category overview page

### Priority 3 — Order/Request Flow
- [x] Order request form (per pipeline)
- [x] POST /api/pipeline-order → Supabase pipeline_orders when env keys are configured
- [ ] Admin notification (Telegram via n8n)
- [ ] Confirmation email (Resend или простой шаблон)

### Priority 4 — Pricing Page
- [x] `/pricing` — страница с тарифами подписки
- [x] Pricing cards: Maintain / Scale / Operator
- [x] Bundle section

### Priority 5 — Internal Admin Workspace Extension
- [ ] `/internal/orders` — список новых заказов на pipeline (preview exists; Supabase-backed list pending)
- [ ] `/internal/orders/[id]` — детали заказа, статус, заметки
- [ ] Status flow: New → In Progress → Deployed → Active

## Immediate Next Actions After 2026-06-20 Build

- [ ] Create `.env.local` from `.env.example` and connect the real Supabase project.
- [ ] Apply `supabase/migrations/202606200001_flowops_phase1_marketplace.sql`.
- [ ] Replace static catalog reads with Supabase reads or a hybrid static fallback.
- [ ] Build real `/internal/orders` Supabase-backed list and order detail/status update routes.
- [ ] Expand catalog from 8 to 12–15 systems.
- [ ] Add Telegram notification path for new `pipeline_orders`.
- [ ] Exclude or remove `design-extract-output/` from lint/project artifacts if keeping extraction output locally.

---

## Design

- [x] Premium homepage redesign concept in Figma (2026-06-20) — https://www.figma.com/design/Pv2Rkr3W6pbbspoxT6B0DH (see [[sessions/2026-06-20-figma-website-design]])
- [x] Port bright/light redesign into existing Next.js site after user sketch + juanmora.co reference
- [x] Desktop/mobile QA for `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders`
- [ ] Optional follow-up: refine copy and section names from sketch into final marketing language

---

## Phase 2 — After First 5 Clients

- [ ] Stripe Checkout для setup fee (one-time payment)
- [ ] Stripe Subscriptions для monthly
- [ ] Базовый email delivery workflow (Resend)
- [ ] Расширить каталог до 20–25 pipeline-систем
- [ ] Добавить testimonials / case study section

---

## Phase 3 — Client Portal

- [ ] Supabase Auth (email login)
- [ ] Client dashboard: активные pipeline-системы
- [ ] Deployment status per pipeline
- [ ] Subscription management
- [ ] Support request form
- [ ] Invoice history

---

## Деferred (Not Now)

- AI автоматический деплой pipeline
- Self-serve onboarding без команды
- Usage-based pricing
- White-label version
- Marketplace для внешних поставщиков pipeline

---

## Success Metrics (3-month targets)

- [ ] 5 платящих клиентов (setup fee)
- [ ] 3 активных подписки
- [ ] MRR > $500
- [ ] 15+ pipeline-систем в каталоге
- [ ] < 5 дней deployment time (среднее)
