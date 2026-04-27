# Claude Code — 32 Hacks (Nate Herk)

> **Источник:** видео "32 Claude Code Hacks in 16 Mins" — автор Nate Herk  
> **PDF-гайд:** доступен у автора, суммаризирует видео по уровням Beginner / Intermediate / Advanced  
> **Таймкоды:** Beginner 0:14 · Intermediate 4:53 · Advanced 10:29

## Связанные заметки
- [[agent-memory]]
- [[patterns/claude-code-workflow]]

---

## Главная идея

Claude Code — это не "напиши код", а **junior developer / agent team**.  
Ты даёшь контекст, план, правила, проверки, инструменты и память проекта.

> **Главный ресурс — контекст.**  
> Меньше мусора = лучше думает, дешевле работает, реже ломает проект.  
> Держи контекст маленьким. Планируй до исполнения. Проверяй результат. Сохраняй в `claude.md` и skills.

---

## Beginner Hacks

### 1. /init в каждом проекте
Сканирует проект → создаёт `claude.md` (структура, папки, правила, команды, архитектура).

После `/init` попроси Claude обновить файл:
```
Review this project and update claude.md with:
- project goal, tech stack, key folders
- commands to run/build/test
- coding conventions, known risks
- current active task
- things you must never change without asking
Keep it concise.
```

---

### 2. /statusline
Live-панель в терминале: модель, % контекста, стоимость, состояние сессии.  
Видишь заранее, когда контекст раздувается → делаешь `/compact` до деградации качества.

---

### 3. Voice input
`/voice` — диктовка задач голосом. Удобно для объяснения бизнес-логики (n8n workflow, клиентский процесс) без долгого печатания.

---

### 4. Держи контекст маленьким
Не давай весь проект сразу. Фокусируй агента:
```
We are working only on the n8n workflow export validation.
Read only these files:
- workflow.json
- README.md
- test-data/sample-input.json
Do not inspect unrelated files unless needed.
```

---

### 5. /context — диагностика token bloat
Показывает, что ест токены: system prompt, файлы, MCP-сервера, история.  
Если Claude замедлился или ответы стали хуже → первым делом запустить `/context`.

---

### 6. /compact на ~60% + /clear между задачами

`/compact` с инструкцией, что сохранить:
```
/compact but preserve:
- API integration decisions
- database schema decisions
- current bugs, files changed, next steps
Remove outdated discussion and failed approaches.
```

`/clear` — когда задача закончена и начинается новая. `claude.md` при этом остаётся.

---

### 7. Plan Mode ВСЕГДА первым
**Shift + Tab** → Plan Mode. Claude читает, анализирует, планирует — но не меняет файлы без разрешения.

```
Start in Plan Mode.
Do not edit files yet.
First inspect the relevant files, then propose a step-by-step implementation plan.
Include risks, test plan, and files you expect to modify.
Wait for approval before changing anything.
```

---

### 8. Давай проблему, а не задачу
❌ "Напиши функцию X"  
✅ "We need a robust way to prevent duplicate preorders when users refresh the confirmation page. Analyze the current flow and propose the cleanest approach."

---

### 9. Заставь Claude задавать вопросы
```
Ask me questions until you are 95% confident you understand
the task, constraints, and expected output.
Do not implement until you reach that confidence.
```

---

### 10. Todo с self-check
Каждый шаг — с проверкой перед переходом к следующему:
```
1. Implement the page
2. Run tests
3. Open the page locally
4. Take a screenshot
5. Check layout visually
6. Open DevTools — verify no console errors
7. Fix issues before moving on

Do not move to the next todo until you are 95% confident the current step is correct.
```

---

## Intermediate Hacks

### 11. Sub-agents для параллельной работы
Каждый sub-agent — отдельный контекст. Главный агент делегирует:
```
Use sub-agents where helpful:
- one sub-agent should inspect the existing workflow logic
- one sub-agent should research the API docs
- one sub-agent should design test cases
Then synthesize their findings into one implementation plan.
```

---

