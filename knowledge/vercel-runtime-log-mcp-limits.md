# Vercel Runtime Log MCP — Practical Limits

The `mcp__...__get_runtime_logs` tool returns one row per HTTP request and shows only the **first log line** of each request in the `Message` column. It also caps output at roughly **5 entries** per query regardless of `limit: 100`. This means subsequent `console.log` / `console.error` lines from the same request (including the actual error stack and `[*][error.inner]` / `[*][error.outer]` payloads) are NOT visible through this tool.

**Implication:** when investigating a 500 in a serverless function, the tool will tell you the request reached the handler (first `logStep("entry")` line) but will not surface the failure point. Do not rely on it for root-cause analysis.

**Workarounds:**
- Read the function source and trace which `logStep` calls would have fired, then infer the failure window between the last visible log and the next expected one.
- Use `mcp__...__web_fetch_vercel_url` to call the Vercel API directly for full event streams (the log endpoint is `/v1/projects/<projectId>/logs` or `/v2/deployments/<deploymentId>/events`, but `web_fetch_vercel_url` only works for project URLs, not API endpoints — verified failing for `api.vercel.com`).
- Ask the owner to copy the actual error stack from Vercel's web UI, where full per-request log streams are visible.
- Add structured error output to the response itself (visible to the client) when debugging in production.

Discovered while investigating `label.generate` 500 on Griffes Vivienne Studio (2026-05-08).
