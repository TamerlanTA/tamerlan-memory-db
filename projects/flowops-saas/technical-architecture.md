# FlowOps SaaS — Technical Architecture

## Related
- [[overview]]
- [[decisions]]
- [[roadmap]]

---

## Tech Stack (Confirmed)

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14+ (App Router) |
| Language | TypeScript |
| Styling | Tailwind CSS + CSS Modules |
| Animation | Framer Motion + GSAP (selective) + Lenis |
| Backend/API | Next.js API Routes |
| Database | Supabase (PostgreSQL) |
| Auth | Supabase Auth (Phase 3) |
| Automation Engine | n8n (self-hosted or cloud) |
| Payments | Stripe (Phase 2+) |
| AI Layer | OpenAI / Claude / Gemini (Phase 2+) |
| Email | Resend (Phase 2) / Telegram (Phase 1) |
| Notifications | Telegram via n8n (Phase 1) |
| Hosting | Vercel (frontend) |

---

## Database Schema (Supabase)

### Existing Tables (не трогаем)
```sql
audit_requests         -- Audit form submissions
audit_work_items       -- Internal work items
audit_response_drafts  -- Draft responses
```

### New Tables (Phase 1)

```sql
-- Pipeline definitions (static catalog)
pipeline_categories (
  id uuid PRIMARY KEY,
  slug text UNIQUE,
  name text,
  description text,
  icon text,
  sort_order int,
  created_at timestamptz
)

pipelines (
  id uuid PRIMARY KEY,
  slug text UNIQUE,
  category_id uuid REFERENCES pipeline_categories,
  name text,
  tagline text,
  description text,
  problem_statement text,
  what_it_does text,
  best_for text[],           -- ['clinics', 'real estate', ...]
  integrations text[],       -- ['CRM', 'WhatsApp', 'Slack']
  setup_price_from int,      -- in USD cents
  monthly_price_from int,
  deploy_days_min int,
  deploy_days_max int,
  tier int,                  -- 1=Entry, 2=Standard, 3=Complex, 4=Enterprise
  is_published boolean DEFAULT false,
  is_featured boolean DEFAULT false,
  requirements jsonb,
  expected_outcomes jsonb,
  related_pipeline_slugs text[],
  sort_order int,
  created_at timestamptz,
  updated_at timestamptz
)

-- Client orders
pipeline_orders (
  id uuid PRIMARY KEY,
  order_number text UNIQUE,  -- FLW-2026-001
  pipeline_id uuid REFERENCES pipelines,
  
  -- Contact info
  client_name text,
  client_email text,
  client_company text,
  client_website text,
  client_phone text,
  
  -- Business context
  current_tools text,        -- CRM they use, etc.
  business_description text,
  specific_requirements text,
  
  -- Status
  status text DEFAULT 'new', -- new|qualified|in_progress|deployed|active|paused|cancelled
  
  -- Pricing
  agreed_setup_price int,
  agreed_monthly_price int,
  subscription_tier text,    -- maintain|scale|operator|enterprise
  
  -- Internal
  internal_notes text,
  assigned_to text,
  deployed_at timestamptz,
  
  -- Audit origin (if came from audit)
  audit_request_id uuid REFERENCES audit_requests,
  
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
)

-- Active subscriptions (Phase 2)
pipeline_subscriptions (
  id uuid PRIMARY KEY,
  order_id uuid REFERENCES pipeline_orders,
  client_email text,
  tier text,                 -- maintain|scale|operator|enterprise
  price_monthly int,
  status text,               -- active|paused|cancelled
  stripe_subscription_id text,
  started_at timestamptz,
  next_billing_date date,
  created_at timestamptz
)

-- Order status history
order_status_history (
  id uuid PRIMARY KEY,
  order_id uuid REFERENCES pipeline_orders,
  from_status text,
  to_status text,
  note text,
  changed_by text,
  created_at timestamptz DEFAULT now()
)
```

### Phase 3 Tables (Client Accounts + Deal Room)
```sql
clients (
  id uuid PRIMARY KEY,
  supabase_user_id uuid,
  company text,
  email text,
  plan_tier text,
  ...
)

client_pipeline_instances (
  id uuid,
  client_id uuid,
  pipeline_id uuid,
  status text,  -- deploying|active|maintenance|paused
  health_score int,
  last_checked_at timestamptz,
  ...
)

automation_requests (
  id uuid PRIMARY KEY,
  client_id uuid REFERENCES clients,
  audit_request_id uuid REFERENCES audit_requests,
  pipeline_id uuid REFERENCES pipelines,
  pipeline_order_id uuid REFERENCES pipeline_orders,
  request_type text, -- pipeline|stack|audit_recommendation|custom
  title text,
  company_context text,
  current_tools text,
  process_description text,
  desired_outcome text,
  urgency text,
  budget_range text,
  status text, -- new|reviewing|scoping|proposal_sent|approved|deploying|active|closed
  assigned_to text,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
)

request_messages (
  id uuid PRIMARY KEY,
  request_id uuid REFERENCES automation_requests,
  sender_type text, -- client|flowops|system
  sender_user_id uuid,
  body text,
  is_internal boolean DEFAULT false,
  created_at timestamptz DEFAULT now()
)

request_status_history (
  id uuid PRIMARY KEY,
  request_id uuid REFERENCES automation_requests,
  from_status text,
  to_status text,
  note text,
  changed_by text,
  created_at timestamptz DEFAULT now()
)

support_requests (...)
invoices (...)
```

---

## API Routes Architecture

