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
Preview deploy completed on 2026-05-27:
- `https://importcar-kz-92phlsa2k-tamertt931-8560s-projects.vercel.app`

For production deploy, promote/deploy with:
- `vercel deploy --prod`

Then follow `docs/live-acceptance-runbook.md`.

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
- **Phase AI-2 — Secure AI Link Extraction MVP** ✅ 2026-05-25: Supabase Edge Function structure `analyze-car-link`, provider abstraction, strict JSON extraction prompt, validation, fallback if URL unreadable, docs, and no-key sanity script. Manual Supabase CLI/Deno verification still needed before deploy because local CLI is unavailable.
- **Phase AI-3 — User Confirmation + AI-assisted Calculation** ✅ 2026-05-25: режимы "Быстрый расчёт" / "По ссылке", frontend Edge Function client, URL/text analysis states, extracted vehicle edit/confirm card, validation, deterministic calculation mapping, snapshot extension, minimal AdminLeads AI context.
- **Phase AI-3.5 — Link Mode QA & Hardening** ✅ 2026-05-26: frontend invalid URL guard, explicit extraction-to-pricing mapping helper, JSON-safe AI snapshots, AdminLeads confidence copy cleanup, `npm run ai:link-ui`, Playwright checks for manual default/save/local request, link failure states, and mocked link success calculation/save.
- **Phase AI-3.6 — Live Edge Function Acceptance Prep** ✅ 2026-05-26: `docs/ai-edge-live-acceptance-runbook.md`, safe example payloads, `npm run ai:edge:live` dry/live check script, and secret-handling verification. Manual Supabase CLI deploy/runtime acceptance is still pending.
- **Manual live acceptance for `analyze-car-link`** ✅ 2026-05-27: reported `npm run ai:edge:live` returned HTTP 200, `ok: true`, confidence `medium`, missing fields `productionDate` and `vin`, warnings `[]`.
- **Phase AI-4 — Risk Reviewer + Explanation Layer** ✅ 2026-05-27: deterministic `riskReview` and `groundedExplanation`, result UI sections, snapshot metadata, AdminLeads risk context, `npm run ai:risk`; AI does not overwrite deterministic total.
- **Phase AI-4.5 — Production Preview QA & UX Tightening** ✅ 2026-05-27: collapsible grounded explanation, top-3 visible risk cap sorted by severity, mobile QA at 375/390/412, mocked link-mode QA, old snapshot compatibility check, and preview QA checklist.
- **Preview Deploy Acceptance Prep** ✅ 2026-05-27: `docs/vercel-preview-acceptance-checklist.md`, README release-candidate section, and clear separation of Vercel frontend env, Supabase Edge secrets, and Supabase DB migrations.
- **Vercel preview deploy + real-device acceptance** ✅ reported complete enough to proceed: preview deployed, AI-link flow confirmed on real iPhone, and live Edge acceptance previously passed.
- **Phase AI-5A — Link Extraction Reliability Layer** ✅ 2026-05-27: source detection, extraction method tracking, isolated extraction pipeline, listing text fallback, Encar/YouCar adapter shell, better error taxonomy, supported-source docs, and `npm run ai:pipeline`.
- **AI-5A Live Acceptance Verification Prep** ✅ 2026-05-27: live check script now prints source/method/confidence/missing/warnings/error code and supports URL-only controlled failure acceptance; runbook documents listingText success, URL-only success/controlled failure, frontend method display, and fallback behavior.
- **AI-5A Live Acceptance** ✅ 2026-05-28: listingText passes (`ok: true`, `extractionMethod: listing_text`); URL-only detects `sourceType: encar` but returns controlled `URL_FETCH_FAILED`, confirming simple fetch is not enough for dynamic/blocked listing pages.
- **Phase AI-5B — Browser Rendering Fallback** ✅ 2026-05-28 local implementation: optional Browserless `/content` fallback, `browser_render` extraction method, server-side Browserless secrets only, docs, and sanity coverage.
- **AI-5B Live Acceptance** ✅ 2026-05-28: URL-only reaches `browser_render` successfully (`httpStatus 200`, `ok true`, `sourceType encar`, `extractionMethod browser_render`), but useful vehicle data was missing and result required review.
- **Phase AI-5C — Browser Render Deep Extraction** ✅ 2026-05-28 local implementation: Browserless `/function` strategy, structured page context, vehicle-like signal gate, diagnostics, and controlled no-vehicle-data errors.
- **Phase AI-5C.1 — AI Output Validation Debug & Repair** ✅ 2026-05-28 local implementation: safe `validationIssues` diagnostics for `AI_OUTPUT_INVALID`, HTTP 422 status mapping, conservative provider-output normalization, stricter prompt, and live-check validation issue summaries.
- **Phase AI-5C.2 — Post-Extraction Quality Gate** ✅ 2026-05-28 local implementation: schema-valid but insufficient AI output now returns `EXTRACTION_INSUFFICIENT_DATA` with HTTP 422, safe missing-field details, frontend fallback copy, and live-check summaries.
- **Deploy updated `analyze-car-link` Edge Function + AI-5C.2 live acceptance** ← immediate next operational step: deploy function, rerun URL-only live acceptance, and confirm page-not-found/no-vehicle data now returns controlled 422 instead of `ok: true`.
- **Phase AI-6 — Accuracy Calibration Foundation** ✅ 2026-05-28 local implementation: migration, RLS-closed calibration table, difference helper, AdminLeads calibration panel, service layer with controlled errors, docs, and `npm run calibration:sanity`.
- **Phase AI-6.5 — Secure Calibration Admin Backend** ✅ 2026-05-28 local implementation: `admin-calibrations` Edge Function, temporary `ADMIN_API_KEY`, server-side service-role writes, server-side validation/difference calculation, frontend service invocation, AdminLeads load/save through Edge Function, and admin lazy-load.
- **Phase AI-6.6 — Internal Calibration Acceptance Test Prep** ✅ 2026-05-29: internal checklist and `npm run admin:calibration:live` dry/live script for safe synthetic Edge Function acceptance.
- **Deploy calibration backend** ← next data step: run `supabase/migrations/20260528_accuracy_calibration.sql`, deploy `admin-calibrations`, set Supabase secrets `ADMIN_API_KEY` / `SUPABASE_SERVICE_ROLE_KEY`, and set `VITE_ADMIN_API_KEY` only in protected internal preview.
- **Phase AI-7 — Verified Calculation Workflow**: manager confirmation, verified quote status, high-confidence calculation path.
- **v0.3** — Supabase Auth: Phone OTP + Google + Apple. Аккаунт запрашивать только при сохранении / заявке. Перенесено после AI-assisted calculator contracts.
- **v0.4** — Real Inventory: 30 качественных реальных листингов, честные лейблы
- **v0.5** — Payments: Kaspi/Halyk, платный точный расчёт от 1 990 ₸, VIN-проверка
- **v0.6** — Subscriptions: Free / Plus план
- **v0.7** — Importer Partner Layer: B2B монетизация
- **v0.8** — Native App (Capacitor): iOS/Android билды
- **v1.0** — App Store / Google Play публичный релиз

Детали каждого этапа — в [[roadmap]].
