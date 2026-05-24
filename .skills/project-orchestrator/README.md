# Project Orchestrator Skill

Reusable skill package for turning an AI agent into a disciplined project orchestrator, technical cofounder assistant, execution manager, prompt engineer, reviewer, and memory keeper.

## What It Is For

Use this skill for:
- SaaS and web app builds
- automation workflows in n8n, Make, Zapier, Airtable, Linear, CRM, or internal ops tools
- AI product MVPs
- client delivery projects
- multi-agent execution where one agent plans and another implements
- final review before shipping

## What It Enforces

- Context before action
- Staged execution instead of random scope drift
- Batch prompts for implementation agents
- Critical review discipline
- Scope control
- Risk tracking
- Memory updates
- Honest verification standards
- Copy-paste execution, review, audit, and handoff templates

## File Structure

```txt
.skills/project-orchestrator/
  skill.md
  README.md
  workflows/
  templates/
  checklists/
  examples/
```

Start with [SKILL.md](SKILL.md). Then open only the workflow or template needed for the current task.

## Recommended Use

```md
Use `.skills/project-orchestrator/SKILL.md`.

Act as project orchestrator for this project. Load context first, classify the active stage, identify risks and constraints, then produce the next best execution batch. Include a copy-paste-ready implementation prompt and the validation gates.
```

## Best Fit

This skill works best when paired with:
- a coding agent that can edit files and run tests
- a memory vault or project docs folder
- clear project goals and acceptance criteria
- a reviewer/fixer loop for risky changes

It is still useful without those pieces, but the orchestrator must mark missing evidence clearly.
