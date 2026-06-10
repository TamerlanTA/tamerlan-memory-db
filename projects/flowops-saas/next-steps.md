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
- [ ] Создать Supabase таблицы: `pipelines`, `pipeline_categories`, `pipeline_orders`, `pipeline_subscriptions`
- [ ] Добавить seed данные для первых 12–15 pipeline-систем
- [ ] Добавить RLS policies

### Priority 2 — Marketplace Public Pages
- [ ] `/os` — Marketplace главная страница (категории + pipeline cards)
- [ ] `/os/[slug]` — Pipeline detail page (описание, pricing, CTA)
- [ ] `/os/[category]` — Category overview page

### Priority 3 — Order/Request Flow
- [ ] Order request form (per pipeline)
- [ ] POST /api/pipeline-order → Supabase pipeline_orders
- [ ] Admin notification (Telegram via n8n)
- [ ] Confirmation email (Resend или простой шаблон)

### Priority 4 — Pricing Page
- [ ] `/pricing` — страница с тарифами подписки
- [ ] Pricing cards: Maintain / Scale / Operator
- [ ] Bundle section

### Priority 5 — Internal Admin Workspace Extension
- [ ] `/internal/orders` — список новых заказов на pipeline
- [ ] `/internal/orders/[id]` — детали заказа, статус, заметки
- [ ] Status flow: New → In Progress → Deployed → Active

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
