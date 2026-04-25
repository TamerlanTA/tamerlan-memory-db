# Session 2026-04-25 — Full JSON Audit And Logic Fixes

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Audited all local n8n JSON workflow files in `/Users/tamerlan/Desktop/linkedin automation/` for JSON validity, broken connections, leftover placeholders, Code-node syntax errors, and core logic gaps.
- Fixed WF-00 upsert matching so Lead Discovery deduplicates by `linkedin_url`.
- Fixed WF-01 Daily Outreach:
  - corrected broken `=={{` expression in `Build Prompt1`
  - restored Sourcegeek-safe 180 character connection note limit
  - fixed `Update Leads Status1` so it updates `Leads` by `linkedin_url` instead of incorrectly targeting `Stats`
  - hardened AI JSON parsing fallback and truncation.
- Fixed WF-02/WF-03/WF-04 placeholders to use the real Google Sheet ID and Telegram chat ID; converted WF-02 risky Set/spread/output-path logic into Code nodes.
- Fixed WF-05 so it is callable from WF-06 only:
  - removed the extra Telegram Trigger from the local export
  - set local export `active=false`
  - made callback parsing pass explicit `{action, post_id, chat_id}` into WF-10.
- Fixed WF-06 callback detection to use a boolean callback check.
- Fixed WF-09 Content Generation:
  - added `Read Topics` and `Resolve Topic`
  - supports matching user text against `Topics` before generation
  - safely handles empty `source_url`
  - marks the resolved topic URL as `used`
  - sends Telegram inline buttons directly on the generated post preview.
- Fixed WF-10 Post Approval:
  - Telegram preview now includes real inline buttons
  - approve path reads by `post_id`, not incorrect `status=approve`
  - passes post payload explicitly into WF-11.
- Fixed WF-11 Publishing:
  - builds a real Buffer JSON request body instead of an empty body
  - updates `Posts` to `published` or `error`
  - requires Buffer `profile_ids` via input or `$env.BUFFER_PROFILE_IDS`
  - fails explicitly instead of silently marking broken publishes as success.
- Updated `create_sheets.gs` to create required `Posts` and `Topics` sheets and add missing Queue columns.

## Key findings
- Local JSON now passes basic checks: JSON parse, connection target/source integrity, no `YOUR_*` / `REPLACE_WITH_*` placeholders, and Code-node syntax validation.
- The main internal logic gaps from [[risks]] R-01/R-07 were addressed in local files.
- Buffer remains externally blocked: the token currently stored in memory/API test returns `401 OIDC tokens are not accepted for direct API access`, and real Buffer profile IDs are still needed.

## Blockers
- Need a valid Buffer API access token that works with direct API calls, or switch WF-11 to an authenticated Buffer/n8n credential flow.
- Need Buffer profile IDs and set them as `BUFFER_PROFILE_IDS` in n8n env or pass/hardcode them into WF-11.
- The updated workflow files still need to be imported into n8n and tested end-to-end.

## Next steps
- Import updated WF files, especially WF-05, WF-06, WF-09, WF-10, WF-11.
- Run `create_sheets.gs` or manually ensure `Posts`, `Topics`, and expanded `Queue` columns exist.
- Configure Buffer token/profile IDs, then test `create post → Telegram buttons → approve → WF-11 → Buffer → Posts status`.
- Keep only WF-06 active as Telegram Trigger; do not activate any Telegram Trigger inside WF-05.
