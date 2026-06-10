# FlowOps SaaS — Overview

## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[roadmap]]
- [[pipeline-catalog]]
- [[pricing]]
- [[technical-architecture]]

---

## Executive Summary

FlowOps OS — это AI operations platform уровня premium B2B SaaS, где бизнес выбирает готовые AI/automation pipeline-системы, заказывает внедрение и платит подписку за поддержку и развитие этих систем как живой инфраструктуры.

**Ключевая разница от агентства:**
> Мы не продаём услуги автоматизации. Мы продаём готовые операционные системы для бизнеса — как продуктовые модули, которые внедряются, подключаются к стеку клиента и обслуживаются через подписку.

---

## Product Definition

### Что это
- SaaS/Platform с marketplace готовых pipeline-систем
- Каждый pipeline = продуктовый модуль с ценой, описанием, setup процессом
- Гибридная бизнес-модель: setup fee + monthly subscription
- Команда FlowOps = delivery engine + operations team

### Что это НЕ
- Не агентство на заказ ("сделаем что угодно")
- Не Fiverr-маркетплейс дешёвых автоматизаций
- Не self-serve SaaS (пока нет автодеплоя)
- Не конструктор воркфлоу для клиента

### Positioning Statement
> "FlowOps OS — AI operations platform for modern businesses. Choose your operational system. We deploy it. You run on it."

---

## Target Customers (Primary)

### Tier 1 — Best fit
- Локальные сервисные бизнесы: клиники, стоматологии, авто, недвижимость, юристы
- SMB с 5–50 сотрудниками, есть CRM или хотят его
- Основатели/операционные директора, которые тратят время на ручные процессы
- Компании с повторяющимися операциями: продажи, входящие лиды, onboarding

### Tier 2 — Growth segment
- E-commerce с операционной болью (возвраты, поддержка, отчёты)
- SaaS-компании на ранних стадиях (customer success, onboarding)
- Агентства (marketing, real estate, legal) с повторяющимися флоу

### Tier 3 — Future
- Mid-market компании (50–200 человек)
- Корпоративный enterprise (отдельная ценовая матрица)

---

## Business Model

### Setup Fee
Единоразовая оплата за развёртывание pipeline-системы.
- Simple pipelines: $300–$500
- Standard pipelines: $500–$900
- Complex pipelines: $1,000–$2,000
- Custom/enterprise: quote

### Monthly Subscription
Регулярная плата за поддержку, мониторинг, обновления, инфраструктуру.

| Tier | Price | Pipelines |
|------|-------|-----------|
| Maintain | $149/mo | 1–2 active pipelines |
| Scale | $299/mo | 3–5 active pipelines |
| Operator | $549/mo | 6–10 active pipelines |
| Enterprise | Custom | 10+ pipelines |

### Loyalty Mechanics
- Stack Bundle Discount (при покупке 3+, 5+ pipeline)
- Subscription Tenure Rewards (3/6/12 месяцев)
- FlowOps Credits за каждый активный pipeline

Подробнее: [[pricing]]

---

## Current State (June 2026)
- Готовый лендинг/сайт FlowOps OS
- Free AI Operations Audit форма
- Supabase lead capture (audit_requests, audit_work_items, audit_response_drafts)
- Internal audit workspace (/internal/audits)
- API routes: POST /api/audit-request, status updates, draft edits
- Rate limiting, shared internal access key
- E2E QA checklist, production activation docs

Детали: [[current-state]]

---

## Tech Stack
- Next.js + React + TypeScript
- Tailwind CSS + CSS Modules
- Framer Motion + GSAP + Lenis
- Supabase (PostgreSQL + Auth future)
- n8n (automation engine, скрыт от клиентов)
- Stripe (future)
- OpenAI / Claude / Gemini (future AI layer)
- Resend (postponed)
- Telegram notifications (free alternative via n8n)

Детали: [[technical-architecture]]
