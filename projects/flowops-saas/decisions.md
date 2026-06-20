# FlowOps SaaS — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

---

## Decision Log

### D-001 — Product Positioning
**Decision**: FlowOps OS позиционируется как AI Operations Platform, а не агентство автоматизаций.
**Why**: Агентства — commodity. Platform — IP и масштабируемый бизнес. Клиент покупает операционную систему, а не часы работы.
**Impact**: Все тексты, CTA, pricing и UX должны отражать platform-логику.

---

### D-002 — Hybrid Business Model (Setup + Subscription)
**Decision**: Гибридная модель: единоразовый setup fee + monthly subscription.
**Why**: Setup покрывает стоимость внедрения и создаёт commitment. Subscription = predictable revenue и long-term relationship.
**Impact**: Нужно объяснить клиенту ценность подписки — это не "поддержка", а living infrastructure.

---

### D-003 — Manual Delivery (Not Self-Serve) for MVP
**Decision**: MVP НЕ включает автодеплой pipeline-систем. Команда FlowOps делает это вручную.
**Why**: Self-serve деплой технически сложен. Для PMF важнее скорость запуска и качество первых клиентов.
**Impact**: Нужен чёткий internal delivery workflow. Клиент заполняет форму → команда deployes.

---

### D-004 — n8n скрыт от клиентов
**Decision**: n8n — внутренний engine. Клиент никогда не видит n8n интерфейс.
**Why**: n8n — не продукт для клиента. Клиент видит только результат (pipeline работает). Показ n8n разрушит премиум-восприятие.
**Impact**: Клиент видит статус, логи и результаты — но через собственный FlowOps UI.

---

### D-005 — Client Portal отложен
**Decision**: Полноценный client portal (login, dashboard, subscription management) — это Phase 3, не MVP.
**Why**: MVP нужен для валидации спроса. Portal — дорого строить до product-market fit.
**Impact**: В MVP клиент получает email-апдейты + ручную коммуникацию.

---

### D-006 — Stripe откладывается на Phase 2
**Decision**: В Phase 1 (MVP) оплата может быть через manual link или базовый Stripe Checkout.
**Why**: Полноценная Stripe-интеграция (subscriptions, invoices, webhooks) требует времени. MVP = validate demand first.
**Impact**: Первые клиенты могут платить через link (Stripe Checkout / PayPal / bank).

---

### D-007 — Design Direction: Premium Dark B2B
**Decision**: Дизайн — тёмный, графитовый, electric blue accents, Linear/Vercel/Stripe quality.
**Why**: Дешёвый дизайн = низкие цены в голове клиента. Premium UI = premium pricing.
**Impact**: Никаких ярких градиентов, никакого crypto-неона, никаких дешёвых карточек.

---

### D-008 — Loyalty через Stack Bundle + Tenure Rewards
**Decision**: Лучшая loyalty-модель — комбинация Stack Bundle Discount + Subscription Tenure Rewards.
**Why**: Bundle discount мотивирует покупать больше pipeline сразу. Tenure rewards удерживают долгосрочно.
**Impact**: 2+ pipelines = 10% discount на следующий setup; 3+ = 15%; 5+ = custom package.

---

### D-009 — Audit Form остаётся главной входной точкой
**Decision**: Free AI Operations Audit сохраняется и усиливается как главный CTA на сайте.
**Why**: Audit снижает барьер входа и создаёт персонализированный recommendation → natural upsell в конкретный pipeline.
**Impact**: После Audit → рекомендуем 2–3 pipeline-системы → ссылки на marketplace.

---

### D-010 — Supabase как единственная БД (MVP)
**Decision**: Supabase — primary database для MVP. Никаких других баз.
**Why**: Уже используется. PostgreSQL + realtime + auth in one. Избегаем overengineering.
**Impact**: Расширяем существующие таблицы, добавляем новые (pipelines, orders, subscriptions).

---

### D-011 — Local-first order API fallback
**Decision**: В Phase 1 `/api/pipeline-order` валидирует запрос и возвращает success payload без persistence, если Supabase env keys не настроены.
**Why**: Это позволяет тестировать UI/order flow локально до подключения реального Supabase проекта, не блокируя frontend build.
**Impact**: Перед production обязательно настроить `.env.local`, применить migration и проверить, что заказы реально пишутся в `pipeline_orders`.

---

### D-012 — Light Bright Product Direction
**Decision**: Текущее визуальное направление FlowOps OS изменено с premium dark на светлый, яркий, технологичный стиль: warm off-white base, strong blue/cyan, пастельные system cards, большие выразительные заголовки, animated workflow diagrams.
**Why**: Пользователь принёс sketch и reference juanmora.co; нужен более запоминающийся, живой и современный продуктовый интерфейс, не сухой dark SaaS.
**Impact**: Дизайн страниц `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders` должен сохранять light/bright direction. D-007 считается историческим решением, заменённым для текущей реализации.
