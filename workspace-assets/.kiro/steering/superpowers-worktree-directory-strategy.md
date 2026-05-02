# Superpowers Worktree Directory Strategy

## Purpose

Bring worktree selection closer to Superpowers while keeping Kiro package safe.

## Directory Preference

When creating a worktree, choose in this order:

1. Project `.worktrees/` if exists or user accepts.
2. Project `worktrees/` if exists or user accepts.
3. Project documented preference in `.kiro/steering`, README, AGENTS.md, CLAUDE.md, or similar.
4. User-specified directory.
5. Global fallback only if explicitly configured.

## Ignore Rules

- If using project-local `.worktrees/` or `worktrees/`, check `.gitignore`.
- If not ignored, ask user whether to add it.
- Do not automatically commit `.gitignore`.
- Do not modify ignore rules without explicit confirmation.

## Metadata

Continue writing worktree metadata as v1.2 introduced.

## Safety

Never delete worktrees, branches, or untracked files without explicit typed confirmation.
