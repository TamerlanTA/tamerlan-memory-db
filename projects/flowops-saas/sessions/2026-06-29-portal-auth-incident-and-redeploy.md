# Session 2026-06-29 — Portal Auth Incident And Redeploy

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Investigated user report that portal authorization does not work, Google button does not work, and signup email does not arrive.
- Verified `.env.local` has `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, and `SUPABASE_SERVICE_ROLE_KEY`.
- Verified Vercel Preview/Production env has `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `INTERNAL_ACCESS_KEY`, and `EMAIL_FROM`; `RESEND_API_KEY` is still missing.
- Ran `npm run lint` and `npm run build`; both passed.
- Deployed fresh production build: `dpl_gSx1wh2sv5JWRRAVKgZkuHt6d6Vm`, URL `https://flowops-saas-cncb1twv2-tamertt931-8560s-projects.vercel.app`, aliased to `https://flowops.agency`.

## Key findings
- `/portal` returns 200 on production after redeploy.
- Supabase public Auth settings show `external.email=true`, `disable_signup=false`, `external.google=false`, and `mailer_autoconfirm=false`.
- Root cause is Supabase Auth configuration, not the current portal React/build code.
- Google login cannot work until the Google provider is enabled in Supabase with OAuth credentials.
- Email/password signup currently expects confirmation email; if Supabase confirmation delivery is not configured/reliable, the user is stuck after signup.

## Blockers
- Google OAuth needs Google Cloud OAuth Client ID/Secret and Supabase provider enablement.
- Email signup needs either disabled email confirmations for MVP or reliable SMTP/custom Auth email delivery.
- Authenticated Phase 3 acceptance is blocked until those provider settings are changed.

## Next steps
- In Supabase Auth, choose MVP path: disable email confirmations so signup logs in immediately, or configure confirmation email SMTP/templates/redirects.
- Enable Google provider and add `https://fmpvyuowglvyrrqecmrn.supabase.co/auth/v1/callback` in Google Cloud OAuth.
- Add allowed redirect URLs for `https://flowops.agency/portal/dashboard`, `https://flowops-saas.vercel.app/portal/dashboard`, current preview URL `/portal/dashboard`, and `http://localhost:3000/portal/dashboard`.
- Run full authenticated portal acceptance after provider setup.
