# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Notion Office
- Project page: https://app.notion.com/p/3793e026e92f81418d0ed4f05bb8eaf1
- Added to Office on 2026-06-08 with status Active, health Yellow, priority P0.
- Notion contains 12 roadmap phases, 14 current operational tasks, 6 decision/risk records, and the production activation weekly review.
- Current Office frontier matches memory: production activation, AI-5C.2 deployment/live acceptance, and calibration backend deployment.

## Status as of 2026-06-08 — PRODUCTION LIVE ✅ + AI-5D implemented locally

All deployment blockers resolved on 2026-06-08:
- Both Supabase migrations applied
- `analyze-car-link` (AI-5C.2) + `admin-calibrations` (AI-6.5) deployed with secrets
- Live acceptance scripts passed (`ai:edge:live`, `admin:calibration:live`)
- `vercel deploy --prod` completed
- Live acceptance runbook completed
- Real iPhone test passed
- **Product is now live in production**

AI-5D (Encar Direct API Adapter) implemented locally on 2026-06-08:
- `extractors/encarApi.ts` — new adapter, browser-like headers, 만원 normalization
- `extractEncarCarId()` in `sourceDetection.ts` — extracts 6–12 digit carId from URL
- Pipeline: Encar API → HTML adapter → generic fetch → browser render → listingText
- Success response adds `carId` and `adapter: "encar_api"` fields
- All ENCAR_API_* errors are non-fatal; pipeline always falls through
- All non-UI scripts pass: lint, build, ai:pipeline, ai:edge, ai:link-ui, ai:contracts, ai:risk, calibration:sanity, admin:calibration
- Pending: `supabase functions deploy analyze-car-link` for production

Next: deploy AI-5D Edge Function, live-test with real Encar carId, then AI-7 Verified Calculation Workflow

---

## Status as of 2026-05-27 — Preview Deploy Acceptance Prepared (historical)

### Strategic direction
- Project direction changed from a basic deterministic import calculator to an **AI-assisted import calculator with deterministic pricing engine**.
- AI must extract, normalize, enrich, explain, and flag risks; AI must not be the source of truth for final price.
- The deterministic pricing engine remains responsible for final totals using versioned rules, exchange rates, logistics rates, customs rules, service fee rules, and buffers.
- Internal long-term target after verified link/VIN/manager confirmation: aim toward 5-7% estimate error, but do not publicly promise this until validated by real data.
- Public language should stay conservative: "максимально приближенный расчёт", "предварительный расчёт", "точный расчёт после проверки ссылки/VIN", and "финальная стоимость зависит от курса, документов, логистики и актуальных ставок".
- Planning docs only were updated on 2026-05-25; no app code, calculator logic, AI API, Edge Function, auth, payments, subscriptions, or UI sections were implemented.

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

