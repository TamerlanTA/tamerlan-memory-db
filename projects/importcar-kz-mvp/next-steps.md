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

### Phase 2 — Saved Calculations + Request Flow (2026-05-21)
- `useSavedCalculations` localStorage hook added with max 10 saved calculations, invalid JSON protection, duplicate replacement, remove/clear/latest helpers
- `useLocalRequests` localStorage hook added with max 10 local request mirrors and invalid JSON protection
- Calculator result now supports "Сохранить расчёт"
- Successful exact-calculation lead submission now saves local request state after Supabase/mock success
- "Заявка" tab now shows latest request, latest saved calculation fallback, saved calculations list, remove buttons, and WhatsApp support CTA
- `npm run lint` ✅ `npm run build` ✅ 470.06 kB

### Phase 3A — Production Backend Activation Prep (2026-05-21)
- Dedicated migration created: `supabase/migrations/20260521_calculator_leads_metadata.sql`
- RLS reviewed and not weakened: anon insert only for `leads`, no anon read/update/delete
- WhatsApp CTAs moved to env-based helper via `VITE_WHATSAPP_PHONE`
- Calculator leads insert top-level `source: 'calculator'`; catalog leads insert `source: 'catalog'`
- `.env.example`, README, and `docs/production-activation-checklist.md` updated
- `npm run lint` ✅ `npm run build` ✅ 469.75 kB
- `npm run smoke:test` ✅

### Phase 3B — Production Deploy & Live Acceptance Prep (2026-05-21)
- `docs/production-activation-checklist.md` expanded with exact SQL verification, RLS checks, env recommendations, expected lead row shape, and rollback notes
- `docs/live-acceptance-runbook.md` created for manual deploy/live acceptance execution
- Confirmed no hardcoded WhatsApp placeholder remains
- Confirmed public production should use `VITE_ENABLE_ADMIN_VIEW=false`
- `npm run lint` ✅ `npm run build` ✅ 469.75 kB

---

## СЛЕДУЮЩИЙ БЛОК: Production Activation (блокирует деплой)

Обязательны до первого реального пользователя. В порядке приоритета:

### 1. Run Supabase migration ⚠️ КРИТИЧНО
Run `supabase/migrations/20260521_calculator_leads_metadata.sql` in Supabase dashboard SQL editor.
Without this, calculator lead form insert can fail in production.

### 2. Set production env vars in Vercel
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `VITE_ENABLE_ADMIN_VIEW=false`
- `VITE_WHATSAPP_PHONE`
- optional: `VITE_WHATSAPP_DEFAULT_MESSAGE`

### 3. Deploy to Vercel
After 1–2 are done: deploy and follow `docs/live-acceptance-runbook.md`.

### 4. Real iPhone test
Test calculator, saved calculation persistence, request submit, "Заявка" screen, bottom nav, and WhatsApp CTA handoff.

---

## ПОСЛЕ Immediate Fixes — Следующие этапы

- **Phase AI-0 — Roadmap and architecture update** ✅ 2026-05-25: зафиксировать стратегию AI-assisted calculator и явно указать, что AI не является authority для финальной цены.
- **Phase AI-1 — AI contracts and schemas** ✅ 2026-05-25:
  - `VehicleExtractionResult` type
  - Zod validation schema
  - AI snapshot extension types
  - confidence logic design
  - no real AI API yet
  - no frontend AI secrets
- **Phase AI-2 — Secure AI Link Extraction MVP** ← следующий strategic implementation block: Supabase Edge Function или secure backend endpoint, provider abstraction, strict JSON extraction, validation, fallback if URL unreadable.
- **Phase AI-3 — User Confirmation + AI-assisted Calculation**: режимы "Быстрый расчёт" / "По ссылке", extracted vehicle card, edit/confirm, normalized data into deterministic pricing engine.
- **Phase AI-4 — Risk Reviewer + Explanation Layer**: AI warnings, grounded explanations, confidence labels; AI does not overwrite deterministic total.
- **Phase AI-5 — Accuracy Calibration**: store estimate vs final manager total, difference percent, reason, actual logistics, exchange rate used, final outcome.
- **Phase AI-6 — Verified Calculation Workflow**: manager confirmation, verified quote status, high-confidence calculation path.
- **v0.3** — Supabase Auth: Phone OTP + Google + Apple. Аккаунт запрашивать только при сохранении / заявке. Перенесено после AI-assisted calculator contracts.
- **v0.4** — Real Inventory: 30 качественных реальных листингов, честные лейблы
- **v0.5** — Payments: Kaspi/Halyk, платный точный расчёт от 1 990 ₸, VIN-проверка
- **v0.6** — Subscriptions: Free / Plus план
- **v0.7** — Importer Partner Layer: B2B монетизация
- **v0.8** — Native App (Capacitor): iOS/Android билды
- **v1.0** — App Store / Google Play публичный релиз

Детали каждого этапа — в [[roadmap]].
