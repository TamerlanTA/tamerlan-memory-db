# Session 2026-06-21 — Phase 1 Live Activation

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Created `.env.local` from the fully populated `.env.example`; file remains gitignored.
- Linked local Supabase CLI workspace to FlowOps remote project `fmpvyuowglvyrrqecmrn`.
- Applied remote migration `202606200001_flowops_phase1_marketplace.sql` with `supabase db push`.
- Verified remote migration list shows local and remote `202606200001`.
- Verified remote table counts after migration:
  - `pipeline_categories`: 7
  - `pipelines`: 15
  - `pipeline_orders`: initially 0
  - `order_status_history`: initially 0
- Restarted local Next dev server with `.env.local`.
- Submitted live test order through public pipeline page; verified row in `pipeline_orders` and initial `order_status_history`.
- Direct Telegram bot test succeeded.
- Submitted second live order; verified app notification returned `sent: true`.
- Opened `/internal/orders`; verified it shows `Supabase live`.
- Opened real `/internal/orders/[id]`; updated status from `new` to `qualified`; verified status and history rows in DB.
- Removed QA orders from production DB after verification; `pipeline_orders` and `order_status_history` returned to 0.

## Key findings
- Supabase MCP connector token was expired, but Supabase CLI was authenticated and usable.
- `PIPELINE_ORDER_WEBHOOK_URL` is empty; notification is currently verified through direct Telegram env.
- One first notification attempt returned transient `fetch failed`; direct Telegram API and second full app submit succeeded.

## Verification
- `npm run lint` passes.
- `npm run build` passes with `.env.local`.
- `supabase migration list` confirms migration parity.
- Live DB order insert, status history, internal workspace read, status update, and Telegram notification were all verified.

## Blockers
- None for Phase 1.

## Next steps
- Move to Phase 2 planning: Stripe setup fee, subscriptions, confirmation email, and deployment flow.
- Optional: configure `PIPELINE_ORDER_WEBHOOK_URL` if n8n should own notifications instead of direct Telegram.
