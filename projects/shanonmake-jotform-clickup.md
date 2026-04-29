# Shanonmake Jotform ClickUp Automation

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[flowops-agency-website]]

## Current status
- Updated `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.blueprint.json`.
- Created import/review copy: `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.updated.blueprint.json`.
- Scenario still preserves the original hierarchy: Jotform trigger -> Collection task -> Item Set task -> Design/Costing/Sampling child tasks.

## Key changes
- Naming changed to confirmed client order: `[Customer][LaunchYY]_[Season/Holiday]_[CollectionName]`, with item suffix `_[OzFill][ItemType]`.
- Collection, Item Set, Design, Costing, and Sampling content blocks were rewritten so each level only carries relevant fields.
- Existing ClickUp API `PUT /v2/task/{id}` Task Type workaround modules were preserved:
  - Collection `custom_type: 1004`
  - Item Set `custom_type: 1005`
  - Design `custom_type: 1001`
  - Sampling `custom_type: 1002`
  - Costing `custom_type: 1003`
- Assignees were left unchanged.
- Attachment upload handling was intentionally not implemented; attachment fields are text references only.

## Blockers / manual follow-up
- Unbranded list ID was not present in the blueprint, so active Unbranded routing was not wired. Current active list remains `Potential/ New Customer` (`901711596089`) for stability.
- Need manual import test in Make/ClickUp to confirm ClickUp accepts `custom_type` via API and exposes type-specific custom fields afterward.
- Existing-task-ID reuse flow is documented/prepared only; it was not implemented to avoid destabilizing the working hierarchy.

## Next steps
- Get the ClickUp List ID for `Unbranded`; then duplicate/wire a small routing branch or replace list IDs with a verified Make-compatible dynamic expression.
- Import the updated blueprint into Make and reselect/reconnect ClickUp/Jotform connections if Make prompts.
- Test sample submissions for standard customer, Unbranded house brand, and each request-type combination.