### Public Routes
```
POST /api/pipeline-order          -- Создать заказ на pipeline
POST /api/audit-request           -- Существующий (не трогаем)
GET  /api/pipelines               -- Список всех pipeline (публичный)
GET  /api/pipelines/[slug]        -- Детали pipeline
GET  /api/pipeline-categories     -- Категории
```

### Internal Routes (shared secret key)
```
GET    /api/internal/orders              -- Список заказов
GET    /api/internal/orders/[id]         -- Детали заказа
PATCH  /api/internal/orders/[id]/status  -- Обновить статус
POST   /api/internal/orders/[id]/note    -- Добавить заметку

GET    /api/internal/pipelines           -- Управление каталогом
POST   /api/internal/pipelines           -- Создать pipeline
PATCH  /api/internal/pipelines/[id]      -- Обновить pipeline
PATCH  /api/internal/pipelines/[id]/publish
```

### Phase 2+ Routes
```
POST /api/stripe/create-checkout        -- Setup fee payment
POST /api/stripe/create-subscription   -- Monthly subscription
POST /api/stripe/webhooks              -- Stripe webhook handler
POST /api/auth/login                   -- Client portal auth
```

### Phase 3 Client Account / Deal Room Routes
```
GET    /api/portal/me                         -- Current client account
POST   /api/portal/requests                   -- Create automation request / offer
GET    /api/portal/requests                   -- Client request list
GET    /api/portal/requests/[id]              -- Client-visible request detail
POST   /api/portal/requests/[id]/messages     -- Add client message

GET    /api/internal/requests                 -- FlowOps request inbox
GET    /api/internal/requests/[id]            -- Internal request detail
PATCH  /api/internal/requests/[id]/status     -- Update request status
POST   /api/internal/requests/[id]/messages   -- FlowOps reply or internal note
POST   /api/internal/requests/[id]/convert    -- Convert approved request to pipeline_order
```

---

## Page Architecture

### Public Pages
```
/                          -- Homepage (существующий, обновить)
/os                        -- Marketplace homepage (NEW)
/os/[category]             -- Category page (NEW)
/os/[slug]                 -- Pipeline detail page (NEW)
/pricing                   -- Subscription tiers (NEW)
/audit                     -- Free AI Audit (существующий)
/about                     -- About FlowOps
```

### Internal Pages (access key protected)
```
/internal                        -- Dashboard (существующий)
/internal/audits                 -- Audit list (существующий)
/internal/audits/[id]            -- Audit detail (существующий)
/internal/orders                 -- Pipeline orders list (NEW)
/internal/orders/[id]            -- Order detail + status management (NEW)
/internal/pipelines              -- Catalog management (NEW)
/internal/pipelines/[id]/edit    -- Edit pipeline (NEW)
```

### Phase 3 Client Accounts + Deal Room
```
/portal                    -- Client login
/portal/dashboard          -- Active pipelines
/portal/new-request        -- Submit automation request / offer inside account
/portal/requests           -- Client request list
/portal/requests/[id]      -- Request detail + in-site discussion
/portal/pipelines/[id]     -- Pipeline detail + health
/portal/billing            -- Subscription + invoices
/portal/support            -- Support requests

/internal/requests         -- FlowOps request inbox
/internal/requests/[id]    -- Scope, discuss, assign, convert to order
```

---

## n8n Automation Layer

### Internal Delivery Workflows
```
WF-01: New Order Notification
  Trigger: New row in pipeline_orders
  Action: Telegram notification to FlowOps team + summary

WF-02: Order Status Update Notification
  Trigger: Status change in pipeline_orders
  Action: Email to client (Resend) + internal Telegram

WF-03: Deployment Completion Flow
  Trigger: Status → 'deployed'
  Action: Welcome email to client, create subscription record, start billing

WF-04: Monthly Health Check
  Trigger: Cron (weekly)
  Action: Check active pipelines, flag issues, notify team

WF-05: Subscription Renewal Reminder
  Trigger: 7 days before renewal
  Action: Email to client with renewal confirmation
```

### Client Pipeline Flows (per pipeline type)
n8n workflows для каждой pipeline-системы — скрыты от клиентов.
Каждый workflow запускается в изолированном проекте n8n.

---

## Frontend Component System

### Core Components
```
<PipelineCard />          -- Marketplace карточка (grid view)
<PipelineDetailHero />    -- Hero section на detail page
<PipelineWorkflow />      -- Visual step diagram
<PipelinePricing />       -- Setup + monthly price block
<CategoryNav />           -- Категории с фильтрацией
<OrderForm />             -- Request deployment форма
<PricingCard />           -- Subscription tier card
<PricingTable />          -- Comparison table
<AuditForm />             -- Existing audit form
```

### Internal Components
```
<OrderCard />             -- Order summary в списке
<OrderDetail />           -- Полная карточка заказа
<StatusBadge />           -- Status chip (new/in_progress/deployed)
<OrderStatusTimeline />   -- История статусов
<PipelineEditorForm />    -- Редактирование pipeline в каталоге
```

---

## Security

- Internal routes: `x-internal-key` header (shared secret, env variable)
- Rate limiting: существующий middleware, расширить на /api/pipeline-order
- Supabase RLS: включить с Phase 1 для публичных данных
- No PII in logs
- Stripe webhooks: signature verification
- Phase 3: Supabase Auth + RLS per user

---

## Deployment

- Vercel: frontend + API routes
- Supabase: managed (уже настроен)
- n8n: self-hosted на VPS или n8n.cloud
- Environment variables: разделить dev/staging/prod
