# FlowOps SaaS — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[automation-card-audit-brief]]

---

## Status: MVP SALES VALIDATION — PORTAL / CHAT / DEAL ROOM DEFERRED (July 3, 2026)

Проект задеплоен на Vercel: `https://flowops.agency` (production alias) / `https://flowops-saas.vercel.app`
**Текущий production-деплой**: `dpl_J49enzwnhJgcmpT7mR3NsBPmhf1X` (July 3, 2026) — commit `30e8d26` deployed: Stack Bundle Discount logic (10%/15% loyalty pricing on repeat pipeline orders, `src/lib/loyalty.ts`, migration `20260703091233_bundle_discount.sql` already live on remote Supabase). Deployed via `vercel deploy --prod`, aliased to `https://flowops.agency`. Smoke-verified: `/`, `/os`, `/pricing`, `/stacks`, `/os/missed-call-recovery`, `/stacks/sales-stack` all return 200. See [[sessions/2026-07-03-bundle-discount-logic]] and [[decisions]] D-019.
**Предыдущий production-деплой**: `dpl_DFfYu4FMe4sKJTccEw2J1Chh2Fnc` (July 3, 2026) — commit `ba2e6ac` deployed: `/pricing` FAQ (10 entries) + bottom CTA + 2×2 bundle grid; site-wide card polish (unified neutral borders + numbered watermark motif on homepage/`/os/[slug]`/`/stacks`/pipeline cards); `RevealOnView.tsx` hydration-mismatch fix + `react-hooks/set-state-in-effect` lint fix; `layout.tsx` noscript reveal fallback. Deployed via `vercel deploy --prod`, aliased to `https://flowops.agency`. Smoke-verified: `/`, `/os`, `/pricing`, `/stacks`, `/os/missed-call-recovery`, `/stacks/sales-stack` all return 200. See [[sessions/2026-07-03-pricing-polish-commit-hydration-fix]].
**Предыдущий production-деплой**: `dpl_HdSh2VFzbURmifLZ9KyHLhDF1HA7` (July 2, 2026) — 7 pending commits deployed:
- 88c8bb2 — Before/after examples for all 25 pipeline detail pages; fixed 2 slug key mismatches (appointment-booking, customer-onboarding). Build clean (68 pages).
- 9b7ba12 — Homepage: CompareApproachesSection + HeroIllustrationMobile
- 75f996f — Automation card audit phase 2: enriched descriptions, setupScope/monthlySupport, mobile pass, RevealOnView
- 98af96c — PipelineIllustration.tsx: 7 category SVG workflow diagrams on all 25 cards
- 16a3c07 — How it works: RequestToProofIllustration animated SVG
- c1f014b — SEO metadata + OG image + sitemap + robots + Phase 2F trust layer
- eea3471 — MVP scope reversal: unauthenticated order flow, portal gated
Note: repo has no git remote; deploy via `vercel deploy --prod` from project root.
**Предыдущий production-деплой**: `dpl_Fy6kk9u4sLzyxQnntNtqH3TwtRzJ` (June 30, 2026) — OG Image + SEO metadata + sitemap + robots + Phase 2F trust layer committed (c1f014b) and deployed. 68 pages. Aliased to `https://flowops.agency`. See [[sessions/2026-06-30-og-image-commit-deploy]].
Предыдущий production-деплой: `dpl_Fy6kk9u4sLzyxQnntNtqH3TwtRzJ` (June 30, 2026) — OG Image + SEO metadata + sitemap + robots + Phase 2F trust layer committed (c1f014b) and deployed. 68 pages. Aliased to `https://flowops.agency`. Includes design overhaul (fonts, shadows, animations) + OG image + sitemap.xml + robots.txt. See [[sessions/2026-06-30-og-image-commit-deploy]].
Предыдущий production-деплой: `dpl_52MqBqFmpHSoSDTArDv12YtZ8cf3` (June 30, 2026) — DESIGN OVERHAUL. Fonts → Bricolage Grotesque (headings) + Plus Jakarta Sans (body); fixed cramped big headers (relaxed negative letter-spacing site-wide); layered shadow system + `.fo-card`/`.fo-pill`; gradient buttons w/ sheen+hover lift; PROOF OF WORK CASE SIGNAL illustrations (trend/bars/donut) w/ CSS draw-in; enlarged bundle/stack cards; on-theme CSS-only animations. Now committed in git at c1f014b. См. [[sessions/2026-06-30-design-overhaul-fonts-proof-bundles]].
Предыдущий production-деплой: `dpl_7Hakt94et4m9QrLh4eq5nFWJSpCs` (June 30, 2026) — MVP scope reversal committed and deployed. Public order flow restored to `/api/pipeline-order`, Portal removed from public nav, `/portal/*` and `/api/portal/*` gated behind `ENABLE_CLIENT_PORTAL=true`. Commit: eea3471. Aliased to `https://flowops.agency`. Smoke: / → 200, /os → 200, /portal → /#audit redirect, /api/portal/me → 404.
Предыдущий production-деплой: `dpl_ERbN4qfo2YhjX7HjUTTMXmaFuKXF` (June 30, 2026) — Phase 3 deal room quality + portal order flow + internal inbox filters. Now superseded by MVP reversal deploy.
Предыдущий preview-деплой: `https://flowops-saas-pvoewrzoy-tamertt931-8560s-projects.vercel.app` (`dpl_92thMKzyip2qEvXBSi1MtV37EiKu`, June 30, 2026) — MVP scope reversal preview: public order flow restored to `/api/pipeline-order`, Portal removed from public nav/CTA, `/portal/*` gated behind `ENABLE_CLIENT_PORTAL=true`.
Предыдущий production-деплой: `dpl_BFmqow1CuW5GJaBrm97H6MMSXLwH` (June 29, 2026) — Phase 2F trust layer + Phase 3 Client Accounts + Deal Room + Stacks + before/after + PlatformCapabilitySection.
Предыдущий preview-деплой: `https://flowops-saas-iitm3l12k-tamertt931-8560s-projects.vercel.app` (`dpl_HB686N97K3PHnrZomt9Vya9rCZTu`, June 29, 2026) — Phase 3 Client Accounts + Deal Room, email/password + Google auth UI, portal/internal request workspace, request-to-order conversion, notifications/readiness
Предыдущий preview-деплой: `https://flowops-saas-lgumct4fo-tamertt931-8560s-projects.vercel.app` (`dpl_EFSeU9rDXWs8Nz5G3FHMrHEfSFaj`, June 26, 2026) — homepage marketplace section refinement + marquee overlap fix
Предыдущий preview-деплой: `https://flowops-saas-ixaq9qpdk-tamertt931-8560s-projects.vercel.app` (`dpl_E2S1npxw1oy3hUnfNBLeffhhPxWm`, June 26, 2026) — frameless homepage `How it works` refinement
Предыдущий деплой: `https://flowops-saas-2eawb4npr-tamertt931-8560s-projects.vercel.app` (June 25, 2026) — Stack pages deployment
Предыдущий деплой: `dpl_4PmR3BmbGgFhA27FGrhSuobtkQTS` (June 23, 2026)

