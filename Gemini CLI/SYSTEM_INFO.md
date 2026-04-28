# System Architecture & Tech Stack

## Core Engine
- **Language**: TypeScript (Node.js v25.8.0)
- **Framework**: Custom Bridge for Gemini CLI
- **Process Manager**: PM2 (Daemon mode)
- **Database**: SQLite 3 (`better-sqlite3`)
- **OS**: Darwin (macOS)
- **Bot Library**: `node-telegram-bot-api`

## Security Layer
- **Access Control**: Strict Telegram ID white-listing.
- **Filesystem Sandbox**: The bot is forbidden to access system folders (Library, .ssh, etc.). It can only work in:
  - `/Users/tamerlan/Desktop`
  - `/Users/tamerlan/Documents`
  - `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`
  - `/Users/tamerlan/Downloads`
- **Secret Protection**: `.env` values are never printed in logs or sent to Telegram.

## Data Storage
- **`data/bridge.sqlite`**: Tasks, logs, and audit data.
- **`logs/bridge.log`**: General system events.
- **`logs/runs/`**: Full history of every Gemini execution (unique log for each run).
- **`data/uploads/`**: Multimedia files received from you.
