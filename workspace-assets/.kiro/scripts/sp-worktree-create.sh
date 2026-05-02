#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${1:-.}"
TASK_NAME="${2:-kiro-task}"
BASELINE_CMD="${3:-}"
RELATED_SPEC_TASK="${4:-}"

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
METADATA_DIR="$ROOT/.worktrees/.metadata"
METADATA_FILE="$METADATA_DIR/${SAFE_TASK}-${STAMP}.json"

mkdir -p "$ROOT/.worktrees" "$METADATA_DIR"

ensure_gitignore() {
  local gitignore="$ROOT/.gitignore"
  if [ -f "$gitignore" ] && grep -qxF ".worktrees/" "$gitignore"; then
    echo "Gitignore OK: .worktrees/"
    return 0
  fi
  echo "WARNING: .worktrees/ is not listed in .gitignore."
  echo "This can make isolated worktree directories appear as untracked files."
  read -r -p "Add .worktrees/ to .gitignore now? 输入 y 添加，其他任意键跳过: " ADD_GITIGNORE
  if [ "$ADD_GITIGNORE" = "y" ] || [ "$ADD_GITIGNORE" = "Y" ]; then
    touch "$gitignore"
    printf '\n.worktrees/\n' >> "$gitignore"
    echo "Added .worktrees/ to .gitignore."
    echo "NOTE: This script does not auto-commit .gitignore. Review and commit it yourself if appropriate."
  else
    echo "Skipped .gitignore update. Continuing only because user explicitly skipped."
  fi
}

detect_baseline_cmd() {
  if [ -n "$BASELINE_CMD" ]; then
    printf '%s' "$BASELINE_CMD"
    return 0
  fi
  if [ -f "package.json" ]; then
    if grep -q '"test"[[:space:]]*:' package.json; then
      if [ -f "pnpm-lock.yaml" ] && command -v pnpm >/dev/null 2>&1; then printf 'pnpm test'; return 0; fi
      if [ -f "yarn.lock" ] && command -v yarn >/dev/null 2>&1; then printf 'yarn test'; return 0; fi
      if command -v npm >/dev/null 2>&1; then printf 'npm test'; return 0; fi
    fi
  fi
  if [ -f "go.mod" ] && command -v go >/dev/null 2>&1; then printf 'go test ./...'; return 0; fi
  if [ -f "Cargo.toml" ] && command -v cargo >/dev/null 2>&1; then printf 'cargo test'; return 0; fi
  if [ -d "tests" ] && command -v pytest >/dev/null 2>&1; then printf 'pytest'; return 0; fi
  if [ -f "pyproject.toml" ] && command -v pytest >/dev/null 2>&1; then printf 'pytest'; return 0; fi
  return 1
}

json_escape() {
  python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().rstrip("\n")))'
}

ensure_gitignore

BASELINE_RESULT="not-run"
BASELINE_EXIT=""
DETECTED_BASELINE=""
if DETECTED_BASELINE="$(detect_baseline_cmd)"; then
  echo "Baseline verification command: $DETECTED_BASELINE"
else
  echo "WARNING: Could not identify a baseline verification command automatically."
  read -r -p "请输入 baseline 验证命令；留空则取消创建 worktree: " DETECTED_BASELINE
  if [ -z "$DETECTED_BASELINE" ]; then
    echo "ERROR: Baseline command is required unless the user explicitly decides to stop. Worktree creation cancelled." >&2
    exit 1
  fi
fi

echo "Creating isolated worktree:"
echo "  base:     $CURRENT_BRANCH"
echo "  branch:   $BRANCH"
echo "  location: $WORKTREE_DIR"
git worktree add -b "$BRANCH" "$WORKTREE_DIR" HEAD

echo "Running baseline verification in worktree: $DETECTED_BASELINE"
set +e
(cd "$WORKTREE_DIR" && bash -lc "$DETECTED_BASELINE")
BASELINE_EXIT="$?"
set -e
if [ "$BASELINE_EXIT" -eq 0 ]; then
  BASELINE_RESULT="passed"
else
  BASELINE_RESULT="failed"
fi

CREATED_TIME="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
cat > "$METADATA_FILE" <<JSON
{
  "worktree_path": $(printf '%s' "$WORKTREE_DIR" | json_escape),
  "branch_name": $(printf '%s' "$BRANCH" | json_escape),
  "base_branch": $(printf '%s' "$CURRENT_BRANCH" | json_escape),
  "created_time": $(printf '%s' "$CREATED_TIME" | json_escape),
  "related_spec_task": $(printf '%s' "$RELATED_SPEC_TASK" | json_escape),
  "task_name": $(printf '%s' "$TASK_NAME" | json_escape),
  "baseline_command": $(printf '%s' "$DETECTED_BASELINE" | json_escape),
  "baseline_result": $(printf '%s' "$BASELINE_RESULT" | json_escape),
  "baseline_exit_code": $BASELINE_EXIT
}
JSON

echo "Metadata written: $METADATA_FILE"
if [ "$BASELINE_EXIT" -ne 0 ]; then
  echo "ERROR: Baseline verification failed in the new worktree. Do not continue implementation unless the user explicitly confirms." >&2
  echo "WORKTREE_CREATED=$WORKTREE_DIR"
  echo "BRANCH_CREATED=$BRANCH"
  echo "METADATA_FILE=$METADATA_FILE"
  exit "$BASELINE_EXIT"
fi

echo "WORKTREE_CREATED=$WORKTREE_DIR"
echo "BRANCH_CREATED=$BRANCH"
echo "METADATA_FILE=$METADATA_FILE"
echo "BASELINE_RESULT=$BASELINE_RESULT"
