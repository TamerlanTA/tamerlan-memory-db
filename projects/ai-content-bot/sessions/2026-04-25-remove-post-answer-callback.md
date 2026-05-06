# Session 2026-04-25 — Remove Post Answer Callback

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- User reported WF-10 still receives Telegram `{ok,result}` and throws the new guard error.
- Removed `Answer Post Callback` from the post approve/skip data path entirely in WF-06.
- Current WF-06 post_action topology:
  - `Switch Command Route` → `Prepare WF-10 Post Action` → `Call WF-10 Post Action`
  - `Answer Post Callback` remains orphaned/disconnected.

## Key findings
- Parallel callback answer still risks confusion in n8n UI/imported graph. The safest production path is no `answerCallbackQuery` before WF-10.
- Telegram may show button loading briefly, but WF-10/WF-11 will send the real confirmation message.

## Next steps
- Re-import WF-06 only.
- In n8n canvas, confirm `Answer Post Callback` has no outgoing/incoming path from post_action branch.
- Test approve/skip again. WF-10 input should be `{action, post_id, chat_id}`.
