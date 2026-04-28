# Operations & Security Manual

## Management (PM2)
- **Check Status**: `pm2 status`
- **View Real-time Logs**: `pm2 logs gemini-bridge`
- **Restart**: `pm2 restart gemini-bridge`
- **Persistence**: To ensure auto-start after Mac reboot, run `pm2 save`.

## Security Policies
- **Allowlist**: Only IDs in `.env` can interact.
- **Secret Handling**: Never print secrets from `.env`.
- **Filesystem**: Operations are locked within:
  - Desktop
  - Documents
  - Memory DB
  - Downloads

## Backup & Export
- **Database**: The file `data/bridge.sqlite` contains all tasks and history.
- **Manual Backup**: `cp gemini-telegram-bridge/data/bridge.sqlite ./backup.sqlite`

## Troubleshooting
- **ETELEGRAM 404**: Bot Token is invalid.
- **Access Denied**: Telegram ID is missing from `ALLOWED_TELEGRAM_USER_IDS`.
- **Compile Error**: Run `npm run build` after any manual source changes.
