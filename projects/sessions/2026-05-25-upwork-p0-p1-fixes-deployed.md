# Session 2026-05-25 — Upwork P0/P1 Fixes Deployed

## Related
- [[upwork-auto-response-system]]

## What was done

- Deployed updated Pipeline A v2 workflow to n8n (`AukneuPwvXK7xVaw`, 31 nodes)
- **P0 fixed: tunnel connectivity** — `Check Auto-Submit Gate` reads `browser_submit_url` from settings sheet; `Trigger Browser Submit` uses `$json.submit_url` + `Authorization: Bearer $vars.BROWSER_SERVER_TOKEN`
- **P0 fixed: fixed-price budget gate** — rejects fixed-price jobs below `min_fixed_budget` ($300 default) with block reason in proposal record
- **P0 fixed: connects tracking** — `Compute New Connects` + `Update Connects Counter` nodes added after submit; created daily reset workflow `zuidpv2R4fErdB0X` (cron: 19:00 UTC = 00:00 Almaty)
- **P1 fixed: browser server rewrite** — token auth (`BROWSER_SERVER_TOKEN` env var, 401 on mismatch), React-aware native setter + event dispatch, profile highlight click selection, CDP `DOM.setFileInputFiles` for attachment upload, pre-submit cover letter length verification, screenshots at steps 01_job_page / 02_proposal_form / 03_before_submit / 04_after_submit
- Ran auth tests: no-token → 401 ✓, wrong-token → 401 ✓, /health → 200 with `auth: token_set` ✓
- Both attachment files confirmed present: `TamerlanCases.png`, `TamerlanPortfolio.png`
- Browser server running on port 8765 (dev mode, no token — set env var before live use)

## Key findings

- Browser server binds to `0.0.0.0` for tunnel compatibility
- Daily reset workflow uses cron `0 19 * * *` (UTC) = 00:00 Asia/Almaty
- `computeNewConnects` reads from `$('Prepare Submission Row')` + `$('Prepare Submit Payload')` explicitly — not `$input`; avoids stale data if Sheets passthrough changes
- `notifySubmissionResult` also reads explicitly from `$('Prepare Submission Row')` and `$('Prepare Submit Payload')`

## Blockers

- **User must complete** before any live test:
  1. Run `setup-sheets.gs` to create Google Sheets tabs
  2. Set n8n credentials (Gmail, Sheets, OpenAI, Telegram)
  3. Set n8n workflow variables: `FIRECRAWL_API_KEY`, `BROWSER_SERVER_TOKEN`
  4. Set up tunnel (Cloudflare/ngrok), update `browser_submit_url` in settings sheet
  5. Restart browser server with `export BROWSER_SERVER_TOKEN=<token>`
  6. Publish daily reset workflow `zuidpv2R4fErdB0X`

## Next steps

- Test 7: health check with token set → confirm `auth: token_set` + both attachments
- Test 9: real Gmail dry-run E2E with `auto_submit_enabled=false`
- Test 10: controlled live submit (only after Test 9 verified)
- `auto_submit_enabled` must stay `false` until Test 10 is deliberately enabled
