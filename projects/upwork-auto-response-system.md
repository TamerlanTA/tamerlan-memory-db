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

## Next Steps

1. Audit/import the existing Upwork Radar n8n workflow and decide whether to extend or rebuild.
2. Build Google Sheets schema for jobs, scoring, generated proposals, submissions, profile highlights, errors, and settings.
3. Implement Gmail alert ingestion, full job detail retrieval, screening question extraction, scoring, proposal generation, and Telegram notification.
4. Implement browser/MCP proposal submission with strict safeguards: score >=85, target category match, reject category absence, daily Connects <=50, no duplicates, required fields present.
5. Add monitoring, runbook, manual kill switch, and failure notifications.
6. Configure Telegram credential securely in n8n; do not commit or paste bot token into workflow JSON.
