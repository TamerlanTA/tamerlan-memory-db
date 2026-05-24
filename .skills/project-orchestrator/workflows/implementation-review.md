# Workflow: Implementation Review

Use this after an implementation agent reports completion or before accepting a milestone.

## Review Stance

Be critical, concrete, and evidence-based. Do not praise generic effort. Accept only what is verified.

## Required Inputs

- Original task prompt
- Agent completion summary
- Changed files
- Git diff or patch
- Test/build/lint/typecheck output
- Relevant screenshots/logs where user-facing or integration behavior changed
- Known risks and constraints

## Review Steps

1. Compare outcome against objective
   - Was the requested behavior actually implemented?
   - Were all acceptance criteria addressed?
   - Are any requirements missing or only partially done?

2. Check scope discipline
   - Do changed files match expected surface area?
   - Were unrelated files changed?
   - Was architecture replaced without reason?
   - Were speculative features added?

3. Inspect correctness
   - Edge cases
   - Error handling
   - Data shape and migration compatibility
   - Async/race/retry/idempotency behavior
   - API contract consistency

4. Inspect product and UX behavior
   - Does the user workflow still make sense?
   - Are empty/loading/error states covered?
   - Is copy direct and useful?
   - Does the interface remain usable on target screens?

5. Inspect safety
   - Secrets not exposed
   - Auth and permissions respected
   - Sensitive data handled safely
   - Env/config documented
   - Logs avoid leaking private data

6. Inspect validation
   - Build/test/typecheck/lint pass?
   - Failures explained?
   - Manual verification done when automated tests are insufficient?

7. Decide
   - Accept
   - Accept with documented residual risks
   - Request fixer iteration
   - Escalate for architecture/product decision

## Review Output

```md
## Review Report

Verdict: Accept / Accept with risks / Fix required / Escalate

Findings:
- [Severity] File/area: issue and why it matters

Validation evidence:
- ...

Scope check:
- ...

Residual risks:
- ...

Required fixer prompt:
...

Next action:
...
```
