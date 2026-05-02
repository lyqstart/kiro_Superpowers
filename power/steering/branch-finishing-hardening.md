# Branch Finishing Hardening v1.2.0

## Purpose

Make branch finishing safer and closer to Superpowers discipline while preserving the existing four-option user experience.

## Required behavior before showing options

Before displaying finishing options, Kiro must have fresh verification evidence. The finishing script requires a verification command before showing options.

If verification fails:

- Do not merge.
- Do not push as ready.
- Do not mark the task complete.
- Report NOT COMPLETE or BLOCKED.

## Required context display

Before merge or discard, display:

- current branch
- base branch
- worktree path
- working tree status
- changed files
- commits since base branch when available
- verification command used

## Four finishing options remain unchanged

1. 合并回主分支
2. 推送并创建 PR
3. 保留分支
4. 丢弃本次工作

Do not select for the user.

## Merge hardening

Before merge:

- working tree must be clean
- current branch and base branch must be shown
- changed files must be shown
- user must explicitly type `确认合并`

After merge:

- recommend re-running verification on the base branch
- allow the user to run it immediately
- offer worktree cleanup as a separate confirmation

## Discard hardening

Before discard:

- show branch name
- show worktree path
- show changed files
- show commits since base
- require explicit confirmation: `DISCARD_WORK`

After discard:

- do not remove worktree automatically
- offer worktree cleanup as a separate confirmation
- cleanup requires explicit confirmation: `CLEAN_WORKTREE`

## Safety rules

- Never delete user code by default.
- Dangerous operations require explicit typed confirmation.
- Cleanup is separate from merge/discard.
- If context is unclear, stop and ask.
