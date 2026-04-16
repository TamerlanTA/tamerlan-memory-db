# Session 2026-04-16 — Order Preview submit state mapping fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## Project
AI-Powered Woven Label Generator (Griffes Vivienne)

## What was done

- Audited `/order-preview` submit state handling after a user report about contradictory UI
- Confirmed that backend submit result mapping for `submitted`, `already_submitted`, and `email failed after successful submit` was already correct
- Fixed the frontend contradiction by making the Order Preview header / feedback rendering depend on the actual preorder submit state instead of always using success-like copy
- Added stateful inline warning support for `confirmationEmail.status === failed` while keeping preorder success intact
- Added focused tests for:
  - submitted => success only
  - already_submitted => success-like only
  - submitted + email failed => success + warning
  - true failure => error only

## Exact root cause

- The page-level header and hero treatment on `/order-preview` were always using success-sounding copy such as “Votre demande est enregistrée”, even before or after a failed submit
- The red inline failure message was driven by `preorderState`, but the main title/subtitle were not
- Result: the page could visually communicate success-like state and failure state at the same time even though the reducer itself was exclusive

## Verification

- `pnpm exec vitest run client/src/domain/preorder.test.ts server/orderIntent.router.test.ts server/preorderConfirmationEmail.test.ts`: PASS
- `pnpm check`: PASS
- `pnpm build`: PASS

## Changed files

- `client/src/domain/preorder.ts`
- `client/src/domain/preorder.test.ts`
- `client/src/pages/OrderPreview.tsx`
- `client/src/contexts/LanguageContext.tsx`

## Remaining risks

- The submit path still depends on a valid backend `oi` token; this fix addressed contradictory UI mapping, not the broader fallback behavior of local-vs-backend intent
- Email failure warning is now visible inline as well as via toast; inbox/provider delivery still needs live verification in production
