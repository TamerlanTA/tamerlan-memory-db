# Session 2026-05-29 — Vercel Preview Deploy

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

## What was done
- Ran local `npm run build` successfully.
- Deployed ImportCar.kz MVP to Vercel preview with `npx vercel deploy . -y`.
- Deployment completed with `readyState: READY`.

## Key findings
- Global `vercel` CLI was not installed, so deploy used `npx vercel`.
- Vercel installed CLI package on demand and deployed successfully.
- Preview URL: `https://importcar-kz-lvrvupbns-tamertt931-8560s-projects.vercel.app`.
- Inspect URL: `https://vercel.com/tamertt931-8560s-projects/importcar-kz-mvp/9iMLct51fZZX6umGDgH2FBosBSYh`.
- Deployment id: `dpl_9iMLct51fZZX6umGDgH2FBosBSYh`.

## Blockers
- This is a Vercel frontend preview deploy only. Supabase migration/Edge Function deployment for calibration still must be handled separately if not already done.

## Next steps
- Run preview acceptance checklist on real device.
- Deploy/apply Supabase backend changes needed for AI-5C.2/AI-6/AI-6.5 if not yet live.
