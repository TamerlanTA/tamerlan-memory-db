# Session 2026-05-21 — Production Calculator QA & Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

---

## What was done

Full QA & Hardening pass on Production Calculator v1. Two back-to-back sessions (context limit triggered mid-session; resumed cleanly).

### CalculatorScreen.tsx fixes
- Added `calculatedAt` state (ISO string set at button click, not at submit time)
- Fixed `handleLeadSubmit` race condition: captured `const currentCost = cost` at async start before any awaits
- Expanded calc snapshot fields: renamed `country` → `source_country`, `engine_type` → `fuel_type`, added `destination_country: 'Kazakhstan'`, `result_total_usd`, `calculated_at`, `result_total_kzt`, full breakdown line items
- Added disabled-button validation hint: "Заполните цену, год и объём двигателя для расчёта."

### AdminLeads.tsx fixes
- Updated `CalcSnapshot` type: `country` → `source_country`, `engine_type` → `fuel_type`, added `result_total_kzt`, `result_total_usd`, `calculated_at`
- Updated `CalcContext` component to access `snap.source_country` and `snap.fuel_type`

### ImporterCard.tsx — full Russification
All English strings replaced:
- "Verified importer" → "Проверено"
- "Request" → "Запросить"
- "Details" / "Hide details" → "Подробнее" / "Скрыть детали"
- Detail panel labels: "Years in business", "Document support", "Customs broker", "Warranty / service" → Russian

### ImporterList.tsx
- "Concierge partners" eyebrow → "Партнёры-импортёры"

### LeadForm.tsx
- "Lead form" eyebrow → "Заявка"
- "Request sent" eyebrow → "Отправлено"

### App.css
- Added `.calcInputHint` style (13px, color #6f7782, centered, margin-top 8px)
- Added `overflow-wrap: anywhere` to `.calcResultV2Total`
- Added `word-break: break-all` to `.adminCarLink`

### scripts/smoke-test.mjs — rewritten
Old script referenced non-existent English text. New script:
- Checks calculator header ("Рассчитайте стоимость авто под ключ") is visible as default tab
- Clicks "Рассчитать стоимость" with pre-filled defaults
- Checks `.calcResultV2Total` appears
- Mobile-only (< 720px): navigates to Каталог tab via `.bottomNav`, counts car cards, opens detail, counts importer cards, clicks "Запросить", checks `.leadModal`

### scripts/calc-sanity.mjs — created (new file)
5 Playwright pricing sanity scenarios run against the live dev server:
1. Korea / 80M KRW / 2023 / 2998cc / petrol → expected 38,190,000 ₸
2. USA / 40k USD / 2020 / 3500cc / diesel → expected 28,400,000 ₸
3. Japan / 5M KRW / 2018 / 1500cc / hybrid → expected 4,797,500 ₸
4. UAE / 25k USD / 2022 / 2000cc / electric → expected 17,917,500 ₸
5. Korea / 20M KRW / 2015 / 1600cc / petrol → expected 12,060,000 ₸

All expected values computed manually from pricingRules.ts v2026.05.
Script added to package.json as `"calc:sanity": "node scripts/calc-sanity.mjs"`.

### package.json
- Added `"calc:sanity"` script

---

## Build status at end of session
- `npm run lint` — ✅ 0 errors
- `npm run build` — ✅ 0 errors, 460.99 kB JS bundle

---

## Key findings

### TypeScript / runtime
- All 4 `Country` values have delivery costs in pricingRules (Record<Country, number>) — no undefined possible
- All 4 `EngineType` values have utilization fees — no undefined possible
- `buildCar` returns null for price=0, year<2000 or >2030, vol=0 — button is correctly disabled in these cases
- `calculateCost` throws if no active pricing rule — guarded by `if (!cost)` in CalculatorScreen
- Admin view uses server-side RLS; frontend only reads leads, no write/update from admin UI

### Snapshot consistency
- AdminLeads CalcSnapshot type now matches CalculatorScreen output field names exactly
- Old leads with `country` field (pre-fix) will show empty source_country chip in admin — acceptable, old data

### Pending before production use
- Run schema migration in Supabase dashboard (make car_id/importer_id nullable, add metadata JSONB + source text)
- Replace WhatsApp placeholder `77071234567` in StickyCta.tsx, RequestScreen.tsx, CalculatorScreen.tsx
- Add desktop top-nav (tabs not accessible from desktop without it)

---

## Next steps
See [[next-steps]] — "Immediate fixes + v0.3" block.

Immediate priority: Supabase schema migration, WhatsApp number, desktop nav.
Then v0.3: Phone OTP + Google Auth.
