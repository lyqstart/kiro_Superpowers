# Worktree Hardening v1.2.0

## Purpose

Strengthen the existing worktree automation without changing the user's daily entrypoints. Implementation-class work should be isolated, baseline-verified, and recorded with metadata before code edits begin.

## Required behavior

Before creating a worktree, Kiro must ensure:

1. The repository is a git repository.
2. The current branch is not detached.
3. The working tree is clean.
4. `.worktrees/` is checked against `.gitignore`.
5. If `.worktrees/` is not ignored, ask whether to add it.
6. Do not auto-commit `.gitignore` unless the user explicitly confirms in a separate step.
7. Record metadata after the worktree is created.

## Worktree metadata contract

After creating a worktree, record metadata containing:

- worktree path
- branch name
- base branch
- created time
- related spec/task
- baseline command
- baseline result
- baseline exit code

The provided scripts write metadata under `.worktrees/.metadata/`.

## Baseline verification

After creating a worktree, attempt baseline verification.

Prefer the explicit command provided by the user or task packet. If no command is provided, infer common commands when safe:

- `pnpm test`
- `yarn test`
- `npm test`
- `pytest`
- `go test ./...`
- `cargo test`

If no baseline command can be identified, ask the user to provide one. Do not continue implementation without a baseline command unless the user explicitly decides to stop or handle baseline manually.

If baseline fails, stop. Do not continue implementation unless the user explicitly confirms that the baseline failure is known and acceptable.

## Safety rules

- Do not delete user code by default.
- Do not auto-commit `.gitignore`.
- Do not continue implementation after a dirty tree or failed baseline.
- Do not treat worktree creation as success without metadata and baseline result.
