# Session 2026-04-25 — WF06 Answer Callback Payload Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Fixed a real n8n runtime issue found in WF-10 `Parse Action`: it received `{ ok: true, result: true }` from Telegram `Answer Callback`, not `{ action, post_id, chat_id }`.
- Root cause: WF-06 routed `Answer Post Callback` output into `Call WF-10 Post Action`; Telegram callback-answer node replaces the incoming item with Telegram API response.
- Updated WF-06:
  - Added `Prepare WF-10 Post Action`.
  - `Switch Command Route` post_action branch now fans out in parallel:
    - `Answer Post Callback` for Telegram UX only.
    - `Prepare WF-10 Post Action` → `Call WF-10 Post Action` for the actual business payload.
  - Disconnected `Answer Post Callback` from WF-10 call.
- Local simulation confirms:
  - `approve_post_post_1777095673426` → `{ action: "approve", post_id: "post_1777095673426", chat_id: "405182031" }`
  - WF-10 `Parse Action` outputs `action=approve`, not `show`.

## Key findings
- Do not put Telegram `answerCallbackQuery` nodes before business logic when downstream nodes need the original callback payload.
- Callback acknowledgement should be a side branch, not the data path.

## Blockers
- Need to re-import updated WF-06 into n8n.

## Next steps
- Import WF-06 again.
- Test clicking `✅ Publish`.
- In WF-10 `Parse Action`, input should now show `action`, `post_id`, `chat_id`, not `ok/result`.
