# Handoff Summary Template

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[OC LLM]]
- [[patterns/batch-prompt-template]]

---

## Когда использовать

При передаче работы от одного агента к другому или при начале новой сессии после перерыва.
Цель — любой агент должен за 30 секунд понять: где проект, что было сделано, что нужно делать дальше.

**Команды:**
- `handoff sync` — подготовить handoff summary и записать в память
- `memory sync` — обновить память без специального акцента на передачу
- `end-of-day sync` — полная синхронизация в конце рабочего блока

---

## Шаблон

```
## Project
[Название проекта и клиент]

## Branch / Commit state
- Branch: ...
- Latest commit: `sha` — description
- Build status: pnpm build PASS/FAIL | pnpm check PASS/FAIL

## What was completed this session
- [Конкретно что было сделано]
- [Файлы изменены]
- [Миграции применены]

## Decisions made
- [Решение 1 — почему]
- [Решение 2 — почему]

## Open risks / blockers
- [Блокер 1]
- [Блокер 2]

## Immediate next actions (in order)
1. [Первое действие — конкретное]
2. [Второе действие]
3. ...

## Env vars / infra still required
- VAR_NAME — для чего нужна
- ...

## Key files touched
- path/to/file.ts — что там изменилось
- ...
```

---

## Промпт для начала новой сессии с агентом

```
Read the memory for project [project-name]:
- /Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/projects/[project-name]/overview.md
- /Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/projects/[project-name]/current-state.md
- /Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/projects/[project-name]/next-steps.md
- Latest session note in sessions/

Get in sync with the current state. Then I will give you the next task.
```

---

## Пример заполненного handoff

```
## Project
AI-Powered Woven Label Generator — Griffes Vivienne

## Branch / Commit state
- Branch: milestone4-auth-completion
- Latest commit: 0a658ea — Add reliable preorder confirmation emails
- Build: pnpm build PASS | pnpm check FAIL (pre-existing server env typing issue)

## What was completed this session
- Transactional pre-order confirmation emails via Resend
- Delivery tracking columns on preorder_submissions
- Migration 0012_preorder_confirmation_email.sql applied to Railway MySQL
- Guest email capture synced to preorder submission backend
- Header refinement: mobile preserved, desktop brand restored

## Decisions made
- Resend via direct HTTP call, no SDK — keeps footprint minimal
- Email failure does not block preorder storage — graceful degradation
- Desktop and mobile header compositions intentionally diverge

## Open risks / blockers
- RESEND_API_KEY and RESEND_FROM_EMAIL not yet set in production
- Live email delivery unverified
- Railway DB credential should be rotated (URL exposed in chat)
- Header needs browser-based visual QA (build-verified only)

## Immediate next actions
1. Set RESEND_API_KEY + RESEND_FROM_EMAIL in Vercel/Railway env
2. Redeploy
3. Submit one live preorder → confirm email arrives
4. Rotate Railway DB credential
5. Run visual QA: desktop Home, Prepare, Result, Account + mobile Home

## Key files touched
- server/routers.ts — preorder submission with email dispatch
- drizzle/schema.ts — delivery tracking columns
- drizzle/migrations/0012_preorder_confirmation_email.sql
- client/src/components/AppHeader.tsx
- client/src/components/BrandLogo.tsx
```
