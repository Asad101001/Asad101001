#!/usr/bin/env bash
set -euo pipefail
OUT_DIR="assets"
OUT_FILE="$OUT_DIR/github-contribution-grid-snake.svg"
mkdir -p "$OUT_DIR"
if ! command -v snk >/dev/null 2>&1; then
  echo "snk not found — installing globally"
  npm install -g snk
fi
snk --username Asad101001 --color "#00FFB3" --output "$OUT_FILE"
echo "Wrote: $OUT_FILE"
