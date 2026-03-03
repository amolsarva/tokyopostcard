# Auto Push Workflow

## Files
- /usr/local/bin/push_tokyo_postcard.sh – stages/commits/pushes, auto-fetches/rebases, retries once if remote wins the race.
- /usr/local/bin/push_tokyo_postcard_if_dirty.sh – checks for changes on main and calls the push helper.
- ~/Library/LaunchAgents/com.amol.tokyo-postcard-auto-push.plist – LaunchAgent that runs the helper every 60 s at login.

## How it works
1. LaunchAgent wakes every minute (and at login).
2. `push_tokyo_postcard_if_dirty.sh` runs inside the repo; if `git status` is clean it exits.
3. When dirty, `push_tokyo_postcard.sh` fetches origin/main, rebases with autostash, commits with “Auto update”, and pushes.

## Manual controls
- Trigger immediately: `launchctl kickstart -k gui/$UID/com.amol.tokyo-postcard-auto-push`
- Pause: `launchctl unload ~/Library/LaunchAgents/com.amol.tokyo-postcard-auto-push.plist`
- Resume: `launchctl load -w ~/Library/LaunchAgents/com.amol.tokyo-postcard-auto-push.plist`

## Logs
- Success/output: `/tmp/tokyo-postcard-auto-push.out`
- Errors: `/tmp/tokyo-postcard-auto-push.err`

## Troubleshooting
- If you see “Operation not permitted”, re-check Full Disk Access for `/bin/zsh`, `/usr/bin/git`, and `/usr/local/bin/push_tokyo_postcard_if_dirty.sh`.
- If pushes are rejected, the helper already retries after an auto-rebase; inspect logs if it still fails.
