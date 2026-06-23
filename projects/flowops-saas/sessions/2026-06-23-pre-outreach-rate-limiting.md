# Session 2026-06-23 — Pre-Outreach Rate Limiting

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Added shared `src/lib/rate-limit.ts` with hashed IP+email identifiers, Supabase-backed RPC checks, and in-memory fallback.
- Connected rate limiting to `POST /api/audit-request` and `POST /api/pipeline-order`.
- Added Supabase migrations:
  - `202606230002_rate_limit_buckets.sql`
  - `202606230003_fix_rate_limit_function_returning.sql`
- Fetched the canonical remote audit migration `20260623085205_audit_requests.sql` from Supabase history and removed the duplicate local `202606230001_audit_requests.sql`.
- Applied rate limiting SQL to linked Supabase project `fmpvyuowglvyrrqecmrn` and repaired migration history for `202606230002` and `202606230003`.
- Created Vercel preview deploy: `dpl_9WcPzfPgLUAb52HJbRKTGaxkPThe` — `https://flowops-saas-lnswlp9vu-tamertt931-8560s-projects.vercel.app`.

## Key findings
- Next.js docs warn that Route Handlers may run as lambdas and cannot rely on shared in-memory state; durable Supabase-backed limiting is the right production default.
- `supabase db push` was blocked by remote migration-history mismatch and missing `SUPABASE_DB_PASSWORD`; `supabase db query --linked` plus `migration repair --linked` worked.
- Initial RPC smoke exposed a PL/pgSQL `RETURNING` qualification bug, fixed by `202606230003`.

## Verification
- `npm run lint` passed.
- `npm run build` passed locally.
- Supabase migration list shows local and remote synced through `202606230003`.
- REST/service-role smoke for `check_rate_limit` returned `allowed: true`, `remaining: 2`, and a reset timestamp.
- Vercel preview build completed successfully.

## Blockers
- Production domain was not promoted in this work block because the deployment skill defaults to preview unless production is explicitly requested.
- Stripe/Resend live verification remains deferred.

## Next steps
- Promote the preview to production if ready to update `https://flowops-saas.vercel.app`.
- Manually verify/enrich the 20-account seed list.
- Start the first outreach batch.
