# Session 2026-04-18 — Batch B Color Consistency Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## What was done

Grounded audit and fix for the color consistency bug across the full generation pipeline.

### Root cause identified
Three separate places received the original multicolor logo instead of the user-selected single-color silhouette:

1. **`GenerationLoadingScreen.tsx` hero** — rendered raw `config.logoDataUrl` (original colorful logo) while config summary already said the selected color (e.g. "Black") → visual contradiction during loading
2. **`LoadingConfigSummary.tsx` thumbnail** — same raw logo, same contradiction
3. **`Result.tsx` generation API call** — sent original colorful logo as `logoDataUrl` to the server → AI model received a red-flower (or multicolor) logo + prompt saying "make it black" → partially preserved source colors in generated result

### Canonical rule applied
> **Selected logo color controls generation.** The logo is pre-tinted to the selected color via canvas before being sent to the AI. The AI receives a clean single-color silhouette that unambiguously matches the prompt instruction.

The Prepare page preview was already correct (using `LogoTintPreview`). The fix propagates that same tinting downstream.

## Files changed (local, not yet committed)

| File | Change |
|---|---|
| `client/src/domain/generator.ts` | Exported `namedColorToHex(color: NamedColor): HexColor` domain helper |
| `client/src/components/LogoTintPreview.tsx` | Exported `buildTintedLogoDataUrl` (was internal) |
| `client/src/components/generator/GenerationLoadingScreen.tsx` | Hero logo now uses `LogoTintPreview` with resolved logo color hex |
| `client/src/components/generator/LoadingConfigSummary.tsx` | Thumbnail now uses `LogoTintPreview` with resolved logo color hex |
| `client/src/pages/Result.tsx` | Pre-tints logo via `buildTintedLogoDataUrl` before calling `generateMutation.mutate`; original is preserved as `originalLogoDataUrl` |

## Verification

- `pnpm check`: PASS (no type errors)
- `pnpm test`: all client domain tests pass (165 total: 152 pass — 13 pre-existing server-side failures unrelated to this fix)
- Pre-existing failing tests: `server/texturePresets`, `server/label.domain`, `server/nanoBanana*`, `server/auth.logout` — none related to color

## Key findings

- `LogoTintPreview` component was already correct on Prepare page — tinting was purely a display effect there
- `buildTintedLogoDataUrl` uses browser canvas: luminance-based masking to extract foreground, then applies target color hex — reliable for single-color silhouette generation
- Fallback: if canvas tinting fails, falls back to original logo (so generation still triggers, never breaks)
- `originalLogoDataUrl` is preserved unchanged as the true source of record

## Blockers
None — local changes only, no deploy needed for this fix.

## Next steps
- Commit and push Batch B along with the existing local batch (post-M5 order flow polish + back-office mini-block batches 1–4)
- Run live QA: upload a multicolor logo, select BLACK, confirm loading screen + generated result are both black
- Run QA with GOLD logo color to confirm the full end-to-end color path is consistent
