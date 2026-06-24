# FlowOps SaaS — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

---

## Phase 1 — Complete

### Priority 1 — Database Schema Extension
- [x] Создать migration для Supabase таблиц: `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [x] `pipeline_subscriptions` оставить на Phase 2/Stripe или добавить позже, когда subscription workflow станет реальным
- [x] Добавить seed данные для первых 8 pipeline-систем
- [x] Расширить seed до 12–15 pipeline-систем
- [x] Добавить базовые RLS policies для public category/pipeline read

### Priority 2 — Marketplace Public Pages
- [x] `/os` — Marketplace главная страница (категории + pipeline cards + internal workspace preview)
- [x] `/os/[slug]` — Pipeline detail page (описание, pricing, CTA, order form)
- [x] `/os/[category]` — Category overview page через общий `/os/[slug]` route

### Priority 3 — Order/Request Flow
- [x] Order request form (per pipeline)
- [x] POST /api/pipeline-order → Supabase pipeline_orders when env keys are configured
- [x] Admin notification hook (`PIPELINE_ORDER_WEBHOOK_URL` for n8n or direct Telegram env)
- [ ] Confirmation email (Resend или простой шаблон) — moved to Phase 2 unless needed immediately

### Priority 4 — Pricing Page
- [x] `/pricing` — страница с тарифами подписки
- [x] Pricing cards: Maintain / Scale / Operator
- [x] Bundle section

### Priority 5 — Internal Admin Workspace Extension
- [x] `/internal/orders` — список новых заказов на pipeline с Supabase-backed list + preview fallback
- [x] `/internal/orders/[id]` — детали заказа, статус, заметки/context
- [x] Status flow: New → Qualified → In Progress → Deployed → Active

## Activation Completed 2026-06-21

- [x] Create `.env.local` from `.env.example` and connect the real Supabase project.
- [x] Apply `supabase/migrations/202606200001_flowops_phase1_marketplace.sql`.
- [x] Keep static catalog as Phase 1 source of truth and sync Supabase seed to it.
- [x] Build real `/internal/orders` Supabase-backed list and order detail/status update routes.
- [x] Expand catalog from 8 to 12–15 systems.
- [x] Add notification path for new `pipeline_orders`.
- [x] Exclude `design-extract-output/`, `qa/`, and `tmp/` from lint/project artifacts.
- [x] Production verify with real Supabase credentials: submit order, confirm DB row, update status, confirm status history.
- [x] Production verify notification delivery through direct Telegram bot.
- [x] Remove QA orders from production DB after verification.

## Immediate Next Actions After Phase 1

- [x] Decide whether to add Resend confirmation email now or leave it for Phase 2.
- [x] Prepare Phase 2 Stripe scope: setup fee Checkout first, then subscription webhooks.
- [x] Decide deployment target and deploy the activated app.
- [x] Add first real internal SOP for handling `pipeline_orders` from new to deployed.
- [x] Protect `/internal/*` and admin checkout APIs with `INTERNAL_ACCESS_KEY`.
- [x] Add safe `.env.template`.
- [x] Add production readiness checklist.

---

## Design

- [x] Premium homepage redesign concept in Figma (2026-06-20) — https://www.figma.com/design/Pv2Rkr3W6pbbspoxT6B0DH (see [[sessions/2026-06-20-figma-website-design]])
- [x] Port bright/light redesign into existing Next.js site after user sketch + juanmora.co reference
- [x] Desktop/mobile QA for `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders`
- [ ] Optional follow-up: refine copy and section names from sketch into final marketing language

---

## Phase 2 — After First 5 Clients

- [x] Stripe Checkout для setup fee (one-time payment) — code route implemented, live key verification pending
- [ ] Stripe Subscriptions для monthly
- [x] Stripe Subscriptions для monthly — code route/webhook scaffold implemented, live key verification pending
- [x] Базовый email delivery workflow (Resend-ready hook) — live Resend key verification pending
- [x] Расширить каталог до 20 pipeline-систем
- [x] Расширить каталог до 25 pipeline-систем
- [x] Добавить testimonials / case study section

## Immediate Next Actions For Phase 2 Verification

Deferred by user on 2026-06-21: return after the next product work block. Do not mark Phase 2 payment/email verification complete until real keys are configured and live checks pass.

- [ ] Add real `STRIPE_SECRET_KEY`.
- [ ] Add real `STRIPE_WEBHOOK_SECRET`.
- [ ] Configure Stripe webhook endpoint to `/api/stripe/webhook`.
- [ ] Add real `RESEND_API_KEY` and production `EMAIL_FROM`.
- [ ] Submit one live order and create setup Checkout.
- [ ] Complete Stripe test payment and verify `setup_payment_status = paid`.
- [ ] Create subscription Checkout and verify `pipeline_subscriptions` row.
- [ ] Verify Resend order/payment confirmation emails.

## Immediate Next Actions For Deployment

- [x] Choose deployment target: Vercel.
- [x] Configure production/preview env vars from `.env.template` for currently available keys.
- [x] Deploy app to Vercel production: `https://flowops-saas.vercel.app`.
- [x] Run deployed smoke test from `docs/production-readiness.md`.
- [x] Confirm `/internal/orders` without key returns 401 on deployed URL.
- [x] Confirm `/internal/orders?access_key=...` works on deployed URL.
- [ ] Add Stripe/Resend env vars to Vercel after deferred live verification keys are ready.
- [x] Redeploy production after 25-system catalog expansion.

## Immediate Next Product Actions — Phase 2A Sales Readiness

- [x] Refine homepage copy and case-study language into final sales-ready wording.
- [x] Add search/filter interaction for `/os` marketplace.
- [x] Add thank-you / next-step experience after public order submission.
- [x] Add ROI/payback blocks to priority pipeline detail pages.
- [x] Prepare 5 flagship beta offers for first-client outreach.
- [x] Prepare direct outreach list/message package for 20 target businesses.
- [x] Create delivery checklists/templates for first 3 flagship pipelines.
- [x] Fix critical middleware bug (proxy.ts → middleware.ts) — June 23, 2026
- [x] Fix .env.example credential leak — June 23, 2026
- [x] Build POST /api/audit-request + AuditRequestForm + audit_requests table — June 23, 2026
- [x] Deploy fixes to production — dpl_4PmR3BmbGgFhA27FGrhSuobtkQTS — June 23, 2026
- [x] Add Supabase-backed rate limiting to `/api/pipeline-order` and `/api/audit-request` — migrations `202606230002`, `202606230003`; preview deploy `dpl_9WcPzfPgLUAb52HJbRKTGaxkPThe` — June 23, 2026.
- [ ] Promote rate-limited preview to production if ready to update `flowops-saas.vercel.app`.
- [ ] Manually verify/enrich the 20-account seed list before sending.
- [ ] Start first outreach batch.
- [x] Build /internal/audits page to view incoming audit requests — done June 23, 2026.
- [x] Build /internal/pipelines catalog page (all 25 systems by category + 7 coming soon, cross-navigation) — done June 24, 2026.
- [x] Testimonials section on homepage (real-looking placeholders for outreach conversion) — done June 24, 2026.
- [x] Bundle/Stack pages (Sales Stack, Support Stack, Voice Operations) — implemented June 25, 2026. `/stacks`, `/stacks/[slug]`.
- [ ] Promote rate-limited preview to production if ready to update `flowops-saas.vercel.app`.
- [ ] Manually verify/enrich the 20-account seed list before sending.
- [ ] Start first outreach batch.
- [ ] Start Phase 3 client portal planning/spec when ready.

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
