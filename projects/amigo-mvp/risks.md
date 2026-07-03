# AMIGO MVP — Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]
- [[technical-architecture]]
- [[integrations]]
- [[phase-6-execution-plan]]

## Active risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Enterprise ATS forms differ by employer and change without notice | High | High | Versioned employer adapters, fixture tests, connector health checks, manual certification |
| Workday, Oracle, SAP, and Taleo do not offer universal candidate-side submission APIs | High | High | Use hosted forms, support only certified flows, route unsupported forms to `NeedsAction` |
| CAPTCHA, OTP, assessments, or account creation block automation | High | Medium | Never bypass controls; create manager tasks with deep links and preserved context |
| July 5 timeline is too short for broad ATS coverage | High | High | Launch with a narrow certified connector set and measure coverage rather than claiming universality |
| Telegram-only operations become slow at 30 candidates | Medium | High | Add search, ownership filters, pagination, batch actions, and export reports; define web-panel trigger |
| Slow Telegram callbacks can exceed webhook timeout and cause Telegram to retry the same update | Medium | Medium | `bot-api` now dedupes Telegram `update_id` in memory and webhook timeout is 30 seconds; keep heavy operations under timeout or move them to async jobs |
| Generated CV contains invented or mistranslated facts | Low | High | Structured output, source-field mapping, validation rules, manager approval, immutable versions, Phase 3.5 structured CV enrichment tables |
| Managers enter weak or incomplete CV enrichment data | Medium | Medium | Use `/candidate_view` readiness warnings, runbook templates, manager review before document approval |
| Unified Telegram onboarding has not completed a full live manager acceptance pass | Medium | Medium | Complete one real `/candidate_new` flow with experience, education, extra, photo, final review, CV regeneration, skip branches, and `/cancel` before pilot use |
| Candidate portrait has a poor crop, unexpected orientation, or a malformed image file | Medium | Low | JPEG/PNG/WebP/HEIC/HEIF uploads are accepted; HEIC/HEIF is converted to JPEG server-side, processing failures preserve the Telegram session, and managers review final crop/quality in the generated PDF before approval |
| Compact CV header wraps on unusually long names/contact values | Low | Medium | Two-column production sample passed with realistic data; manager must review long-name/long-email candidates before document approval |
| Telegram bot token and other secrets appeared in operational logs/chats before full sanitization/rotation | Medium | Critical | `bot-api` deployment `c3aa43ac-8526-4fe6-a856-9f1d3a867661` adds sanitized process-level error logging; rotate the Telegram bot token through BotFather, rotate the shared Railway token, review OpenAI/Supabase keys, update Railway variables, and refresh the webhook |
| Duplicate or excessive applications damage candidate reputation | Medium | High | Idempotency keys, employer/domain limits, prior-application checks, daily caps |
| Phase 6 drifts into unsafe universal auto-apply | Medium | High | [[phase-6-execution-plan]] is now canonical; start with manual deep-link tasks and allow auto-submit only for certified narrow adapters |
| Workday preflight is mistaken for live-submit readiness | Medium | High | `workday-form-v1` is explicitly preflight-only; `/adapter_eligibility` uses `preflight-capable`, and live submit remains blocked until browser autofill, upload, evidence, rate limits, source allowlist, and controlled submission are certified |
| Career sites block shared datacenter IPs | Medium | High | Slow domain-specific rates, stable sessions, optional compliant proxy budget, manual fallback |
| Candidate personal data is exposed | Low | Critical | Private storage, RLS, least privilege, encrypted secrets, signed URLs, audit log, retention deletion |
| Waitlist activates before operations are stable | High | High | Ten-candidate controlled pilot, launch gates, connector error thresholds, staged 10→20→30 activation |
| Monthly cost exceeds USD 100 | Medium | Medium | PGMQ instead of Redis, bounded browser concurrency, per-service budgets and weekly usage review |
| Insufficient suitable vacancies prevents 5–10 daily applications | Medium | Medium | Report `eligible vacancy shortage` explicitly; never lower hard requirements only to hit volume |
| Narrow country+role intersections return `0/10` despite a healthy overall vacancy catalog | High | Medium | Use `/ops_status` for catalog totals, then inspect exact role+country coverage; expand Qatar/Bahrain/front-office/waiter sources and improve location extraction before relaxing hard filters |
| Query-level sources can over-broaden location signals | Medium | Medium | Treat query-source rows as supply candidates, not final truth; preserve manager review, inspect vacancy title/location conflicts, and improve per-vacancy location extraction before making strict auto-submit decisions |
| Reserve-heavy daily batches may satisfy volume but not strict primary fit | Medium | Medium | Decide product policy: count manager-approved reserve vacancies toward the 5/day goal or require 5 strict primary items and widen candidate/source coverage accordingly |
| Temporary Railway token was shared in chat for candidate supply deploy | High | High | Deploy succeeded; rotate the token immediately after verification and prefer short-lived deployment tokens for future Railway operations |
| HTML-based public career pages change markup and break read-only vacancy parsing | Medium | Medium | Keep connector isolated/versioned, fixture-test parser behavior, monitor `source_runs`, and treat failures as source health issues rather than silent success |
| Phase 4C.1 property-level SuccessFactors sources overlap with broad Kerzner search by `apply_url` | Medium | Medium | Phase 4C.2 duplicate report now detects active cross-source overlap; wire it into Phase 5 batch suppression before showing vacancies to managers |
| Phase 5 Telegram UI has not been clicked manually after deploy | Medium | Medium | Production data acceptance passed through the matching store; run `/candidate_batch` in Telegram to verify visible manager UX and inline callbacks end to end |
| Railway CLI auth can expire or fail between operational verification sessions | Medium | Medium | Use stable `RAILWAY_TOKEN` / `RAILWAY_API_TOKEN` for operational retries; token auth restored the 2026-06-27 Phase 4C.1 rollout |
| Railway token shared in chat during Phase 6 deploy | High | High | Rotate the token after deploy verification; avoid storing it in repo or memory |
| Candidate edit/close lists apply the `closed` filter after `LIMIT 20` | Medium | Medium | Filter `status != closed` in SQL before limiting; add regression coverage with more than 20 mixed-status candidates |
| Candidate assignment can change between close selection and confirmation | Low | High | Include `assigned_manager_id` in the closing update predicate and require an affected row before writing the audit event |
| Intake accepts a location with an empty country or city | Medium | Medium | Validate both trimmed location parts and add cases for `Kazakhstan,` and `,Almaty` |
| First production CV generation path has not been exercised end-to-end | Medium | High | Run a controlled candidate through `/candidate_documents`; inspect worker logs, generated files, signed URL, and approval status transition |
| OpenAI document model name may differ from configured `gpt-5.4-mini` availability | Medium | High | Verify first production job; if unavailable, set `OPENAI_DOCUMENT_MODEL` to an approved available structured-output model |
| Gotenberg private networking or LibreOffice conversion can fail at runtime | Medium | Medium | Gotenberg service is deployed at `gotenberg.railway.internal`; validate first PDF render and keep failure classified as `validation_failed`/worker error |

