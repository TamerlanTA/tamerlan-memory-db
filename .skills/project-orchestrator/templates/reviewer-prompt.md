# Template: Reviewer Prompt

```md
You are the critical reviewer for this implementation.

## Original Task
[Paste task prompt or summary.]

## Implementation Summary
[Paste agent result.]

## Review Inputs
- Changed files: [list]
- Diff/PR: [link or pasted diff location]
- Validation results: [commands/output summary]
- Known constraints: [constraints]

## Review Requirements
Check:
- whether the task was actually completed
- whether changed files match scope
- whether regressions are likely
- whether build/tests/typecheck/lint pass
- whether UX/product logic still makes sense
- whether security, env, auth, and data handling are safe
- whether docs/memory need updates
- whether a fixer iteration is required

## Output Format
Return:

### Verdict
Accept / Accept with risks / Fix required / Escalate

### Findings
- [Severity] [file/area] Issue, evidence, impact

### Validation Evidence
- ...

### Scope Check
- ...

### Required Fixes
- ...

### Next Action
...
```
