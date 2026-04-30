# Session 2026-04-30 — Critical Review Fixes

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Updated `/Users/tamerlan/Desktop/storehouse-n8n/workflows/workflow-1-main-ai-agent-photo-recognition.json`.
- Updated `/Users/tamerlan/Desktop/storehouse-n8n/workflows/workflow-2-low-stock-alert.json`.
- Updated `/Users/tamerlan/Desktop/storehouse-n8n/workflows/workflow-3-suspicious-activity-alert.json`.
- Added requested `FIXED:` markers to existing sticky notes.

## Key findings
- WF2 and WF3 each had duplicate outgoing `GET — Last Processed Timestamp` connections; each now has exactly one.
- WF2 and WF3 now use the safe cursor expression:
  `$('GET — Last Processed Timestamp').first()?.json?.last_processed_at ?? new Date(Date.now() - 15 * 60 * 1000).toISOString()`
- WF1 `ERROR — SH Tool Failure Alert` now includes triggering Telegram user first name and chat ID.
- WF1 `ACTION — Download Invoice File Binary` now has no HTTP authentication or credentials configured.

## Blockers
- No live n8n import/smoke test was run in this session.

## Next steps
- Import the three JSON files into n8n and smoke-test WF1/WF2/WF3 against the target credentials and sheets.