Полный технический аудит выявил и исправил критические баги — ряд задач был помечен в памяти как "done" без реальной реализации в коде.

---

## Что уже готово (проверено по коду)

### Public Site
- [x] FlowOps OS homepage с полным контентом и proof/case-study секцией
- [x] Homepage `How it works` section upgraded into a frameless, canvas-integrated deployment-loop composition with abstract color fields and only two functional product surfaces — June 25, 2026
- [x] Homepage marketplace teaser rebuilt into an editorial product-shelf composition: one featured workflow, overlapping pastel system tiles, abstract color fields, and retained trust marquee — June 26, 2026
- [x] Homepage custom workflow section rebuilt from a block grid into an open, canvas-integrated process map with trigger/map/build/approve nodes and lightweight decision logic — June 29, 2026
- [x] Testimonials section replaced with `DeploymentScenariosSection` — 3 labeled Before/Deployed/Signal cards for dental clinic, real estate, HVAC; disclaimer note; no fake attributed quotes — June 29, 2026
- [x] `SafeDeploymentSection` on homepage — 5-step deployment process (audit map → owner-approved scope → manual build + QA → live with monitoring → monthly check-in) + trust badge pills — June 29, 2026
- [x] "What happens next" 3-step mini-timeline added to audit CTA left column — June 29, 2026
- [x] Секция `#audit` — реальная форма `AuditRequestForm` с POST `/api/audit-request`
- [x] 25 pipeline систем в `src/lib/catalog.ts` и в Supabase
- [x] `/os` marketplace с working search/filter через `MarketplaceExplorer`
- [x] `/os` "Coming Soon" pipeline cards — 7 announced systems in separate "On the Roadmap" section
- [x] Homepage `How it works` section — `RequestToProofIllustration.tsx` animated SVG deployment-loop panel (CSS-only, SSR-safe, reduced-motion); flat blue buttons; Geist headers; clean trend illustration — committed 16a3c07, June 30, 2026
- [x] Pipeline card illustrations — `PipelineIllustration.tsx` with 7 category SVG mini-flow diagrams; added to all 25 live cards via `PipelineCard.tsx` — committed 98af96c, June 30, 2026
- [x] Automation card audit phase 2 — all 25 pipeline descriptions enriched to 2-3 buyer-facing sentences; `problem` made concrete; `whatItDoes` expanded to full trigger→steps→result; `setupScope` and `monthlySupport` fields added to Pipeline type and filled for all 25 systems — committed 75f996f, July 1, 2026
- [x] `/os/[slug]` pipeline detail pages now show Setup Scope and Monthly Support sections — July 1, 2026
- [x] Mobile responsive pass — all public page h1/h2/price nodes get fluid mobile sizes with sm: breakpoints; HeroIllustration min-h mobile fix; portrait mobile SVG variant for RequestToProofIllustration — July 1, 2026
- [x] `RevealOnView.tsx` — new scroll-reveal utility component (IntersectionObserver + lazy state init, lint-safe) — July 1, 2026
- [x] `HeroIllustrationMobile.tsx` — phone-native hero SVG (chaos→engine→outputs, CSS-only animations, RevealOnView, staggered entrance) — committed July 1, 2026 (was untracked, would have broken Vercel build)
- [x] `CompareApproachesSection` on homepage — "Why FlowOps" section (DIY tools vs agency build vs FlowOps OS, 3-column 5-point comparison, FlowOps card highlighted with `#audit` CTA) — July 1, 2026
- [x] Before/After operational examples on all 25 pipeline detail pages — fixed 2 slug mismatches (appointment-booking, customer-onboarding were silently broken); added 17 new entries covering all remaining pipelines — July 2, 2026
- [x] Production deploy `dpl_HdSh2VFzbURmifLZ9KyHLhDF1HA7` — all 7 pending commits live at `https://flowops.agency` — July 2, 2026
- [x] `/pricing` FAQ section — 10 buyer-facing Q&A entries (native `<details>/<summary>` accordion, SSR-safe, no JS); addresses all main objections before audit CTA — written July 2, committed `ba2e6ac` July 3, 2026
- [x] `/pricing` bottom CTA section — gradient card with "Start with a free workflow audit" heading, dual CTAs to `/#audit` and `/os`, trust tagline — written July 2, committed `ba2e6ac` July 3, 2026
- [x] `/pricing` bundle grid fix — changed `lg:grid-cols-3` to `sm:grid-cols-2` so 4 bundles show in clean 2×2 grid — written July 2, committed `ba2e6ac` July 3, 2026
- [x] Site-wide card polish — unified neutral `border-[#101728]/[0.06]` card borders (replacing per-category colored borders) + `CardWatermark` numbered-watermark motif on homepage (`SafeDeploymentSection`, `DeploymentScenariosSection`, proof cards), `/os/[slug]` payback/after-FlowOps panels, `/stacks` bundle cards, `PipelineCard`/`ComingSoonPipelineCard` — committed `ba2e6ac`, July 3, 2026
- [x] `RevealOnView.tsx` SSR/client hydration mismatch fixed — `shown` state now initializes identically on server and client; no-`IntersectionObserver` fallback deferred into `requestAnimationFrame` to satisfy `react-hooks/set-state-in-effect` lint rule; `layout.tsx` adds `<noscript>` CSS fallback — committed `ba2e6ac`, July 3, 2026
- [x] `/os/[slug]` pipeline detail pages (32 pages)
- [x] SEO metadata: per-page `metadata` exports on `/`, `/os`, `/pricing`, `/stacks`; `generateMetadata` on `/os/[slug]` and `/stacks/[slug]`; all pages have unique OG title + description + Twitter card — June 30, 2026
- [x] `metadataBase` set to `https://flowops.agency` in root layout — OG URLs resolve correctly in production — June 30, 2026
- [x] `src/app/sitemap.ts` — generates `/sitemap.xml` with 36 URLs (4 static + 25 pipelines + 7 categories + 4 stacks), priorities and changeFrequency set — June 30, 2026
- [x] `src/app/robots.ts` — generates `/robots.txt`: crawlers allowed on public routes, blocked on `/internal/`, `/portal/`, `/api/`, sitemap pointer — June 30, 2026
- [x] `src/app/opengraph-image.tsx` — dynamic branded OG card via ImageResponse (1200×630): gradient warm bg, "Deploy proven AI systems" 3-line heading, blue logo mark, stats pills (25 systems, 7 categories, 48h), 5 decorative pastel system tiles, flowops.agency URL — June 30, 2026
- [x] `/os/[slug]` Before/After operational examples section — 10 priority pipelines (missed-call-recovery, leados-lead-research, inboxos-support-inbox, crmos-automation-suite, faq-automation, crm-follow-up, proposal-automation, daily-operations-report, onboarding-automation, appointment-booking-automation) — June 29, 2026
- [x] `/stacks` — System Stacks overview page (all 4 bundles with savings badge, system tags, pricing) — June 25, 2026
- [x] `/stacks/[slug]` — Individual stack detail pages: Sales Stack, Support Stack, Voice Operations, Full Ops Stack — June 25/29, 2026 (Full Ops Stack data was already in stackDetails, confirmed via build output)
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
- [x] Stack Bundle Discount logic — `src/lib/loyalty.ts` + `POST /api/pipeline-order` apply D-008's 10%/15% loyalty tiers automatically at order time by counting a client's prior distinct pipelines by email; `pipeline_orders` gained `original_setup_price`/`discount_percent`/`discount_reason` columns; surfaced in order confirmation, Telegram notification, and `/internal/orders/[id]` — implemented and verified end-to-end July 3, 2026 (commit `30e8d26`)

