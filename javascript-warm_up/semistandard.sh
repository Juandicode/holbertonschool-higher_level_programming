#!/usr/bin/env bash
#
# chmod_and_lint.sh — mark warm‑up JS files executable and validate with semistandard

set -e  # exit on any error
shopt -s nullglob

# List of your exercise files:
FILES=(
  "0-javascript_is_amazing.js"
  "1-multi_languages.js"
  "2-arguments.js"
  "3-value_argument.js"
  "4-concat.js"
  "5-to_integer.js"
  "6-multi_languages_loop.js"
  "7-multi_c.js"
  "8-square.js"
  "9-add.js"
  "10-factorial.js"
  "11-second_biggest.js"
  "12-object.js"
  "13-add.js"
)

# Determine script location and target directory
SCRIPT_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
if [ -d "$SCRIPT_DIR/javascript-warm_up" ]; then
  TARGET_DIR="$SCRIPT_DIR/javascript-warm_up"
else
  TARGET_DIR="$SCRIPT_DIR"
fi

echo "⮕ Operating in: $TARGET_DIR"
cd "$TARGET_DIR"

# Ensure semistandard is installed
if ! command -v semistandard &> /dev/null; then
  echo "❌ semistandard is not installed. Install it with 'npm install -g semistandard'."
  exit 1
fi

# Loop through files
FAILED=0
for f in "${FILES[@]}"; do
  if [ -f "$f" ]; then
    # 1) Make executable
    chmod u+x "$f"
    echo "✔ chmod +x $f"

    # 2) Run semistandard
    if semistandard "$f"; then
      echo "✔ semistandard passed: $f"
    else
      echo "❌ semistandard failed: $f"
      FAILED=1
    fi
  else
    echo "⚠ file not found (skipped): $f"
  fi
done

if [ $FAILED -eq 1 ]; then
  echo ""
  echo "One or more files failed semistandard. Fix lint errors and run again."
  exit 2
else
  echo ""
  echo "All files marked executable and semistandard checks passed ✅"
fi
