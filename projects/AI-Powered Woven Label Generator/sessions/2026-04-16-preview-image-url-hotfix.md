# Session 2026-04-16 — Preview image URL hotfix for preorder submit

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/decisions]]
- [[projects/David/risks]]
- [[projects/David/next-steps]]

## Project
AI-Powered Woven Label Generator (Griffes Vivienne)

## What was done

- Audited preorder submit payload construction after production evidence showed `orderIntent.submitPreOrder` failing with `400 BAD_REQUEST`
- Confirmed the bad payload source: `previewImageUrl` was taken directly from `state.lastGeneratedUrl`
- Confirmed that `state.lastGeneratedUrl` can still contain an inline `data:image/...` URL from the immediate generation response instead of a short hosted URL
- Added a targeted client-side sanitization step so preorder submit only includes `previewImageUrl` when it is a short hosted `http(s)` URL
- Inline `data:` URLs and oversized strings are now omitted from the submit payload instead of being sent
- Synced the shared submit contract limit to the production max length (`200000`)

## Exact root cause

- The frontend was sourcing `previewImageUrl` from the immediate result state (`lastGeneratedUrl`)
- That state can contain a base64 `data:` URL
- The preorder submit payload therefore sent a huge inline image string to the backend
- Backend validation rejected it with `too_big` on `previewImageUrl`

## Verification

- `pnpm exec vitest run client/src/domain/preorder.test.ts server/orderIntent.router.test.ts server/preorderConfirmationEmail.test.ts`: PASS
- `pnpm check`: PASS
- `pnpm build`: PASS

## Changed files

- `client/src/domain/preorder.ts`
- `client/src/domain/preorder.test.ts`
- `shared/orderIntentBridge.ts`

## Remaining risks

- In the current Milestone 5 client flow, preorder submit usually has no hosted preview URL available at submit time, so the field is now often omitted entirely
- If the client later wants thumbnail-in-email to work reliably in all environments, the frontend will need access to a short hosted result URL rather than only the immediate inline preview

## Next steps

- Redeploy the frontend/backend bundle containing this hotfix
- In production, submit a preorder from a freshly generated result and confirm:
  - `orderIntent.submitPreOrder` no longer returns `400 BAD_REQUEST`
  - the request payload omits `previewImageUrl` when the current value is inline `data:`
  - preorder submit completes successfully