### Migrations applied to Supabase (fmpvyuowglvyrrqecmrn)
- `202606200001` — Phase 1 schema
- `202606210001` — Phase 2 payments
- `202606210002` — Catalog to 20 systems
- `202606220001` — Catalog to 25 systems
- `20260623085205` — audit_requests table (remote canonical migration fetched from Supabase history)
- `202606230002` — rate_limit_buckets table + check_rate_limit RPC
- `202606230003` — check_rate_limit RPC returning fix
- `20260703091233` — bundle_discount: `pipeline_orders.original_setup_price`/`discount_percent`/`discount_reason`

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
- [x] `/internal` root overview dashboard — audit counts, order counts, portal request counts, 3-column recent activity, quick nav — implemented June 29, 2026
- [x] Full Ops Stack (4th bundle) — confirmed live via build output, data was already in stackDetails June 29, 2026
- [ ] Первый outreach batch (20 целевых аккаунтов)
- [x] Remove/de-emphasize portal/account/deal-room from public MVP buyer flow in preview; production promotion pending

---

## Активная фаза

**Phase 2A — Sales Readiness COMPLETE** (June 25, 2026). Все code tasks Phase 2A выполнены: audit form, coming soon cards, footer, rate limiting, /internal/audits, /internal/pipelines, testimonials, bundle/stack pages.

