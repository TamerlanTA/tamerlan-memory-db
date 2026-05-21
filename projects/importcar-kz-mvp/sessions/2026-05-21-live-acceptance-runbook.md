# Session 2026-05-21 — Live Acceptance Runbook

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Prepared Phase 3B — Production Deploy & Live Acceptance Test.
- Expanded `docs/production-activation-checklist.md` with:
  - exact Supabase migration verification SQL
  - RLS policy verification SQL
  - public production env recommendations
  - staging/internal admin env recommendations
  - expected calculator lead row shape
  - stronger rollback warnings
- Created `docs/live-acceptance-runbook.md` with:
  - pre-deploy checklist
  - Supabase migration steps
  - Vercel env setup
  - deployment steps
  - live calculator test
  - saved calculation test
  - exact calculation request test
  - Supabase row verification
  - WhatsApp CTA verification
  - admin view verification
  - pass/fail criteria
  - rollback plan

## Key findings
- No hardcoded WhatsApp placeholder `77071234567` remains in source/docs/env example.
- Production env should keep `VITE_ENABLE_ADMIN_VIEW=false`.
- Admin view remains staging/internal-only until authenticated admin access exists.

## Verification
- `npm run lint` — passed.
- `npm run build` — passed, output JS bundle about 469.75 kB.

## Blockers
- Manual Supabase migration still needs to be run in production.
- Vercel production env vars still need to be set.
- Production deploy and real iPhone live acceptance still need to be executed.

## Next steps
- Run `supabase/migrations/20260521_calculator_leads_metadata.sql` in production Supabase.
- Set Vercel production env vars with `VITE_ENABLE_ADMIN_VIEW=false`.
- Deploy and follow `docs/live-acceptance-runbook.md`.
