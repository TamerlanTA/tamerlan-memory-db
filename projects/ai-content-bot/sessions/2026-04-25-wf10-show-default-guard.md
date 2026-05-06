# Session 2026-04-25 — WF10 Show Default Guard

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- User confirmed approve/skip still invoked WF-10 `show`; WF-10 input showed only `ok/result`.
- Updated WF-06 again:
  - `Switch Command Route` post_action output now goes only to `Prepare WF-10 Post Action`.
  - `Prepare WF-10 Post Action` then fans out to both `Answer Post Callback` and `Call WF-10 Post Action`.
  - `Call WF-10 Post Action` explicitly maps `action`, `post_id`, `chat_id` from prepared JSON.
- Updated WF-10 `Parse Action`:
  - no longer silently defaults to `show` when it receives `{ok,result}` or boolean `result`.
  - throws a clear upstream mapping error if Telegram callback-answer output reaches WF-10.

## Key findings
- The safe topology is:
  `Switch post_action → Prepare WF-10 Post Action → [Answer Callback + Call WF-10]`
- Do not connect `Switch post_action → Answer Callback → Call WF-10`.
- Do not connect `Switch post_action → [Answer Callback + Call WF-10]` if there is any chance the imported graph order in n8n is ambiguous; prepare first is clearer and inspectable.

## Next steps
- Re-import both WF-06 and WF-10.
- Test approve/skip. WF-10 `Parse Action` input must show `action/post_id/chat_id`.
- If WF-10 ever receives `ok/result` again, it will now throw instead of showing another draft.
