# FlowOps SaaS — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Status: PLANNING / PRE-BUILD (June 2026)

Проект находится на стадии стратегического планирования.  
Существующая кодовая база — сайт FlowOps + внутренний аудит-воркспейс — является фундаментом для масштабирования в SaaS-платформу.

---

## Что уже готово

### Public Site
- [ ] Product-like FlowOps OS homepage
- [ ] Free AI Operations Audit section
- [ ] Systems positioning
- [ ] Client Workspace Preview
- [ ] CTA flow

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

---

## Что НЕ существует пока

- [ ] Pipeline marketplace
- [ ] Pipeline detail pages
- [ ] Order/request form per pipeline
- [ ] Pricing page
- [ ] Stripe integration
- [ ] Client portal / login
- [ ] Admin order management workspace
- [ ] Subscription management
- [ ] Loyalty program logic
- [ ] n8n delivery workflows
- [ ] Pipeline catalog in database

---

## Активная фаза

**Phase 0 → Phase 1 transition**: от audit-MVP к полноценному Marketplace MVP

Следующий шаг: начать Phase 1 (см. [[roadmap]] и [[next-steps]])

---

## Key Metrics (baseline)
- Активных клиентов: 0 (platform не запущена)
- Pipeline-систем в каталоге: 0 (не создан)
- MRR: $0
- Leads через Audit Form: неизвестно (нужно уточнить из Supabase)
