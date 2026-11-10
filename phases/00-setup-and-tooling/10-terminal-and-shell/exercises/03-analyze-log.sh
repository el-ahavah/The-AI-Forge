#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LOG="$SCRIPT_DIR/sample-training.log"

cat > "$LOG" <<'LOGEOF'
2026-11-10 09:00:00 INFO epoch=1 step=10 loss=1.250 accuracy=0.62
2026-11-10 09:00:05 INFO epoch=1 step=20 loss=1.080 accuracy=0.68
2026-11-10 09:00:10 WARNING epoch=1 step=30 loss=0.940 accuracy=0.71
2026-11-10 09:00:15 INFO epoch=1 step=40 loss=0.810 accuracy=0.75
2026-11-10 09:00:20 ERROR epoch=1 step=50 loss=nan accuracy=0.00 message=non_finite_loss
2026-11-10 09:00:25 INFO epoch=2 step=10 loss=0.720 accuracy=0.78
2026-11-10 09:00:30 INFO epoch=2 step=20 loss=0.610 accuracy=0.81
LOGEOF

echo "== Matching loss lines (grep) =="
grep -n 'loss=' "$LOG"
echo
echo "== Warnings and errors (grep) =="
grep -nE 'WARNING|ERROR' "$LOG"
echo
echo "== Last five lines (tail) =="
tail -n 5 "$LOG"
echo
echo "== Loss values (awk) =="
awk '{
  for (i=1; i<=NF; i++) {
    if ($i ~ /^loss=/) {
      split($i, part, "=")
      print part[2]
    }
  }
}' "$LOG"
echo
printf 'Error count: '
grep -c 'ERROR' "$LOG" || true
echo "Sample log saved at: $LOG"
