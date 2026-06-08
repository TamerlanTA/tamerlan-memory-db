# Notion Office Operating System

## Related
- [[All about Agents/agent-memory|agent-memory]]
- [[current-focus]]
- [[projects/amigo-mvp|AMIGO MVP]]

## Purpose
Notion page `Office` is the shared operating center for managing multiple parallel projects with an assistant.

## Location
- Page: https://app.notion.com/p/3753e026e92f8008a797d3446e02752c

## Structure
- **Проекты**: portfolio status, priority, health, owner, deadline, current phase, next result, and next action.
- **Фазы**: measurable project stages with acceptance criteria, progress, blockers, and approval state.
- **Задачи**: unified execution queue related to projects and phases.
- **Журнал и решения**: notes, decisions, meetings, ideas, risks, and updates.
- **Еженедельный контроль**: weekly progress, blockers, required decisions, next priority, and owner approval.

## Operating rhythm
- Daily: review active work and blocked tasks; keep owners and deadlines current.
- Weekly: assistant updates project health and creates weekly reviews.
- Project completion: close phases only after the expected result is accepted.
- Historical work is retained through completion statuses or archive flags, not deletion.

## Key design decision
The system separates portfolio, phases, tasks, knowledge/decisions, and reviews while connecting them through Notion relations. This keeps daily execution simple without losing management visibility.

## First project
- `AMIGO MVP 1.0` was added on 2026-06-08 as the first active project.
- It validates the full operating model: project, phases, tasks, decisions/risks, and weekly review.
