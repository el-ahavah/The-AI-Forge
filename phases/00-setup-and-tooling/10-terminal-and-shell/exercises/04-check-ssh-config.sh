#!/usr/bin/env bash
set -euo pipefail

if ! command -v ssh >/dev/null 2>&1; then
  echo "OpenSSH client is required." >&2
  exit 1
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
CONFIG="$TMP_DIR/config"
CURRENT_USER="$(id -un)"

cat > "$CONFIG" <<EOF
Host lesson10-local
    HostName localhost
    User $CURRENT_USER
    Port 22
    ServerAliveInterval 30
EOF
chmod 600 "$CONFIG"

echo "Resolved configuration (ssh -G):"
ssh -F "$CONFIG" -G lesson10-local | grep -E '^(hostname|user|port|serveraliveinterval) '
echo
echo "Safe check only: no SSH connection was opened."
echo "Your ~/.ssh/config was not changed."
