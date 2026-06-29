# FlowOps SaaS — Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

---

## Active Risks

### R-001 — Slow first sales cycle
**Risk**: Marketplace запущен, но нет клиентов. Pipeline-системы выглядят убедительно, но никто не заказывает.
**Probability**: Medium
**Impact**: High
**Mitigation**: Запустить с 3–5 beta клиентами через прямой outreach (не через organic). Audit Form → personal follow-up → первый pipeline бесплатно или со скидкой для первых 3.

---

### R-002 — Pricing too high for small businesses
**Risk**: Setup $500–$1000 + $149/mo выглядит дорого для малого бизнеса.
**Probability**: Medium
**Impact**: High
**Mitigation**: Entry-level pipeline ($299 setup + $99/mo). Ясная ROI-математика на каждой pipeline detail page. "Missed Call Recovery Pipeline окупается за 3 клиента."

---

### R-003 — Delivery bottleneck
**Risk**: Заказы приходят, но команда не успевает деплоить вовремя.
**Probability**: Medium (при росте > 5 заказов/месяц)
**Impact**: High
**Mitigation**: Стандартизировать delivery workflow для каждого pipeline. Создать template n8n flows. Ограничить количество активных деплоев.

---

### R-004 — Cheap agency perception
**Risk**: Несмотря на premium positioning, клиенты воспринимают FlowOps как "ещё одно агентство".
**Probability**: Medium
**Impact**: High
**Mitigation**: Строгий copy (никогда "мы делаем автоматизации"). UI уровня Stripe/Linear. Case studies с операционными результатами.

---

### R-005 — Technical debt from early decisions
**Risk**: Быстрая разработка MVP создаёт архитектурные проблемы при масштабировании.
**Probability**: Low–Medium
**Impact**: Medium
**Mitigation**: Заложить правильную DB-структуру с Phase 1. Не хардкодить бизнес-логику. Supabase RLS с самого начала.

---

### R-006 — Subscription churn
**Risk**: Клиенты платят setup, получают pipeline, отменяют подписку.
**Probability**: Medium
**Impact**: High (уничтожает MRR)
**Mitigation**: Подписка должна давать реальную ценность. Monthly check-in calls. Proactive improvement suggestions. "Без подписки — pipeline не поддерживается и может сломаться."

---

### R-007 — n8n infrastructure reliability
**Risk**: n8n падает → pipeline клиента не работает → churn + reputational damage.
**Probability**: Low–Medium
**Impact**: Very High
**Mitigation**: Redundant n8n instances. Monitoring alerts (Telegram notifications). SLA в договоре с клиентом. Backup workflows.

---

### R-008 — Marketplace feels empty
**Risk**: 15–20 pipeline-карточек в marketplace выглядят как "мало".
**Probability**: Low (если правильно сгруппировать)
**Impact**: Medium
**Mitigation**: Правильная группировка по категориям. "Coming Soon" карточки для запланированных pipeline. Показывать roadmap.

---

### R-009 — Over-building before validation
**Risk**: Тратим месяц на идеальный UI до первой продажи.
**Probability**: Medium
**Impact**: High (потеря времени)
**Mitigation**: Phase 1 = работающий MVP за 3–4 недели. Сначала 5 pipeline-карточек, потом расширяем.

---

### R-010 — Stripe / Payment complexity
**Risk**: Полноценная Stripe subscription + webhook логика занимает много времени.
**Probability**: Low (если откладываем)
**Impact**: Low–Medium
**Mitigation**: Phase 1 = manual payment link. Phase 2 = Stripe Checkout. Phase 3 = full subscription management.

---

### R-011 — Deployment env drift
**Risk**: Vercel production работает с текущими Supabase/Internal/Telegram env vars, но Stripe/Resend keys намеренно не добавлены до live verification; future deploys могут выглядеть готовыми, хотя payment/email verification ещё не завершена.
**Probability**: Medium
**Impact**: Medium
**Mitigation**: Держать Stripe/Resend verification отдельным checklist в [[next-steps]]. Перед включением оплат добавить `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `RESEND_API_KEY`, production `EMAIL_FROM` в Vercel и пройти live smoke. Rate limiting changes are currently verified on preview deploy `dpl_9WcPzfPgLUAb52HJbRKTGaxkPThe`; promote deliberately when ready to update production.

### R-012 — Owner trust gap before outreach
**Risk**: Владельцы бизнеса могут не доверить FlowOps реальные процессы, если сайт выглядит как обычный AI/automation лендинг без доказательств качества, аккуратности внедрения и снижения риска.
**Probability**: High
**Impact**: High
**Mitigation**: До масштабного outreach реализовать Phase 2F Trust Layer: risk-reduction deployment process, proof-of-work surfaces, implementation examples/mini-cases, audit next-step clarity, owner-approved workflow map, manual QA/monitoring signals, founder/operator credibility. Placeholder testimonials заменить, убрать или переформатировать до появления реальных клиентских результатов.
