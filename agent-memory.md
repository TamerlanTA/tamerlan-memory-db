# Agent Memory

## Related
- [[current-focus]]
- [[routing-rules]]
- [[ОС LLM]]
- [[Obsidian - память агента]]
- [[projects/AI-Powered Woven Label Generator/overview|AI-Powered Woven Label Generator]]
- [[projects/David/overview|Make-David — WhatsApp automation (Колумбия)]]
- [[knowledge/firecrawl|Firecrawl — веб-скрапинг для LLM]]
- [[projects/linkedin-automation|LinkedIn Outreach Automation (WF-00..WF-05)]]
- [[projects/ai-content-bot/overview|AI Content Bot — Telegram бот контент + публикация (WF-06..WF-12)]]

---

## Owner
- **Name:** Tamerlan
- **Timezone:** Asia/Almaty (UTC+5)
- **Vault path:** `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`
- **Vault repo:** private GitHub `TamerlanTA/tamerlan-memory-db`

---

## Professional Profile
- Full-stack developer + automation engineer
- Business-first orientation — values shipped outcomes over technical perfection
- Builds products that combine web apps, AI, and automation pipelines
- Also does Upwork freelance work in automation / integrations

### Core technical strengths
- **Automation:** n8n, Make (Integromat), Zapier
- **AI integrations:** Claude Code, Codex, ChatGPT, OpenAI API, Gemini, Resend
- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Backend:** Node.js, tRPC, Drizzle ORM, MySQL/TiDB, Supabase
- **Commerce:** Stripe (checkout, webhooks, credit packs), Shopify
- **CRM / comms:** Kommo, WhatsApp integrations
- **Deployment:** Vercel, Railway
- **Databases:** MySQL, Supabase (Postgres), Drizzle migrations
- **Memory / continuity:** Obsidian vault as cross-session memory for AI agents

---

## Multi-Agent Orchestration (ОС LLM pattern)

Tamerlan runs a 3-agent pipeline. Do not confuse the roles:

| Agent | Role | Use for |
|---|---|---|
| **ChatGPT** | Orchestrator / Strategic Control Plane | Task design, context packaging, routing, batch prompt prep, client comms, handoff synthesis |
| **Codex** | Primary Execution Agent (~80% of production work) | Implementation, refactors, tests, file edits, batch changes, local repo ops |
| **Claude Code** | Chief Reasoning Agent (selective use) | Architecture decisions, hard debugging / RCA, design review, validation, prompt design for other agents, big project steering |

**Core rule:** Do not use Claude Code for routine work. Engage it only for high-risk or ambiguous problems. Prefer Codex for execution.

### Task pipeline
1. **Classify** — what type of task is this? (strategic / architecture / implementation / debugging / review / communication / research / memory update)
2. **Route** — send to the right agent
3. **Package context** — give only what's needed, not the full chat history
4. **Execute in batches** — one strong batch prompt with goal + constraints + context + files + edge cases + tests + expected output
5. **Compress result** — summary / decisions / changed files / risks / next steps
6. **Write back to Obsidian**

---

## Response Preferences
- **Language:** Russian by default; English only for client-facing output
- **Technical work:** step-by-step, complete solutions (no partial implementations)
- **Client communication:** short, direct, natural chat style
- **Prompts:** batch prompts that combine implementation + validation + edge cases + tests in one pass
- **Context passing:** always compress into operational handoff format, never dump raw chat

---

## Execution Preferences
- Prefer reading existing code before suggesting changes
- Prefer updating existing files over creating new ones
- Prefer complete, working solutions — no stubs, no "you can add this later"
- Always include error handling at system boundaries (user input, external APIs)
- Do not add speculative features or abstractions beyond what was asked
- Validate: `pnpm build` + `pnpm check` after UI/code changes

---

## Memory Conventions
- Memory vault is the canonical source of truth for project continuity
- Before non-trivial work: read `agent-memory.md` + relevant project files + latest session note
- After significant work: write session note + update `current-state.md` / `risks.md` / `next-steps.md` as needed
- Session notes go in `projects/<project>/sessions/` using `YYYY-MM-DD-short-topic.md`
- Use Obsidian wikilinks; preserve graph connections
- Do not dump raw conversation transcripts into memory
- Do not create new project folders for casual or one-session work

---

## Core Behavioral Rules
- Never leave key decisions undocumented
- Track blockers, fixes, client preferences, next steps
- At the end of a meaningful work block: do a memory sync
- When switching agents: do a handoff sync
- Prompt to start a new chat: `Read the memory for project [project-name], get in sync with the current state, and then I will give you the next task.`
