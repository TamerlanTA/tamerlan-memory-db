# Session 2026-04-19 — Codex: Moodboard Brand Leakage Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done (by Codex, session cut by token limit)

Codex performed a full grounded audit of the generation pipeline and fixed a critical brand-leakage bug where generated labels were contaminated with competitor brand names (e.g. "Chloé Stora", "DIOR", "SAINT LAURENT") that came from reference moodboard images.

### Root cause (confirmed by visual inspection of reference images)

Two sources of contamination, both present simultaneously:

1. **Visual**: Reference images (`taffeta_ideal_1.jpeg`, `satin_ideal_1.jpeg`, `satin_ideal_2.jpeg`, `hd_ideal_1.jpeg`, `hd_cotton_ideal_1.jpeg`) contained large, clearly readable competitor brand names visible to the AI model. The model used these as content source, not just as texture reference.

2. **Textual**: Prompt guidance in `server/moodboards.ts` explicitly named the brands in descriptive text:
   - `"The approved satin ideal references (Dior, Saint Laurent) show..."` 
   - `"The approved taffeta ideal reference shows..."` (comment above said "Chloé Stora white taffeta")
   - Motif instructions said `"replicate the ideal reference"` — ambiguous about what "ideal" means for content vs. texture

### Canonical rule enforced

> **User-uploaded logo is the only allowed brand/content source.**
> Reference images guide material realism only (weave structure, thread density, surface texture, lighting).
> References must NEVER be the source of brand identity, letters, words, logo shapes, or marks.

### Fix implemented (commit `320262f`)

**14 files changed: 6 new safe reference images + 8 modified source files**

#### server/moodboards.ts (+14/-19)
- Replaced all `*_ideal_*.jpeg` reference paths with new `*_material_safe_*.jpeg/png` paths for taffeta, HD, HD Cotton, and satin
- New safe images contain only fabric texture/weave close-ups with no readable text
- Taffeta: replaced 5 files (`taffeta_1–4.jpeg` + `taffeta_ideal_1.jpeg`) → 2 safe crops (`taffeta_light_material_safe_1.jpeg` + `taffeta_dark_material_safe_1.png`)
- HD: `hd_ideal_1.jpeg` → `hd_material_safe_1.jpeg`
- HD Cotton: `hd_cotton_ideal_1.jpeg` → `hd_cotton_material_safe_1.jpeg` (+ kept 3 cotton_macro refs which are text-free)
- Satin: `satin_ideal_1.jpeg` + `satin_ideal_2.jpeg` → `satin_material_safe_1.jpeg` + `satin_material_safe_2.jpeg`
- Removed all brand names from prompt guidance text (Dior, Saint Laurent, Chloé Stora removed)
- Changed motif instruction wording: `"replicate the ideal reference"` → `"follow the supplied logo artwork only"`

#### New safe reference files added (all text-free material crops)
- `server/moodboards/hd_material_safe_1.jpeg`
- `server/moodboards/hd_cotton_material_safe_1.jpeg`
- `server/moodboards/satin_material_safe_1.jpeg`
- `server/moodboards/satin_material_safe_2.jpeg`
- `server/moodboards/taffeta_light_material_safe_1.jpeg`
- `server/moodboards/taffeta_dark_material_safe_1.png`

#### client/src/domain/logoAssets.ts (new file)
New domain module with pure utility functions:
- `isSupportedLogoUpload(input)` — validates MIME type or extension for upload acceptance (PNG/JPG/WEBP/SVG)
- `isSupportedGenerationLogoDataUrl(dataUrl)` — validates MIME type in data URL for generation (PNG/JPG/WEBP only)
- `getLogoDataUrlMimeType(dataUrl)` — extracts MIME from data URL header
- `isNearWhiteHexColor(hex)` — detects near-white colors (R≥230, G≥230, B≥230) for contrast-aware preview rendering

#### client/src/domain/logoAssets.test.ts (new file)
Tests for all logoAssets.ts helpers.

#### Other files modified in same commit (mobile/UX fixes bundled by Codex)
- `client/src/components/generator/GenerationLoadingScreen.tsx` — uses `isNearWhiteHexColor` for contrast-aware logo surface (white logo on dark background)
- `client/src/components/generator/LoadingConfigSummary.tsx` — same contrast-aware thumbnail surface
- `client/src/contexts/LanguageContext.tsx` — unknown change (minor)
- `client/src/pages/Home.tsx` — likely HEIC/mobile format upload guard using `isSupportedLogoUpload`
- `client/src/pages/Result.tsx` — likely uses `isSupportedGenerationLogoDataUrl` to validate before generation

## Verification state

- Commit `320262f` pushed to `milestone4-auth-completion` ✓
- Build/type check: **not recorded** — Codex hit token limit before confirming
- Tests for logoAssets.ts: added (pass/fail state not confirmed)
- Live generation QA with multicolor logos: **not yet done**

## Blockers / what was NOT done before token limit

- Codex did not write memory (hence this note)
- `pnpm check` + `pnpm test` pass/fail not confirmed after commit
- No explicit negative prompt additions to `buildGenerationPrompt.ts` for brand/text copying — the fix relied entirely on safer reference images + cleaned prompt guidance
- No new test for moodboard reference safety (checking that no `*_ideal_*` paths remain active)

## Next steps for next agent

1. Run `pnpm check` and `pnpm test` to confirm the commit is clean
2. Run one live generation with a simple logo (no text) → confirm no "Chloé Stora" / competitor brand appears in output
3. Optionally: add a safety test asserting no `_ideal_` paths remain in active MOODBOARD sets
4. Consider adding negative prompt line to `buildGenerationPrompt.ts`: "Do not reproduce any text, brand name, monogram, or logo from the reference images — use references only for weave structure, thread interlacing, fiber depth, fabric density, and lighting."
