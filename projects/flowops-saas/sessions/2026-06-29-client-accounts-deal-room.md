# Session 2026-06-29 — Client Accounts Deal Room

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[roadmap]]

## What was done
- Checked existing FlowOps SaaS plans for accounts/chat.
- Confirmed accounts existed only as Phase 3 client portal: login, active pipelines, billing, support requests.
- Added decision D-014: client accounts should become a deal room, not only a dashboard.
- Updated [[roadmap]] to rename Phase 3 as "Client Accounts + Deal Room" and add in-site automation request, request list, request detail, conversation threads, internal request inbox, and notifications.
- Updated [[technical-architecture]] with proposed Phase 3 tables and routes: `automation_requests`, `request_messages`, `request_status_history`, `/portal/requests`, `/internal/requests`.
- Updated [[next-steps]] so Phase 3 planning includes account timing, deal-room UX, internal reply workflow, RLS, and notification policy.
- Updated [[current-state]] with Phase 3 planning note.

## Key findings
- Existing plan had account/login/dashboard later, but did not capture the user's stronger idea: clients should order and discuss automation inside the site instead of defaulting to email.
- The new direction makes FlowOps feel more like a platform and preserves client context better.
- This should not imply self-serve deployment; delivery remains manual until validated.

## Blockers
- Phase 3 should not be built before trust layer/outreach/first-client validation unless the user explicitly reprioritizes.
- Attachments/files need a separate storage/security/RLS design before implementation.

## Next steps
- Complete Phase 2F trust layer first.
- When Phase 3 planning starts, decide whether accounts are created before an order, after audit submission, or after first qualified request.
- Design `portal/new-request`, `portal/requests/[id]`, `internal/requests/[id]`, message threads, status timeline, and request-to-order conversion.
