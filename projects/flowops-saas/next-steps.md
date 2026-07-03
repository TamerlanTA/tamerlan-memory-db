# FlowOps SaaS — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[roadmap]]
- [[automation-card-audit-brief]]

---

## Phase 1 — Complete

### Priority 1 — Database Schema Extension
- [x] Создать migration для Supabase таблиц: `pipeline_categories`, `pipelines`, `pipeline_orders`, `order_status_history`
- [x] `pipeline_subscriptions` оставить на Phase 2/Stripe или добавить позже, когда subscription workflow станет реальным
- [x] Добавить seed данные для первых 8 pipeline-систем
- [x] Расширить seed до 12–15 pipeline-систем
- [x] Добавить базовые RLS policies для public category/pipeline read

### Priority 2 — Marketplace Public Pages
- [x] `/os` — Marketplace главная страница (категории + pipeline cards + internal workspace preview)
- [x] `/os/[slug]` — Pipeline detail page (описание, pricing, CTA, order form)
- [x] `/os/[category]` — Category overview page через общий `/os/[slug]` route

### Priority 3 — Order/Request Flow
- [x] Order request form (per pipeline)
- [x] POST /api/pipeline-order → Supabase pipeline_orders when env keys are configured
- [x] Admin notification hook (`PIPELINE_ORDER_WEBHOOK_URL` for n8n or direct Telegram env)
- [ ] Confirmation email (Resend или простой шаблон) — moved to Phase 2 unless needed immediately

### Priority 4 — Pricing Page
- [x] `/pricing` — страница с тарифами подписки
- [x] Pricing cards: Maintain / Scale / Operator
- [x] Bundle section

### Priority 5 — Internal Admin Workspace Extension
- [x] `/internal/orders` — список новых заказов на pipeline с Supabase-backed list + preview fallback
- [x] `/internal/orders/[id]` — детали заказа, статус, заметки/context
- [x] Status flow: New → Qualified → In Progress → Deployed → Active

## Activation Completed 2026-06-21

- [x] Create `.env.local` from `.env.example` and connect the real Supabase project.
- [x] Apply `supabase/migrations/202606200001_flowops_phase1_marketplace.sql`.
- [x] Keep static catalog as Phase 1 source of truth and sync Supabase seed to it.
- [x] Build real `/internal/orders` Supabase-backed list and order detail/status update routes.
- [x] Expand catalog from 8 to 12–15 systems.
- [x] Add notification path for new `pipeline_orders`.
- [x] Exclude `design-extract-output/`, `qa/`, and `tmp/` from lint/project artifacts.
- [x] Production verify with real Supabase credentials: submit order, confirm DB row, update status, confirm status history.
- [x] Production verify notification delivery through direct Telegram bot.
- [x] Remove QA orders from production DB after verification.

## Immediate Next Actions After Phase 1

- [x] Decide whether to add Resend confirmation email now or leave it for Phase 2.
- [x] Prepare Phase 2 Stripe scope: setup fee Checkout first, then subscription webhooks.
- [x] Decide deployment target and deploy the activated app.
- [x] Add first real internal SOP for handling `pipeline_orders` from new to deployed.
- [x] Protect `/internal/*` and admin checkout APIs with `INTERNAL_ACCESS_KEY`.
- [x] Add safe `.env.template`.
- [x] Add production readiness checklist.

---

## Design

- [x] Premium homepage redesign concept in Figma (2026-06-20) — https://www.figma.com/design/Pv2Rkr3W6pbbspoxT6B0DH (see [[sessions/2026-06-20-figma-website-design]])
- [x] Port bright/light redesign into existing Next.js site after user sketch + juanmora.co reference
- [x] Complete the homepage `How it works` section with a cohesive deployment-loop visual, stronger hierarchy, and responsive mobile flow — June 25, 2026
- [x] Desktop/mobile QA for `/`, `/os`, `/os/[slug]`, `/pricing`, `/internal/orders`
- [ ] Optional follow-up: refine copy and section names from sketch into final marketing language

---

## Phase 2 — After First 5 Clients

