#!/bin/zsh
set -euo pipefail

REPO_DIR="/Users/amol/Library/Mobile Documents/com~apple~CloudDocs/Documents/root/tokyo-postcard"
PUSH_SCRIPT="/usr/local/bin/push_tokyo_postcard.sh"
DEFAULT_MESSAGE="Auto update"

cd "$REPO_DIR"

# Skip if you’re not on main (prevents accidental branch pushes)
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [[ "$current_branch" != "main" ]]; then
  exit 0
fi

# Exit quietly if nothing changed
if git status --short --untracked-files=normal | grep -q '.'; then
  "$PUSH_SCRIPT" "$DEFAULT_MESSAGE"
fi

