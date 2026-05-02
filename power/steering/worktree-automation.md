# Worktree Automation Discipline

Purpose: keep implementation work isolated without making the user manage git worktrees manually.

## When worktree is required

Default to the worktree flow for implementation-class work:

- feature implementation
- bugfix that edits code
- refactor
- database migration
- API/interface changes
- task execution from `.kiro/specs/**/tasks.md`

Do not force a worktree for:

- read-only analysis
- documentation-only edits
- typo/text-only changes
- installation/configuration explanation
- inspection/review that does not edit files

## Gate before implementation

Before editing code for an implementation-class task:

1. Check whether the workspace is a git repository.
2. Check current branch.
3. Check `git status --short`.
4. If current branch is `main` or `master`, do not edit there by default.
5. If the tree is dirty, stop and ask the user whether to commit/stash/continue manually. Do not hide or overwrite changes.
6. Prefer creating a worktree under `.worktrees/` using the package script:
   - Windows: `.kiro/scripts/sp-worktree-create.ps1`
   - macOS/Linux: `.kiro/scripts/sp-worktree-create.sh`
7. If a baseline test command is known, run it in the new worktree before implementation.
8. If baseline verification fails, report it and ask before continuing.

## User-facing behavior

Do not ask the user to understand git worktree details unless there is a conflict or risk.

Good:

```text
当前是实现类任务，并且当前分支是 main。我会先创建隔离 worktree，再执行任务。
```

Bad:

```text
请你手动运行 git worktree add ...
```

## Safety rules

- Never delete a worktree automatically.
- Never force clean user changes.
- Never merge automatically.
- Never discard work without explicit user confirmation.
- If git state is unclear, stop and report.
