# Session 2026-05-21 — Mobile-First PWA Refactor

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done

Full mobile-first PWA transformation. This was NOT a rewrite — all existing business logic, pricing engine, Supabase lead submission, mock fallback, and TypeScript safety were preserved. The architecture was refactored incrementally.

### New files created
- `public/manifest.json` — PWA manifest (name: ImportCar.kz, short_name: imcar, theme_color: #16c784, display: standalone)
- `src/hooks/useFavorites.ts` — localStorage-backed favorites hook (toggle, isFavorite, persists across sessions, STORAGE_KEY: `importcar_favorites`)
- `src/components/BottomNav.tsx` — fixed mobile-only 4-tab nav with inline SVG icons; emerald active state, badge count on Избранное
- `src/components/CalculatorScreen.tsx` — standalone calculator screen; builds synthetic Car from user inputs (price/currency/year/engineVol/engineType) and calls existing `calculateCost()`; shows live breakdown; preserves pricingRuleVersion + warnings
- `src/components/FavoritesScreen.tsx` — shows favorited Car cards; empty state "Вы пока не сохранили авто"
- `src/components/ProfileScreen.tsx` — Мои заявки (empty state), WhatsApp CTA, 4 trust notes (заявки не публикуются / расчёт предварительный / менеджер уточнит / импортёры проверены)

### Files updated
- `index.html` — lang=ru, viewport-fit=cover, manifest link, apple-mobile-web-app meta tags, PWA theme-color
- `src/App.tsx` — app shell with appShell/appContent containers; 4-tab state (activeTab + detailSource for back navigation); favorites wired through all screens; admin view preserved behind VITE_ENABLE_ADMIN_VIEW
- `src/components/CarCard.tsx` — favoriteBtn overlay on image (stopPropagation), isFavorite + onToggleFavorite props added
- `src/components/CarDetail.tsx` — detailTopBar with back + favorite button; detailPriceSummary card (mobile price + CTA); preserved all existing content; removed hero "премиальный импорт из Кореи" eyebrow
- `src/components/StickyCta.tsx` — added WhatsApp button (stickyWaBtn) alongside "Запросить расчёт"; WA_NUMBER constant at top for easy update
- `src/App.css` — ~500 lines added: appShell, appContent, bottomNav, bottomNavItem, favoriteBtn, detailTopBar, detailPriceSummary, calcForm/calcResult, favEmptyState, profileSection, profileTrustList, mobile overrides

### Verified working
- ✅ Bottom nav tabs switch correctly (Каталог / Калькулятор / Избранное / Профиль)
- ✅ Calculator live-computes as inputs change; uses real calculateCost engine
- ✅ Favorites: heart on card → persists to localStorage → appears in Избранное tab with count badge
- ✅ Car detail: price summary card, favorite toggle, sticky CTA with WhatsApp
- ✅ Back from detail returns to originating tab (catalog or favorites)
- ✅ Desktop: bottom nav hidden, 3-column card grid, 2-column detail layout preserved
- ✅ `npm run lint` — 0 errors
- ✅ `npm run build` — 0 errors, clean production output

## Key findings
- The preview_click tool has unreliable behavior with `position: fixed` elements; used JS eval to verify tab switching works correctly via React handlers
- Previous memory mentioned gold (#C9A84C) accent from "premium design overhaul" but the actual code at time of this session had green (#16c784) — the current session preserved and extended the green system
- WhatsApp number in ProfileScreen.tsx and StickyCta.tsx is a placeholder (77071234567) — must be updated before launch

## Blockers
- None for current MVP scope

## Next steps
- Add desktop top-nav with the 4 tabs (Каталог/Калькулятор/Избранное/Профиль) — desktop users currently can't access Calculator/Favorites/Profile screens
- Replace placeholder WhatsApp number (77071234567) with real business contact
- Deploy to Vercel after confirming new PWA manifest and tabs work on real device
- Add PWA install prompt / service worker for offline support (optional)
- Add real app icons (currently uses favicon.svg placeholder in manifest)
