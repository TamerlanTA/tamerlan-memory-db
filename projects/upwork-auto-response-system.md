# Upwork Auto Response System

## Related
- [[All about Agents/agent-memory]]
- [[All about Agents/routing-rules]]
- [[projects/FlowOps Team/Pipeline A — Upwork Radar]]
- [[patterns/project-orchestrator-skill]]

## Goal

Build a highly automated Upwork job response pipeline that detects matching job alerts, retrieves full job details, scores job quality, drafts high-conversion proposals and screening-question answers, and prepares/submits responses through a controlled approval flow.

## Current Status

- 2026-05-24: Project planning started from screenshots of Gmail Upwork job alerts and Upwork proposal flow.
- Existing related memory found: [[projects/FlowOps Team/Pipeline A — Upwork Radar]], with a prior n8n workflow at `/Users/tamerlan/Desktop/flowopsteamPipelines/upwork-radar-workflow.clean-import.json`.
- The old workflow appears to cover radar/import/reconnect steps, not full proposal generation/submission.
- 2026-05-25: Claude Code created `Pipeline A v2 - Upwork Auto Response` in n8n with workflow ID `AukneuPwvXK7xVaw` and local artifacts under `/Users/tamerlan/Desktop/upwork proposals/`.
- Local artifacts include `pipeline-a-v2.workflow.js`, `upwork-browser-server.py`, `google-sheets-schema.md`, `setup-runbook.md`, `test-plan.md`, `risk-rollback-notes.md`, and `setup-sheets.gs`.
- Reported tests passed so far are mostly pinned/synthetic n8n tests: duplicate prevention, reject filter, low score, and high-score dry-run. They are not yet full real Gmail -> full Upwork scrape -> Sheets -> Telegram -> browser submit E2E validation.

## Key Decisions

- Treat fully automatic proposal submission as high-risk until compliance and account-safety implications are accepted.
- 2026-05-24: Tamerlan explicitly accepted the risk for full auto-submit, but requires Telegram notification after every submitted proposal.
- Source of truth: Google Sheets.
- Initial implementation should use available stack only: n8n + browser/MCP + Gmail + Google Sheets + Telegram + LLMs. Do not use paid UpHunt/GigRadar yet.
- Target jobs: n8n, Make, AI agents, full-stack, SaaS, CRM, automation/integrations.
- Reject jobs: design, WordPress, generic low-fit website/design tasks, and similar unrelated work.
- Daily Connects cap: 50.
- Proposal boost: 0 Connects initially.
- Fixed-price strategy: only apply from $300+ unless manually overridden.
- Proposal must include both overview video links:
  - `https://vimeo.com/1182418384?fl=ip&fe=ec`
  - `https://vimeo.com/1184948875?fl=ip&fe=ec`
- Proposal attachment source folders:
  - `/Users/tamerlan/Desktop/TamerlanTAresume/TamerlanCases`
  - `/Users/tamerlan/Desktop/TamerlanTAresume/TamerlanPortfolio`
- Telegram notification chat ID: `405182031`.
- Telegram bot token was provided in chat on 2026-05-24; do not store it in memory or source files. Configure it as an n8n credential or env var `TELEGRAM_BOT_TOKEN`.
- Proposal style must follow Tamerlan's core template: client problem first, real challenge, systems thinking, one controlled-confidence line, video slot, timeline + estimate, short close.
- Proposal must be English only, max 1 emoji, no long walls, no excessive bullets, no generic AI enthusiasm, no "I'm perfect for this" fluff, no em dash symbol.
- Profile highlights should be selected from relevant completed/in-progress Upwork jobs and portfolio proof, especially AI Automation Expert for Research & Lead Pipeline, AI-Powered Woven Label Design Tool, Jotform/Zapier/ClickUp Automation, WhatsApp AI Bot, FlowOps Client Acquisition OS, Pipeline C, and AI automation portfolio examples.

## Risks

- Upwork TOS/API restrictions: scraping, browser plugins, and unauthorized automation can create account risk.
- Connects are paid/limited; bad scoring could burn budget fast.
- Generic AI proposals can lower reply rate; proposal engine must use Tamerlan-specific proof, case studies, and job-specific hooks.
- Proposal form structure may change; browser automation requires monitoring and fallback.
- Full job details and screening questions may require authenticated Upwork access.
- Full auto-submit requires strict guardrails: daily Connects budget, duplicate prevention, scoring threshold, reject categories, Telegram notification, and emergency kill switch.
- Telegram bot token was exposed in chat; consider rotating it after setup if this chat or logs may be shared.
- Critical implementation gap: n8n cloud cannot call `http://localhost:8765` on Tamerlan's Mac. Auto-submit requires either local n8n, a secure tunnel to the browser server, or a browser automation host reachable from n8n.
- Critical guardrail gap: current workflow does not appear to update `connects_used_today` after successful submission, so the daily 50 Connects cap can drift.
- Critical guardrail gap: current auto-submit gate checks score/connects but does not appear to enforce fixed-price budget >= $300.
- Browser server currently fills cover letter, bid, and some screening textareas, but does not yet implement attachments, profile highlights, duration/milestones, or robust Upwork React-controlled field verification.
- If a tunnel is used for browser server, it must require an auth header/token; otherwise a public endpoint could submit proposals.

## Next Steps

0. 2026-05-25 focus: finish implementation for Tamerlan's own use by closing P0 guardrails, proving a real dry-run E2E path, and preparing one controlled live submit only after evidence is reviewed.
1. Do not enable live `auto_submit_enabled=true` until P0 gaps are fixed and one controlled live test passes.
2. Fix n8n cloud -> browser server connectivity: use local n8n or a secure tunnel URL with auth header, not raw `localhost`.
3. Add guardrails to workflow: enforce `min_fixed_budget >= 300`, update `connects_used_today` after success, add reset workflow or daily reset schedule.
4. Extend browser server to handle profile highlights, attachments, duration/milestones/project terms, and verify React field values before submit.
5. Run real dry-run E2E using a real Gmail Upwork alert and real Sheets/Telegram writes.
6. Run one controlled live submit only after dry-run evidence is reviewed.
