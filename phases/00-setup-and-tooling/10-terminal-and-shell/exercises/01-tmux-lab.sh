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
HEARTBEAT="python3 -u -c 'import time; from datetime import datetime; exec(\"while True:\\n print(datetime.now().astimezone().isoformat(timespec=\\\"seconds\\\"), \\\"— training heartbeat\\\", flush=True); time.sleep(2)\")'"

tmux new-session -d -s "$SESSION" "$MONITOR"
tmux split-window -h -t "$SESSION:0.0" "watch -n1 date"
tmux split-window -v -t "$SESSION:0.1" "$HEARTBEAT"
tmux select-layout -t "$SESSION:0" tiled

echo "Three-pane session created. Detach with Ctrl+B then D."
echo "Reattach: tmux attach -t $SESSION"
exec tmux attach -t "$SESSION"
