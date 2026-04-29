# Shanonmake Jotform ClickUp Automation

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[flowops-agency-website]]

## Current status
- Updated `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.updated.blueprint.json` with active two-list routing.
- Created import/review copy: `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.routed.blueprint.json`.
- Scenario now uses a top-level router with two duplicated create-new-tree branches:
  - House Brand = `Unbranded` -> ClickUp list `901711595874`
  - Default / all other submissions -> ClickUp list `901711596089`
- Both branches preserve the hierarchy: Jotform trigger -> Collection task -> Item Set task -> Design/Costing/Sampling child tasks.

## Key changes
- Naming changed to confirmed client order: `[Customer][LaunchYY]_[Season/Holiday]_[CollectionName]`, with item suffix `_[OzFill][ItemType]`.
- Collection, Item Set, Design, Costing, and Sampling content blocks were rewritten so each level only carries relevant fields.
- Existing ClickUp API `PUT /v2/task/{id}` Task Type workaround modules were preserved:
  - Collection `custom_type: 1004`
  - Item Set `custom_type: 1005`
  - Design `custom_type: 1001`
  - Sampling `custom_type: 1002`
  - Costing `custom_type: 1003`
- Unbranded branch duplicated the original task tree with new module IDs:
  - Collection `107`, API `118`
  - Item Set `105`, API `119`
  - child router `108`
  - Design `109`, API `120`
  - Sampling `112`, API `121`
  - Costing `113`, API `116`
- Default branch keeps original module IDs:
  - Collection `7`, API `18`
  - Item Set `5`, API `19`
  - child router `8`
  - Design `9`, API `20`
  - Sampling `12`, API `21`
  - Costing `13`, API `16`
- Assignees were left unchanged.
- Attachment upload handling was intentionally not implemented; attachment fields are text references only.

## Blockers / manual follow-up
- Need manual import test in Make/ClickUp to confirm ClickUp accepts `custom_type` via API and exposes type-specific custom fields afterward.
- Existing-task-ID reuse flow is documented/prepared only in module metadata notes; it was not implemented to avoid destabilizing the working hierarchy.
- Verify Make accepts `text:equal` / `text:notequal` filters on `q10_housebrand`; if Make UI prompts, reselect filter operators as equals / does not equal.

## Next steps
- Import the updated blueprint into Make and reselect/reconnect ClickUp/Jotform connections if Make prompts.
- Test sample submissions for standard customer, Unbranded house brand, and each request-type combination.
- Later, implement existing-task-ID reuse as a separate safe pass:
  - if `q105_idcollection` is provided, skip Collection creation and create/attach Item Set under that ID
  - if `q106_iditemset` is provided, skip Item Set creation and create Design/Costing/Sampling under that ID
