# ImportCar.kz MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Immediate (post-PWA refactor)

1. **Replace WhatsApp placeholder number** — update `77071234567` in `StickyCta.tsx` and `ProfileScreen.tsx` with real business contact before any real user sees the app
2. **Desktop top-nav for tabs** — desktop users currently can't reach Calculator/Favorites/Profile; add a top nav bar or tab links for viewports ≥ 720px
3. **Deploy to Vercel** — push and verify PWA manifest, bottom nav, and all 4 tabs work on a real iPhone device

## Medium priority

4. **Real app icons** — generate PNG icons (192×192, 512×512) for the PWA manifest; currently only `favicon.svg` is referenced
5. **Add service worker** — for offline support and real PWA installability (Vite PWA plugin is the simplest path)
6. **Confirm image licensing** — verify Encar.com photo provenance before any real launch
7. **Add authenticated admin access** — before enabling operational lead management

## Backlog

8. **Configure real Supabase project** — apply `schema.sql` + `seed.sql` if moving beyond demo mode
9. **Validate pricing rules** — against real Kazakhstan import law and broker quotes
10. **Saved requests in Profile** — currently placeholder; wire to Supabase or localStorage lead history
