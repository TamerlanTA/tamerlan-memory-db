# Prompts

## Related
- [[projects/AI-Powered Woven Label Generator/overview]]
- [[projects/AI-Powered Woven Label Generator/current-state]]
- [[projects/AI-Powered Woven Label Generator/next-steps]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-07-02-block1-review-and-block2-prompt|Block 1 review and Block 2 prompt]]

## Outcome-First Stabilization Prompt Pattern

Use this when directing Claude/Fable-style implementation agents on the Griffes Vivienne reliability work.

Principle:
- Give the agent a production outcome, current known evidence, non-negotiable constraints, and acceptance checks.
- Avoid over-prescribing the exact implementation path unless there is a known hard constraint.
- Ask the agent to inspect, decide, implement, verify, and report tradeoffs.
- Codex reviews the resulting diff/tests before accepting the block.

Reusable frame:
```text
You are taking ownership of the next production-stability block for Griffes Vivienne.

Primary outcome:
<describe the customer/business outcome, not the exact code path>

Current context:
<briefly summarize accepted previous blocks and current residual risks>

Your task:
Audit the current implementation, identify the highest-leverage fixes within this scope, implement the smallest robust solution, and prove it with tests. Use the existing codebase patterns. Do not rewrite unrelated systems.

Non-negotiables:
- Protect paid credits and guest free-trial value.
- Do not show customers clearly broken/off-brand/no-result states.
- Preserve valid-user flow when external validators/providers are temporarily unavailable.
- Keep diagnostics visible enough for admin/root-cause analysis.
- Keep UX errors understandable and action-oriented.

Acceptance:
- Explain what you changed and why.
- Show where the pipeline behavior changed.
- Run focused tests, full tests, and typecheck.
- Report residual risks and what should be monitored after deploy.
- Do not commit or deploy unless explicitly asked.
```
