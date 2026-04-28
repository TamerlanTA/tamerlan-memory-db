# Project Map: Gemini Telegram Bridge

## Overview
A secure Node.js + TypeScript bridge to control Gemini CLI via Telegram with multimodal and scheduling support.

## Key Path
- **Project Root**: `/Users/tamerlan/gemini-telegram-bridge`
- **Memory Vault Integrated**: `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`

## Architecture
- **Runtime**: Node.js (v25+)
- **Process Manager**: PM2
- **Database**: SQLite (`data/bridge.sqlite`) for tasks, settings, and audit logs.
- **Security**: 
  - Restricted to `ALLOWED_TELEGRAM_USER_IDS`.
  - Filesystem access limited to specific `ALLOWED_WORKSPACE_ROOTS`.
  - Child processes (Gemini CLI) have strict timeouts.

## File Structure
- `src/index.ts`: Entry point.
- `src/commandRouter.ts`: Central logic for command routing.
- `src/commands.ts`: Implementation of all 40+ commands.
- `src/scheduler.ts`: Persistent task scheduling (SQLite based).
- `src/fileService.ts`: Multimodal file handling (Photos/Docs).
- `src/geminiRunner.ts`: Secure execution of Gemini CLI.
- `logs/runs/`: Session logs for every single Gemini execution.
