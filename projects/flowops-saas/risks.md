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
**Probability**: Medium (reduced from High — Phase 2F partially implemented June 29)
**Impact**: High
**Mitigation**: Phase 2F Trust Layer implemented June 29, 2026: `SafeDeploymentSection` (5-step owner-safe process), `DeploymentScenariosSection` (labeled examples, no fake quotes, disclaimer), "What happens next" audit clarity. Remaining: before/after examples on priority pipeline pages; founder/operator credibility block; real client results to replace scenarios as they become available.

### R-013 — Phase 3 before revenue validation
**Risk**: Client Accounts + Deal Room may consume implementation time before real clients create validated portal requirements.
**Probability**: Reduced after June 30 scope reversal, but still present if future agents resume portal work too early.
**Impact**: Medium–High
**Mitigation**: User reversed the MVP scope on June 30, 2026. Account/chat/deal-room must be deferred out of MVP and kept as future infrastructure. Current MVP should return to public audit + public system request/order form + internal order workspace + manual follow-up. Do not resume portal/deal-room work until explicitly reprioritized after sales/client validation.

### R-014 — Supabase Auth provider configuration blocks portal acceptance
**Risk**: Portal code is deployed, but real signup/login cannot pass acceptance while Supabase Auth is not fully configured.
**Probability**: High if/when portal is reactivated; currently deferred out of MVP.
**Impact**: Low for current MVP, high for future portal launch.
**Evidence**: Public Auth settings showed `external.google=false` and `mailer_autoconfirm=false`; user reported Google button does not work and confirmation email does not arrive. Vercel Preview/Production env contains required Supabase keys, so the blocker is provider/email configuration.
**Mitigation**: No longer a blocker for MVP because portal is not part of the current buyer-facing flow. Before future portal launch, enable Google provider in Supabase, configure callback/redirect URLs, and either disable email confirmations for MVP or configure reliable SMTP/custom Auth email delivery before testing signup.

### R-015 — Deal room becomes generic chat instead of operational workspace
**Risk**: If Phase 3 only adds messages, clients still will not have confidence about scope, next action, proposal, delivery state, decisions, billing, and support. The product would feel like an embedded inbox rather than a premium managed operations platform.
**Probability**: Medium when future portal work resumes.
**Impact**: High for future SaaS maturity, low for current MVP.
**Mitigation**: Keep `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md` as the future quality target. Do not expose a half-finished generic chat in MVP. When resumed, prioritize next-action visibility, scope summary, status timeline, proposal/approval layer, decision log, internal unread/waiting cues, and active-system links before decorative chat features.
