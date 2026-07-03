# Session 2026-07-02 — Source Expansion To 85 Sources

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Expanded `data/employer-catalog.seed.csv` from 31 to 85 production sources.
- Added query/property sources focused on Qatar/UAE/Bahrain/Kuwait/Saudi F&B and front-office coverage across Accor, Four Seasons Workday, Marriott, and selected Gulf hotel groups.
- Updated Workday discovery to honor `searchText`/`q`/`keyword` endpoint parameters and added regression coverage.
- Imported the expanded catalog to production and manually ran discovery for Accor, Workday, Marriott, and generic connectors.
- Redeployed `worker-vacancy-discovery`; Railway logs show the scheduler now checking 85 sources.

## Key findings
- Production now has 85 sources / 85 employers, 1353 active vacancies, 2613 total vacancy rows, and 481 distinct active apply URLs.
- Today's source runs after expansion: 103 succeeded and 38 failed; failures are mainly fragile generic sources with 403/404/410/empty results.
- Active country coverage is materially better: QA 233, AE 316, BH 53, KW 36, SA 128, plus 461 unknown-location rows.
- Current production candidate supply:
  - Юля Иванова Иванов: 10 primary + 10 reserve.
  - Жанибек Иванов: 10 primary + 10 reserve.
  - Тамерлан Тог: 1 strict primary + 10 reserve after already-approved vacancies are excluded.

## Blockers
- Generic HTML sources are noisy and should be repaired, replaced, or disabled if they keep failing.
- Query-level sources can make supply look broader than the individual vacancy location truly supports; keep manager review in the loop.
- For narrow Qatar-only waiter candidates, strict primary volume may still be below 5 after previous approved vacancies are excluded, even though reserve volume is available.

## Next steps
- Re-run `/candidate_supply` and `/candidate_batch` in Telegram for the pilot candidates.
- Decide whether approved reserve items count toward the 5/day target or whether strict primary must reach 5.
- Harden source quality: replace failing generic pages with dedicated APIs/connectors and improve per-vacancy location extraction.
- Rotate the temporary Railway token shared in chat.
