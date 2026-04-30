# Batch Prompt Template

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[OS LLM]]

---

## Когда использовать

Этот шаблон — основной формат для задач, которые отправляются в Codex или Claude Code.
Один сильный batch prompt резко снижает расход токенов и уменьшает количество итераций.

**Правило:** один prompt = полная задача. Не дробить на мелкие чаты.

---

## Шаблон

```
## Goal
[Что нужно сделать — одно предложение]

## Context
[Минимально необходимый контекст. Не весь чат. Только то, что нужно агенту прямо сейчас.]
- Branch / state: ...
- Relevant files: ...
- Key decisions already made: ...

## Requirements
[Конкретный список требований к реализации]
1. ...
2. ...
3. ...

## Constraints
[Что нельзя делать / изменять / трогать]
- Do not change ...
- Keep existing ...
- Must be compatible with ...

## Edge cases to handle
[Явно перечисли граничные случаи]
- If X is null / missing: ...
- If the user is a guest (no account): ...
- On error: ...

## Tests expected
[Что должно быть покрыто тестами]
- Unit test for ...
- Integration test for ...
- Or: no tests needed for this change

## Expected output format
[Как должен выглядеть результат]
- List of changed files
- Summary of decisions made
- Any new env vars or migrations required
- Risks or open questions if any
```

---

## Пример заполненного промпта

```
## Goal
Add transactional preorder confirmation email via Resend after successful preorder submission.

## Context
- Branch: milestone4-auth-completion
- Preorder submission is handled in server/routers.ts → submitPreorder
- preorder_submissions table exists (schema in drizzle/schema.ts)
- Resend API is available via HTTP, no SDK installed yet

## Requirements
1. After a preorder is stored successfully, send a confirmation email via Resend POST API
2. Track delivery state on preorder_submissions: status, sentAt, messageId, lastError
3. Add new migration for the delivery tracking columns
4. Fail gracefully — if email fails, preorder stays stored, log the error

## Constraints
- Do not add a generic email abstraction layer — use direct HTTP call only
- Do not change the existing preorder submission response contract
- Do not send email if preorder is a duplicate (idempotent path)

## Edge cases to handle
- Resend API returns non-200: store error in lastError, do not throw
- Missing RESEND_API_KEY env var: skip sending, log warning
- Guest without email: skip sending silently

## Tests expected
- Unit tests for the email sending helper (mock HTTP)
- Test for failure path (email fails → preorder still stored)

## Expected output format
- Changed files list
- New migration filename
- Required env vars: RESEND_API_KEY, RESEND_FROM_EMAIL, RESEND_REPLY_TO_EMAIL
```

---

## Ключевые принципы

- **Context = только операционное.** Не пересказывать историю проекта. Давать только то, что нужно для этой задачи.
- **Requirements = конкретный список.** Не "улучши UX", а "добавь кнопку X которая делает Y".
- **Constraints явные.** Агент не знает, что нельзя трогать, если ты не скажешь.
- **Edge cases заранее.** Лучше потратить 2 минуты на список, чем получить реализацию без обработки ошибок.
- **Expected output** — агент знает, что ты ожидаешь увидеть в ответ.
