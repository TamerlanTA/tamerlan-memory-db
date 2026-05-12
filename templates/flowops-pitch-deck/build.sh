#!/usr/bin/env bash
# Render an HTML pitch deck to A4 PDF via headless Chrome.
#
# Usage:
#   bash build.sh <input.html> <output.pdf>
#
# Examples:
#   bash build.sh ~/Desktop/MyDeck/index.html ~/Desktop/MyDeck/MyDeck.pdf
#   bash build.sh "./index.html" "./output.pdf"

set -euo pipefail

INPUT="${1:?usage: build.sh <input.html> <output.pdf>}"
OUTPUT="${2:?usage: build.sh <input.html> <output.pdf>}"

# Resolve absolute paths (works even if relative).
INPUT_ABS="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
OUTPUT_ABS="$(cd "$(dirname "$OUTPUT")" 2>/dev/null && pwd || dirname "$OUTPUT")/$(basename "$OUTPUT")"

# Percent-encode the path so Cyrillic/spaces survive the file:// URL.
INPUT_URL="file://$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "$INPUT_ABS")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [[ ! -x "$CHROME" ]]; then
  echo "Chrome not found at: $CHROME" >&2
  exit 1
fi

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --hide-scrollbars \
  --virtual-time-budget=2000 \
  --print-to-pdf-no-header \
  --print-to-pdf="$OUTPUT_ABS" \
  "$INPUT_URL" 2>&1 | grep -E "bytes|ERROR" || true

if [[ -f "$OUTPUT_ABS" ]]; then
  SIZE=$(du -h "$OUTPUT_ABS" | cut -f1)
  echo "✓ PDF written: $OUTPUT_ABS ($SIZE)"
else
  echo "✗ PDF not created" >&2
  exit 1
fi
