#!/usr/bin/env python3
"""A harmless, visible process for practising tmux detach and reattach."""

from datetime import datetime
from time import sleep

try:
    while True:
        now = datetime.now().astimezone().isoformat(timespec="seconds")
        print(f"{now} — training heartbeat (practice only)", flush=True)
        sleep(2)
except KeyboardInterrupt:
    print("\nHeartbeat stopped.")
