# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Status as of 2026-05-21 — Production Calculator v1 + Phase 3B Deploy Prep Complete

### Architecture
- **App shell**: `div.appShell` → `div.appContent` container; bottom nav fixed at bottom on mobile
- **Routing**: state-based (no React Router); `activeTab` + `detailSource` for back-navigation
- **4 tabs**: Калькулятор (default) / Каталог / Избранное / Заявка
- **Bottom nav**: mobile-only (`display: none` at ≥ 720px); active tab shown with emerald accent; badge count on Избранное

### Features complete
- **Calculator screen (v1)**: hero header, trust strip, 6-field form (country, price, currency, year, volume, engine type, delivery city), CTA button → result card with large KZT + approx USD, 7-line breakdown, explainability accordion (age/volume/type/customs band/rule version/warnings), disclaimer, lead capture form with calculation snapshot
- **Saved calculations (Phase 2)**: localStorage hook with resilient parsing, max 10 records, duplicate replacement, remove/clear/latest helpers; calculator result has "Сохранить расчёт" action and success feedback
- **Local request mirror (Phase 2)**: successful calculator lead submissions are mirrored locally after Supabase/mock success so the "Заявка" tab can show latest request pre-auth
- **Request screen (Phase 2)**: no longer placeholder; shows latest request, latest saved calculation fallback, recent saved calculations list with remove buttons, WhatsApp support CTA, and "Получить точный расчёт" action back to calculator
- **Production backend activation prep (Phase 3A)**: dedicated Supabase migration file exists, WhatsApp CTAs use env-based config, `.env.example` and production activation checklist added, calculator/catalog lead payloads set top-level `source`
- **Live acceptance prep (Phase 3B)**: production checklist expanded and `docs/live-acceptance-runbook.md` added for deploy, Supabase verification, live tests, pass/fail criteria, and rollback
- **Catalog screen**: full existing listing + filter logic; car cards have favorite heart button
- **Favorites screen**: localStorage persistence (key: `importcar_favorites`); empty state; count badge on nav
- **Request screen (Заявка)**: latest request, latest saved calculation fallback, saved calculations list, remove actions, WhatsApp CTA
- **Car detail**: price summary card (mobile), favorite button, sticky CTA with WhatsApp + "Запросить расчёт"
- **PWA**: manifest.json, viewport-fit=cover, apple-mobile-web-app meta tags, theme-color #16c784
- **Lead form (catalog)**: preserved; Supabase + mock fallback work
- **Lead form (calculator)**: inserts with metadata JSONB containing calc_snapshot; requires schema migration
- **Admin view**: shows calculator context (source_country, year, volume, fuel_type, rule version, car URL) from metadata; CalcSnapshot type aligned to CalculatorScreen output field names
- **UI fully Russian**: ImporterCard, ImporterList, LeadForm, AdminLeads all Russified (no English user-facing copy remaining)
- **Pricing sanity tests**: `scripts/calc-sanity.mjs` — 5 Playwright scenarios with expected totals computed from v2026.05 rules; run with `npm run calc:sanity`
- **Smoke test**: `scripts/smoke-test.mjs` updated for Russian calculator-first UI; run with `npm run smoke:test`

### Schema (Supabase)
- `leads` table: production migration file exists at `supabase/migrations/20260521_calculator_leads_metadata.sql`
- Manual migration still must be run in Supabase dashboard before production calculator lead use
- RLS posture reviewed: anonymous insert only for `leads`; no anonymous lead read/update/delete policy added

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
- `npm run build` — ✅ clean, 469.75 kB JS bundle after Phase 3B docs
- TypeScript — 0 errors

### Placeholders that need updating before launch
- Set `VITE_WHATSAPP_PHONE` in Vercel before real traffic
- App icons: only `favicon.svg` referenced in manifest — real PNG icons needed
- Run schema migration in Supabase dashboard before using calculator lead form in production
