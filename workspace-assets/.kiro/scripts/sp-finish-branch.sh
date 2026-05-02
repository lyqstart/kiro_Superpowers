#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${1:-.}"
VERIFY_CMD="${2:-}"
cd "$PROJECT_ROOT"

if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "ERROR: Not inside a git repository." >&2
  exit 1
fi

ROOT="$(git rev-parse --show-toplevel)"
GIT_COMMON_DIR="$(git rev-parse --git-common-dir)"
if [[ "$GIT_COMMON_DIR" != /* ]]; then
  GIT_COMMON_DIR="$ROOT/$GIT_COMMON_DIR"
fi
WORKTREE_PATH="$ROOT"
cd "$ROOT"

CURRENT_BRANCH="$(git branch --show-current || true)"
if [ -z "$CURRENT_BRANCH" ]; then
  echo "ERROR: Detached HEAD is not supported by this safety script." >&2
  exit 1
fi

MAIN_BRANCH=""
if git show-ref --verify --quiet refs/heads/main; then
  MAIN_BRANCH="main"
elif git show-ref --verify --quiet refs/heads/master; then
  MAIN_BRANCH="master"
fi

STATUS="$(git status --short)"
CHANGED_FILES="$(git diff --name-only; git diff --cached --name-only)"
CHANGED_FILES="$(printf '%s\n' "$CHANGED_FILES" | sed '/^$/d' | sort -u)"

if [ -z "$VERIFY_CMD" ]; then
  echo "A fresh verification command is required before branch finishing options are shown."
  read -r -p "请输入 verification 命令；留空则取消 finishing: " VERIFY_CMD
  if [ -z "$VERIFY_CMD" ]; then
    echo "ERROR: Verification command is required before finishing." >&2
    exit 1
  fi
fi

echo "Running fresh verification before branch finishing: $VERIFY_CMD"
set +e
bash -lc "$VERIFY_CMD"
VERIFY_EXIT="$?"
set -e
if [ "$VERIFY_EXIT" -ne 0 ]; then
  echo "ERROR: Verification failed. Do not merge, push PR, or discard as completed." >&2
  exit "$VERIFY_EXIT"
fi

COMMITS=""
if [ -n "$MAIN_BRANCH" ]; then
  COMMITS="$(git log --oneline "$MAIN_BRANCH..$CURRENT_BRANCH" 2>/dev/null || true)"
fi

echo "Branch finishing check"
echo "  repo:      $ROOT"
echo "  branch:    $CURRENT_BRANCH"
echo "  base:      ${MAIN_BRANCH:-not found}"
echo "  worktree:  $WORKTREE_PATH"
echo "  verify:    $VERIFY_CMD"
echo ""
if [ -n "$STATUS" ]; then
  echo "Working tree status:"
  echo "$STATUS"
else
  echo "Working tree status: clean"
fi
if [ -n "$CHANGED_FILES" ]; then
  echo "Changed files:"
  echo "$CHANGED_FILES"
else
  echo "Changed files: none"
fi
if [ -n "$COMMITS" ]; then
  echo "Commits since ${MAIN_BRANCH}:"
  echo "$COMMITS"
else
  echo "Commits since base: none or base unavailable"
fi

cleanup_worktree_prompt() {
  echo ""
  read -r -p "是否清理当前 worktree？输入 CLEAN_WORKTREE 才会执行 git worktree remove: " CLEAN_CONFIRM
  if [ "$CLEAN_CONFIRM" != "CLEAN_WORKTREE" ]; then
    echo "Worktree cleanup skipped."
    return 0
  fi
  local path="$WORKTREE_PATH"
  cd /tmp
  git --git-dir="$GIT_COMMON_DIR" worktree remove "$path"
  echo "Worktree removed: $path"
}

echo ""
echo "Choose next action:"
echo "1. 合并回主分支"
echo "2. 推送并创建 PR"
echo "3. 保留分支"
echo "4. 丢弃本次工作"
read -r -p "请输入 1/2/3/4: " CHOICE

case "$CHOICE" in
  1)
    if [ -z "$MAIN_BRANCH" ]; then
      echo "ERROR: Cannot find main or master branch." >&2
      exit 1
    fi
    if [ -n "$STATUS" ]; then
      echo "ERROR: Working tree has uncommitted changes. Commit them before merging." >&2
      exit 1
    fi
    echo "About to merge $CURRENT_BRANCH into $MAIN_BRANCH."
    echo "Current branch: $CURRENT_BRANCH"
    echo "Base branch: $MAIN_BRANCH"
    echo "Changed files:"
    [ -n "$CHANGED_FILES" ] && echo "$CHANGED_FILES" || echo "none"
    read -r -p "确认合并？输入 '确认合并' 继续: " CONFIRM
    if [ "$CONFIRM" != "确认合并" ]; then
      echo "Merge cancelled."
      exit 0
    fi
    git checkout "$MAIN_BRANCH"
    git merge --no-ff "$CURRENT_BRANCH"
    echo "Merge completed. Suggested: run verification again on $MAIN_BRANCH: $VERIFY_CMD"
    read -r -p "是否现在重新运行验证？输入 RUN_VERIFY 继续: " RUN_VERIFY
    if [ "$RUN_VERIFY" = "RUN_VERIFY" ]; then
      bash -lc "$VERIFY_CMD"
    fi
    cleanup_worktree_prompt
    ;;
  2)
    echo "Pushing current branch: $CURRENT_BRANCH"
    git push -u origin "$CURRENT_BRANCH"
    if command -v gh >/dev/null 2>&1; then
      read -r -p "GitHub CLI detected. 输入 '创建PR' 继续: " CONFIRM_PR
      if [ "$CONFIRM_PR" = "创建PR" ]; then
        gh pr create
      else
        echo "PR creation skipped."
      fi
    else
      echo "Branch pushed. GitHub CLI not found; create PR manually if needed."
    fi
    ;;
  3)
    echo "Keeping branch/worktree unchanged."
    ;;
  4)
    echo "DANGER: This can discard work. Review carefully before confirming."
    echo "Branch: $CURRENT_BRANCH"
    echo "Worktree path: $WORKTREE_PATH"
    echo "Changed files:"
    [ -n "$CHANGED_FILES" ] && echo "$CHANGED_FILES" || echo "none"
    echo "Commits since ${MAIN_BRANCH:-base}:"
    [ -n "$COMMITS" ] && echo "$COMMITS" || echo "none or base unavailable"
    read -r -p "二次确认：输入 DISCARD_WORK 才会丢弃未提交改动: " CONFIRM_DELETE
    if [ "$CONFIRM_DELETE" != "DISCARD_WORK" ]; then
      echo "Discard cancelled."
      exit 0
    fi
    git reset --hard
    git clean -fd
    echo "Uncommitted changes discarded in current worktree."
    cleanup_worktree_prompt
    ;;
  *)
    echo "Invalid choice. No action taken."
    exit 1
    ;;
esac
