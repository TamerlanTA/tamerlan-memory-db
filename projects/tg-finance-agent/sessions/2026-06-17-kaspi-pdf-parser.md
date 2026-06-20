# Session 2026-06-17 — Kaspi PDF Parser

## Related
- [[../overview|overview]]
- [[../current-state|current-state]]
- [[../next-steps|next-steps]]
- [[../decisions|decisions]]
- [[../risks|risks]]

## What was done
- Added `pdf-parse` for PDF text extraction.
- Implemented Kaspi parser under `/Users/tamerlan/Desktop/tg-finance-agent/src/statements/kaspi/`.
- Added raw parser transaction model with `operationType`, raw operation/details, merchant/person best effort, original currency fields, blocked flag, source file, statement period, and parser confidence.
- Added CLI command: `npm run parse -- ./path/to/kaspi_statement.pdf`.
- Added synthetic smoke script: `npm run parse:sample`.
- Added parser documentation at `/Users/tamerlan/Desktop/tg-finance-agent/docs/parser.md`.
- Generated sample output at `/Users/tamerlan/Desktop/tg-finance-agent/data/sample_outputs/parsed_statement.json`.

## Key findings
- `npm run typecheck` passes.
- `npm run parse:sample` successfully extracts 4 synthetic transactions and summary totals.
- Synthetic test confirmed handling of Russian dates, KZT amounts, USD original amount details, multiline rows, own account transfers, fees, and top-ups.

## Decisions made
- Keep parser output separate from categorized domain transactions.
- Preserve `rawText` in parsed statement output for debugging.
- Keep parser confidence as extraction confidence only, not categorization confidence.

## Blockers
- Parser has not yet been validated against a real or anonymized Kaspi Gold PDF.

## Next steps
- Run CLI against a real or anonymized Kaspi statement.
- Refine row extraction and summary label matching from actual extracted PDF text.
- Implement deterministic categorization engine after parser validation.