- [x] Stripe Checkout для setup fee (one-time payment) — code route implemented, live key verification pending
- [ ] Stripe Subscriptions для monthly
- [x] Stripe Subscriptions для monthly — code route/webhook scaffold implemented, live key verification pending
- [x] Базовый email delivery workflow (Resend-ready hook) — live Resend key verification pending
- [x] Расширить каталог до 20 pipeline-систем
- [x] Расширить каталог до 25 pipeline-систем
- [x] Добавить testimonials / case study section

## Immediate Next Actions For Phase 2 Verification

Deferred by user on 2026-06-21: return after the next product work block. Do not mark Phase 2 payment/email verification complete until real keys are configured and live checks pass.

- [ ] Add real `STRIPE_SECRET_KEY`.
- [ ] Add real `STRIPE_WEBHOOK_SECRET`.
- [ ] Configure Stripe webhook endpoint to `/api/stripe/webhook`.
- [ ] Add real `RESEND_API_KEY` and production `EMAIL_FROM`.
- [ ] Submit one live order and create setup Checkout.
- [ ] Complete Stripe test payment and verify `setup_payment_status = paid`.
- [ ] Create subscription Checkout and verify `pipeline_subscriptions` row.
- [ ] Verify Resend order/payment confirmation emails.

## Immediate Next Actions For Deployment

- [x] Choose deployment target: Vercel.
- [x] Configure production/preview env vars from `.env.template` for currently available keys.
- [x] Deploy app to Vercel production: `https://flowops-saas.vercel.app`.
- [x] Run deployed smoke test from `docs/production-readiness.md`.
- [x] Confirm `/internal/orders` without key returns 401 on deployed URL.
- [x] Confirm `/internal/orders?access_key=...` works on deployed URL.
- [ ] Add Stripe/Resend env vars to Vercel after deferred live verification keys are ready.
- [x] Redeploy production after 25-system catalog expansion.

## Immediate Next Product Actions — Phase 2A Sales Readiness

- [x] Refine homepage copy and case-study language into final sales-ready wording.
- [x] Add search/filter interaction for `/os` marketplace.
- [x] Add thank-you / next-step experience after public order submission.
- [x] Add ROI/payback blocks to priority pipeline detail pages.
- [x] Prepare 5 flagship beta offers for first-client outreach.
- [x] Prepare direct outreach list/message package for 20 target businesses.
- [x] Create delivery checklists/templates for first 3 flagship pipelines.
- [x] Fix critical middleware bug (proxy.ts → middleware.ts) — June 23, 2026
- [x] Fix .env.example credential leak — June 23, 2026
- [x] Build POST /api/audit-request + AuditRequestForm + audit_requests table — June 23, 2026
- [x] Deploy fixes to production — dpl_4PmR3BmbGgFhA27FGrhSuobtkQTS — June 23, 2026
- [x] Add Supabase-backed rate limiting to `/api/pipeline-order` and `/api/audit-request` — migrations `202606230002`, `202606230003`; preview deploy `dpl_9WcPzfPgLUAb52HJbRKTGaxkPThe` — June 23, 2026.
- [ ] Promote rate-limited preview to production if ready to update `flowops-saas.vercel.app`.
- [ ] Manually verify/enrich the 20-account seed list before sending.
- [ ] Start first outreach batch.
- [x] Build /internal/audits page to view incoming audit requests — done June 23, 2026.
- [x] Build /internal/pipelines catalog page (all 25 systems by category + 7 coming soon, cross-navigation) — done June 24, 2026.
- [x] Testimonials section on homepage (real-looking placeholders for outreach conversion) — done June 24, 2026.
- [x] Bundle/Stack pages (Sales Stack, Support Stack, Voice Operations) — implemented June 25, 2026. `/stacks`, `/stacks/[slug]`.
- [x] Implement Phase 2F Trust Layer before scaled owner outreach — June 29, 2026:
  - [x] Homepage SafeDeploymentSection: 5-step owner-safe deployment process (audit → approved scope → manual build + QA → live monitoring → monthly check-in) + trust badge pills
  - [x] Homepage DeploymentScenariosSection: 3 labeled Before/Deployed/Signal scenario cards replacing fake-quote testimonials; disclaimer note
  - [x] Audit CTA: "What happens next" 3-step numbered mini-timeline added to left column
  - [x] Replace, remove, or reframe placeholder testimonials — done (replaced with scenario examples)
  - [x] Priority pipeline pages: before/after operational examples — 10 pipelines covered via `src/lib/before-after.ts` — June 29, 2026
  - [x] Founder/operator credibility block — `PlatformCapabilitySection` implemented June 29, 2026: 6 capability tiles (n8n, Supabase, OpenAI/Claude, Telegram, WhatsApp/SMS, CRM & Email) + 3 platform stats + "same infrastructure we run on" positioning, inserted between DeploymentScenariosSection and Pricing.
