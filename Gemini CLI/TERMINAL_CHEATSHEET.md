# Terminal & Maintenance Cheatsheet

## Basic Control (PM2)
- **Check if running**: `pm2 status`
- **Restart (after Mac update/reboot)**: `pm2 restart gemini-bridge`
- **Stop**: `pm2 stop gemini-bridge`
- **View Live Logs**: `pm2 logs gemini-bridge`
- **Check Errors only**: `pm2 logs gemini-bridge --err`

## Development & Updates
- **Path to Project**: `cd /Users/tamerlan/gemini-telegram-bridge`
- **Update after code changes**: 
  1. `npm run build`
  2. `pm2 restart gemini-bridge`
- **Fix "gemini command not found"**:
  1. `export PATH="$PATH:/usr/local/bin"`
  2. `source ~/.zshrc`

## Database Access
- **Location**: `gemini-telegram-bridge/data/bridge.sqlite`
- **Audit Log**: To see who used the bot: 
  `sqlite3 data/bridge.sqlite "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT 10;"`

## Critical Path Security
If you need to move the bot to a new Mac:
1. Copy the folder.
2. Run `npm install`.
3. Copy `.env` manually (it is hidden).
4. Run `pm2 start dist/index.js --name gemini-bridge`.
