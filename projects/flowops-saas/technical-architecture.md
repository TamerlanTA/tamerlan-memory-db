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

### Phase 3 Quality Target Data Extensions

The current MVP tables are enough for the first portal/deal-room flow. The quality target in `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md` adds these future data needs.

Recommended additions when implementing quality batches:
- `automation_requests.next_action` or derived next-action fields (`waiting_for`, `next_action_label`, `next_action_due_at`)
- `automation_requests.proposal_status`
- proposal fields: recommended system, setup fee, monthly plan, included scope, excluded scope, timeline, required access, risk notes, approval state
- scope fields/versioning: problem statement, included workflow, excluded workflow, inputs, outputs, approval gates, edge cases, launch criteria
- message metadata for system events: event type, old/new status, proposal ID, approval ID, delivery stage, actor display name
- read/unread state for client/internal users
- internal inbox fields or derived views: last client message, last FlowOps reply, waiting state, overdue flag, assigned owner
- support request linkage to `client_pipeline_instances`
- billing state fields only after Stripe/subscription verification is reliable

Do not add file uploads until Supabase Storage buckets, RLS, file type limits, retention, and client/internal visibility rules are designed.

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

### Phase 3 Quality Target API Needs
```
PATCH  /api/portal/me                         -- Update profile/company/notification preferences
PATCH  /api/internal/requests/[id]/next-action
PATCH  /api/internal/requests/[id]/scope
POST   /api/internal/requests/[id]/proposal
PATCH  /api/internal/requests/[id]/proposal
POST   /api/portal/requests/[id]/approve      -- Approve proposal/scope when ready
POST   /api/portal/requests/[id]/support      -- Support/change request tied to request/system
PATCH  /api/portal/messages/[id]/read         -- Later read/unread tracking
```

Use these only when implementing the corresponding quality batch. Do not add unused endpoints speculatively.

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
/portal                    -- Client login / account entry
/portal/dashboard          -- Action-required, open deal rooms, active systems, recent activity
/portal/new-request        -- Structured automation/support/upgrade request intake
/portal/requests           -- Client request list with status, waiting state, last activity
/portal/requests/[id]      -- Deal room: chat, scope, status, next action, timeline, proposal, decisions
/portal/pipelines/[id]     -- Active system detail: status, health, monitoring summary, support/change path
/portal/billing            -- Honest billing overview; invoices/subscriptions only when Stripe data is reliable
/portal/support            -- Support/change request entry point, ideally tied to active system

/internal/requests         -- FlowOps request inbox with filters: status, owner, waiting, unread, overdue
/internal/requests/[id]    -- Client context, scope, chat, internal notes, status, proposal, convert to order
```

Current MVP gate (June 30, 2026):
- Client portal/account/chat/deal-room is deferred out of MVP.
- `ENABLE_CLIENT_PORTAL` must stay false/empty for the current MVP.
- When false, `src/middleware.ts` redirects `/portal/*` to `/#audit` and returns 404 for `/api/portal/*`.
- Public system ordering uses `/api/pipeline-order`, not `/api/portal/requests`.
- Preserve portal schema/routes/components as future infrastructure; do not delete unless explicitly requested.

### Deal Room Layout Contract
- Header: request number, title, client-visible status, last update, owner, next action.
- Main column: structured chat/activity stream.
- Side panel: scope summary, selected pipeline, desired outcome, tools, urgency, timeline, proposal/payment state, related links.
- Mobile: tabs for Conversation, Scope, Status, Proposal.
- Every open deal room must make the next action visible.
- Internal-only notes must be visually distinct and never returned to portal APIs.

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

### Phase 3 Portal / Deal Room Components
```
<PortalShell />                 -- Authenticated portal frame and nav
<AccountProfileForm />          -- Client/company profile and notification preferences
<PortalDashboard />             -- Action-required, open deal rooms, active systems, recent activity
<RequestIntakeForm />           -- Structured request creation
<RequestList />                 -- Request cards/table with status, waiting state, last activity
<DealRoom />                    -- Request detail workspace
<DealRoomHeader />              -- Number/title/status/owner/next action
<DealRoomChat />                -- Client-visible messages + system events
<DealRoomComposer />            -- Reliable message composer
<ScopeSummaryPanel />           -- Problem/outcome/tools/included/excluded/launch criteria
<StatusTimeline />              -- Request status history and system events
<ProposalPanel />               -- Proposal state, price, scope, approval CTA when implemented
<DecisionLog />                 -- Scope/price/access/launch/change decisions
<ActiveSystemCard />            -- Client pipeline instance summary
<SupportRequestForm />          -- Support/change request intake
```

### Phase 3 Internal Components
```
<InternalRequestInbox />         -- Filters by status/owner/waiting/unread/overdue
<InternalRequestDetail />        -- Client context + scope + chat + internal notes
<InternalReplyComposer />        -- Client-visible reply vs internal note toggle
<NextActionControl />            -- Waiting state / owner / due date
<ProposalEditor />               -- Manual proposal drafting
<ConvertToOrderAction />         -- Approved request to pipeline_order
```

---

## Security

- Internal routes: `x-internal-key` header (shared secret, env variable)
- Rate limiting: существующий middleware, расширить на /api/pipeline-order
- Supabase RLS: включить с Phase 1 для публичных данных
- No PII in logs
- Stripe webhooks: signature verification
- Phase 3: Supabase Auth + RLS per user
- Phase 3 portal APIs require bearer-token auth.
- Client can only read/write own `clients`, `automation_requests`, and non-internal `request_messages`.
- Client cannot set internal fields: assignment, internal status, price/proposal, conversion, internal notes.
- Internal APIs require `INTERNAL_ACCESS_KEY` and use service-role only server-side.
- Message/request creation should be rate-limited before public traffic.
- Test RLS boundary: client A cannot read client B request; clients cannot read `is_internal = true` messages.

---

## Deployment

- Vercel: frontend + API routes
- Supabase: managed (уже настроен)
- n8n: self-hosted на VPS или n8n.cloud
- Environment variables: разделить dev/staging/prod
