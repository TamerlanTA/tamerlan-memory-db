# Shanonmake Jotform ClickUp Automation

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[flowops-agency-website]]

## Current status
- Make import/test fix on 2026-05-04:
  - Screenshot showed module `22` (`Tools - Set multiple variables`) failing with `BundleValidationError: Missing value of required parameter 'scope'`.
  - Patched module `22` to include `mapper.scope = roundtrip`, restore metadata `scope = One cycle`, expected `scope`/`variables` schema, and output interface entries for the normalization variables.
  - Applied the same patch to `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.updated.blueprint.json`, `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.final-fallback-safe.blueprint.json`, and `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.production-stabilized.blueprint.json`.
- Fallback safety fix on 2026-05-04:
  - Router `23` now has exactly two routes.
  - Route 1 remains filtered for `q10_housebrand = Unbranded`.
  - Route 2 is now unfiltered (`filter: null`) and acts as the true fallback/default to `Potential/ New Customer` list `901711596089`.
  - Added explicit TODO variables in module `22` for future Ecommerce and Big Sky Supply dedicated list IDs.
  - Saved final fallback-safe copy: `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.final-fallback-safe.blueprint.json`.
- Stabilization pass on 2026-05-04 for Shannon Kiefer complaint: Big Sky Supply/Ecommerce submissions did not appear, Cracker Barrel naming needed `CB`, and ClickUp plan limits could break Task Type/custom field steps.
- Updated `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.updated.blueprint.json`.
- Created production-stabilized copy: `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.production-stabilized.blueprint.json`.
- Created pre-stabilization backup: `/Users/tamerlan/Desktop/shanonmake/Integration Jotform.pre-stabilization.backup.json`.
- Completed as of 2026-04-30: Make project with Shanon/Shen is marked done in [[My-tasks]].
- Scenario uses a top-level router with two duplicated create-new-tree branches:
  - House Brand = `Unbranded` -> ClickUp list `901711595874`
  - all non-Unbranded submissions -> fallback ClickUp list `901711596089`
- Both branches preserve the hierarchy: Jotform trigger -> Collection task -> Item Set task -> Design/Costing/Sampling child tasks.

## Key changes
- Naming changed to confirmed client order: `[Customer][LaunchYY]_[Season/Holiday]_[CollectionName]`, with item suffix `_[OzFill][ItemType]`.
- Module `22` normalization now exposes:
  - `customer_display`
  - `customer_code`
  - `normalized_customer`
  - `fallback_list_id`
  - `unbranded_list_id`
  - `target_list_id`
  - TODO placeholders for missing Big Sky Supply and Ecommerce list IDs
- `customer_code` mappings currently include:
  - `Cracker Barrel` -> `CB`
  - `Big Sky Supply` / `Big Sky` / `BSS` -> `BSS`
  - `Ecommerce` / `E-commerce` / `Ecom` / `EComm` / `eCommerce` -> `ECOM`
- Task names now use `customer_code` instead of visible full customer name.
- Collection, Item Set, Design, Costing, and Sampling content blocks were rewritten so each level only carries relevant fields.
- ClickUp Task Type API workaround modules were bypassed as no-op `util:SetVariable2` modules to avoid ClickUp free/testing plan failures blocking task creation:
  - Collection `custom_type: 1004`
  - Item Set `custom_type: 1005`
  - Design `custom_type: 1001`
  - Sampling `custom_type: 1002`
  - Costing `custom_type: 1003`
- `custom_fields` payloads were removed from ClickUp task creation mappers for the same stability reason.
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

## Historical manual follow-up
- Big Sky Supply and Ecommerce actual ClickUp list IDs were not present in the blueprint or memory. They currently fall back to `Potential/ New Customer` instead of disappearing. Add real list IDs later if Shannon provides them.
- Need manual import test in Make/ClickUp to confirm basic task creation works without Task Type/custom field payloads.
- Existing-task-ID reuse flow is documented/prepared only in module metadata notes; it was not implemented to avoid destabilizing the working hierarchy.
- Verify Make accepts `text:equal` / `text:notequal` filters on `q10_housebrand`; if Make UI prompts, reselect filter operators as equals / does not equal.

## Next steps
- No immediate next step tracked after completion mark.
- Historical implementation notes retained below; not tracked as active tasks after the completion mark.
- Import the updated blueprint into Make and reselect/reconnect ClickUp/Jotform connections if Make prompts.
- Test sample submissions for standard customer, Unbranded house brand, and each request-type combination.
- Later, implement existing-task-ID reuse as a separate safe pass:
  - if `q105_idcollection` is provided, skip Collection creation and create/attach Item Set under that ID
  - if `q106_iditemset` is provided, skip Item Set creation and create Design/Costing/Sampling under that ID
