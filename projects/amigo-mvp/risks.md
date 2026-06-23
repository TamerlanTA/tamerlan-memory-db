# AMIGO MVP — Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]
- [[technical-architecture]]
- [[integrations]]

## Active risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Enterprise ATS forms differ by employer and change without notice | High | High | Versioned employer adapters, fixture tests, connector health checks, manual certification |
| Workday, Oracle, SAP, and Taleo do not offer universal candidate-side submission APIs | High | High | Use hosted forms, support only certified flows, route unsupported forms to `NeedsAction` |
| CAPTCHA, OTP, assessments, or account creation block automation | High | Medium | Never bypass controls; create manager tasks with deep links and preserved context |
| July 5 timeline is too short for broad ATS coverage | High | High | Launch with a narrow certified connector set and measure coverage rather than claiming universality |
| Telegram-only operations become slow at 30 candidates | Medium | High | Add search, ownership filters, pagination, batch actions, and export reports; define web-panel trigger |
| Generated CV contains invented or mistranslated facts | Low | High | Structured output, source-field mapping, validation rules, manager approval, immutable versions, Phase 3.5 structured CV enrichment tables |
| Managers enter weak or incomplete CV enrichment data | Medium | Medium | Use `/candidate_view` readiness warnings, runbook templates, manager review before document approval |
| Candidate portrait is uploaded in unsupported format or poor crop | Medium | Low | JPEG/PNG portraits are embedded into generated CVs; unsupported formats fall back to placeholder, and managers should review final crop/quality before approval |
| Duplicate or excessive applications damage candidate reputation | Medium | High | Idempotency keys, employer/domain limits, prior-application checks, daily caps |
| Career sites block shared datacenter IPs | Medium | High | Slow domain-specific rates, stable sessions, optional compliant proxy budget, manual fallback |
| Candidate personal data is exposed | Low | Critical | Private storage, RLS, least privilege, encrypted secrets, signed URLs, audit log, retention deletion |
| Waitlist activates before operations are stable | High | High | Ten-candidate controlled pilot, launch gates, connector error thresholds, staged 10→20→30 activation |
| Monthly cost exceeds USD 100 | Medium | Medium | PGMQ instead of Redis, bounded browser concurrency, per-service budgets and weekly usage review |
| Insufficient suitable vacancies prevents 5–10 daily applications | Medium | Medium | Report `eligible vacancy shortage` explicitly; never lower hard requirements only to hit volume |
| Candidate edit/close lists apply the `closed` filter after `LIMIT 20` | Medium | Medium | Filter `status != closed` in SQL before limiting; add regression coverage with more than 20 mixed-status candidates |
| Candidate assignment can change between close selection and confirmation | Low | High | Include `assigned_manager_id` in the closing update predicate and require an affected row before writing the audit event |
| Intake accepts a location with an empty country or city | Medium | Medium | Validate both trimmed location parts and add cases for `Kazakhstan,` and `,Almaty` |
| First production CV generation path has not been exercised end-to-end | Medium | High | Run a controlled candidate through `/candidate_documents`; inspect worker logs, generated files, signed URL, and approval status transition |
| OpenAI document model name may differ from configured `gpt-5.4-mini` availability | Medium | High | Verify first production job; if unavailable, set `OPENAI_DOCUMENT_MODEL` to an approved available structured-output model |
| Gotenberg private networking or LibreOffice conversion can fail at runtime | Medium | Medium | Gotenberg service is deployed at `gotenberg.railway.internal`; validate first PDF render and keep failure classified as `validation_failed`/worker error |

## Launch blockers
- No production-certified application connector.
- No end-to-end evidence trail for applications.
- No duplicate prevention.
- No manager approval gate.
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

## Scale-to-30 gates
- At least 95% of jobs finish in a terminal or actionable state.
- Queue lag stays below 30 minutes during daily batch execution.
- No duplicate applications in load testing.
- Domain rate limiting and retry backoff are active.
- Managers can find any candidate or pending action within two Telegram commands.
