# Session 2026-04-30 — StoreHouse API Reachability

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Interpreted the on-site browser response from `http://10.0.23.2:9797/api/sh5`.
- Confirmed the StoreHouse WebAPI service is reachable and identifies as `SH5WAPI2` version `1.12`.

## Key findings
- Plain browser GET returns `errorCode: 1` and `errMessage: JSON is absent`.
- This indicates the endpoint expects a JSON request body rather than a raw browser request.
- Next tests should use PowerShell/Postman/n8n HTTP Request with `Content-Type: application/json` and StoreHouse auth fields.

## Blockers
- Exact StoreHouse username/password and accepted discovery payload shape still need confirmation.
- Procedure names for `SH_PROC_*` are not discovered yet.

## Next steps
- POST JSON to `/api/sh5` with `UserName` and `Password` to discover available procedures.
- POST JSON to `/api/sh5struct` with a candidate `procName` to inspect procedure parameters.
- Map discovered procedure names to the n8n variables `SH_PROC_STOCK_BALANCES`, `SH_PROC_INCOMING_INVOICE`, `SH_PROC_STOCK_MOVEMENT`, `SH_PROC_EXPENSE_REPORT`, and `SH_PROC_DOCUMENT_LOG`.
