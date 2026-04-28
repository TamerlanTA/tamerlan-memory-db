# Commands Guide: Gemini Telegram Bridge

## General Commands
- `/start`: Greeting and system info.
- `/help`: List all available commands.
- `/status`: Current engine state, workdir, and mode.
- `/health`: System uptime and memory usage.

## Workspace & Memory
- `/workdir <path>`: Change working directory (must be in allowed list).
- `/memory`: Fast-switch to the Memory Vault directory.
- `/files`: List last 5 uploaded files.

## Gemini Operations
- `/ask <prompt>`: Quick question to Gemini CLI.
- `/run <prompt>`: Full CLI execution (staged for V2).
- `/cancel`: Kill the currently running Gemini process.
- `/mode <default|creative|precise>`: Set AI behavior/temperature.

## Scheduler
- `/schedule <daily HH:mm | every Xh | once ISO> <type> <payload>`: Schedule tasks.
- `/tasks`: Show all active scheduled tasks.
- `/cancel-task <id>`: Remove a task from the schedule.

## Multimodal
- **Images**: Send any photo to analyze it.
- **Documents**: Send `.txt`, `.md`, `.json` for content analysis.
- **Voice**: Send voice message for transcription (Stub active).
- **Albums**: Media groups are debounced (2s) and processed as one batch.
