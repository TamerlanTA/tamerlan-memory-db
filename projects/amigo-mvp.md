# AMIGO MVP

## Related
- [[current-focus]]
- [[knowledge/notion-office-operating-system|Notion Office Operating System]]

## Goal
Build an MVP automated job-search platform through Telegram by 2026-07-05.

## Notion
- Project: https://app.notion.com/p/3793e026e92f813f838be7212aa1d8a5
- Office: https://app.notion.com/p/3753e026e92f8008a797d3446e02752c

## Current status
- Status: Active
- Health: Green
- Priority: P0
- Dates: 2026-06-08 to 2026-07-05
- Current phase: Basic infrastructure
- Notion plan contains 10 phases, 33 tasks, 5 decision/risk records, and the initial weekly review.

## Scope decisions
- Core search, filtering, and application flow is deterministic and algorithm-first.
- LLM is limited to consulting, resume help, recommendations, and statistics explanation.
- MVP vacancy sources are Greenhouse and Lever; Email Apply is also supported.
- LinkedIn, Indeed, multi-step ATS, CAPTCHA bypass, tests, video interviews, tailored cover letters, and complex AI agents are excluded.

## Key risks
- Greenhouse and Lever forms vary and may contain unsupported questions or anti-bot controls.
- The four-week schedule is aggressive for two connectors plus auto-apply.
- Unsupported or unsafe forms must be marked `Skipped`; protective controls must not be bypassed.

## Immediate next steps
1. Approve technical stack and architecture.
2. Create repository, environments, and backend skeleton.
3. Implement database schema and Telegram authentication.
4. Complete API foundation by 2026-06-12.
5. Run the first weekly review on 2026-06-12.
