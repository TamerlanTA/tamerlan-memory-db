# ImportCar.kz MVP — Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

## Content
## Current risks
- Pricing and customs formulas are still estimates/placeholders and need jurisdiction-validated rules before real use.
- Catalog records are demo data, not live inventory.
- Current imagery is still demo imagery and should be validated for rights and exact listing fit before real launch.
- Supabase admin workflows are not production-ready without auth and role-based access.
- Proof artifacts are mock trust devices and must eventually be tied to real importer operations.
- **Production WhatsApp env required**: WhatsApp CTAs now read `VITE_WHATSAPP_PHONE`; production deploy must set it in Vercel before real traffic.
- **Production migration required**: `supabase/migrations/20260521_calculator_leads_metadata.sql` exists, but must be run in Supabase dashboard before calculator leads are used in production.
- **AI authority risk**: product copy and implementation must not imply that AI calculates final price by itself. Deterministic pricing engine remains source of truth.
- **AI extraction risk**: listing pages such as Encar may be dynamic, blocked, or unreadable from backend contexts; fallback paths must include pasted text, later screenshot upload, manual edit, and manager verification.
- **AI validation risk**: invalid/missing extracted fields must not silently enter pricing engine. Strict schema validation and user confirmation are now implemented for AI-3, with AI-3.5 frontend URL validation and mapping sanity checks. AI-5A adds source/method tracking and clearer extraction errors; AI-5B adds optional browser rendering; AI-5C.1 adds safe validation diagnostics and conservative pre-validation normalization for provider output; AI-5C.2 blocks schema-valid but insufficient extracted vehicles before confirmation UI. Remaining risk is live provider behavior after deploy.
- **Frontend secret risk**: AI provider keys must never be exposed in frontend env vars; future AI calls must go through Supabase Edge Function or secure backend.
- **Accuracy promise risk**: do not publicly promise 5-7% accuracy until enough real estimate-vs-final data exists.
- **Live Edge runtime risk**: reduced after reported AI-3.6 live acceptance success, but production monitoring is still needed for provider failures, blocked listing pages, and quota/rate-limit behavior.
- **Browser rendering risk**: Browserless can improve dynamic page extraction but can still fail on anti-bot, CAPTCHA, geo-blocking, quotas, provider timeouts, or pages whose useful vehicle data is hidden behind protected APIs. It must remain optional and server-side only.
- **Calibration admin auth risk**: AI-6.5 uses temporary `ADMIN_API_KEY` / `x-admin-key` protection for internal preview/admin builds. This is not final auth; production admin should move to Supabase Auth plus admin roles. Public production must keep `VITE_ENABLE_ADMIN_VIEW=false` and avoid `VITE_ADMIN_API_KEY`.
- **Calibration backend deployment risk**: calibration saves require the `calculation_calibrations` migration, deployed `admin-calibrations` Edge Function, `ADMIN_API_KEY`, and `SUPABASE_SERVICE_ROLE_KEY` secrets.

## Mitigated / reduced risks
- Anonymous lead select/update access is not exposed in public schema.
- Admin status updates are read-only in UI until authenticated access exists.
- Former dead buttons now open real inline mock content.
- Proof-case purchase price is data-driven.
- Phone validation exists before submit.
- Smoke tests exist as a repeatable verification path (`npm run smoke:test`).
- WhatsApp placeholder number was removed from source components and replaced with env-based config.
- Desktop top nav exists, so calculator/catalog/favorites/request tabs are reachable on desktop.
- AI-3.5 reduced link-mode regression risk with explicit pricing mapping helpers, JSON-safe snapshots, `npm run ai:link-ui`, and mocked Playwright success/failure checks.
- AI-3.6 reduced live rollout risk with a dedicated Edge Function acceptance runbook, sample payloads, and `npm run ai:edge:live` dry/live script.
- AI-4 reduced explanation/positioning risk by adding deterministic risk review and grounded explanation without AI final-price authority.
- AI-5A reduced link reliability/debugging risk by adding source detection, extraction method tracking, isolated extractor modules, listing text fallback, Encar/YouCar adapter shell, clearer error taxonomy, and `npm run ai:pipeline`.
- AI-5B reduced URL-only extraction risk by adding optional Browserless rendering fallback after simple fetch failure, with controlled errors and no frontend secrets.
- AI-5C reduced hallucination/empty-page risk by adding deep browser-render context extraction, vehicle-like signal gating, and safe diagnostics before AI extraction.
- AI-5C.1 reduced provider-output debugging risk by returning HTTP 422 plus capped `validationIssues` for `AI_OUTPUT_INVALID`, while keeping strict validation and not exposing raw AI output.
- AI-5C.2 reduced false-success risk by returning `EXTRACTION_INSUFFICIENT_DATA` when schema-valid AI output lacks required calculator handoff fields.
- AI-6 reduced future accuracy-blindness risk by adding structured estimate-vs-verified calibration capture without changing deterministic pricing formulas.
- AI-6.5 reduced calibration RLS pressure by routing admin saves through a service-role Edge Function instead of adding public table policies.
- AI-6.5 reduced bundle-size risk by lazy-loading AdminLeads/calibration into a separate chunk.
