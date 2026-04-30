# Session 2026-04-30 — StoreHouse ProcName Discovery Blocker

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Interpreted n8n HTTP Request tests to `/api/sh5`, `/api/sh5struct`, and `/api/sh5exec`.
- Checked official r_keeper SH5 WebAPI behavior: `/api/sh5struct` and `/api/sh5exec` both require `UserName`, `Password`, and known `procName`.

## Key findings
- `/api/sh5struct` returning `Json element not found: "procName"` is expected when `procName` is omitted.
- `/api/sh5exec` returning `procedure not found` for guessed names means the guessed procedure does not exist; it does not provide procedure-name discovery.
- Official docs describe `sh5struct` as returning datasets/fields for a known procedure, not as listing all procedure names.
- TEMPLATE scan later found real procedure templates; `sh5struct` succeeded for `GRemns`, `GDocs`, `InsGDoc0`, and `InsGDoc1`.
- SH5 WebAPI II execution payloads should be built with `Input` tables, not the placeholder `params` object currently used in generated workflow drafts.

## Blockers
- Exact procedure names for `SH_PROC_*` remain unknown.
- Full field structures for the confirmed procedures still need to be exported/copied before final workflow payload mapping.

## Next steps
- Search the SH5 WebAPI installation folder for `*_desc.json` files; filenames reveal available procedure names.
- Use the installed `Swat.exe` utility, if present, to inspect/test procedures.
- Try official sample procedure names such as `XDivisions` only as connectivity checks, not as final business procedures.
