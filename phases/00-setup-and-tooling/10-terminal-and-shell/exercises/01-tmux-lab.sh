#!/usr/bin/env bash
set -euo pipefail

SESSION="lesson10-lab"
if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux is required. On Ubuntu/Debian: sudo apt install tmux" >&2
  exit 1
fi

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "Attaching to existing session: $SESSION"
  exec tmux attach -t "$SESSION"
fi

MONITOR="top"
command -v htop >/dev/null 2>&1 && MONITOR="htop"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
HEARTBEAT_SCRIPT="$SCRIPT_DIR/heartbeat.py"

tmux new-session -d -s "$SESSION" "$MONITOR"
tmux split-window -h -t "$SESSION:0.0" "watch -n1 date"
tmux split-window -v -t "$SESSION:0.1" "python3 -u \"$HEARTBEAT_SCRIPT\""
tmux select-layout -t "$SESSION:0" tiled

echo "Three-pane session created. Detach with Ctrl+B then D."
echo "Reattach: tmux attach -t $SESSION"
exec tmux attach -t "$SESSION"
