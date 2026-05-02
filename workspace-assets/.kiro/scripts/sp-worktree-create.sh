#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${1:-.}"
TASK_NAME="${2:-kiro-task}"
BASELINE_CMD="${3:-}"

cd "$PROJECT_ROOT"

if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "ERROR: Not inside a git repository." >&2
  exit 1
fi

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

CURRENT_BRANCH="$(git branch --show-current || true)"
if [ -z "$CURRENT_BRANCH" ]; then
  echo "ERROR: Detached HEAD is not supported by this safety script." >&2
  exit 1
fi

STATUS="$(git status --short)"
if [ -n "$STATUS" ]; then
  echo "ERROR: Working tree is not clean. Commit, stash, or resolve changes before creating an isolated worktree." >&2
  echo "$STATUS" >&2
  exit 1
fi

SAFE_TASK="$(printf '%s' "$TASK_NAME" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9._-]+/-/g; s/^-+//; s/-+$//')"
[ -n "$SAFE_TASK" ] || SAFE_TASK="kiro-task"
STAMP="$(date +%Y%m%d-%H%M%S)"
BRANCH="sp/${SAFE_TASK}-${STAMP}"
WORKTREE_DIR="$ROOT/.worktrees/${SAFE_TASK}-${STAMP}"

mkdir -p "$ROOT/.worktrees"

if [ -f "$ROOT/.gitignore" ] && grep -qxF ".worktrees/" "$ROOT/.gitignore"; then
  echo "Gitignore OK: .worktrees/"
else
  echo "NOTICE: .worktrees/ is not listed in .gitignore. Add it if you do not want worktree directories to appear as untracked files."
fi

echo "Creating isolated worktree:"
echo "  branch:   $BRANCH"
echo "  location: $WORKTREE_DIR"
git worktree add -b "$BRANCH" "$WORKTREE_DIR" HEAD

if [ -n "$BASELINE_CMD" ]; then
  echo "Running baseline verification in worktree: $BASELINE_CMD"
  (cd "$WORKTREE_DIR" && bash -lc "$BASELINE_CMD")
else
  echo "No baseline command provided. Baseline verification skipped."
fi

echo "WORKTREE_CREATED=$WORKTREE_DIR"
echo "BRANCH_CREATED=$BRANCH"
