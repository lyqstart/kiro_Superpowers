# Branch Finishing Discipline

Purpose: close implementation work safely after verification, without silently merging or deleting anything.

## When to use

Use this after an implementation-class Kiro task or bugfix task has passed verification.

Do not use it for read-only analysis or documentation-only discussion.

## Required finishing flow

After tests/review pass, present exactly these numbered options:

1. 合并回主分支
2. 推送并创建 PR
3. 保留分支
4. 丢弃本次工作

Do not choose for the user.

## Safety gates

Before presenting options:

1. Show current branch.
2. Show current worktree path.
3. Show changed files summary.
4. Show verification evidence.
5. If verification is missing or failed, do not offer merge as a ready option.

## Discard rule

Discarding work is destructive. It must require a second explicit confirmation.

Acceptable confirmation examples:

```text
确认丢弃
DELETE
```

Without confirmation, do not discard and do not clean up the worktree.

## Script usage

Use package-installed scripts when appropriate:

- Windows: `.kiro/scripts/sp-finish-branch.ps1`
- macOS/Linux: `.kiro/scripts/sp-finish-branch.sh`

Scripts are safety helpers. They must not bypass user confirmation.