**Phase 2F — Trust Layer COMPLETE** (June 29, 2026). Homepage has `SafeDeploymentSection`, `DeploymentScenariosSection`, "What happens next" mini-timeline, and `PlatformCapabilitySection` (founder/operator credibility block — 6 capability tiles: n8n, Supabase, OpenAI/Claude, Telegram, WhatsApp/SMS, CRM & Email; 3-stat grid: 25 systems, 7 categories, 48h delivery; "same infrastructure we run on" positioning). Pipeline detail pages show concrete before/after operational examples for 10 priority pipelines via `src/lib/before-after.ts`. All Phase 2F code tasks complete. Changes local (uncommitted). Build passes lint + TypeScript clean.

**Current MVP direction update (June 30, 2026)**: User changed direction. Account system, chat, and deal room are not needed for the current MVP. They are required future platform features, but not now. Current MVP should return to: public audit, public system request/order form, internal order workspace, Telegram/internal notifications, manual follow-up, and first-client sales validation.

**Следующий шаг**: if preview is accepted, promote `dpl_92thMKzyip2qEvXBSi1MtV37EiKu` to production; then manually verify/enrich the 20-account seed list and start outreach.

**Historical Phase 3 planning update (future-only after June 30 reversal)**: Client portal should become "Client Accounts + Deal Room", not just a passive dashboard. Future authenticated clients should be able to submit automation requests/offers inside the site, discuss scope with FlowOps in a request thread, receive status updates, and later see active systems/billing/support. Email/Telegram should become notifications, while the canonical conversation lives in FlowOps.

