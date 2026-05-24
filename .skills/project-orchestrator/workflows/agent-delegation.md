# Workflow: Agent Delegation

Use this to create strong prompts for implementation, research, review, or fixer agents.

## Delegation Principle

Give an agent enough context to succeed without dumping the whole project. Be explicit about objective, scope, validation, and output.

Prefer batch prompts that combine:
- implementation
- validation
- error handling
- tests/builds
- changed file reporting
- residual risk notes

## Required Prompt Sections

- Role
- Objective
- Project context
- Files/directories to inspect first
- Exact changes required
- Constraints
- Out of scope
- Validation commands
- Acceptance criteria
- Risk notes
- Expected output format

Use [Agent task prompt](../templates/agent-task-prompt.md) for copy-paste-ready prompts.

## Delegation Rules

- Do not ask an implementation agent to make broad improvements without boundaries.
- Do not hide risks from the agent.
- Do not ask for "production ready" unless production gates are defined.
- Tell the agent to read before editing.
- Tell the agent to preserve unrelated changes.
- Tell the agent to report changed files and tests run.
- Tell the agent to state what was not tested.

## Batch Sizing

Good batch:
- coherent objective
- one owner
- clear affected area
- validation possible in one pass

Too large:
- mixes unrelated product features
- requires unresolved architecture decisions
- depends on credentials or manual access the agent lacks
- spans too many services without staged checkpoints

## Output

Return the prompt only, or return:

~~~md
Recommended agent:
Reason:
Prompt:
```md
...
```
~~~
