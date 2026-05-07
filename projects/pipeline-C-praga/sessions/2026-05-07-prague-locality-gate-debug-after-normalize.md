# Session 2026-05-07 — Prague Locality Gate Debug After Normalize

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated why `Prague Locality Gate` returned no output.
- Found the gate was receiving a Normalize diagnostic item (`debug_no_search_candidates`), not normalized lead rows.
- Updated Normalize again to recursively extract candidates from official Firecrawl output, including `data.web` represented as either an array or object.
- Added website-level dedupe inside Normalize to prevent recursive extraction duplicates.
- Regenerated workflow JSON and copied the latest Normalize code to the macOS clipboard.

## Key findings
- `Prague Locality Gate` was behaving correctly for its input; the upstream Normalize node still needed the fix.
- Local tests:
  - Firecrawl `data.web` array -> normalized `magicsmile.cz`, `yourdentist.cz`
  - Firecrawl `data.web` object -> normalized `dsmile.cz`
  - Locality gate passed Prague row and rejected Berlin row.

## Blockers
- Live n8n must receive the updated Normalize code by paste or workflow re-import.

## Next steps
- Paste the clipboard code into live `Normalize URLs and Reject Aggregators`.
- Re-run Normalize first; it should output real domains, not `debug_no_search_candidates`.
- Then run `Prague Locality Gate`.
