# Template: Fixer Prompt

```md
You are the fixer agent. Address only the review findings below.

## Context
- Project: [project]
- Original objective: [objective]
- Current implementation state: [summary]

## Review Findings To Fix
1. [finding with file/area and expected correction]
2. [finding]

## Files To Inspect First
- [file]
- [test file]

## Constraints
- Do not rewrite unrelated code.
- Do not add new features.
- Preserve behavior that already passed review.
- Keep changes minimal and targeted.
- Preserve unrelated user changes.

## Validation
Run:
- [command]
- [command]

## Expected Output
Return:
- Fix summary
- Changed files
- Validation results
- Any remaining risks or untested areas
```