### 12. Custom Skills
Повторяемые инструкции в `.claude/skills/`.  
Примеры файлов:
- `n8n-workflow-architect.md`
- `n8n-workflow-validator.md`
- `client-automation-discovery.md`
- `upwork-proposal-writer.md`
- `make-scenario-review.md`
- `memory-update.md`
- `handoff-sop-generator.md`

---

### 13. Haiku для дешёвых sub-agents
Сильная модель — для решений. Дешёвая модель (Haiku) — для чтения доков и простых задач.  
Экономит лимиты без потери качества на ключевых решениях.

---

### 14. Постоянно обновляй claude.md
Новое правило, gotcha, архитектурное решение → сразу в `claude.md`:
```
Update claude.md with this new rule:
When editing preorder flow, never bypass orderIntent token validation.
Keep it under the "Project-specific rules" section.
```
**Лимит:** держать `claude.md` в пределах 150–200 строк.

---

### 15. claude.md как роутер к внешним docs
```markdown
# Project Memory
For full business context, read: docs/business-context.md
For coding rules, read: docs/coding-standards.md
For current milestone, read: docs/current-state.md
For prompts and agent workflows, read: docs/agent-prompts.md
```
Совпадает с Obsidian Memory Protocol: `overview`, `current-state`, `decisions`, `risks`, `next-steps`, `prompts`.

---

### 16. Останавливай Claude рано
Если агент пошёл не туда → `Escape` сразу.  
Неправильная работа тратит и время, и контекст.

---

### 17. Жёстко чeлленджи средний результат
```
This is too generic. Scrap it and propose a more elegant production-ready approach.
Not good enough. Try again with a simpler architecture and fewer moving parts.
This solves the happy path only. Redesign with edge cases, retries, logging, and failure handling.
```
После хорошей версии:
```
Update the relevant skill/claude.md so you don't repeat the previous weak approach.
```

---

### 18. /rewind
Откат сессии к предыдущему состоянию. Лучше, чем начинать заново, если агент зашёл не туда.

---

### 19. /hooks — уведомления
Звуковой сигнал или действие после завершения шага.  
Полезно при нескольких параллельных Claude Code сессиях.

---

### 20. Screenshots для UI
```
Open the app locally.
Take a screenshot of the page.
Compare it to the reference.
List visual issues.
Fix them.
Repeat for 3 passes.
```

---

### 21. Chrome DevTools
```
Open the app in Chrome.
Use DevTools to check console errors.
Test the main user flow:
1. upload logo → select material → generate preview → proceed to order
Report any functional issues before editing.
```

---

### 22. Inspiration sites как референс
```
Use this as visual inspiration.
Do not copy the brand or content.
Recreate the layout quality, spacing, typography feel, and interaction style
for our own website.
```

---

## Advanced Hacks

### 23. Параллельные сессии через Git worktrees
Две Claude Code сессии в одной папке → конфликты. Git worktrees решает:
```bash
claude-worktree admin-preorders
claude-worktree generation-thumbnails
claude-worktree ops-asset-actions
```
Разные ветки, отдельные копии, потом обычный merge.

---

### 24. Прямые API endpoints вместо MCP
MCP грузит много tool definitions в контекст.  
Если нужен один endpoint — лучше дать Claude напрямую API docs или curl-запрос.

---

### 25. /loop для повторяющихся задач
```
/loop every 5 minutes check the Vercel deployment logs
and notify me only if the build fails or finishes.
```
Мониторинг PR, deployment, logs, тестов.  
**Ограничение:** loops живут до 3 дней.

---

### 26. Claude Code на VPS
Запуск долгой сессии на удалённом сервере — не зависит от ноутбука.

---

### 27. Управление с телефона
Claude Code поддерживает remote control из браузера. Агент работает на компе, ты даёшь approve/feedback с телефона.

---

### 28. CLI как "разговорный интерфейс"
Подключи любой CLI (BigQuery, Supabase, etc.) и спрашивай на естественном языке:
```
What were the top 10 revenue sources last quarter?
```
Claude превращает вопрос в запрос, выполняет и объясняет.

