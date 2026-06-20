# FlowOps SaaS — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Status: PHASE 1 FOUNDATION BUILT / LIGHT REDESIGN APPLIED (June 20, 2026)

Проект перешёл из planning/pre-build в начальную реализацию Phase 1.  
Локальный workspace `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas` инициализирован как Next.js/TypeScript app с первым Marketplace MVP vertical slice. 20 июня 2026 редизайн портирован в код: светлая яркая FlowOps OS визуальная система, blue/cyan акценты, пастельные pipeline-карточки, animated workflow sections, mobile/desktop QA.

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
- [x] API routes: pipeline categories, pipelines, pipeline by slug, pipeline order
- [x] Supabase migration for `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [x] Seed SQL for first 8 Phase 1 pipeline systems
- [x] Order request form with Supabase persistence when env keys are configured and validated fallback when not configured
- [x] Modern light redesign across `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders`
- [x] QA screenshots captured for desktop/mobile and order form success path

---

## Что НЕ существует пока

- [x] Pipeline marketplace (MVP static-data version)
- [x] Pipeline detail pages (MVP static-data version)
- [x] Order/request form per pipeline (MVP version)
- [x] Pricing page (MVP version)
- [ ] Stripe integration
- [ ] Client portal / login
- [ ] Admin order management workspace (preview exists; real Supabase-backed workspace pending)
- [ ] Subscription management
- [ ] Loyalty program logic
- [ ] n8n delivery workflows
- [ ] Pipeline catalog in live database (migration/seed exists; applying to Supabase pending)

---

## Активная фаза

**Phase 1 — Marketplace MVP foundation**: первый вертикальный срез создан локально и визуально обновлён; следующий шаг — подключить Supabase env, применить миграции и заменить preview/internal статические данные реальными queries.

Следующий шаг: production activation Phase 1 (см. [[roadmap]] и [[next-steps]])

---

## Key Metrics (baseline)
- Активных клиентов: 0 (platform не запущена)
- Pipeline-систем в каталоге: 8 в code/static seed; live database pending
- MRR: $0
- Leads через Audit Form: неизвестно (нужно уточнить из Supabase)