**Superseded Phase 3 execution update**: User explicitly reprioritized work on June 29, 2026: move to Phase 3 Client Accounts + Deal Room now. This was superseded on June 30, 2026 by the MVP scope reversal: account/chat/deal-room is future-only, not current MVP.

**Phase 3 Batch 1 update**: Database/auth foundation implemented and applied to Supabase remote via migration `202606290001_phase3_client_accounts_deal_room.sql`. New tables: `clients`, `client_pipeline_instances`, `automation_requests`, `request_messages`, `request_status_history`. RLS policies restrict client reads/inserts by `auth.uid()` and hide internal messages from clients. Added `src/lib/portal.ts` minimal auth/client helper and documented `NEXT_PUBLIC_SUPABASE_ANON_KEY`.

**Phase 3 Batch 2 update**: Portal Request MVP implemented: `/portal`, `/portal/dashboard`, `/portal/new-request`, `/portal/requests`, `/portal/requests/[id]`, API routes under `/api/portal/*`, and Portal nav entry. Browser UI now supports Supabase email/password sign-in, email/password account creation, Google OAuth button, client profile setup, request creation, request list, deal-room detail, visible request messages, and status timeline shell. Manual smoke verified portal routes return 200 and `/api/portal/me` returns 401 without bearer token. Full authenticated flow still requires Supabase Auth provider configuration.

**Phase 3 Batch 3 update**: Internal Requests Workspace implemented: `/internal/requests`, `/internal/requests/[id]`, `/api/internal/requests`, `/api/internal/requests/[id]`, `/api/internal/requests/[id]/status`, `/api/internal/requests/[id]/messages`. Middleware now protects `/api/internal/*` as well as `/internal/*`. FlowOps can view portal requests, inspect client context, update status/assignment, send client-visible replies, and add internal-only notes. Manual smoke verified `/internal/requests` and `/api/internal/requests` return 401 without internal access.