### AI-assisted architecture state
- AI-1 contracts/schemas infrastructure is implemented under `src/domain/aiCalculator/`.
- Added `VehicleExtractionResult`, `NormalizedVehicleInput`, `AiExtractionMetadata`, `CalculatorInputSource`, and additive snapshot extension types.
- Added Zod schemas and safe `parseVehicleExtraction(input)` validation.
- Added normalization helpers for engine volume, fuel type, currency, and money parsing.
- Added confidence scoring with `low`, `medium`, `high`, and `requires_review` levels plus Russian labels.
- Added `npm run ai:contracts` sanity script.
- AI-2 secure backend extraction endpoint structure is implemented under `supabase/functions/analyze-car-link/`.
- Added OpenAI-compatible provider abstraction, strict extraction prompt, request validation, safe listing fetch/text fallback, AI output validation, normalization, confidence scoring, and controlled JSON error responses.
- Added `docs/ai-link-extraction-endpoint.md` and `npm run ai:edge`.
- AI provider secrets are documented as Supabase Edge Function secrets only, not frontend `VITE_` variables.
- Manual frontend calculator behavior remains unchanged; no auth, payments, subscriptions, or App Store work was added.
- Supabase CLI/Deno are not installed locally, so Edge runtime verification/deploy still needs manual Supabase CLI check.
- AI-3 frontend flow is implemented in `CalculatorScreen`.
- Calculator now has two modes: "Быстрый расчёт" (default manual flow) and "По ссылке".
- Link mode lets the user enter URL/listing text, invokes `analyze-car-link` through Supabase Functions, shows loading/error states, then renders an extracted vehicle confirmation/edit card.
- Confirmed AI-extracted data is mapped into the existing deterministic `calculateCost()` path; AI does not calculate final totals.
- Saved calculation and lead metadata include additive `inputSource`, `aiExtraction`, and `normalizedVehicle` extension data for link mode; manual mode includes `inputSource: manual`.
- AdminLeads minimally shows link input source, confidence, and brand/model when present.
- AI-3.5 link-mode QA/hardening is complete.
- Added explicit AI extraction to pricing-engine mapping helper: `src/domain/aiCalculator/pricingMapping.ts`.
- Added `npm run ai:link-ui` sanity checks for link-mode mapping and snapshot JSON safety without real AI credentials.
- Link mode now validates malformed URLs in the frontend before invoking the Edge Function.
- AI-assisted saved/lead snapshots are cleaned of `undefined` nested values before JSON/localStorage/Supabase use.
- Manual quick mode was rechecked as default; manual save and mock/local request flow still work.
- Mocked link-mode success path was checked with Playwright: extracted card renders, editable price/engine fields calculate through deterministic `calculateCost()`, and saved snapshot stores `inputSource: ai_link`.
- Link failure paths were checked: empty URL/text, invalid URL, missing Supabase/AI configuration, retry/switch back to manual.
- Build now passes without the previous Vite chunk-size warning; main JS chunk is about 481.77 kB.
- AI-3.6 live Edge Function acceptance prep is complete.
- Added `docs/ai-edge-live-acceptance-runbook.md` with Supabase CLI login/link, secrets setup, deploy, local serve, curl tests, frontend test, pass/fail criteria, and rollback.
- Added example request/response payloads under `docs/examples/ai-link-*.json`.
- Added `npm run ai:edge:live` script for live `analyze-car-link` checks; dry-run mode works without endpoint or credentials.
- Verified AI secrets are documented only as Supabase Edge Function secrets (`AI_PROVIDER`, `OPENAI_API_KEY`, `AI_MODEL`) and not as frontend `VITE_` variables.
- AI-3.6 live Edge Function acceptance passed in the real Supabase environment. Reported `npm run ai:edge:live` result: HTTP 200, `ok: true`, confidence `medium`, missing fields `productionDate` and `vin`, warnings `[]`.
- 2026-05-27 preview deployment to Vercel succeeded with deployment id `dpl_7W5Nkr2DGNqZNEk6dsJtkNUaY9E5`.
- Preview URL: `https://importcar-kz-92phlsa2k-tamertt931-8560s-projects.vercel.app`.
- Vercel inspect URL: `https://vercel.com/tamertt931-8560s-projects/importcar-kz-mvp/7W5Nkr2DGNqZNEk6dsJtkNUaY9E5`.
- AI-4 deterministic Risk Reviewer + Grounded Explanation Layer is implemented.
- Added `src/domain/aiCalculator/riskReview.ts` and `src/domain/aiCalculator/explanation.ts`.
- Calculator result now shows "Надёжность расчёта" and "Пояснение к расчёту" sections for manual and AI-link calculations.
- Risk/explanation are grounded in confirmed inputs, AI extraction metadata, pricing warnings, and deterministic calculation result only.
- AI-4 does not call AI APIs and does not calculate or change final totals.
- Saved calculation and lead metadata snapshots include JSON-safe `riskReview` / `groundedExplanation` when available.
- AdminLeads shows minimal risk context and remains compatible with old leads.
- Added `npm run ai:risk`.
- AI-4.5 preview QA/UX tightening is complete.
- Calculator result order remains: total, breakdown, reliability, grounded explanation, deterministic explainability, disclaimer, save, lead form.
- "Пояснение к расчёту" is now collapsible to reduce result-page overload.
- Visible risk list is capped to the top 3 risks, sorted by severity; full risk snapshot is still stored.
- Added `docs/ai-4-preview-qa-checklist.md`.
- Added `docs/vercel-preview-acceptance-checklist.md` for preview deploy and real-device acceptance.
- README now has a current release candidate section covering what works, required configuration, and what is not production-complete.
- Environment documentation now separates Vercel frontend env vars, Supabase Edge Function secrets, and Supabase DB migration requirements.
- Mobile Playwright checks passed at 375px, 390px, and 412px; manual and mocked link-mode flows passed.
- Old saved calculation/local request snapshots without AI-4 fields still render.
- Latest build passes; main JS chunk is about 494.35 kB and remains under Vite's default warning threshold.
- AI-5A Link Extraction Reliability Layer is implemented.
- Edge Function now detects listing sources as `encar`, `youcar_encar`, `mobile_de`, `copart`, or `unknown` via `sourceDetection.ts`.
- Edge extraction pipeline now tracks `extractionMethod`: `site_adapter`, `simple_fetch`, `listing_text`, or `unavailable`.
- Added isolated extractor modules for generic fetch, pasted listing text, and a conservative Encar/YouCar adapter shell.
- `analyze-car-link` success/error responses now include safe source/method context when available; frontend preserves `sourceType` and `extractionMethod` in AI snapshot metadata.
- Link confirmation UI subtly shows source and analysis method.
- Added `docs/supported-listing-sources.md` and `npm run ai:pipeline`.
- Latest local validation for AI-5A passes: lint, build, AI contracts, Edge contract, link UI, risk, pipeline, smoke, and calc sanity.
- AI-5A live acceptance verification prep is ready.
- `scripts/ai-edge-live-check.mjs` now prints `httpStatus`, `ok`, `sourceType`, `extractionMethod`, `confidenceLevel`, `missingFields`, `warnings`, and failed `errorCode` without printing secrets.
- `npm run ai:edge:live -- --payload docs/examples/ai-link-url-only-request.json --allow-controlled-error` supports URL-only acceptance where dynamic/blocked pages may return a controlled failure.
- AI-5A is live accepted in Supabase Edge runtime.
- Reported AI-5A listingText acceptance: HTTP 200, `ok: true`, `extractionMethod: listing_text`.
- Reported AI-5A URL-only acceptance: source detection works (`sourceType: encar`), but simple fetch fails in a controlled way with HTTP 422, `ok: false`, `extractionMethod: simple_fetch`, `errorCode: URL_FETCH_FAILED`.
- AI-5B Browser Rendering Fallback is implemented and deployed.
- Added optional `browser_render` extractor using Browserless REST `/content` via server-side Supabase Edge Function secrets only.
- Updated Edge pipeline order: source adapter -> generic fetch -> optional browser render -> listingText -> controlled error.
- Added Browserless config secrets documentation: `BROWSER_RENDER_PROVIDER`, `BROWSERLESS_API_KEY`, `BROWSERLESS_ENDPOINT`.
- Missing Browserless config skips browser rendering safely and does not break listingText fallback.
- Frontend preserves `browser_render` as extraction method and shows Russian label "страница открыта в браузере".
- AI-5B local validation passes: lint, build, AI contracts, Edge contract, link UI, pipeline, smoke, and calc sanity.
- AI-5B live URL-only test reached browser rendering: HTTP 200, `ok: true`, `sourceType: encar`, `extractionMethod: browser_render`.
- AI-5B exposed a content-quality issue: Browserless opened the page, but rendered text had no useful vehicle fields, causing `requires_review` and warning "Listing text is unreadable or contains no vehicle data."
- AI-5C Browser Render Deep Extraction is implemented locally.
- Browser rendering now uses Browserless `/function` to collect structured page context: final URL, title, visible body text, meta tags, JSON-LD, selected script snippets, and diagnostic flags.
- Browser-rendered content is sent to AI only when enough vehicle-like signals exist; otherwise the endpoint returns controlled errors with diagnostics instead of letting AI infer from empty text.
- Added controlled errors: `BROWSER_RENDER_NO_VEHICLE_TEXT`, `BROWSER_RENDER_BLOCKED_OR_EMPTY`, `BROWSER_RENDER_DYNAMIC_DATA_UNAVAILABLE`.
- Live check script now prints safe diagnostics for controlled failures.
- AI-5C local validation passes: lint, build, AI contracts, Edge contract, link UI, pipeline, smoke, and calc sanity.
- AI-5C live URL-only test reached `browser_render` and AI provider, but returned `AI_OUTPUT_INVALID`, meaning provider JSON failed strict schema validation.
- AI-5C.1 AI Output Validation Debug & Repair is implemented locally.
- `AI_OUTPUT_INVALID` now returns HTTP 422 with safe `validationIssues` diagnostics instead of misleading 502.
- Edge pre-validation now conservatively normalizes harmless provider variations: currency symbols/names, Korean/Russian fuel labels, numeric strings for year/price/mileage/engine, and missing `missingFields`/`warnings`.
- Invalid confidence labels such as `"medium"` remain validation errors with diagnostics; they are not silently accepted.
- Extraction prompt is stricter about JSON-only output, enum values, numeric confidence, numeric fields, and no import-cost calculation.
- Live check script now prints validation issue summaries without raw provider output or secrets.
- AI-5C.1 local validation passes: lint, build, AI contracts, Edge contract, link UI, pipeline, smoke, and calc sanity.
- AI-5C.1 live URL-only test returned HTTP 200 `ok: true` but with `confidenceLevel: requires_review` and all key vehicle fields missing, showing that schema-valid AI JSON can still be product-invalid.
- AI-5C.2 Post-Extraction Quality Gate is implemented locally.
- After schema validation, `analyze-car-link` now checks required calculator handoff fields: `year`, `price`, `currency`, `engineVolumeCc`, and `fuelType`.
- If required fields are missing, the endpoint returns HTTP 422 with `EXTRACTION_INSUFFICIENT_DATA`, safe `missingRequiredFields` / `missingRecommendedFields`, warnings, source/method context, and optional small `partialVehiclePreview`.
- Frontend link mode maps `EXTRACTION_INSUFFICIENT_DATA` to Russian fallback guidance and can show missing key fields instead of opening the confirmation card.
- Live check script now prints missing required/recommended fields and warnings for insufficient extraction failures.
- AI-5C.2 local validation passes: lint, build, AI contracts, Edge contract, link UI, pipeline, smoke, and calc sanity.
- AI-5C.2 has not yet been deployed/live-accepted; deploy updated `analyze-car-link` and rerun URL-only live acceptance.
- AI-6 Accuracy Calibration Foundation is implemented locally.
- Added `calculation_calibrations` migration with RLS enabled, no public anon/authenticated policies, and service-role access only.
- Added calibration domain helper for estimate-vs-verified difference in KZT/percent, direction, target label, and invalid input handling.
- Added compact AdminLeads calibration panel for manager verified totals, final totals, reason category/text, actual logistics/customs/service fee, exchange rate, and notes.
- Added calibration service layer with controlled errors for missing migration, Supabase not configured, or RLS/access denial.
- Added `docs/accuracy-calibration.md` and `npm run calibration:sanity`.
- Pricing formulas remain unchanged; calibration data is stored separately for future analysis.
- Browser-side calibration save will need secure admin access/service backend before production use because the table is intentionally not public-readable.
- Latest build passes but main JS is about 504.64 kB and Vite reports a chunk-size warning; later admin/calibration code-splitting is recommended.
- AI-6.5 Secure Calibration Admin Backend is implemented locally.
- Added Supabase Edge Function `admin-calibrations` for `create`, `update`, and `getByLeadId` calibration actions.
- `admin-calibrations` uses `ADMIN_API_KEY` and `SUPABASE_SERVICE_ROLE_KEY` as Supabase Edge Function secrets only; service role is not referenced in frontend code.
- Frontend calibration service now calls `supabase.functions.invoke('admin-calibrations')` with `x-admin-key`; it no longer writes `calculation_calibrations` directly.
- Edge Function validates UUIDs, positive numeric totals, reason categories, and calibration status; it computes `difference_kzt` and `difference_percent` server-side.
- AdminLeads loads existing calibration by `lead_id` and saves/updates via the Edge Function with controlled errors when function/env is missing.
- RLS remains strict: no public calibration policies were added.
- AdminLeads is now lazy-loaded into a separate `AdminLeads` chunk; main JS dropped to about 494.75 kB and Vite chunk warning is gone.
- Added `npm run admin:calibration` sanity script.
- AI-6.6 Internal Calibration Acceptance Test prep is complete.
- Added `docs/internal-calibration-acceptance-checklist.md` with migration/RLS/secrets/deploy/internal Vercel/AdminLeads/database row/error/rollback checks.
- Added `npm run admin:calibration:live` dry/live script for synthetic `admin-calibrations` create checks using `ADMIN_CALIBRATIONS_FUNCTION_URL` and `ADMIN_API_KEY`.
- Live-check script prints only safe summaries and does not require local service role.
- AI-6.6 local validation passes: lint, build, admin calibration contract, calibration sanity, and admin live-check dry-run.
- Vercel preview deploy completed on 2026-05-29.
- Preview URL: `https://importcar-kz-lvrvupbns-tamertt931-8560s-projects.vercel.app`.
- Vercel inspect URL: `https://vercel.com/tamertt931-8560s-projects/importcar-kz-mvp/9iMLct51fZZX6umGDgH2FBosBSYh`.
- Deployment id: `dpl_9iMLct51fZZX6umGDgH2FBosBSYh`.
- Next strategic implementation block: deploy/apply AI-5C.2, AI-6, and AI-6.5 backend changes, then plan secure verified-calculation workflow.

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
- `npm run build` — ✅ TypeScript/build clean, 494.75 kB main JS bundle after AI-6.5
- AdminLeads/calibration is lazy-loaded as a separate 11.01 kB chunk; no Vite chunk-size warning
- TypeScript — 0 errors

### Placeholders that need updating before launch
- Set `VITE_WHATSAPP_PHONE` in Vercel before real traffic
- App icons: only `favicon.svg` referenced in manifest — real PNG icons needed
- Run schema migration in Supabase dashboard before using calculator lead form in production
