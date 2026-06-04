# Session 2026-05-27 — Vercel Preview Deploy

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Ran local `npm run build` successfully.
- Deployed ImportCar.kz MVP to Vercel as a preview deployment using `npx vercel deploy . -y`.
- Global `vercel` CLI was not installed, but `npx` installed/ran Vercel CLI for the deploy.

## Key findings
- Deployment completed with `readyState: READY`.
- Preview URL: `https://importcar-kz-92phlsa2k-tamertt931-8560s-projects.vercel.app`.
- Inspect URL: `https://vercel.com/tamertt931-8560s-projects/importcar-kz-mvp/7W5Nkr2DGNqZNEk6dsJtkNUaY9E5`.
- Deployment id: `dpl_7W5Nkr2DGNqZNEk6dsJtkNUaY9E5`.

## Blockers
- This was a preview deploy, not production. Production promotion still requires an explicit `vercel deploy --prod`.
- Live Supabase Edge Function acceptance remains pending.

## Next steps
- Manually review the preview URL.
- If preview is accepted, run production deploy/promotion.
- Continue with Supabase Edge Function live acceptance before AI-4.
