---
name: 2026-04-21 QA sweep — security fix + double-generation fix
description: Post-M5/V1.5 QA audit results, previewImageUrl injection fix, and back-forward double-generation fix
type: project
---

# Session 2026-04-21 — QA Sweep: Security Fix + Double-Generation Fix

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done

### 1. Post-M5/V1.5 QA audit (static analysis)

Ran a structured QA sweep across generation flow, order/email flow, back-office/admin, and auth/account areas. Findings:

**Confirmed bug (HIGH)**: `previewImageUrl` injection in preorder submission  
**Confirmed bug (MEDIUM)**: back-forward double-generation on Result page  
**Not a real bug**: OrderPreview direct navigation / hard reload  
**Non-issues**: same-mount double-generation, preorder idempotency

---

### 2. previewImageUrl schema fix — HIGH severity (two commits)

**Root cause**: `submitPreOrderInputSchema.previewImageUrl` in `shared/orderIntentBridge.ts` accepted any non-empty string (max 200,000 chars). Server-side in `server/routers.ts`, `input.previewImageUrl ?? validation.draft.previewImageUrl` — client value wins. A crafted tRPC request (bypassing client-side https validation) could inject `data:` URIs or internal URLs into the sales team email thumbnail.

**Fix 1 (`fb0c5e4`)**: added `.url().max(4096)` — rejects data URIs and malformed URLs at schema boundary  
**Fix 2 (`466f897`)**: added `.refine(v => v.startsWith("https://") || v.startsWith("http://"))` — explicitly blocks non-http(s) schemes (matches `orderIntentDraftPayloadSchema` pattern)

**Files**: `shared/orderIntentBridge.ts` (line 84) — one field, two chained validators  
**Verification**: `pnpm check` PASS, all preorder/orderIntent/bridge tests PASS

---

### 3. Back-forward double-generation fix — MEDIUM severity (commit `e6b7739`)

**Root cause**: `canStartGeneration` was computed from `snapshot.hasResult` (= `Boolean(state.lastGeneratedUrl)`) and credit eligibility — both pass during an in-flight generation because `lastGeneratedUrl` is only set on success. `state.isGenerating` existed in the Zustand store but was never included in `GeneratorFlowSnapshot`. On back-navigate + forward-navigate: new Result mount got fresh `hasTriggeredRef = false` and `lastGeneratedUrl = null` → both guards passed → second `label.generate` fired → second credit consumed.

**Fix**:
- Added `isGenerating: boolean` to `GeneratorFlowSnapshot` in `generatorFlow.ts`
- Added `&& !snapshot.isGenerating` to `canStartGeneration`
- Added `isGenerating: state.isGenerating` to snapshot in `useGeneratorFlowController.ts`
- Added `isGenerating: false` to test fixture; added regression test: `isGenerating: true` → `canStartGeneration: false`

**Files**:
- `client/src/domain/generatorFlow.ts`
- `client/src/hooks/useGeneratorFlowController.ts`
- `client/src/domain/generatorFlow.test.ts` (+1 regression test, 9 total)

**Verification**: `pnpm check` PASS, `generatorFlow.test.ts` 9/9 PASS

---

### 4. Risk A — OrderPreview direct navigation (NOT a real bug)

`resolveOrderPreviewAccess` exhaustively handles all no-context cases. With no `?oi=` param and empty store: `backendIntentState = { status: "none" }`, `parsedIntent = { status: "missing" }` → falls through to final `else` → `redirectTo: guardRedirectTo ?? "result"` (never null). useEffect immediately redirects. Only transient `redirectTo: null` is `backend_loading` — self-clears when query resolves. **No fix needed.**

---

## Key findings

- `state.isGenerating` was isolated from the flow/eligibility system — a whole category of in-flight state was invisible to `canStartGeneration`
- `orderIntentDraftPayloadSchema` already had the https refine; `submitPreOrderInputSchema` was inconsistent (missed it)
- OrderPreview access control is comprehensive — the `resolveOrderPreviewAccess` function correctly handles all edge cases with redirects

## Verification state

- `pnpm check`: PASS (all commits)
- `generatorFlow.test.ts`: 9/9 PASS (+1 new regression test)
- All preorder/orderIntent/bridge tests: PASS
- Pre-existing server failures (texturePresets, nanoBananaService.pipeline): unchanged

## Commits this session

- `fb0c5e4` — Fix previewImageUrl schema: reject non-URL values at schema boundary
- `466f897` — Tighten previewImageUrl to http/https only via explicit refine
- `e6b7739` — Block double-generation on back-forward during in-flight generation

## Next steps

- White logo browser QA (still pending visual verification)
- Admin Users table QA in production
- Mobile Safari smoke test
- Batch B QA (multicolor logo → BLACK/GOLD color path)
- Live generation — confirm no brand leakage
- Live preorder — confirm email arrives and reply preserves thread
- Server test failures investigation (texturePresets, nanoBananaService.pipeline)
