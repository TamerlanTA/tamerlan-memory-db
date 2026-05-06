# Session 2026-04-24 — Brand-mark rebalance after photo-safety fix

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- Re-audited the recent product-photo brand-mark interpretation fix and confirmed the regression source: product-photo defensive wording had been applied across nearly every prompt path, including explicit `TEXT_ONLY`, `SYMBOL_ONLY`, and `SYMBOL_AND_TEXT`.
- Added branched source-image interpretation modes in the generation layer:
  - exact artwork for explicit logo/text/monogram inputs
  - ambiguous source handling for `AUTO`
  - reserved product-photo guardrails mode for future explicit use
- Reworked the full prompt builder and Nano Banana compact/runtime prompts so explicit logo types now use stronger supplied-artwork fidelity wording again, while `AUTO` keeps conditional product-photo isolation guidance.
- Narrowed inline payload labels so explicit artwork paths send `SUPPLIED LOGO ARTWORK:` and ambiguous paths send `SOURCE IMAGE / BRAND MARK:`.
- Updated focused tests to verify exact-artwork vs ambiguous-source branching instead of the old universal source-image guardrail string.

## Key findings
- The quality regression was prompt-scoping, not texture/material logic.
- `logoType` is the only safe built-in signal currently available for branching; there is still no explicit product-photo flag in the payload.
- Best current compromise is:
  - exact fidelity for explicit logo types
  - guarded ambiguity for `AUTO`
- This restores normal text/logo quality without fully reopening the original catastrophic “weave the whole shirt/product scene” bug class.

## Blockers
- None in code for this batch.
- Manual QA is still needed for:
  - standard text/logo quality recovery
  - monogram quality
  - product-photo chest-logo safety
  - tiny/low-contrast branded-detail edge cases

## Next steps
- Run browser/live generation QA on:
  - standard text logo
  - monogram
  - product photo with small chest logo
  - product photo with centered visible branding
- If `AUTO` still proves too ambiguous in production, consider a later lightweight explicit product-photo hint/toggle, but do not add that in this batch without evidence.
