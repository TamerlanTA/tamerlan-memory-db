# Session 2026-06-25 — Step 5/9 Experience Buttons Fix (Task E)

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## Root cause
Manager `405182031` session was at `cv_experience_form` with `workExperienceCount=0`. The manager pressed `+ Добавить опыт` previously, session advanced, experience form was sent, BUT `editMessageReplyMarkup()` silently failed → Step 5/9 keyboard remained visible. Re-clicking any of the three buttons (add/none/skip) triggered the `isOnboardingActionAllowed` guard which only allowed these actions at `onboarding_experience_choice`, not `cv_experience_form`.

## Production session state before fix
```
manager_telegram_id: 405182031
step: cv_experience_form
workExperienceCount: 0   ← no experience added despite session advancing
```

## Fix applied — commit c905fb5
**File: `apps/bot-api/src/intake/cv-enrichment.ts`**

Extended `isOnboardingActionAllowed` to add recovery entries:
```javascript
cv_experience_form: ["experience:add", "experience:none", "experience:skip"],
cv_education_form: ["education:add", "education:skip"],
```

Behavior after fix:
- `experience:add` at `cv_experience_form` → re-sends experience form template (idempotent upsert)
- `experience:none`/`experience:skip` at `cv_experience_form` → calls `startEducationStep` → advances to education ✅
- Same pattern for education recovery

Stale button protection still works for all steps AFTER the experience phase:
`onboarding_experience_continue`, `onboarding_education_choice`, `onboarding_photo_choice`, `onboarding_review` → all still REJECT experience buttons.

## Tests updated
**cv-enrichment.test.ts:**
- Updated "rejects experience buttons" test to remove `cv_experience_form` from stale list, added later steps
- Added "allows experience buttons at cv_experience_form (recovery)" test
- Added "allows education buttons at cv_education_form (recovery)" test
- Added "rejects education buttons past education phase" test

**onboarding.test.ts (3 new tests):**
- `experience:add` at `cv_experience_form` re-sends experience form
- `experience:none` at `cv_experience_form` advances to education, no work experience inserted
- `experience:skip` at `cv_experience_form` advances to education, no work experience inserted

Total: 74 tests passing (up from 68 before fix, 6 new tests).

## Validation
- `pnpm test` → 74/74 passing
- `tsc --noEmit` → clean
- `pnpm format:check` → clean
- Railway deploy → `/health` 200

## Manual Telegram walkthrough needed
The session for manager 405182031 is still at `cv_experience_form`. With the fix deployed:
- Pressing `Нет опыта` or `Пропустить` on the visible Step 5/9 message → should now advance to education
- Pressing `+ Добавить опыт` → should re-send the experience form template
- Alternatively: `/candidate_new` → "Продолжаем незавершённый onboarding." + experience form template

## Pattern: keyboard removal reliability
`editMessageReplyMarkup()` can fail silently for multiple reasons (Telegram rate limit, message too old, race conditions). The recovery fix in `isOnboardingActionAllowed` is the correct defense-in-depth approach: even if the keyboard persists, the manager can always use the visible buttons to advance or retry.

## Next steps
1. Manual Telegram walkthrough:
   - Manager 405182031: press visible experience buttons → verify they work
   - Full fresh flow: /cancel → /candidate_new → form → consent → Step 5/9 → add experience → experience form → fill → continue → education → photo → review
2. Manager 935784686 is stuck at `consent` step — may need their own walkthrough
3. Build first vacancy discovery connector (Phase 4)