**Phase 3 Batch 5 update**: Request-to-order conversion implemented. `/api/internal/requests/[id]/convert` creates a `pipeline_orders` record, writes `order_status_history`, links `automation_requests.pipeline_order_id`, moves the request to `deploying`, writes request status history, and adds a client-visible system message. Internal request detail shows a convert form and links to the existing order if conversion already happened. Manual smoke verified convert API returns 401 without internal access.

**Phase 3 Batch 6 update**: Client Dashboard/Support/Billing stub implemented. Added `/portal/billing`, `/portal/support`, `/portal/pipelines/[id]`, `/api/portal/pipelines/[id]`, dashboard active-system links, billing manual-state overview, support entry point, and client pipeline detail shell. Manual smoke verified new portal routes return 200 and pipeline detail API returns 401 without bearer token. Real authenticated data still requires Supabase anon key/Auth config.

**Phase 3 Batch 7 update**: Notifications/production readiness implemented. Added portal request notifications via existing Telegram/webhook env path for new requests, client messages, FlowOps replies, and status updates. Added Resend email notifications for client-visible FlowOps replies/status updates when `RESEND_API_KEY` is configured. Updated production readiness with Phase 3 routes, bearer/internal protection checks, and authenticated acceptance checklist. Manual smoke verified `/api/portal/me` and `/api/portal/pipelines/test` return 401 without bearer, `/api/internal/requests` returns 401 without key, and `/portal/support` returns 200.

**Auth UX update**: User rejected magic-link-first auth on June 29, 2026. Portal auth UI now uses standard email/password sign-in, email/password account creation, and Google OAuth button via Supabase Auth. Magic link is no longer the primary portal login UX. Full acceptance still requires `NEXT_PUBLIC_SUPABASE_ANON_KEY`, Supabase email/password provider, Google provider, and redirect URLs.

**Auth incident update** (June 29, 2026): User reported portal auth broken: Google button does not work and signup confirmation email does not arrive. Verified local/Vercel env now contain `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, and `INTERNAL_ACCESS_KEY` for Preview/Production. Fresh production deploy `dpl_gSx1wh2sv5JWRRAVKgZkuHt6d6Vm` was aliased to `https://flowops.agency`; `/portal` returns 200. Supabase public Auth settings show `external.google=false`, `external.email=true`, `disable_signup=false`, and `mailer_autoconfirm=false`. Root cause is Supabase Auth configuration, not current portal React/build code: Google provider must be enabled with Google OAuth credentials, and email confirmation either needs reliable SMTP/redirect setup or should be disabled for MVP.

**Portal loading fix** (June 29, 2026): After Google started working, user hit an infinite `Loading portal...` state on `/portal/dashboard#`. Vercel logs showed repeated `GET /api/portal/me 200` calls, indicating a client auth effect loop rather than a backend failure. Fixed `src/components/PortalClient.tsx` by making `loadMe` stable, removing the `session` dependency from the auth bootstrap effect, adding a 12s abort timeout/error path for `/api/portal/me`, and wiring immediate email/password sessions directly into portal loading. Validated with `npm run lint` and `npm run build`. Deployed production `dpl_CUcueGPhYPLRTZ3NTeRqn5DoXFnc`, aliased to `https://flowops.agency`.

**Superseded system detail deal-room ordering update** (June 29, 2026): User requested every system card/detail page allow ordering automation directly from the system page and remove the old email/order-style `Request deployment` flow. Updated `src/components/OrderRequestForm.tsx` so the sidebar on every `/os/[slug]` page created a portal automation request through `/api/portal/requests`. This was superseded by the June 30 MVP scope reversal; current preview restores `/api/pipeline-order` for public system ordering.

