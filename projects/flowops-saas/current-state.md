# FlowOps SaaS — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Status: PHASE 2 ACTIVE / VERCEL DEPLOYED (June 21, 2026)

Проект перешёл из planning/pre-build в начальную реализацию Phase 1.  
Локальный workspace `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas` инициализирован как Next.js/TypeScript app с Marketplace MVP. 20 июня 2026 редизайн портирован в код: светлая яркая FlowOps OS визуальная система, blue/cyan акценты, пастельные pipeline-карточки, animated workflow sections, mobile/desktop QA. 21 июня 2026 Phase 1 завершена и активирована: remote Supabase migration применена в проект FlowOps, 15 систем опубликованы, live order submit пишет в `pipeline_orders`, status history работает, direct Telegram notification подтверждён. Phase 2 начата: payment/subscription schema, Stripe Checkout routes, webhook scaffold, payment UI, and Resend-ready email hooks implemented. По решению пользователя live Stripe/Resend verification отложена; следующий блок выполнен: catalog expanded to 20, Supabase seed applied, internal order SOP added, internal routes/payment actions protected by `INTERNAL_ACCESS_KEY`. 21 июня 2026 приложение задеплоено на Vercel в проект `flowops-saas`; production alias: `https://flowops-saas.vercel.app`.

---

## Что уже готово

### Public Site
- [x] Product-like FlowOps OS homepage with bright/light animated redesign
- [x] Free AI Operations Audit section
- [x] Systems positioning
- [x] Client/Internal Workspace Preview
- [x] CTA flow

### Backend / Internal
- [x] POST /api/audit-request
- [x] Supabase: audit_requests table
- [x] Supabase: audit_work_items table
- [x] Supabase: audit_response_drafts table
- [x] Internal page: /internal/audits
- [x] Internal draft page: /internal/audits/[id]
- [x] Status update routes
- [x] Draft edit routes
- [x] Shared internal access key
- [x] Rate limiting
- [x] Migration files
- [x] E2E QA checklist
- [x] Production activation docs
- [x] Phase 1 static pipeline catalog in code
- [x] `/os` marketplace page
- [x] `/os/[slug]` pipeline detail pages
- [x] `/pricing` page
- [x] `/internal/orders` preview page
- [x] `/internal/orders` Supabase-backed workspace with preview fallback
- [x] `/internal/orders/[id]` detail page
- [x] Manual status flow: New → Qualified → In Progress → Deployed → Active
- [x] Status history writes to `order_status_history`
- [x] API routes: pipeline categories, pipelines, pipeline by slug, pipeline order
- [x] Supabase migration for `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [x] Seed SQL for 15 Phase 1 pipeline systems
- [x] Order request form with Supabase persistence when env keys are configured and validated fallback when not configured
- [x] Pipeline order admin notification hook via `PIPELINE_ORDER_WEBHOOK_URL` or direct Telegram env
- [x] `.env.local` создан из заполненного `.env.example`
- [x] Remote Supabase project linked via CLI (`fmpvyuowglvyrrqecmrn`)
- [x] Remote migration `202606200001_flowops_phase1_marketplace` applied
- [x] Live order submit verified against Supabase and Telegram
- [x] Phase 2 payment migration `202606210001_flowops_phase2_payments` applied to Supabase
- [x] Tables: `pipeline_payments`, `pipeline_subscriptions`
- [x] Payment fields added to `pipeline_orders`
- [x] Stripe Checkout API routes for setup fee and monthly subscription
- [x] Stripe webhook route for checkout/subscription events
- [x] Internal order detail payment actions UI
- [x] Resend-ready order/payment confirmation email hooks
- [x] User deferred live Stripe/Resend verification for later; tracked in [[next-steps]]
- [x] Catalog expanded from 15 to 20 systems
- [x] Supabase migration `202606210002_expand_catalog_to_20` applied
- [x] Internal order handling SOP added at `docs/internal-order-sop.md`
- [x] Internal access gate added via `src/proxy.ts`
- [x] `/internal/*` protected by `INTERNAL_ACCESS_KEY`
- [x] Admin Stripe checkout APIs protected by internal cookie/header
- [x] Safe `.env.template` added; `.env.local` and filled `.env.example` remain ignored
- [x] Production readiness checklist added at `docs/production-readiness.md`
- [x] Vercel project `flowops-saas` created/linked
- [x] Production deployment ready: `https://flowops-saas.vercel.app`
- [x] Vercel Production/Preview env vars configured for Supabase, internal access, Telegram notification, and email sender
- [x] Modern light redesign across `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders`
- [x] QA screenshots captured for desktop/mobile and order form success path

---

## Что НЕ существует пока

- [x] Pipeline marketplace (MVP static-data version)
- [x] Pipeline detail pages (MVP static-data version)
- [x] Order/request form per pipeline (MVP version)
- [x] Pricing page (MVP version)
- [ ] Stripe integration live verification (needs `STRIPE_SECRET_KEY` + `STRIPE_WEBHOOK_SECRET`)
- [ ] Client portal / login (Phase 3)
- [ ] Subscription management
- [ ] Loyalty program logic
- [ ] n8n delivery workflows
- [x] Pipeline catalog in live database

---

## Активная фаза

**Phase 2 — active**: payment/email scaffold готов, но live Stripe/Resend verification intentionally deferred. Current completed Phase 2 work: catalog expanded to 20 systems, remote Supabase synchronized, internal manual order SOP added, production access hardening completed, and Vercel production deployment created.

Следующий шаг: Phase 2 planning/implementation (Stripe setup payments/subscriptions, confirmation email, client portal planning) см. [[roadmap]] и [[next-steps]].

---

## Key Metrics (baseline)
- Активных клиентов: 0 (platform не запущена)
- Pipeline-систем в каталоге: 20 в code/static seed and live Supabase
- MRR: $0
- Leads через Audit Form: неизвестно (нужно уточнить из Supabase)
