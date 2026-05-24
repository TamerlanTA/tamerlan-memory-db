# Memory Dashboard

## Related
- [[../All about Agents/agent-memory]]
- [[../current-focus]]
- [[../My-tasks]]

## Current status
- 2026-05-24: Local React + Vite + TypeScript MVP created at `/Users/tamerlan/Desktop/PC/memory-dashboard`, outside the Obsidian vault.
- The app reads the real vault at `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB` through a local Express API.
- Dashboard currently shows tasks, project status summaries, latest sessions, current focus, risks, next steps, activity metrics, and rule-based AI suggestions.
- Task add/complete flows write markdown through constrained server functions. MVP write target is `My-tasks.md`.

## Implementation notes
- Safe filesystem rules are implemented in `server/vault.ts`: writes must stay inside the vault and target `.md` files.
- Fixture-vault tests cover dashboard reading, task add/complete markdown writes, and unsafe write rejection.
- Local dev processes:
  - API: `npm run server` on `http://127.0.0.1:8787`
  - UI: `npm run dev -- --port 5173` on `http://127.0.0.1:5173`

## Verification
- `npm run check` passed: TypeScript + Vitest, 3 tests.
- `npm run build` passed.
- Playwright fallback verified the running dashboard against the real vault:
  - 6 metric cards
  - 16 open task rows shown
  - 17 project cards shown
  - desktop and mobile screenshots saved under `qa/`

## Open risks
- The UI has only rule-based suggestions; no LLM/API integration is wired.
- Real-vault add/complete was not exercised with a disposable task to avoid memory spam; fixture tests prove markdown write behavior.
- Vite and dependencies currently report 5 moderate `npm audit` findings; not remediated in this MVP pass.

## Next steps
- Add optional task destination selection beyond `My-tasks.md` if project-local task capture becomes necessary.
- Add richer markdown extraction for project folders with non-canonical FlowOps structures.
- Consider a dedicated session-note writer once the user wants dashboard-driven memory sync, not only task writes.
