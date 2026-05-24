# Project Orchestrator Skill

## Related
- [[All about Agents/agent-memory]]
- [[All about Agents/routing-rules]]
- [[All about Agents/Skills]]
- [[patterns/batch-prompt-template]]

## Summary

Created a reusable Project Orchestrator Skill package at:

`.skills/project-orchestrator/`

Also installed it as an active local Codex skill at:

`/Users/tamerlan/.codex/skills/project-orchestrator/SKILL.md`

The skill turns an agent into a project control plane for software, automation, SaaS, AI MVP, and client delivery projects. It emphasizes context-first operation, staged execution, strong batch prompts, critical review, scope control, quality gates, risk tracking, and memory sync.

## Key Contents

- `SKILL.md` is the central entrypoint.
- Installed Codex entrypoint is `SKILL.md` with frontmatter name `project-orchestrator`.
- `workflows/` covers intake, execution planning, delegation, implementation review, memory sync, risk control, and final audit.
- `templates/` includes copy-paste-ready prompts and project/status/audit/memory formats.
- `checklists/` covers pre-task, implementation, review, production readiness, and scope control.
- `examples/` includes SaaS/web app, automation workflow, and review examples.

## Usage

Activation prompt:

```md
Use `.skills/project-orchestrator/SKILL.md`.

Act as project orchestrator for this project. Load context first, classify the active stage, identify risks and constraints, then produce the next best execution batch. Include a copy-paste-ready implementation prompt and the validation gates.
```

## Notes

- This should be used for orchestration and quality control, not routine direct coding.
- It pairs naturally with the existing [[patterns/batch-prompt-template]] and the OS LLM routing model in [[All about Agents/routing-rules]].
- For future updates, preserve the central `skill.md` entrypoint and keep workflows/templates modular.
