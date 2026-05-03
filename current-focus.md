# Current Focus

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team — overview]]
- [[Linear/Linear Ops Automation System/overview|Linear Ops Automation System]]
- [[projects/AI-Powered Woven Label Generator/current-state|AI-Powered Woven Label Generator — current state]]

---

## Active project (as of 2026-05-03)

**FlowOps Team** — agency operating system + Linear execution layer

### Status
FlowOps is now the active operating focus. The CRM system exists, Pipeline B / LinkedIn Pain Radar is complete, and Linear has been populated with detailed FlowOps execution issues.

### What was last completed
- FlowOps Linear projects, labels, and issues were created and rewritten with detailed context and acceptance criteria.
- Linear Ops Automation System was specified in Obsidian memory and linked from [[My-tasks]].
- FlowOps CRM is treated as created; future work starts from QA, validation, data hygiene, and production-safe automation wiring.
- Pipeline B / LinkedIn Pain Radar is treated as complete; future work is operational QA and iteration, not initial build.

### Immediate blockers / next actions
1. Build or prototype the Linear Ops Automation System from [[Linear/Linear Ops Automation System/implementation-plan]].
2. Run CRM QA / automation-readiness review before scaling n8n/Make workflows.
3. Build the first 5 Demo Library Loom assets.
4. Continue Upwork Radar from the prepared workflow state: import, reconnect credentials, test, then operationalize.
5. Operationalize Website Audit Generator v2: import local Pipeline C v2 workflows, reconnect Firecrawl/OpenAI/Airtable/Telegram/Gmail credentials, patch WF-06 `audit_*` routing, run first 10-candidate QA batch, then approve/send first emails from Telegram.
6. Resolve FlowOps duplicate note structure before deleting old folders.

---

## Secondary / watch
- **AI-Powered Woven Label Generator** — client: Griffes Vivienne. Product-flow work is functionally complete through Milestone 5, but remaining risk notes still mention production env / QA / credential rotation. См. [[projects/AI-Powered Woven Label Generator/current-state]] and [[projects/AI-Powered Woven Label Generator/risks]].
- **AI Content Bot** — Telegram бот (@FlowOpstg_bot) для генерации и публикации контента (WF-06..WF-12). Статус: WF-09 Gemini image gen ✅, WF-06 callback routing ✅, WF-10 inline кнопки ✅. Блокер: WF-11 ID нужен для финального флоу. См. [[projects/ai-content-bot/overview]]
- **LinkedIn Outreach Automation** — n8n воркфлоу для личного LinkedIn (WF-00..WF-05). Статус: WF-05 переработан. См. [[projects/linkedin-automation]]
- Upwork freelance work (automation / integrations — episodic)
- Knowledge building: Firecrawl, n8n patterns (see `knowledge/`)
