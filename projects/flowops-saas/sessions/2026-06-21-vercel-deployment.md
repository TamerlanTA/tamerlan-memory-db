# Session 2026-06-21 — Vercel Deployment

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Created/linked Vercel project `flowops-saas` in scope `tamertt931-8560s-projects`.
- Deployed the app; Vercel reports deployment `dpl_JByYWzV2Mgx7yuHQkd9EDfv9c53n` as `Ready`.
- Production alias is `https://flowops-saas.vercel.app`.
- Configured persistent Vercel env vars for Production and Preview for available non-deferred values: Supabase URL/service role, internal access key, Telegram notification vars, and email sender.
- Removed temporary `vercel.json` after project linking because the `name` property is deprecated and `.vercel/project.json` now tracks the project.
- 2026-06-22 continuation: deployed smoke passed. Verified `/`, `/os`, `/os/document-processing`, `/pricing`, `/api/pipelines` with 20 systems, protected internal/API 401 behavior, internal header/cookie access, public QA order submission, Telegram notification result, and Supabase cleanup.

## Key findings
- First Vercel attempt failed because the local directory name `FlowOps Saas` is not a valid Vercel project slug.
- Explicit project slug `flowops-saas` resolved the issue and created the Vercel project.
- Deployment was reported by Vercel as production and assigned the `flowops-saas.vercel.app` alias.

## Blockers
- Stripe and Resend live verification remain intentionally deferred by user decision.

## Next steps
- When ready, add Stripe/Resend production keys to Vercel and complete payment/email verification.
- Continue Phase 2 product work: expand catalog toward 25 systems, testimonials/case study section, and client portal planning.
