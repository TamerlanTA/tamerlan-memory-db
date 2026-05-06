# Session 2026-04-25 — Deterministic Router And Approval Fix

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- Reworked the bot flow so critical commands no longer depend on AI Agent interpretation:
  - WF-06 now has `Route Telegram Update` + `Switch Command Route`.
  - `create post ...` / `создай пост ...` routes directly to WF-09 with extracted `topic`, `source_url`, and `chat_id`.
  - `show pending posts` / draft-preview style commands route directly to WF-10 with `action=show`.
  - `approve_post_{post_id}` / `skip_post_{post_id}` callbacks route directly to WF-10 with explicit `action`, `post_id`, and `chat_id`.
  - Only outreach callbacks (`a` / `s`) continue to WF-05.
- Added explicit input schemas to WF-06 AI tools as a fallback improvement.
- Updated WF-05 post callback path:
  - added `Prepare WF-10 Post Action`
  - disconnected local post skip/update path
  - both approve and skip post callbacks now pass through WF-10 with explicit action data.
- Hardened WF-09 topic resolution:
  - extracts URL from input text if `source_url` is missing
  - normalizes URLs and text
  - scores topic matches instead of selecting first row
  - source URL match gets dominant priority
  - prompt now explicitly forbids generic automation case studies when a source URL/article is provided.
- Hardened WF-10:
  - `Parse Action` now parses callback data defensively and throws if approve/skip has no `post_id`
  - added `Prepare WF-11 Publish Payload`
  - WF-11 call now receives current item JSON instead of schema-dependent `workflowInputs`
  - preview includes topic, post_id, and draft counter.
- Hardened WF-11:
  - added `IF: Buffer Configured`
  - if Buffer profile IDs are missing, post status becomes `approved` and Telegram explains Buffer setup is pending
  - if Buffer is configured, it publishes and updates `published` or `error`.
- Updated `create_sheets.gs` post status validation to include `approved`.

## Key findings
- The screenshot issue `approve → WF-10 show` was caused by action data not reliably reaching WF-10. The new flow avoids that by routing callback data in WF-06/WF-05 Code nodes and passing current JSON to Execute Workflow.
- The screenshot issue `VentureBeat URL → generic first topic post` was caused by URL/topic depending on AI tool extraction and weak topic matching. The new WF-06 direct router and WF-09 resolver prioritize source URL.

## Blockers
- Updated local JSON still needs import into n8n.
- Buffer publishing still requires valid direct API credentials/profile IDs. Without them, approval will now be preserved as `approved` instead of silently failing.

## Next steps
- Import in this order: WF-06, WF-05, WF-09, WF-10, WF-11.
- Keep only WF-06 active as Telegram Trigger.
- Test:
  - `Создай пост <VentureBeat URL>` → generated content must match that article headline.
  - click `✅ Publish` → WF-10 must receive `action=approve`, not `show`.
  - with no Buffer profile IDs, `Posts.status` should become `approved` and Telegram should explain Buffer setup.
  - after Buffer profile IDs are configured, approval should publish and set `Posts.status=published`.
