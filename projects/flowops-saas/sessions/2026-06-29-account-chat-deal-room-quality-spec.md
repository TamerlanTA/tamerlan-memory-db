# Session 2026-06-29 — Account Chat Deal Room Quality Spec

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Used the project-orchestrator workflow to frame a product-quality spec for FlowOps client accounts, chat, and deal rooms.
- Read current FlowOps SaaS memory and the Phase 3 source-of-truth plan.
- Confirmed Phase 3 MVP already exists as client accounts + request deal room + internal request workspace + conversion-to-order foundation.
- Created repo spec: `/Users/tamerlan/Desktop/FlowOps/FlowOps Saas/docs/phase-3-account-chat-deal-room-quality-spec.md`.

## Key findings
- The next product bar is not merely "more portal pages"; it is a canonical workspace where the client always sees status, next action, scope, proposal, conversation, delivery state, support, and billing context.
- Chat should not become a generic messenger; it should be structured around requests, proposals, decisions, status changes, delivery, support, and internal-only notes.
- Deal rooms should eventually include scope, next action, proposal/approval, decision log, delivery timeline, and conversion/order/system links.

## Blockers
- Supabase Auth email/password confirmation behavior and redirect setup still need full acceptance.
- Stripe/Resend live verification remains pending before billing/email features can be treated as production-complete.
- File uploads, multi-user workspaces, realtime logs, and AI-generated proposals remain intentionally out of scope until real client usage proves need.

## Next steps
- Use the new quality spec as the checklist for the next Phase 3 upgrade batch.
- Recommended first implementation batch: improve dashboard information architecture, deal-room layout, next-action visibility, chat composer states, request filters, and internal unread/waiting cues.
- Continue to preserve manual-delivery positioning and keep n8n hidden from clients.
