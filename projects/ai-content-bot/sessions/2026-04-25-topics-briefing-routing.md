# Session 2026-04-25 — Topics Briefing Routing

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Fixed WF-06 routing so `топ тем / темы для постов / briefing` requests call WF-08 instead of WF-07 discovery.
- Made WF-08 callable from WF-06 via `executeWorkflowTrigger`.
- Updated WF-08 to show pending Topics sorted by `score`, default top 7 with minimum 5.
- Added AI Agent tool `show_topic_briefing` as fallback for natural language variants.
- Updated WF-09 numeric topic selection: `создай пост 1` chooses the first topic by score, `создай пост 2` chooses the second, etc.

## Key findings
- The previous behavior saved 30 topics because `run_topic_discovery` was the only topic-related tool and was described too broadly.
- Briefing and discovery must be separate intents:
  - briefing = read existing `Topics` sorted by `score`
  - discovery = scrape/refresh and save new topics

## Blockers
- Local files must be imported into n8n before Telegram behavior changes.

## Next steps
- Import WF-06, WF-08, and WF-09.
- Test `Дай мне топ тем для постов на сегодня`.
- Test `создай пост 1` from the returned list.
