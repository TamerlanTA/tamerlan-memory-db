# Workflow: Project Intake

Use this before planning, delegating, or reviewing meaningful work.

## Objective

Build a truthful project context map so the orchestrator does not operate from stale assumptions or narrow user wording.

## Inputs To Gather

- User request
- Repository structure
- Existing project memory or docs
- Recent session notes or handoff summaries
- Git status and changed files
- Relevant code modules, workflows, tests, configs, and deployment docs
- Known product/business goal
- Known constraints: budget, deadline, platform, client promise, stack, security, compliance

## Intake Steps

1. Identify project identity
   - Is this an existing project?
   - Is it a one-off task, small project file, or large ongoing project?
   - What is the canonical memory/doc location?

2. Load current state
   - What exists today?
   - What was last completed?
   - What is blocked?
   - What is the next known milestone?

3. Identify active stage
   - Stage 0: audit/context loading
   - Stage 1: foundation/architecture
   - Stage 2: core feature implementation
   - Stage 3: integration
   - Stage 4: UX polish
   - Stage 5: QA/hardening
   - Stage 6: production readiness
   - Stage 7: documentation/handoff

4. Map affected surface area
   - Files/modules likely involved
   - External services or APIs
   - Data models and migrations
   - Auth, permissions, env vars, secrets
   - UI routes and user-facing flows
   - Tests and validation commands

5. Define non-goals
   - What should not be changed?
   - Which architecture should remain intact?
   - Which files are unrelated?
   - Which nice-to-have ideas are out of scope?

6. State uncertainties
   - Missing files
   - Missing credentials
   - Untested assumptions
   - Ambiguous user expectations
   - Stale memory

## Output Format

```md
## Project Intake

Project:
Goal:
Current state:
Active stage:

Relevant context loaded:
- ...

Likely files/systems involved:
- ...

Constraints:
- ...

Out of scope:
- ...

Risks / unknowns:
- ...

Recommended next action:
...
```