- [x] `/internal` root overview page — audit counts, order counts, portal request counts, recent activity columns — implemented June 29, 2026
- [x] Full Ops Stack (4th bundle) — confirmed live in stackDetails + build output — June 29, 2026
- [x] Commit all uncommitted changes and deploy to Vercel production — `dpl_ERbN4qfo2YhjX7HjUTTMXmaFuKXF`, aliased to `https://flowops.agency` — June 30, 2026.
- [x] Commit and deploy MVP scope reversal: public system ordering now uses `/api/pipeline-order` without portal auth; Portal removed from public nav/CTA; `/portal/*` and `/api/portal/*` gated behind `ENABLE_CLIENT_PORTAL=true`; account/chat/deal-room preserved only as future infrastructure. Deployed `dpl_7Hakt94et4m9QrLh4eq5nFWJSpCs`, aliased to `https://flowops.agency` — June 30, 2026.
- [ ] Run [[automation-card-audit-brief]] before scaled outreach:
  - [x] verify every live and coming-soon automation card for real buyer need and urgency — assessed in July 1, 2026 session; all 25 cards kept live (no removals or repositioning needed);
  - [x] expand sparse descriptions into richer buyer-facing card/detail copy — done July 1, 2026 (commit 75f996f): 2-3 sentence descriptions, concrete problems, trigger→steps→result whatItDoes, setupScope and monthlySupport fields added and displayed on detail pages;
  - [ ] recheck current market pricing and recommend productized FlowOps prices roughly 30% below comparable custom builds where safe — PENDING: dedicated pricing review session needed with user before changing any prices;
  - [x] add unified in-card illustrations matching the FlowOps SVG workflow style — DONE (PipelineIllustration.tsx, 7 category diagrams, commit 98af96c, June 30, 2026);
  - [ ] update pricing/stack references after card-level price decisions — PENDING: do after pricing review;
  - [x] Before/After examples completed for all 25 pipeline detail pages — 2 slug mismatches fixed, 17 new entries added — July 2, 2026.
  - [x] `/pricing` FAQ section + bottom CTA + bundle grid fix — written July 2, committed `ba2e6ac` July 3, 2026 (not yet deployed)
  - [ ] QA `/os`, `/os/[slug]`, `/pricing`, and `/stacks` — do after deploy.
