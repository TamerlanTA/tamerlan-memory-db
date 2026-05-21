# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Status as of 2026-05-21 — Mobile-First PWA Refactor Complete

### Architecture
- **App shell**: `div.appShell` → `div.appContent` container; bottom nav fixed at bottom on mobile
- **Routing**: state-based (no React Router); `activeTab` + `detailSource` for back-navigation
- **4 tabs**: Каталог / Калькулятор / Избранное / Профиль
- **Bottom nav**: mobile-only (`display: none` at ≥ 720px); active tab shown with emerald accent; badge count on Избранное

### Features complete
- **Catalog screen**: full existing listing + filter logic; car cards have favorite heart button
- **Calculator screen**: standalone form → live `calculateCost()` breakdown; preserves pricingRuleVersion + warnings
- **Favorites screen**: localStorage persistence (key: `importcar_favorites`); empty state; count badge on nav
- **Profile screen**: заявки placeholder + WhatsApp CTA + 4 trust notes
- **Car detail**: price summary card (mobile), favorite button, sticky CTA with WhatsApp + "Запросить расчёт"
- **PWA**: manifest.json, viewport-fit=cover, apple-mobile-web-app meta tags, theme-color #16c784
- **Lead form**: preserved; Supabase integration + mock fallback mode both work
- **Admin view**: preserved behind `VITE_ENABLE_ADMIN_VIEW` env var

### Design system (current code)
- Font: 'Avenir Next', 'Segoe UI', Arial (system sans-serif)
- Accent: emerald #16c784 (--showroom-accent)
- Background: #f4f5f7 light / #090b0e dark hero
- Cards: white, subtle borders, 30px border-radius
- Note: previous session memory mentions gold (#C9A84C) overhaul but actual code has green — green system is what's deployed

### Data
- 15 real Encar listings with local images at `public/cars/encar-*.jpg`
- 5 mock importers
- Versioned pricing rules engine

### Build status
- `npm run lint` — ✅ 0 errors
- `npm run build` — ✅ clean, 451 kB JS bundle
- TypeScript — 0 errors

### Placeholders that need updating before launch
- WhatsApp number in `StickyCta.tsx` and `ProfileScreen.tsx`: `77071234567` — replace with real number
- App icons: only `favicon.svg` referenced in manifest — real PNG icons needed
