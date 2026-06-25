# Session 2026-06-25 — Stale Button Debug, UX Fix, Manager Users Row

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done

### Root cause investigation
Exhaustively traced `/candidate_new` → form → consent → experience buttons path through:
- `handleConsentConfirm` transaction (session → `onboarding_experience_choice`)
- `isOnboardingActionAllowed` lookup map
- grammY callback routing (`/^onboarding:(.+)$/`)
- All DB reads/writes in the flow

**Conclusion:** The session state machine logic is CORRECT. The stale button error occurs when a user presses buttons from an already-processed message (e.g. pressed "Добавить опыт" → session moved to `cv_experience_form` → tried pressing "Нет опыта" or "Пропустить" on the old message). First press works, subsequent presses on same message are rejected — this is the intended protection.

### Critical DB fix
Manager `935784686` had no row in `users` table. `getManagerId()` returned `null` → consent failed with "Ошибка: менеджер не найден". Inserted via Supabase MCP:
```sql
INSERT INTO users (telegram_id, role, display_name)
VALUES (935784686, 'manager', 'Manager 2')
ON CONFLICT (telegram_id) DO NOTHING;
```
New user ID: `fdf96e85-5025-4c88-8d18-2de7be8a1ccf`

### UX fix (cv-enrichment.ts)
Changed stale button toast → modal alert:
```javascript
// Before
await ctx.answerCallbackQuery("Эта кнопка относится к предыдущему шагу. ...");
// After
await ctx.answerCallbackQuery({
  text: "Этот шаг уже пройден. Используйте /candidate_new для продолжения wizard.",
  show_alert: true,
});
```
`show_alert: true` forces a dismissible popup dialog — impossible to miss.

### New tests (4 added)
**cv-enrichment.test.ts:**
1. All 3 experience buttons allowed at `onboarding_experience_choice`
2. All 3 experience buttons rejected at any post-experience step (`cv_experience_form`, `onboarding_experience_continue`, `onboarding_education_choice`) — double-click protection

**onboarding.test.ts:**
3. Consent session data (`buildCreatedOnboardingData`) satisfies both `handleOnboardingAction` guards
4. `/candidate_new` resume sends experience choice keyboard with correct callback data for all 3 buttons

### Deployment
- commit `75cc6a6` pushed to main
- Railway bot-api deployed, `/health` 200, database ok
- 75 total tests (56 bot-api, 18 worker-documents, 1 contracts)

## Blockers
None from this session.

## Next steps
1. **Manual Telegram walkthrough** (still needed): `/cancel` → `/candidate_new` → form → consent → experience → education → extras → photo → review finish
   - Test with manager `935784686` (just given users row)
   - Test with manager `405182031`
2. Build first vacancy discovery connector (Phase 4)
3. Consent text legal review
