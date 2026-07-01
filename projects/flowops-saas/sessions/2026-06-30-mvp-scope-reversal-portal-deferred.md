# Session 2026-06-30 — MVP Scope Reversal Portal Deferred

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

## What was done
- User reversed MVP scope: account system, client chat, and deal room are not needed for the current MVP.
- Restored buyer-facing order flow in code:
  - `src/components/OrderRequestForm.tsx` now submits unauthenticated requests to `/api/pipeline-order`.
  - Removed portal/deal-room requirement from public system request form.
  - Removed Portal from `src/components/SiteHeader.tsx`.
  - Updated public homepage, marketplace, system detail, and stack CTA copy away from deal-room language.
- Added MVP portal gate:
  - `src/middleware.ts` redirects `/portal/*` to `/#audit` unless `ENABLE_CLIENT_PORTAL=true`.
  - `src/middleware.ts` returns 404 for `/api/portal/*` unless `ENABLE_CLIENT_PORTAL=true`.
  - `.env.template` documents `ENABLE_CLIENT_PORTAL=false` for MVP.
- Updated repo docs:
  - `docs/production-readiness.md`
  - `docs/phase-3-client-accounts-deal-room-plan.md`
- Updated project memory:
  - [[current-state]]
  - [[next-steps]]
  - [[decisions]]
  - [[risks]]
  - [[roadmap]]
  - [[technical-architecture]]

## Key findings
- Account/chat/deal-room is still strategically important and should not be deleted.
- For current MVP, it is over-scoped and should not block outreach or first-client validation.
- Future portal quality spec remains valid: `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md`.

## Validation
- `npm run lint` passed.
- `npm run build` passed.
- Vercel preview deploy passed and is READY:
  - URL: `https://flowops-saas-pvoewrzoy-tamertt931-8560s-projects.vercel.app`
  - Deployment ID: `dpl_92thMKzyip2qEvXBSi1MtV37EiKu`
  - Inspector: `https://vercel.com/tamertt931-8560s-projects/flowops-saas/92thMKzyip2qEvXBSi1MtV37EiKu`
- Public buyer-facing scan found no portal/deal-room mentions in homepage, `/os`, `/os/[slug]`, `/stacks/[slug]`, `SiteHeader`, `SiteFooter`, or `OrderRequestForm`.
- Local runtime smoke on `npm run dev -- --port 3010`:
  - `HEAD /portal` returned `307` redirect to `/#audit`.
  - `GET /api/portal/me` returned `404` with `{"error":"Client portal is deferred for the MVP."}`.
  - `HEAD /os` returned `200`.

## Blockers
- Current production still needs a deploy for this reversal to go live.
- Existing portal/deal-room code remains in repo intentionally, but is gated for MVP.

## Next steps
- Commit and deploy the MVP scope reversal.
- Manually verify `/portal` redirects to `/#audit` and `/api/portal/me` returns 404 when `ENABLE_CLIENT_PORTAL` is false.
- Start first outreach batch after verifying the public order form in production.