**Deal Room Quality Upgrade Batch 2** (June 30, 2026): `src/components/PortalClient.tsx` upgraded with next-action callout banner in deal room header (color-coded by party: amber=client action, blue=FlowOps, green=done), scope context side panel (type, pipeline name, urgency, budget, tools, assignee, timestamps), proposal placeholder card for `proposal_sent` status, chat composer bug fix (body cleared only on success, textarea disabled while sending, send button disabled when empty), empty state for conversation, company context card in main column, improved system message rendering. Build clean (65 pages).

**Internal Inbox Filters** (June 30, 2026): `/internal/requests` page upgraded with 7 filter tabs (All / New / In scope / Awaiting client / Deploying / Active / Closed), count badges per tab, amber alert when client response is needed, waiting-party badge per row (Client / FlowOps / Done), client company + assignee in request row, amber row highlight for `proposal_sent`. `src/lib/portal.ts` updated: new `InternalAutomationRequest` type (extends AutomationRequest + clientCompany/clientEmail), `getInternalAutomationRequests` now batch-fetches client companies. Build clean (65 pages).

**Account/Chat/Deal Room quality spec update** (June 29, 2026): User asked to think through every detail of a high-quality account page/system, 100% quality chat, and maximally useful deal room. Created `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md` and synced it into roadmap/next steps. The spec defines the long-term Phase 3 quality target: account/profile/security/notifications, action-oriented dashboard, structured request intake, deal room with scope/status/next action/proposal/decision/delivery state, structured chat with client/FlowOps/system/internal message types, internal inbox filters, active systems, support, billing, RLS/security, and acceptance gates. This is a quality target for upgrading the already implemented MVP, not a separate new project.

**Chat Reliability + Internal Safety UX** (June 30, 2026): `InternalRequestActions.tsx` upgraded: `InternalRequestMessageForm` now uses controlled textarea (draft preserved on failure), adds `clientCompany` prop, shows "Sending to: [Company]" banner when `isInternal=false`, adds confirm step before client-visible reply (amber warning + Confirm/Cancel buttons), success pill state before reload, retry button on error, Ctrl+Enter shortcut, disabled when body is empty. `internal/requests/[id]/page.tsx` now passes `clientCompany={client?.company}` to reply form and renders message bodies with `whitespace-pre-wrap break-words`. `PortalClient.tsx` upgraded: client chat composer now has Ctrl+Enter/Cmd+Enter shortcut, retry button inline on error, "Ctrl+Enter to send" hint, and message bodies render with `whitespace-pre-wrap break-words`. Build clean (65 pages).

**MVP scope reversal** (June 30, 2026): User decided account/chat/deal-room should not be part of the current MVP. They are not abandoned; they are mandatory future platform capabilities. For now, the MVP must remove the portal/deal-room requirement from public buyer flows and return to the earlier simple order model: unauthenticated system request form → `pipeline_orders` → internal workspace → manual FlowOps follow-up. Existing portal/deal-room code, schema, docs, and quality spec should be preserved as future infrastructure unless explicitly deleted later.

**MVP portal gate implementation** (June 30, 2026): Public buyer-facing MVP flow restored. `src/components/OrderRequestForm.tsx` now submits unauthenticated pipeline requests to `/api/pipeline-order` again. Portal/deal-room copy was removed from public homepage/marketplace/system/stack CTAs and Portal removed from `SiteHeader`. `src/middleware.ts` now gates future portal routes: `/portal/*` redirects to `/#audit` and `/api/portal/*` returns 404 unless `ENABLE_CLIENT_PORTAL=true`. `.env.template` and `docs/production-readiness.md` document that `ENABLE_CLIENT_PORTAL` stays false/empty for MVP.

