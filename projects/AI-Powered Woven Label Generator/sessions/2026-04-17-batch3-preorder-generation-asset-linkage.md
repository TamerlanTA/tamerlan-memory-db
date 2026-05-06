# Session 2026-04-17 — Batch 3 Preorder Generation Asset Linkage

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Implemented Batch 3 by persisting exact preorder linkage to `generationId`, `sourceAssetId`, and `resultAssetId`
- Extended the existing order-intent draft contract so linkage is carried through the Result → order intent → preorder submit path
- Extended `preorder_submissions` schema and DB persistence with dedicated linkage columns
- Extended the admin preorder read-model to expose linkage fields for future Batch 4 retrieval work
- Added focused tests for draft linkage preservation, preorder submission persistence, and admin preorder access to linkage ids

## Key findings
- The cleanest path was to reuse the signed order-intent payload rather than introduce a second linkage transport
- The generation result already had the exact ids available on the backend; the missing part was returning and preserving them through the client flow
- Batch 4 can now build retrieval actions directly on stored preorder linkage instead of approximate payload parsing

## Blockers
- Real environments need migration `0013_preorder_generation_linkage.sql` applied before Batch 3 columns exist outside local/test memory mode
- Historical preorders created before Batch 3 still have no exact linkage

## Next steps
- Execute `Batch 4 — Asset retrieval for ops`
- Expose original logo retrieval and generated preview retrieval using the stored preorder linkage
- Indicate SVG/vector availability when known without building a full production workflow
