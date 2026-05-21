# ImportCar.kz MVP — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

## Content

### Architecture
- Keep Vite + React + TypeScript for MVP speed and extensibility
- Use state-based navigation (no React Router) — `activeTab` + `detailSource` for back-navigation
- Keep frontend car/importer inventory mocked while backend scope remains narrow
- Treat all catalog entries as demo/sample listings, not live offers

### Design
- Make final KZT price the primary commercial signal; show source KRW price as supporting context
- Mobile-first app shell with `appShell`/`appContent`/`bottomNav` — desktop bottom nav hidden at ≥ 720px
- Bottom nav is mobile-only; desktop may later get a top-nav tab bar
- Design accent: emerald #16c784 (green system) — this is what's in the actual code as of 2026-05-21
  - Note: a "gold overhaul" was mentioned in earlier session memory but it was reverted; current code uses green

### Pricing / calculator
- Treat the calculator as an estimate engine, not legal/tax advice
- Version pricing rules and expose calculation reasoning instead of hiding uncertainty
- Calculator screen uses a synthetic Car object from user inputs — does not require a real listing

### Favorites
- Favorites use localStorage only (no auth required)
- STORAGE_KEY: `importcar_favorites`

### Lead capture
- Allow anonymous lead insert for public testing, but do not allow anonymous lead read/update
- Supabase RLS must not be weakened; mock fallback mode used when env vars missing
- Keep admin status controls read-only until authenticated admin access exists

### PWA
- theme_color: #16c784, display: standalone, viewport-fit=cover
- WhatsApp number is a placeholder (77071234567) — must be updated before launch
- Real app icons (PNG) needed before production PWA install