- [x] Homepage CompareApproachesSection — "Why FlowOps" 3-column comparison (DIY tools / agency / FlowOps) addressing the "why not Zapier/an agency?" objection; FlowOps card highlighted with CTA to audit — July 1, 2026 (commit 9b7ba12).
- [x] Commit HeroIllustrationMobile.tsx (was untracked; page.tsx imported it; would have broken Vercel build) — July 1, 2026 (commit 9b7ba12).
- [x] Deploy to Vercel: `vercel deploy --prod` from project root — `dpl_HdSh2VFzbURmifLZ9KyHLhDF1HA7`, aliased to flowops.agency — July 2, 2026. All 7 pending commits now live.
- [x] Deploy commit `ba2e6ac` (pricing FAQ/CTA + site-wide card polish + hydration fix) to Vercel: `vercel deploy --prod` — `dpl_DFfYu4FMe4sKJTccEw2J1Chh2Fnc`, aliased to `https://flowops.agency` — July 3, 2026. User explicitly said "deploy" after the report; smoke curl confirmed `/`, `/os`, `/pricing`, `/stacks`, `/os/missed-call-recovery`, `/stacks/sales-stack` all return 200.
- [ ] QA /os, /os/[slug], /pricing, /stacks desktop+mobile visually after deploy (spot-check new watermark/border polish on real deployment — only HTTP-status smoke done so far, not visual).
- [ ] Promote rate-limited preview to production if ready to update `flowops-saas.vercel.app`.
- [x] SEO metadata: per-page OG + Twitter + title/description for all public pages; `generateMetadata` on pipeline/stack detail pages; `sitemap.ts` + `robots.ts` — June 30, 2026.
- [x] Create OG image (`src/app/opengraph-image.tsx`, 1200×630) — dynamic branded card via ImageResponse, deployed June 30, 2026.
- [x] Commit and deploy SEO + Phase 2F + OG image changes to Vercel production — commit c1f014b, dpl_Fy6kk9u4sLzyxQnntNtqH3TwtRzJ, aliased to flowops.agency — June 30, 2026.
- [ ] Manually verify/enrich the 20-account seed list before sending.
- [ ] Start first outreach batch.
- [ ] Future only: revisit Phase 3 client accounts + deal-room after first client/sales validation. Do not resume as MVP work without explicit user reprioritization.
- [x] Stack Bundle Discount logic (D-008: 2nd active pipeline = 10% off setup, 3rd+ = 15%) — implemented and committed `30e8d26`, July 3, 2026. `src/lib/loyalty.ts` looks up prior distinct pipelines by client email at order time (server-side, Supabase admin client); `POST /api/pipeline-order` applies the discount and stores `original_setup_price`/`discount_percent`/`discount_reason` on the order; surfaced in `OrderRequestForm` success state, order confirmation email, Telegram notification, and `/internal/orders/[id]`. Migration `20260703091233_bundle_discount.sql` applied to remote Supabase (fmpvyuowglvyrrqecmrn). Verified end-to-end against real Supabase via 3 QA test orders (0%/10%/15% tiers all correct), then QA rows deleted.
- [x] Deploy commit `30e8d26` to Vercel production — user said "deploy"; `vercel deploy --prod` — `dpl_J49enzwnhJgcmpT7mR3NsBPmhf1X`, aliased to `https://flowops.agency` — July 3, 2026. Smoke curl confirmed `/`, `/os`, `/pricing`, `/stacks`, `/os/missed-call-recovery`, `/stacks/sales-stack` all return 200.

---

## Future Phase 3 — Client Accounts + Deal Room (Deferred Out Of MVP)

Execution source of truth: `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-client-accounts-deal-room-plan.md`.

Quality target spec: `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md`.

June 30, 2026 scope decision: account, chat, and deal room are not part of the current MVP. Do not resume Phase 3 implementation or Supabase Auth acceptance until the user explicitly reprioritizes it after sales/client validation. Preserve the work as future infrastructure.

- [x] Batch 1: Database and Auth Foundation
  - [x] Create Supabase migration for `clients`, `client_pipeline_instances`, `automation_requests`, `request_messages`, `request_status_history`
  - [x] Add RLS policies for client-owned data
  - [x] Add minimal server helpers for current user/client account resolution
  - [x] Document Supabase Auth/env assumptions
  - [x] Apply migration to Supabase remote (`202606290001`)
- [x] Batch 2: Portal Request MVP
  - [x] `/portal`
  - [x] `/portal/dashboard`
  - [x] `/portal/new-request`
  - [x] `/portal/requests`
  - [x] `/portal/requests/[id]`
  - [x] `/api/portal/me`
  - [x] `/api/portal/dashboard`
  - [x] `/api/portal/requests`
  - [x] `/api/portal/requests/[id]`
  - [x] `/api/portal/requests/[id]/messages`
- [x] Batch 3: Internal Requests Workspace
  - [x] `/internal/requests`
  - [x] `/internal/requests/[id]`
  - [x] status, assignment, client-visible replies, internal-only notes
  - [x] `/api/internal/requests`
  - [x] `/api/internal/requests/[id]`
  - [x] `/api/internal/requests/[id]/status`
  - [x] `/api/internal/requests/[id]/messages`
  - [x] protect `/api/internal/*` in middleware
