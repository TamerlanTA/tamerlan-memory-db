# Current Focus

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[projects/AI-Powered Woven Label Generator/current-state|AI-Powered Woven Label Generator — current state]]
- [[projects/AI-Powered Woven Label Generator/next-steps|AI-Powered Woven Label Generator — next steps]]

---

## Active project (as of 2026-04-15)

**AI-Powered Woven Label Generator** — client: Griffes Vivienne

### Status
Post-Milestone-5 polish. All 5 milestones functionally complete.
Active branch: `milestone4-auth-completion`
Latest pushed commit: `0a658ea` — `Add reliable preorder confirmation emails`

### What was last completed
- Header system refinement (desktop + mobile), brand logo asset added
- Pre-order confirmation emails via Resend (transactional, delivery tracked on DB)
- Guest email capture at order boundary
- Conversion polish: email gate, unit tests, translations (FR + EN)
- DB migration `0012_preorder_confirmation_email.sql` applied to Railway MySQL

### Immediate blockers / next actions
1. Set `RESEND_API_KEY` + `RESEND_FROM_EMAIL` in production env
2. Redeploy after Resend env setup
3. Run live preorder test → confirm email delivery
4. Rotate Railway DB credential (URL was exposed in chat)
5. Browser-based visual QA: desktop Home, Prepare, Result, My Account + mobile Home
6. Confirm desktop header approved by client after restoration pass
7. Fix `~/.codex/AGENTS.md` vault path (currently points to wrong nested path)

---

## Secondary / watch
- **FlowOps Team** — агентство AI automation. Статус на 2026-05-03: CRM система создана; Pipeline B / LinkedIn Pain Radar завершён. Следующие задачи вести от состояния готовой CRM: QA/валидация, production-safe automation wiring, Demo Library, Upwork Radar, Website Audit Generator. См. [[projects/FlowOps Team/00 - Overview]]
- **AI Content Bot** — Telegram бот (@FlowOpstg_bot) для генерации и публикации контента (WF-06..WF-12). Статус: WF-09 Gemini image gen ✅, WF-06 callback routing ✅, WF-10 inline кнопки ✅. Блокер: WF-11 ID нужен для финального флоу. См. [[projects/ai-content-bot/overview]]
- **LinkedIn Outreach Automation** — n8n воркфлоу для личного LinkedIn (WF-00..WF-05). Статус: WF-05 переработан. См. [[projects/linkedin-automation]]
- Upwork freelance work (automation / integrations — episodic)
- Knowledge building: Firecrawl, n8n patterns (see `knowledge/`)
