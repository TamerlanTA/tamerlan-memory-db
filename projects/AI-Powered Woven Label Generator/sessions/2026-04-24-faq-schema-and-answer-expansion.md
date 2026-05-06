# Session 2026-04-24 — FAQ schema and answer expansion

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done
- Added `FAQPage` JSON-LD generation in the frontend legal-content domain and injected it on `/faq`.
- Expanded FAQ answers in FR and EN to be more specific and citation-friendly instead of short generic replies.
- Verified current app truth before writing the copy:
  - manufactured in Italy
  - indicative 4-week lead time
  - 4 materials
  - 4 folded formats
  - standard production pricing starts at 1,000 pieces
- Preserved truthfulness around the known 500-piece gap by avoiding a false absolute minimum-order claim.
- Added/updated tests for FAQ content and structured data, then ran `vitest`, `pnpm check`, `pnpm build`, and `git diff --check`.

## Key findings
- The FAQ page was missing structured FAQ markup completely before this batch.
- The page was also materially weaker for search and LLM citation because the answers were too short and vague.
- `noindex` is not hardcoded on the page; it is still applied by the staging gate only when `VITE_IS_STAGING === "true"`.
- This means code changes alone are not enough for indexing: the production environment must not ship with the staging noindex flag enabled.

## Blockers
- No blocker in code.
- Real SEO visibility still depends on deployment/environment state and subsequent re-indexation.

## Next steps
- Verify the live production deployment of `methode.griffesvivienne.com` is not running with staging noindex.
- Open the live `/faq` page source after deploy and confirm the JSON-LD script is present.
- Submit/recheck indexing only after the production environment is crawlable.
