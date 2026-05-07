# Session 2026-05-08 — MOQ 1000, R2 hotfix, and freemium gate UX

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## Worktree
- Branch: `claude/magical-mendel-0ac677`
- Local path: `/Users/tamerlan/Desktop/griffes-vivienne-studio-claude-r2-storage-integration-pU2tu/.claude/worktrees/magical-mendel-0ac677`
- Vercel project: `griffes-vivienne-studio-3vop` (`prj_LkPZqybEyxElduycv9y1O1qu6G4j`), team `team_JfRybqpC6WsadUDMtKRb857f`
- Production domain: `methode.griffesvivienne.com`

## What was done

### 1. MOQ 500 → 1000 (commit `35faedc`)
- `client/src/domain/order.ts`: `PRODUCTION_MIN_QUANTITY` raised from 500 to 1000; `PRODUCTION_QUANTITY_OPTIONS` derived array auto-updated; `normalizeProductionQuantity(500)` now clamps up to 1000
- `client/src/contexts/LanguageContext.tsx`: FR/EN copy updated (4 strings: range and minimum)
- `client/src/components/OrderLabelsPanel.tsx`: doc comment + quick-select button filter now show [1000, 2500, 5000, 10000]
- `shared/orderIntentBridge.ts`: added `.refine()` rejecting production quantity < 1000; sample mode (`quantity: 1`) explicitly exempted
- New tests: `client/src/domain/order.test.ts` (8 tests), 3 added to `server/orderIntentBridge.test.ts`
- Sample flow untouched

### 2. label.generate 500 hotfix (commit `ab9b86c`)
- **Root cause:** R2 credentials (`R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`) are NOT set as Vercel env vars in production. R2 storage was already integrated in `416b742` (parent commit on `milestone4-auth-completion`); generation was never tested in production until owner tried it after `35faedc` deploy.
- Call chain: `label.generate handler` → `storeOriginalUploadAsset` → `storeAsset` → `storagePut` → `getR2Config()` throws `"R2 storage credentials missing"`. The catch in `storeAsset` only activated the inline fallback for `!ENV.isProduction`, so production re-threw → 500.
- **Fix:**
  - `server/assets.ts`: removed `!ENV.isProduction` guard. Fallback now stores `inline://assets/<kind>-<nanoid>.<ext>` as the URL placeholder (NOT the data URL — base64 PNG would overflow MySQL TEXT 65535-byte limit). Generation response returns fresh in-memory data URLs; client unaffected.
  - `server/routers.ts`: `getGenerationDownloadUrl` now returns `NOT_FOUND` with clear message when `labelUrl` starts with `inline://`, instead of returning broken URL.
  - `client/index.html`: favicon `?v=2` cache-bust.

### 3. Freemium gate UX fix (commit `5e54191`)
- **Symptom:** owner tested generation with guest session 12 (already used free trial). Bbackend threw plain `new Error("Essai gratuit deja utilise...")` → bubbled up as `INTERNAL_SERVER_ERROR` → client showed generic "Generation stopped — try again" with useless retry button.
- **Fix:**
  - `shared/generationErrors.ts`: added `GUEST_FREE_TRIAL_EXHAUSTED` and `INSUFFICIENT_CREDITS` codes; extended `GenerationErrorAction` with `"sign_up"` and `"buy_credits"`; added presentation entries.
  - `server/label/generationErrors.ts`: new codes map to tRPC `FORBIDDEN`.
  - `server/routers.ts`: replaced 2 `throw new Error(...)` in entitlement checks (user credits + guest free trial) with `toGenerationTrpcError({code, retryable: false, sourceLayer: ...})`.
  - `client/src/pages/Result.tsx`: `handleGenerationErrorAction` routes `sign_up` → `/sign-in` and `buy_credits` → `/credits`.
  - `client/src/contexts/LanguageContext.tsx`: 6 new i18n keys × 2 languages.

## Key findings

- **R2 storage was already integrated before this branch** (commit `416b742` on `milestone4-auth-completion`). `35faedc` did NOT touch `routers.ts`/`assets.ts`/`storage.ts`. The 500 was a latent bug exposed by first real generation attempt in production.
- **Generation works without R2 credentials in degraded mode** after the hotfix: assets get `inline://...` keys, persistent storage requires R2 to be configured. Re-download will return `NOT_FOUND` with explicit message until R2 is set.
- **Vercel runtime log MCP tool is severely limited** — caps at ~5 entries per query and shows only first log line per request. Could not surface `[label.generate][error.inner]` details directly; root cause inferred from code analysis.
- **MySQL TEXT column overflow risk** if data URLs were stored: TEXT = 65535 bytes; PNG base64 commonly 200KB+. Inline-key placeholder approach avoids this.

## Blockers / Required user action

- **R2 env vars must be set in Vercel** (Project Settings → Environment Variables → Production):
  - `R2_ACCESS_KEY_ID`
  - `R2_SECRET_ACCESS_KEY`
  - `R2_BUCKET`
  - `R2_ACCOUNT_ID` (or `R2_ENDPOINT`)
  - Without these: generation works but no persistent storage — re-downloads fail.
- **Favicon update:** owner sent new gold "F" circle logo image; I cannot write binary attachments. User must save manually to `client/public/favicon.png`. `?v=2` cache-bust already in `index.html`.

## Verification

- `pnpm check`: PASS
- `pnpm build`: PASS (`dist/index.js` 440KB, `dist/app.js` 436KB)
- Focused tests (15): MOQ + intent bridge — PASS
- Focused tests (12): generation error presentation + normalization — PASS
- Pre-existing failures unchanged: `texturePresets`, `label.domain`, `nanoBanana.pipeline` (10 tests, identical on base commit, unrelated to this work)

## Next steps

- Owner adds R2 credentials to Vercel production env
- Owner replaces `client/public/favicon.png` with new gold logo
- Test generation end-to-end with fresh guest session (incognito) after R2 vars are set
- Consider whether `claude/magical-mendel-0ac677` should be merged into `milestone4-auth-completion` or directly merged via PR — currently 68 commits ahead of `origin/main`
- Investigate the pre-existing `texturePresets` / `label.domain` / `nanoBanana.pipeline` test failures separately

## Commits

- `35faedc` — Raise production MOQ to 1000 pcs and harden label generation
- `ab9b86c` — Fix label.generate 500 when R2 storage credentials are not configured
- `5e54191` — Surface freemium gate as actionable error in generation UI