**Automation card audit requirement** (June 30, 2026): Before scaled outreach, every marketplace automation card must be audited and upgraded. User specifically flagged that current card descriptions are too sparse, prices may be too high for productized ready automations, and every card needs an in-card illustration consistent with FlowOps SVG workflow visuals. New source of truth: [[automation-card-audit-brief]]. Agents must review every live and coming-soon card for real buyer need, richer copy, pricing around roughly 30% below comparable custom-market builds where safe, and a unified illustration concept before outreach.

---

## Key Metrics (June 25, 2026)
- Активных клиентов: 0
- Pipeline-систем: 25 (code + Supabase)
- MRR: $0
- Audit requests: 0 (форма только запущена)

## Trust Layer Requirements (June 29, 2026)
- Homepage must explain why FlowOps is safe for business owners: audit-first, workflow map, owner approval, test run/manual QA, monitoring/support.
- Use implementation examples and mini-cases before real client results exist; avoid fake-looking testimonial claims.
- Add proof surfaces: audit/internal workspace previews, pipeline/order dashboard surfaces, workflow diagrams, Telegram/status notifications.
- Add owner-facing before/after examples to priority pipeline pages.
- Add audit next-step clarity near CTA so prospects know what happens after submitting.
- Add founder/operator credibility through built systems and delivery discipline, without overclaiming.

## Automation Card Quality Requirements (June 30, 2026)
- Treat marketplace card quality as a sales-readiness blocker before scaled outreach.
- Audit all 25 live systems and 7 coming-soon systems.
- Each card must explain target buyer, pain, trigger, workflow steps, result, integrations, setup scope, monthly support, deployment time, and realistic outcome.
- Current short descriptions must be expanded; avoid generic "save time" phrasing without concrete workflow symptoms.
- Recheck setup/monthly pricing against current market references before changing prices.
- Pricing direction: FlowOps can often price productized ready automations about 30% below comparable custom-market builds, but not at the cost of delivery margin or premium positioning.
- Do not say "cheap"; frame as "productized deployment pricing" because the workflow is pre-mapped and faster to deploy.
- Every card should include a small, consistent illustration in the style of the existing FlowOps SVG workflow maps: pale blue/white canvas, soft shadows, rounded nodes, dotted connectors, small status chips, sky/mint/peach/amber accents.
- Reference assets: `/Users/tamerlan/Downloads/flowops-custom-workflow.svg`, `/Users/tamerlan/Downloads/flowops-request-to-proof-v2_1.svg`, `/Users/tamerlan/Downloads/flowops-request-to-proof.svg`.

## Future Account / Chat / Deal Room Quality Requirements (Deferred June 30, 2026)
- Not part of current MVP.
- Do not expose account/chat/deal-room as the main order flow until explicitly reprioritized.
- Preserve the quality spec and built infrastructure for future SaaS maturity.
- Account system should include email/password + Google auth, profile/company context, notification preferences, security controls, and clear error/session states.
- Dashboard should answer: what is active, what needs client action, what FlowOps updated, what is being scoped/deployed, and where to start a new request.
- Request intake should capture desired outcome, current process, tools, trigger, manual steps, recipient/output, urgency, and success criteria without feeling bureaucratic.
- Deal room should combine conversation, status, next action, scope summary, timeline, proposal/approval state later, decisions, delivery state, and related order/system links.
- Chat should be structured around requests and support client messages, FlowOps replies, system events, proposal/approval events, status updates, and internal-only notes.
- Internal workspace should support filters for status/owner/waiting state/last activity/unread, assignment, private notes, client-visible replies, conversion to order, and related order/system links.
- Active systems should show human-readable health/status/last check/support/change-request context without exposing n8n.
- Billing/support should be honest about current manual state until Stripe/Resend and subscription data are fully verified.
- Security requirements: client-owned RLS, bearer-token portal APIs, `INTERNAL_ACCESS_KEY` internal APIs, no internal notes exposed, no service-role key in client bundles, validation/rate limits on message/request creation.
