# Session 2026-07-03 — Next Automation Layer Decision

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]
- [[risks]]
- [[phase-6-execution-plan]]

## What was done
- Reviewed Phase 6 execution rules, current application adapter code, worker routing, and production adapter/source state.
- Checked production DB for active `mailto:` vacancies and configured `career_sources.application_adapter` values.
- Recorded the next automation layer decision as D-018 in [[decisions]].

## Key findings
- `manual-deep-link-v1` remains the only production execution mode currently routed by `worker-applications`.
- `email-apply-v1` exists locally as a dry-run-default adapter, but `worker-applications` does not yet route it.
- Production check on 2026-07-03 found `0` active `mailto:` vacancies and all `85` career sources have `application_adapter = null`.
- Universal ATS/form auto-submit remains explicitly unsafe and out of scope without narrow certification.

## Decision
- Next automation layer is certification-gated `email-apply-v1` / adapter readiness, not live universal auto-submit.
- Build dry-run/feature-flag worker support and adapter eligibility reporting first.
- Keep live sending disabled until source-level enablement, sender config, rate limits, duplicate prevention, and controlled evidence review are complete.

## Blockers
- No current production `mailto:` vacancy supply, so live email apply cannot improve current daily volume yet.
- Source-level adapter configuration is not populated.

## Next steps
- Add `email-apply-v1` dry-run execution mode to `worker-applications`.
- Persist dry-run evidence and keep status actionable without marking real `applied`.
- Add reporting for manual-only vs email-capable vs future adapter candidates.
- Add import/source-level adapter configuration support and then search for real email-apply sources.
