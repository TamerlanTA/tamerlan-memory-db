# ImportCar.kz MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]
- [[roadmap]]

---

## ЗАВЕРШЕНО ✅

### v0.1 — Production Calculator
Все 8 задач: calculator screen, explainability, lead form with snapshot, admin view, lint/build clean.

### QA Hardening (2026-05-21)
- Race condition fix in `handleLeadSubmit` (captured `currentCost` before async)
- Snapshot field names aligned: `source_country`, `fuel_type`, `calculated_at`, `result_total_usd`
- `AdminLeads.tsx` `CalcSnapshot` type updated to match
- All English UI copy Russified: `ImporterCard`, `ImporterList`, `LeadForm`
- CSS: `.calcInputHint`, overflow protection on `.calcResultV2Total` and `.adminCarLink`
- `scripts/smoke-test.mjs` rewritten for Russian calculator-first UI
- `scripts/calc-sanity.mjs` created: 5 Playwright pricing sanity cases with exact expected totals
- `npm run lint` ✅ `npm run build` ✅ 460.99 kB

---

## СЛЕДУЮЩИЙ БЛОК: Immediate Fixes (блокируют деплой)

Обязательны до первого реального пользователя. В порядке приоритета:

### 1. Supabase schema migration ⚠️ КРИТИЧНО
Run in Supabase dashboard SQL editor:
```sql
alter table public.leads
  alter column car_id drop not null,
  alter column importer_id drop not null;
alter table public.leads
  add column if not exists metadata jsonb,
  add column if not exists source text not null default 'catalog';
```
Without this, calculator lead form insert will fail in production.
Migration SQL is also at the bottom of `supabase/schema.sql`.

### 2. Заменить placeholder WhatsApp номер
File: `src/components/StickyCta.tsx`, `src/components/RequestScreen.tsx`, `src/components/CalculatorScreen.tsx`
Search: `77071234567` → replace with real number.

### 3. Desktop top-nav
Bottom nav is hidden at ≥ 720px (`display: none`). Tabs are inaccessible from desktop.
Need a top nav bar showing Calculator / Каталог / Избранное / Заявка tabs for desktop users.

### 4. Деплой на Vercel
After 1–3 are done: deploy and test on real iPhone.

---

## ПОСЛЕ Immediate Fixes — Следующие этапы

- **v0.3** — Supabase Auth: Phone OTP + Google + Apple. Аккаунт запрашивать только при сохранении / заявке
- **v0.4** — Real Inventory: 30 качественных реальных листингов, честные лейблы
- **v0.5** — Payments: Kaspi/Halyk, платный точный расчёт от 1 990 ₸, VIN-проверка
- **v0.6** — Subscriptions: Free / Plus план
- **v0.7** — Importer Partner Layer: B2B монетизация
- **v0.8** — Native App (Capacitor): iOS/Android билды
- **v1.0** — App Store / Google Play публичный релиз

Детали каждого этапа — в [[roadmap]].
