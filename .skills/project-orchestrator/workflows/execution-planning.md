# Workflow: Execution Planning

Use this when a goal is too large, risky, or ambiguous for a single direct implementation.

## Planning Principle

Plan only enough structure to protect delivery. Avoid process theater. A small bug fix may need one batch; a product milestone may need staged execution and review gates.

## Default Stage Model

### Stage 0: Project Audit / Context Loading
- Read memory/docs
- Inspect repo structure
- Identify current behavior and gaps
- Confirm stack, commands, constraints, and affected files

### Stage 1: Foundation / Architecture
- Data model, routing, integration boundaries, core services
- Technical decisions and tradeoffs
- Migration or env requirements
- Minimal scaffolding needed for future work

### Stage 2: Core Feature Implementation
- Main user or business workflow
- API/backend logic
- UI or automation workflow
- Error handling at system boundaries

### Stage 3: Integration
- Connect frontend/backend/workflows/services
- Add auth, permissions, data persistence
- Validate external service payloads and failure modes

### Stage 4: UX Polish
- Empty/loading/error states
- Responsive behavior
- Copy clarity
- Operational usability for repeated workflows

### Stage 5: QA / Hardening
- Tests, lint, typecheck, build
- Edge cases and regression checks
- Logs and observability where needed
- Security and data safety review

### Stage 6: Production Readiness
- Env vars and secrets documented
- Migrations ready
- Deployment path clear
- Rollback or recovery considered
- Manual acceptance checklist ready

### Stage 7: Documentation / Handoff
- Updated project memory
- Changed files summary
- Remaining risks
- Next steps
- Owner instructions

## Plan Output

```md
## Execution Plan

Goal:
Active stage:
Recommended path:

### Batch 1: [name]
Objective:
Files/systems:
Actions:
Validation:
Risks:
Exit criteria:

### Batch 2: [name]
...

Immediate next action:
...
```

## Planning Heuristics

- Put unknown discovery before irreversible implementation.
- Put data model changes before UI that depends on them.
- Put integrations behind clear validation and logs.
- For client work, preserve promised behavior before adding polish.
- For automation workflows, validate triggers, idempotency, payload shape, retries, and approval gates.
- For AI products, validate prompt inputs/outputs, fallback behavior, cost/rate limits, and user trust.
- For SaaS/web apps, validate auth, permissions, state persistence, responsive UI, and production config.
