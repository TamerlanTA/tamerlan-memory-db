# FlowOps SaaS — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Status: PHASE 2A — SALES READINESS COMPLETE (June 25, 2026)

Проект задеплоен на Vercel: `https://flowops-saas.vercel.app`
Последний деплой: `https://flowops-saas-2eawb4npr-tamertt931-8560s-projects.vercel.app` (June 25, 2026) — Stack pages deployment
Предыдущий деплой: `dpl_4PmR3BmbGgFhA27FGrhSuobtkQTS` (June 23, 2026)

Полный технический аудит выявил и исправил критические баги — ряд задач был помечен в памяти как "done" без реальной реализации в коде.

---

## Что уже готово (проверено по коду)

### Public Site
- [x] FlowOps OS homepage с полным контентом и proof/case-study секцией
- [x] Testimonials section on homepage — 3 placeholder cards (Bright Dental, Northbar Realty, Pioneer HVAC) — June 24, 2026
- [x] Секция `#audit` — реальная форма `AuditRequestForm` с POST `/api/audit-request`
- [x] 25 pipeline систем в `src/lib/catalog.ts` и в Supabase
- [x] `/os` marketplace с working search/filter через `MarketplaceExplorer`
- [x] `/os` "Coming Soon" pipeline cards — 7 announced systems in separate "On the Roadmap" section
- [x] `/os/[slug]` pipeline detail pages (32 pages)
- [x] `/stacks` — System Stacks overview page (all 3 bundles with savings badge, system tags, pricing) — June 25, 2026
- [x] `/stacks/[slug]` — Individual stack detail pages: Sales Stack, Support Stack, Voice Operations — June 25, 2026
- [x] `StackDetail` type + `stackDetails` array in `src/lib/pricing.ts` — June 25, 2026
- [x] Stacks link added to SiteHeader nav and SiteFooter — June 25, 2026
- [x] Homepage pricing section → "View system stacks — save up to 23%" link — June 25, 2026
- [x] Pricing page bundle cards → link to `/stacks/[slug]` — June 25, 2026
- [x] `/pricing` page
- [x] `SiteFooter` on all 4 public pages (/, /os, /pricing, /os/[slug])

### Backend / Internal
- [x] `POST /api/audit-request` → Supabase audit_requests + Telegram notification
- [x] Supabase: `audit_requests` table (migration `202606230001` applied June 23)
- [x] `src/middleware.ts` РАБОТАЕТ: экспортирует `middleware`
  - КРИТИЧНО: В Next.js 16.2.9 только `middleware.ts` + `export function middleware` регистрирует прокси
  - `proxy.ts` + `export function proxy` = пустой manifest = все маршруты открыты публично
- [x] `/internal/*` и Stripe checkout APIs защищены `INTERNAL_ACCESS_KEY`
- [x] `/internal/orders` список с Supabase + preview fallback
- [x] `/internal/orders/[id]` детали заказа
- [x] `/internal/audits` список audit requests (Supabase + preview fallback)
- [x] `/internal/audits/[id]` детали + status update (new → contacted → audit_sent → converted | closed)
- [x] Status flow: New → Qualified → In Progress → Deployed → Active
- [x] Telegram notifications для pipeline_orders и audit_requests
- [x] Durable rate limiting для `/api/pipeline-order` и `/api/audit-request`
  - Supabase-backed `check_rate_limit` RPC + `rate_limit_buckets`
  - 3 requests/hour per IP+email pair
  - In-memory fallback for local/no-Supabase environments
- [x] Stripe Checkout routes (scaffold, live verification pending)
- [x] Stripe webhook с signature verification и корректным `items.data[0].current_period_start`
- [x] Resend email hooks (live verification pending)

### Migrations applied to Supabase (fmpvyuowglvyrrqecmrn)
- `202606200001` — Phase 1 schema
- `202606210001` — Phase 2 payments
- `202606210002` — Catalog to 20 systems
- `202606220001` — Catalog to 25 systems
- `20260623085205` — audit_requests table (remote canonical migration fetched from Supabase history)
- `202606230002` — rate_limit_buckets table + check_rate_limit RPC
- `202606230003` — check_rate_limit RPC returning fix

---

## Что НЕ существует / pending

- [ ] Stripe live key verification (нужны STRIPE_SECRET_KEY + STRIPE_WEBHOOK_SECRET в Vercel)
- [ ] Resend live verification (нужен RESEND_API_KEY)
- [x] `/internal/audits` list + `/internal/audits/[id]` detail — implemented June 23
- [x] Coming Soon pipeline cards on `/os` — implemented June 23
- [x] Site footer on public pages — implemented June 23
- [x] Rate limiting на `/api/pipeline-order` и `/api/audit-request`
- [x] `/internal/pipelines` catalog page — implemented June 24, 2026
- [x] Bundle/Stack pages — implemented June 25, 2026
- [ ] Первый outreach batch (20 целевых аккаунтов)
- [ ] Client portal / login (Phase 3)

---

## Активная фаза

**Phase 2A — Sales Readiness COMPLETE** (June 25, 2026). Все code tasks Phase 2A выполнены: audit form, coming soon cards, footer, rate limiting, /internal/audits, /internal/pipelines, testimonials, bundle/stack pages. Следующий шаг: manually verify/enrich 20-account seed list, затем отправить первый outreach batch. Redeploy to Vercel production needed.

---

## Key Metrics (June 25, 2026)
- Активных клиентов: 0
- Pipeline-систем: 25 (code + Supabase)
- MRR: $0
- Audit requests: 0 (форма только запущена)
