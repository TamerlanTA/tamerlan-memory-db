# Session 2026-06-08 — Link Extraction Diagnostic Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Full diagnostic audit of AI link extraction pipeline: source detection, adapters, browser render, AI validation, quality gate
- Read all Edge Function files, docs, scripts, frontend service
- Identified root causes for URL-only extraction failures
- Made minor safe code changes: added `finalUrl` to live check summary, added 3 new example payload files
- All validation scripts pass: lint ✅ build ✅ ai:pipeline ✅ ai:edge ✅ ai:link-ui ✅ ai:contracts ✅

## Key findings

### Root causes ranked
1. **CRITICAL**: Encar is a JS SPA — server-side fetch gets React shell without vehicle data
2. **HIGH**: Geo-blocking — Supabase/Browserless US datacenters blocked by Korean anti-bot
3. **HIGH**: User-Agent `ImportCar.kz AI extraction bot` is immediately identifiable and blockable
4. **HIGH**: Encar/YouCar adapter = generic fetch + English regex patterns — Encar uses Korean-named properties or React state, not simple `"price"` JSON
5. **HIGH**: No Encar direct API adapter — `car.encar.com/cars/detail/{carId}` implies a discoverable REST API (`api.encar.com`) that could be called directly

### What works
- listingText path works reliably
- Quality gate correctly blocks insufficient data (not a bug)
- Schema validation and normalization are solid
- Browser render diagnostics are good but `finalUrl` wasn't printed in live check (fixed)

### What doesn't work
- URL-only for Encar/YouCar: always falls to EXTRACTION_INSUFFICIENT_DATA or BROWSER_RENDER_*
- Bot-UA + datacenter IP combination is unworkable for protected Korean listing sites

## Blockers
- None new — audit confirms known limitations

## Next steps
1. **AI-5D — Encar direct API adapter**: extract carId from URL → call `api.encar.com` directly → structured JSON → no scraping needed
2. **UX improvement**: listingText paste instruction, better placeholder, "open listing" button
3. **Start Accuracy Calibration**: AdminLeads calibration panel is deployed — start collecting data from listingText + manual flows now
4. **AI-7**: Verified Calculation Workflow after calibration data starts flowing
