# FlowOps SaaS — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Status: PHASE 2A ACTIVE / SALES READINESS (June 22, 2026)

Проект перешёл из planning/pre-build в начальную реализацию Phase 1.  
Локальный workspace `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas` инициализирован как Next.js/TypeScript app с Marketplace MVP. 20 июня 2026 редизайн портирован в код: светлая яркая FlowOps OS визуальная система, blue/cyan акценты, пастельные pipeline-карточки, animated workflow sections, mobile/desktop QA. 21 июня 2026 Phase 1 завершена и активирована: remote Supabase migration применена в проект FlowOps, 15 систем опубликованы, live order submit пишет в `pipeline_orders`, status history работает, direct Telegram notification подтверждён. Phase 2 начата: payment/subscription schema, Stripe Checkout routes, webhook scaffold, payment UI, and Resend-ready email hooks implemented. По решению пользователя live Stripe/Resend verification отложена; следующий блок выполнен: catalog expanded to 20, Supabase seed applied, internal order SOP added, internal routes/payment actions protected by `INTERNAL_ACCESS_KEY`. 21 июня 2026 приложение задеплоено на Vercel в проект `flowops-saas`; production alias: `https://flowops-saas.vercel.app`. 22 июня 2026 deployed smoke passed: public pages/API render, catalog returns 20 systems, protected routes reject unauthenticated access, internal cookie flow works, QA order writes to Supabase, Telegram notification returns sent, and QA data was cleaned up. Later on 22 июня 2026 catalog expanded to 25 systems, Supabase migration applied, homepage proof/case-study section added, and production redeployed to Vercel. Phase 2A conversion readiness started: `/os` search/filter, ROI/payback blocks, and post-submit thank-you/next-step flow are deployed. First-client package and flagship delivery checklists are drafted in `docs/`. Homepage/case-study sales copy is polished and deployed for outreach.

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
- [x] Deployed smoke test passed on `https://flowops-saas.vercel.app`
- [x] Catalog expanded from 20 to 25 systems in code and live Supabase
- [x] Migration `202606220001_expand_catalog_to_25` applied
- [x] Homepage proof/case-study section added
- [x] Production redeployed after 25-system expansion: deployment `dpl_HdoJ5gcsjsJKqijeYum4WG6gAzdT`
- [x] `/os` search/filter deployed
- [x] ROI/payback blocks deployed on pipeline detail pages
- [x] Order form success state upgraded with order number and next steps
- [x] Production redeployed after conversion readiness batch: deployment `dpl_Ew2YwmupiEFqRyex3LSpzCxHh4AP`
- [x] First-client package added at `docs/first-client-package.md`
- [x] Flagship delivery checklists added at `docs/flagship-delivery-checklists.md`
- [x] Homepage/case-study sales copy polished and deployed: deployment `dpl_5GkRf37UBBNZwMZ6Y2yki7TjoVHs`
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

**Phase 2A — active**: Sales Readiness & First Clients. Payment/email scaffold готов, но live Stripe/Resend verification intentionally deferred. Current completed Phase 2 work: catalog expanded to 25 systems, remote Supabase synchronized, internal manual order SOP added, production access hardening completed, Vercel production deployment created, deployed smoke passed, and homepage proof/case-study section added.

Следующий шаг: manually verify/enrich the 20-account seed list, then start the first outreach batch. См. [[roadmap]] и [[next-steps]].

---

## Key Metrics (baseline)
- Активных клиентов: 0 (platform не запущена)
- Pipeline-систем в каталоге: 25 в code/static seed and live Supabase
- MRR: $0
- Leads через Audit Form: неизвестно (нужно уточнить из Supabase)
