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
- 2026-05-24 late: UI/UX reworked into a clearer morning command center after user rejected the first MVP layout as confusing. The dashboard now prioritizes a Codex morning brief, next execution task, project curator, activity summary, and recommendations.
- Codex automation `Memory Dashboard Morning Brief` is active and scheduled for 09:00 daily. It updates `dashboard/ai-brief.md`, which the UI reads as the main morning briefing source.

## Implementation notes
- Safe filesystem rules are implemented in `server/vault.ts`: writes must stay inside the vault and target `.md` files.
- Fixture-vault tests cover dashboard reading, task add/complete markdown writes, and unsafe write rejection.
- UI redesign follows `ui-ux-pro-max` guidance: operational dashboard, neutral/monochrome base, blue/green/amber status colors, Fira Code/Fira Sans, strong hierarchy, no horizontal overflow.
- `server/vault.ts` now reads `dashboard/ai-brief.md` and extracts curated sections instead of showing only rule-based suggestions.
- Project scoring was adjusted to prioritize projects with actionable next steps and risks over projects with many old session notes.
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
- 2026-05-24 redesign verification: `npm run check` passed, `npm run build` passed, Playwright verified desktop `1440x1100` and mobile `390x1100` with no horizontal overflow. Screenshots saved:
  - `/Users/tamerlan/Desktop/PC/memory-dashboard/qa/dashboard-redesign-desktop-verified.png`
  - `/Users/tamerlan/Desktop/PC/memory-dashboard/qa/dashboard-redesign-mobile-verified.png`

## Open risks
- The UI reads a Codex-generated markdown brief, but there is not yet a manual in-app "Run morning scan" button.
- Real-vault add/complete was not exercised with a disposable task to avoid memory spam; fixture tests prove markdown write behavior.
- Vite and dependencies currently report 5 moderate `npm audit` findings; not remediated in this MVP pass.
- Some older project notes use non-canonical structures, so their summaries may still need additional parsing rules.

## Next steps
- Add optional task destination selection beyond `My-tasks.md` if project-local task capture becomes necessary.
- Add richer markdown extraction for project folders with non-canonical FlowOps structures.
- Consider a dedicated session-note writer once the user wants dashboard-driven memory sync, not only task writes.
- Add a manual "run scan / refresh AI brief" flow if Codex exposes a callable automation trigger from the app or CLI.
