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
| Generated CV contains invented or mistranslated facts | Medium | High | Structured output, source-field mapping, validation rules, manager approval, immutable versions |
| Duplicate or excessive applications damage candidate reputation | Medium | High | Idempotency keys, employer/domain limits, prior-application checks, daily caps |
| Career sites block shared datacenter IPs | Medium | High | Slow domain-specific rates, stable sessions, optional compliant proxy budget, manual fallback |
| Candidate personal data is exposed | Low | Critical | Private storage, RLS, least privilege, encrypted secrets, signed URLs, audit log, retention deletion |
| Waitlist activates before operations are stable | High | High | Ten-candidate controlled pilot, launch gates, connector error thresholds, staged 10→20→30 activation |
| Monthly cost exceeds USD 100 | Medium | Medium | PGMQ instead of Redis, bounded browser concurrency, per-service budgets and weekly usage review |
| Insufficient suitable vacancies prevents 5–10 daily applications | Medium | Medium | Report `eligible vacancy shortage` explicitly; never lower hard requirements only to hit volume |

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

## Scale-to-30 gates
- At least 95% of jobs finish in a terminal or actionable state.
- Queue lag stays below 30 minutes during daily batch execution.
- No duplicate applications in load testing.
- Domain rate limiting and retry backoff are active.
- Managers can find any candidate or pending action within two Telegram commands.
