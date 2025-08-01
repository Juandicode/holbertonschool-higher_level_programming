#!/usr/bin/env bash
#
# chmod_js.sh — mark all JS warm‑up files executable for the user

# List all the target files
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

# Determine where to run: if a subfolder javascript-warm_up exists next to this script, use it.
SCRIPT_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
if [ -d "$SCRIPT_DIR/javascript-warm_up" ]; then
  TARGET_DIR="$SCRIPT_DIR/javascript-warm_up"
else
  TARGET_DIR="$SCRIPT_DIR"
fi

echo "⮕ Applying chmod in: $TARGET_DIR"
cd "$TARGET_DIR" || { echo "❌ Cannot cd into $TARGET_DIR"; exit 1; }

# Apply chmod u+x to each file
for f in "${FILES[@]}"; do
  if [ -f "$f" ]; then
    chmod u+x "$f"
    echo "✔ marked executable: $f"
  else
    echo "⚠ file not found: $f"
  fi
done