---

### 29. ultrathink для сложных задач
Режим глубокого reasoning. Только для архитектуры, сложного дебага, больших refactor решений.
```
ultrathink about the safest architecture for this n8n workflow
so it supports retries, deduplication, human approval, and future CRM migration.
```

---

### 30. Permissions вместо --dangerously-skip-permissions

**Разрешить:**
```
npm test, npm run build, npm run lint, git diff, git status, cat, ls
```

**Запретить:**
```
rm -rf, git reset --hard, git clean -fd, delete database, drop table, overwrite env files
```

---

### 31. Agent Teams для больших проектов
Sub-agents работают параллельно, но не общаются.  
Agent Teams — координированный режим: общий task list, обмен выводами.  
Пример: backend agent + frontend agent + QA agent + product reviewer.

---

### 32. Context 7 MCP — свежая документация
Даёт Claude актуальную документацию по библиотекам вместо устаревших знаний модели.  
Критично для: Next.js, React, Vercel, Drizzle, tRPC, Shopify API, n8n nodes, Microsoft Graph, Stripe.

---

## Ключевые команды (шпаргалка)

| Команда | Что делает |
|---|---|
| `/init` | Создаёт claude.md для проекта |
| `/statusline` | Live-панель: контекст, стоимость, модель |
| `/voice` | Голосовой ввод |
| `/context` | Показывает, что ест токены |
| `/compact` | Сжимает историю сессии |
| `/clear` | Очищает диалог (claude.md остаётся) |
| `/rewind` | Откат к предыдущему моменту |
| `/hooks` | Уведомления и автоматические действия |
| `/loop` | Повторяющаяся задача внутри сессии |
| `ultrathink` | Глубокое reasoning для сложных задач |
| `claude-worktree <name>` | Параллельная работа в отдельной ветке |
| `Shift + Tab` | Включить / выключить Plan Mode |
| `Escape` | Остановить агента досрочно |

---

## Применение для n8n / автоматизаций

### Структура claude.md (минимум)
```markdown
# Project Context
## Goal
## Current Active Task
## Tech Stack
## Key Files
## Commands (run / test / build / lint)
## Rules
## Do Not Touch Without Asking
## Quality Bar
```

### Полный "full-cycle" промпт для n8n
```
You are working as a senior n8n automation architect.
Start in Plan Mode. Do not edit anything until you inspect
the relevant files and produce a plan.

Task: Build/review this n8n workflow for [business process].

Requirements:
- robust trigger handling, clean data normalization
- deduplication, retries and error handling
- structured logs, clear node names
- test payloads, final handoff notes

Process:
1. Inspect existing workflow/config/docs.
2. Ask questions until you are 95% confident.
3. Produce implementation plan.
4. After approval, implement.
5. Validate with 3 test cases:
   - happy path
   - missing/invalid input
   - downstream API failure
6. Fix issues before finishing.
7. Update project memory.

Do not move to the next step until the current one is verified.
```

### claude.md как роутер к Obsidian memory
```markdown
# External Memory
Before non-trivial work, read:
- /path/to/agent-memory.md
- project overview.md, current-state.md, decisions.md, next-steps.md
- latest session note

After meaningful work:
- update current-state.md
- update decisions.md if decisions changed
- update next-steps.md
- append a short session note
```

---

## 5 главных выводов

1. **Процесс важнее одной команды.** Сила в: план → маленький контекст → self-check → память → skills.
2. **Не давай просто писать код.** Пусть думает, спрашивает, планирует и сам проверяет.
3. **Контекст нужно контролировать.** `/context`, `/compact`, `/clear`, короткий `claude.md`, ссылки на отдельные docs.
4. **Качество встроено в workflow.** Скриншоты, DevTools, тесты, edge cases, todo с проверками.
5. **Лучшие результаты — из системы.** `claude.md` + skills + worktrees + sub-agents + Context 7 + permissions + memory protocol.

> **Для автоматизаций:** Plan Mode + ask until 95% + custom n8n skills + self-check todo + claude.md memory + worktrees + Context 7