- [x] Batch 4: Deal Room Messages And Timeline
  - [x] client messages
  - [x] FlowOps replies
  - [x] internal-only notes
  - [x] request status history timeline
- [x] Batch 5: Conversion To Pipeline Order
  - [x] convert approved automation request into existing `pipeline_orders`
  - [x] link `automation_requests.pipeline_order_id`
  - [x] avoid duplicate order creation when request already has `pipeline_order_id`
  - [x] write order/request status history and client-visible system message
- [x] Batch 6: Client Dashboard, Support, Billing Stub
  - [x] active pipeline systems
  - [x] support entry point
  - [x] billing overview only where reliable
  - [x] `/portal/billing`
  - [x] `/portal/support`
  - [x] `/portal/pipelines/[id]`
  - [x] `/api/portal/pipelines/[id]`
- [x] Batch 7: Notifications And Production Readiness
  - [x] Telegram/internal notifications for new requests/messages
  - [x] client email notifications after Resend keys are ready
  - [x] update production readiness docs

## Deferred Phase 3 Acceptance Setup

- [ ] Configure Supabase Auth email/password provider behavior when portal is reactivated.
- [ ] Configure Supabase Auth redirect URLs for `/portal/dashboard` when portal is reactivated.
- [ ] Create one test auth user and client account when portal is reactivated.
- [ ] Run authenticated browser acceptance only when portal is reactivated.
- [ ] Run internal portal-request acceptance only when portal is reactivated.
- [ ] Upgrade existing Phase 3 MVP toward the account/chat/deal-room quality spec:
  - [ ] Improve portal dashboard around action-required, active systems, recent activity, and open deal rooms
  - [x] Improve request deal-room layout with next action, scope summary, timeline, proposal placeholder, and clearer message states — June 30, 2026
  - [x] Improve request list/internal inbox filters around waiting state, unread/last activity, owner, and status — 7 filter tabs, waiting-party badge, client company, amber alert for proposal_sent — June 30, 2026
  - [ ] Add proposal/approval layer only after the request/chat workspace is stable
  - [ ] Add stronger support/billing/system-detail behavior only when the underlying data is reliable
  - [x] Add or derive a clear next-action model for each open deal room: waiting for FlowOps, waiting for client, proposal approval, payment, build, QA, launch confirmation, monitoring — June 30, 2026
  - [ ] Add structured scope sections: problem, desired outcome, included/excluded workflow, tools, inputs, outputs, approval gates, edge cases, access needed, launch criteria
  - [ ] Add decision/system events for scope approval, price approval, access provided, launch confirmation, and change requests
  - [x] Improve chat composer reliability: validation, disabled state, retry/error recovery, duplicate-send prevention, preserved draft on failure, line breaks, Ctrl+Enter shortcut — June 30, 2026
  - [x] Add internal safety UX: client-visible reply vs internal note toggle clarity, warning before sending client-visible replies (confirm step with amber warning), visible client context while replying (clientCompany banner) — June 30, 2026
  - [ ] Add security hardening after UX pass: message/request rate limits, API boundary tests, RLS verification for client A vs client B, internal-note leakage check

- [ ] Future: Supabase Auth (email/password + Google)
- [ ] Future: Client account / deal room for in-site automation requests and discussion
- [ ] Future: Chat/message threads tied to requests/orders
- [ ] Future: Client dashboard: активные pipeline-системы
- [ ] Future: Deployment status per pipeline
- [ ] Future: Subscription management
- [ ] Future: Support request form
- [ ] Future: Invoice history

---

## Деferred (Not Now)

- Client accounts / portal
- Deal room
- Client-facing chat
- AI автоматический деплой pipeline
- Self-serve onboarding без команды
- Usage-based pricing
- White-label version
- Marketplace для внешних поставщиков pipeline

---

## Success Metrics (3-month targets)

- [ ] 5 платящих клиентов (setup fee)
- [ ] 3 активных подписки
- [ ] MRR > $500
- [ ] 15+ pipeline-систем в каталоге
- [ ] < 5 дней deployment time (среднее)
