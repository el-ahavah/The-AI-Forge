#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ALIAS_FILE="$(cd -- "$SCRIPT_DIR/../code" && pwd)/shell_aliases.sh"
TARGET="${1:-$HOME/.bashrc}"
SOURCE_LINE="source \"$ALIAS_FILE\""

if [[ ! -f "$ALIAS_FILE" ]]; then
  echo "Aliases file not found: $ALIAS_FILE" >&2
  exit 1
fi

mkdir -p "$(dirname -- "$TARGET")"
touch "$TARGET"
if grep -Fqx "$SOURCE_LINE" "$TARGET"; then
  echo "Already configured in $TARGET"
  exit 0
fi

BACKUP="$TARGET.lesson10-backup-$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET" "$BACKUP"
printf '\n# AI Engineering from Scratch — Lesson 10 aliases\n%s\n' "$SOURCE_LINE" >> "$TARGET"
echo "Added aliases to $TARGET"
echo "Backup: $BACKUP"
echo "Review shell_aliases.sh, then run: source \"$TARGET\""
