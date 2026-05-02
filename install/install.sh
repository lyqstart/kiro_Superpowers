#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE="$PACKAGE_ROOT/workspace-assets/.kiro"
TARGET="$(cd "$PROJECT_ROOT" && pwd)/.kiro"

if [ ! -d "$SOURCE" ]; then
  echo "Source assets not found: $SOURCE" >&2
  exit 1
fi

echo "Installing Kiro Superpowers Discipline v0.6.0"
echo "Project: $(cd "$PROJECT_ROOT" && pwd)"

mkdir -p "$TARGET/steering" "$TARGET/hooks" "$TARGET/agents" "$TARGET/scripts"

copy_dir() {
  local dir="$1"
  if [ -d "$SOURCE/$dir" ]; then
    for f in "$SOURCE/$dir"/*; do
      [ -f "$f" ] || continue
      cp -f "$f" "$TARGET/$dir/"
      echo "Installed: $TARGET/$dir/$(basename "$f")"
    done
  fi
}

copy_dir steering
copy_dir hooks
copy_dir agents
copy_dir scripts

if command -v python3 >/dev/null 2>&1; then
  python3 - "$TARGET/hooks" <<'PYINSTALL'
import json, sys
from pathlib import Path
hook_dir = Path(sys.argv[1])
for p in hook_dir.glob('*.kiro.hook'):
    json.loads(p.read_text(encoding='utf-8'))
    print(f'Hook JSON OK: {p.name}')
PYINSTALL
fi

echo ""
echo "Installed workspace files."
echo "Now add the Power in Kiro: Powers -> Add power from Local Path -> $PACKAGE_ROOT/power"
echo "Daily use: say '新增xxx', '修复xxx', or '继续当前 spec 的下一个任务'."
