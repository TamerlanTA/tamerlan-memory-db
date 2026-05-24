# Workflow: Risk Control

Use this before risky implementation, after review findings, or when the project seems to drift.

## Risk Categories

- Scope drift
- Architecture churn
- Missing context
- Untested assumptions
- Broken build/test pipeline
- Data loss or migration risk
- Secret/env exposure
- Auth/permissions failure
- External API instability
- Cost/rate-limit risk for AI products
- Client promise mismatch
- UX regression
- Automation loop, duplicate send, or idempotency failure

## Risk Control Steps

1. Name the risk in plain language.
2. Identify trigger and impact.
3. Separate verified facts from assumptions.
4. Define mitigation.
5. Decide whether to proceed, pause, or escalate.
6. Record the risk in memory if it affects future work.

## Risk Register Format

```md
| Risk | Evidence | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|
| Duplicate outbound messages in workflow | Approval gate not verified | Client trust / spam risk | Add idempotency key and manual approval test | Implementation agent | Open |
```

## Common Stop Conditions

Pause or escalate when:
- task requires credentials the agent does not have
- migration may destroy or rewrite production data
- requested change conflicts with known project decisions
- acceptance criteria are unclear and multiple product directions are possible
- build is broken before changes and baseline is unknown
- implementation would require replacing core architecture
- secrets are visible in code or logs

## Scope Drift Response

```md
This is out of scope for the current batch because [reason]. I recommend parking it as a future task unless it is required for the current acceptance criteria.
```
