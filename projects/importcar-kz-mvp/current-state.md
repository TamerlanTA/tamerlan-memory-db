# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Status as of 2026-05-21 — Production Calculator v1 + QA Hardening Complete

### Architecture
- **App shell**: `div.appShell` → `div.appContent` container; bottom nav fixed at bottom on mobile
- **Routing**: state-based (no React Router); `activeTab` + `detailSource` for back-navigation
- **4 tabs**: Калькулятор (default) / Каталог / Избранное / Заявка
- **Bottom nav**: mobile-only (`display: none` at ≥ 720px); active tab shown with emerald accent; badge count on Избранное

### Features complete
- **Calculator screen (v1)**: hero header, trust strip, 6-field form (country, price, currency, year, volume, engine type, delivery city), CTA button → result card with large KZT + approx USD, 7-line breakdown, explainability accordion (age/volume/type/customs band/rule version/warnings), disclaimer, lead capture form with calculation snapshot
- **Catalog screen**: full existing listing + filter logic; car cards have favorite heart button
- **Favorites screen**: localStorage persistence (key: `importcar_favorites`); empty state; count badge on nav
- **Request screen (Заявка)**: заявки placeholder + WhatsApp CTA + 4 trust notes
- **Car detail**: price summary card (mobile), favorite button, sticky CTA with WhatsApp + "Запросить расчёт"
- **PWA**: manifest.json, viewport-fit=cover, apple-mobile-web-app meta tags, theme-color #16c784
- **Lead form (catalog)**: preserved; Supabase + mock fallback work
- **Lead form (calculator)**: inserts with metadata JSONB containing calc_snapshot; requires schema migration
- **Admin view**: shows calculator context (source_country, year, volume, fuel_type, rule version, car URL) from metadata; CalcSnapshot type aligned to CalculatorScreen output field names
- **UI fully Russian**: ImporterCard, ImporterList, LeadForm, AdminLeads all Russified (no English user-facing copy remaining)
- **Pricing sanity tests**: `scripts/calc-sanity.mjs` — 5 Playwright scenarios with expected totals computed from v2026.05 rules; run with `npm run calc:sanity`
- **Smoke test**: `scripts/smoke-test.mjs` updated for Russian calculator-first UI; run with `npm run smoke:test`

### Schema (Supabase)
- `leads` table: migration needed in Supabase dashboard — make car_id/importer_id nullable, add metadata JSONB + source text
- Migration SQL at end of `supabase/schema.sql`

### Design system (current code)
- Font: 'Avenir Next', 'Segoe UI', Arial (system sans-serif)
- Accent: emerald #16c784 (--showroom-accent)
- Background: #f4f5f7 light / #090b0e dark hero
- Cards: white, subtle borders, 30px border-radius

### Data
- 15 real Encar listings with local images at `public/cars/encar-*.jpg`
- 5 mock importers
- Versioned pricing rules engine (v2026.05, USD_TO_KZT=525, KRW_TO_KZT=0.39)

### Build status
- `npm run lint` — ✅ 0 errors
- `npm run build` — ✅ clean, 460 kB JS bundle
- TypeScript — 0 errors

### Placeholders that need updating before launch
- WhatsApp number in `StickyCta.tsx`, `RequestScreen.tsx`, `CalculatorScreen.tsx`: `77071234567` — replace with real number
- App icons: only `favicon.svg` referenced in manifest — real PNG icons needed
- Run schema migration in Supabase dashboard before using calculator lead form in production
