# Session 2026-07-03 — Stack Bundle Discount logic

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done

This was an automated scheduled-task run (`flowops-implementation-loop`). Memory review confirmed (consistent with the prior same-day session `2026-07-03-pricing-polish-commit-hydration-fix`) that all Phase 2A code tasks are complete and every other unchecked `next-steps.md` item is either blocked on a dedicated user pricing-review session, a business/outreach task, or a deploy action — not something to implement autonomously. The task file's "critical gap" (audit form missing) is confirmed stale; audit form/table/route have existed since June 23.

Picked the one genuine, unblocked code gap left in the roadmap: **Stack Bundle Discount logic** (roadmap.md Phase 2 Block E, marked "не реализовано, только статические страницы"). D-008 had already decided the pricing tiers (2nd pipeline = 10% off setup, 3rd+ = 15%) but no code applied them — only static "Save X%" copy existed on `/stacks`.

### Implemented
1. `supabase/migrations/20260703091233_bundle_discount.sql` — adds `original_setup_price`, `discount_percent`, `discount_reason` to `pipeline_orders`; backfills existing rows. Applied directly to remote Supabase (`fmpvyuowglvyrrqecmrn`) via MCP `apply_migration` (confirmed via `list_migrations`/`list_tables`).
2. `src/lib/loyalty.ts` (new) — `bundleDiscountForPriorCount`, `getBundleDiscountForClient` (queries prior distinct pipeline slugs by client email, excludes cancelled + the pipeline being ordered), `applyDiscount`.
3. `src/app/api/pipeline-order/route.ts` — computes the discount at order time, applies it to `agreed_setup_price`, stores `original_setup_price`/`discount_percent`/`discount_reason`, passes discount into notification/email/status-history note.
4. `src/lib/orders.ts` — extended `PipelineOrder` type + row mapping + preview fixtures with the new fields.
5. `src/lib/notifications.ts`, `src/lib/email.ts` — Telegram message and confirmation email now mention the loyalty discount when applied.
6. `src/components/OrderRequestForm.tsx` — success state shows the applied discount; added a small loyalty-policy line above the submit button.
7. `src/app/internal/orders/[id]/page.tsx` — shows a discount banner + "was $X" in the Setup metric when a discount was applied.

### Validation
- `npm run lint` — clean.
- `npm run build` — 68 pages, TypeScript clean.
- End-to-end verification against the real Supabase project (not preview fallback): submitted 3 QA orders for the same test email (`flowops-qa-bundle-test@example.com`) across 3 different pipelines via the running dev server. Confirmed 0% → 10% → 15% tiers applied correctly (e.g. $599 → $539, $649 → $552), confirmed the discount banner renders correctly on `/internal/orders/[id]` (curled the page with the internal access key cookie). Deleted all 3 QA rows from Supabase afterward (`order_status_history` cascades).
- Checked `get_advisors` (security) on the Supabase project after the migration — no new findings introduced; existing findings (`pipeline_orders` RLS-enabled-no-policy, etc.) are pre-existing and expected since the app writes via the service-role admin client, consistent with the existing architecture.

### Committed
- `30e8d26` — "Stack Bundle Discount: automatic 10%/15% loyalty pricing on repeat pipeline orders". **Not deployed to Vercel** — deploy is a shared/production action; left for explicit approval, consistent with how the prior same-day session handled commit `ba2e6ac`.

### Also fixed while updating memory
- `roadmap.md` had a stale line claiming "Full Ops Stack bundle page — не реализовано"; `current-state.md` already confirms it's live (confirmed June 29). Corrected.

## Key findings
- The email-based discount lookup is an approximation (doesn't require the deferred D-018 account system), but a client using a different email per order would miss the automatic match. Documented as [[decisions]] D-019 with a note to re-key off `clients.id` if/when the account system is reactivated.
- No new Supabase security advisories were introduced by the migration.

## Blockers
- None for this feature. Production deploy of `30e8d26` (and the still-undeployed `ba2e6ac` from the prior session, if not yet deployed — check `current-state.md` for the latest deploy pointer) is pending user-approved action.

## Next steps
- Deploy `30e8d26` to Vercel production once approved.
- Pricing recheck session with user (market research → recommended prices → approval → update `catalog.ts`) — still the main blocked next-steps item.
- First outreach batch (business priority, not code).
- If/when Phase 3 account system reactivates, re-key the bundle discount lookup off `clients.id` instead of raw email (see D-019).
