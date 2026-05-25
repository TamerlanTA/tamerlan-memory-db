# Upwork Auto Response System

## Related
- [[All about Agents/agent-memory]]
- [[All about Agents/routing-rules]]
- [[projects/FlowOps Team/Pipeline A — Upwork Radar]]
- [[patterns/project-orchestrator-skill]]

## Goal

Build a highly automated Upwork job response pipeline that detects matching job alerts, retrieves full job details, scores job quality, drafts high-conversion proposals and screening-question answers, and prepares/submits responses through a controlled approval flow.

## Current Status

- 2026-05-24: Project planning started.
- 2026-05-25 (session 1): Claude Code created `Pipeline A v2 - Upwork Auto Response` in n8n, workflow ID `AukneuPwvXK7xVaw`. Local artifacts under `/Users/tamerlan/Desktop/upwork proposals/`. Pinned synthetic tests 1-4 passed.
- 2026-05-25 (session 2): All P0/P1 gaps closed (see Key Decisions). Workflow re-deployed at 31 nodes. Browser server rewritten with auth, React-aware fill, profile highlights, CDP attachments, pre-submit verify. Daily reset workflow created at `zuidpv2R4fErdB0X`.
- **Blocker**: Sheets tabs not yet created (user must run `setup-sheets.gs`), n8n credentials + workflow variables not yet configured, tunnel URL not set.
- **auto_submit_enabled = false. Must stay false until Test 10 controlled live submit passes.**

## Key Decisions

- Treat fully automatic proposal submission as high-risk until compliance and account-safety implications are accepted.
- 2026-05-24: Tamerlan explicitly accepted the risk for full auto-submit, but requires Telegram notification after every submitted proposal.
- Source of truth: Google Sheets (sheet ID `1L7qL5L8210jCxkHUOLiLyCjuZDpA-XUgZs-FYTInOCA`).
- Initial implementation: n8n + browser-harness + Gmail + Google Sheets + Telegram + LLMs. No paid UpHunt/GigRadar yet.
- Target jobs: n8n, Make, AI agents, full-stack, SaaS, CRM, automation/integrations.
- Reject jobs: design, WordPress, Wix, Squarespace, logo, branding, Figma-only, generic redesign.
- Daily Connects cap: 50. Proposal boost: 0 Connects initially.
- Fixed-price minimum: $300 (enforced in `Check Auto-Submit Gate`).
- Both Vimeo video links must be in every proposal: `https://vimeo.com/1182418384?fl=ip&fe=ec` and `https://vimeo.com/1184948875?fl=ip&fe=ec`.
- Attachment files: `~/Desktop/TamerlanTAresume/TamerlanCases.png` and `TamerlanPortfolio.png` (PNG only — no PDFs, no contact info).
- Telegram notification chat ID: `405182031`. Bot token: n8n credential only (never in source/memory).
- Proposal: English only, max 1 emoji, no em dash, no generic fluff, Tamerlan template strictly.
- Browser submit URL is configurable via settings sheet key `browser_submit_url` (supports tunnel).
- `BROWSER_SERVER_TOKEN` and `FIRECRAWL_API_KEY` stored only as n8n workflow variables (`$vars.*`).

## Resolved Risks (session 2)

- ~~n8n cloud cannot call localhost:8765~~ → `browser_submit_url` setting in Sheets; tunnel URL goes there; `Trigger Browser Submit` uses `$json.submit_url` + `Authorization: Bearer $vars.BROWSER_SERVER_TOKEN`.
- ~~connects_used_today not updated after submit~~ → `Compute New Connects` + `Update Connects Counter` nodes added; daily reset workflow `zuidpv2R4fErdB0X` runs at 00:00 Almaty (19:00 UTC).
- ~~no fixed-price budget check~~ → `Check Auto-Submit Gate` now blocks fixed-price jobs below `min_fixed_budget` ($300 default).
- ~~browser server no auth~~ → `_check_auth()` enforces `Authorization: Bearer <token>`; 401 on mismatch; `/health` stays open.
- ~~browser server no attachments/highlights/React verify~~ → All implemented: React native setter + event dispatch, CDP `DOM.setFileInputFiles`, profile highlight checkbox selector, pre-submit cover-letter length check, screenshots at all key steps.

## Active Risks

- Upwork TOS: scraping and browser automation can create account risk.
- Proposal form structure may change; browser automation requires monitoring.
- Full job details may require authenticated Upwork session; Firecrawl may return incomplete data.
- `connects_used_today` tracking requires the daily reset workflow to actually be active (must publish `zuidpv2R4fErdB0X`).
- Tunnel endpoint must be kept private; `BROWSER_SERVER_TOKEN` must be rotated if exposed.
- Profile highlights click logic is best-effort (looks for text match); Upwork form may not always expose this section.
- Telegram bot token was briefly exposed in session 1 chat — consider rotating.

## Next Steps (as of 2026-05-25 session 2)

**User actions needed before any live test:**
1. Run `setup-sheets.gs` in Google Apps Script (Tools → Apps Script → Run `setup()`) to create 5 Sheets tabs.
2. Set n8n credentials: Gmail OAuth2 API, Google Sheets account, OpenAI account, Telegram account.
3. Set n8n workflow variables: `FIRECRAWL_API_KEY` and `BROWSER_SERVER_TOKEN` (Settings → Variables).
4. Set up Cloudflare Tunnel (`cloudflared tunnel --url http://localhost:8765`) or ngrok; update `browser_submit_url` in the settings sheet with the public URL.
5. Restart browser server with token: `export BROWSER_SERVER_TOKEN=<same-token-as-n8n-var> && python3 upwork-browser-server.py`.
6. Publish the daily reset workflow `zuidpv2R4fErdB0X` in n8n.

**Tests to run:**
7. Test 7: `curl http://localhost:8765/health` → confirm `"auth": "token_set"` and both attachments listed.
8. Test 7b: `curl -X POST http://localhost:8765/submit-proposal -d '{}'` → confirm 401.
9. Test 9: Full dry-run E2E — let a real Gmail Upwork alert trigger the workflow with `auto_submit_enabled=false`. Verify Telegram "PROPOSAL READY" message, jobs sheet row, proposal text.
10. Test 10: Controlled live submit — only after Test 9 passes. Set `auto_submit_enabled=true`, let one real high-scoring job submit. Verify Telegram "SUBMITTED", submissions sheet row, screenshot, Upwork "Submitted Proposals" page.

**Do not enable auto_submit_enabled=true until Test 9 passes and Test 10 is intentional.**
