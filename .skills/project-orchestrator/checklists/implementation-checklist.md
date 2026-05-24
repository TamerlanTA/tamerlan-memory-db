# Implementation Checklist

For implementation batches:

- [ ] Inspect relevant files before editing.
- [ ] Preserve existing architecture and conventions.
- [ ] Keep scope tight.
- [ ] Add or update tests when risk justifies it.
- [ ] Handle user input, API failures, nulls, empty states, and permission errors.
- [ ] Avoid exposing secrets.
- [ ] Avoid hidden critical TODOs.
- [ ] Update docs or memory if behavior, config, or next steps changed.
- [ ] Run build/test/typecheck/lint where applicable.
- [ ] Report changed files and validation results.
- [ ] State untested areas honestly.

For automation workflows:

- [ ] Validate trigger payload.
- [ ] Validate approval gate.
- [ ] Add idempotency or duplicate-send protection where needed.
- [ ] Handle retries and partial failures.
- [ ] Log enough to debug without leaking secrets.

For AI product features:

- [ ] Validate prompt inputs and outputs.
- [ ] Handle empty/malformed model responses.
- [ ] Document model/env config.
- [ ] Consider cost/rate limits.
- [ ] Preserve user trust with clear failure states.
