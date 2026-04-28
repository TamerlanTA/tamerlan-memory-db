# Full User & Command Guide

## Multimodal Capabilities
- **Voice**: Send a voice message. The bot will (in future) transcribe and answer.
- **Images**: Send photos. The bot downloads them and asks Gemini to describe/analyze.
- **Documents**: Send `.txt`, `.md`, or `.json`. The bot reads the file content and uses it as context.
- **Albums**: Send multiple files/photos. The bot waits 2 seconds to group them into a single request.

## Core Commands
- `/ask <text>`: Simple question. (Note: Just sending a message without a slash also works as `/ask`).
- `/memory`: Instantly switch the bot's working directory to your Memory DB.
- `/workdir <path>`: Manually switch to a project folder on your Desktop or Documents.
- `/status`: Check if the bot is busy or idle.
- `/cancel`: Stop Gemini if it's taking too long or producing unwanted output.
- `/mode <creative|precise|default>`: Change how Gemini answers (temperature).

## Task Scheduling
- `/schedule daily 09:00 ask How is my day looking?` -> Runs every day at 9 AM.
- `/schedule every 2h ask Analyze recent logs` -> Runs every 2 hours.
- `/schedule once 2026-05-01T10:00 reminder Meeting starts now` -> One-off task.
- `/tasks`: List all active schedules.
- `/cancel-task <id>`: Stop a scheduled job.

## Admin & Files
- `/files`: Show the names of the last 5 files you uploaded.
- `/health`: Show RAM usage and system uptime.
- `/logs`: (Stub) Instructions on where to find logs on the Mac.
