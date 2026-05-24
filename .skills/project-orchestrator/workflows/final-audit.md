# Workflow: Final Audit

Use before declaring a milestone complete, shipping to production, handing off to a client, or closing a project phase.

## Audit Inputs

- Original goal and acceptance criteria
- Execution plan
- Changed files
- Review report
- Build/test/lint/typecheck output
- Manual QA notes
- Deployment/env docs
- Current risks and next steps
- Project memory updates

## Audit Checklist

- Goal achieved or clearly marked partial
- Acceptance criteria verified
- Build passes
- Tests pass or failures explained
- Typecheck/lint pass where applicable
- Changed files match expected scope
- User-facing flows manually verified where needed
- Production env/config documented
- Secrets not exposed
- Error states handled
- External integrations tested or marked untested
- Rollback/recovery considered where relevant
- Memory/docs updated
- Handoff can be understood without the full chat

## Final Audit Output

```md
## Final Audit

Verdict: Ready / Ready with risks / Not ready

Completed:
- ...

Validation evidence:
- ...

Changed files:
- ...

Open risks:
- ...

Production/config notes:
- ...

Handoff notes:
- ...

Next action:
...
```
