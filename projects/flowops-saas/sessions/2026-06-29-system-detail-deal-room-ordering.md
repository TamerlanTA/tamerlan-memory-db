# Session 2026-06-29 — System Detail Deal-Room Ordering

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Replaced the old public `Request deployment` form on system detail pages with portal deal-room ordering.
- Updated `src/components/OrderRequestForm.tsx` to:
  - detect Supabase browser session;
  - offer inline Google sign-in and email sign-in when unauthenticated;
  - require a finished portal client profile before request creation;
  - submit to `/api/portal/requests` with `requestType=pipeline`, `pipelineSlug`, title, process context, current tools, desired outcome, urgency, and budget range;
  - redirect to `/portal/requests/[id]` after request creation.
- Updated copy in `/os/[slug]`, `/os`, homepage, and stack pages from old deployment/order language to deal-room language.
- Deployed production `dpl_gPe18xJ4GBJhmVM9NH6xX9JSqj8Y`, aliased to `https://flowops.agency`.

## Key findings
- The old `/api/pipeline-order` route still exists for legacy/internal/payment scaffolding, but it is no longer used by public system detail page UI.
- Production HTML for `/os/leados-lead-research` now shows `Order this automation`, `Sign in to create the deal room`, and `Create deal room`; old `Request deployment`/Phase 1 public order copy is gone from that page.

## Blockers
- Need live authenticated browser acceptance after profile setup: system detail → sign in → create deal-room request → redirected request detail.

## Next steps
- Test as a logged-in client with a completed `clients` profile.
- If the old `/api/pipeline-order` route is no longer needed at all, plan a separate cleanup because Stripe/internal order code still references `pipeline_orders`.