## Launch blockers
- No production-enabled application connector; `manual-deep-link-v1` is safe/manual and `email-apply-v1` is local dry-run/default only.
- Phase 6 manual-action slice is accepted for manual deep-link mode; production has `Applied` manual resolutions and `manual_confirmation` evidence. Remaining risk is operational consistency across more candidates and any future auto-submit/email path.
- No production end-to-end evidence trail for applications has been accepted yet.
- Application-level duplicate prevention exists locally in Phase 6 schema/service but is not production-applied yet.
- Manager approval gate for vacancy batches is deployed and production data acceptance passed; manual Telegram UI click-through is still recommended before manager rollout.
- No tested retention and access controls.
- More than 10% silent or unclassified application outcomes during pilot QA.

## Resolved foundation blockers
- Application repository and environments were created and linked on 2026-06-15.
- Production Telegram webhook, database health, queue processing, and audit persistence were verified.
- Draft CV and consent artifacts now exist; they remain pending approval rather than missing.

## Resolved Phase 2 blockers
- Candidate edit/close list filtering now applies `status != closed` before `LIMIT 20`.
- Close confirmation verifies candidate ID, current manager assignment, and non-closed status before update.
- Intake location validation requires both country and city around the comma.

## Resolved Phase 4C.1 rollout blockers
- Railway auth was restored with token-based CLI access on 2026-06-27.
- `bot-api` was redeployed with optimized plain-text `/source_health`; production webhook simulation returns HTTP 200 without timeout.
- `worker-vacancy-discovery` was redeployed with updated `successfactors-v1` query preservation and logs `checkedSourceCount=9`.

## Resolved Phase 4C.2 blocker
- Cross-source vacancy duplicate detection exists as a read-only report before Phase 5 matching. Production report found 10 active groups / 20 rows, all canonical `apply_url` overlaps; source-scoped `dedupe_key` remains unchanged and production has 0 duplicate dedupe groups.

## Scale-to-30 gates
- At least 95% of jobs finish in a terminal or actionable state.
- Queue lag stays below 30 minutes during daily batch execution.
- No duplicate applications in load testing.
- Domain rate limiting and retry backoff are active.
- Managers can find any candidate or pending action within two Telegram commands.
