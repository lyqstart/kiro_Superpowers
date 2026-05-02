#!/usr/bin/env bash
set -euo pipefail
SKILL=""
PURPOSE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --skill) SKILL="${2:-}"; shift 2;;
    --purpose) PURPOSE="${2:-}"; shift 2;;
    *) echo "Unknown arg: $1" >&2; exit 2;;
  esac
done
if [[ -z "$SKILL" ]]; then echo "--skill required" >&2; exit 2; fi
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
RUNTIME="$ROOT/.kiro/superpowers-runtime"
mkdir -p "$RUNTIME"
LEDGER="$RUNTIME/SKILL_ACTIVATION_LEDGER.md"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
{
  echo ""
  echo "## $TS | $SKILL"
  echo "- Purpose: ${PURPOSE:-not specified}"
  echo "- Status: activated"
} >> "$LEDGER"
echo "Skill activated: $SKILL"
echo "Ledger: $LEDGER"
