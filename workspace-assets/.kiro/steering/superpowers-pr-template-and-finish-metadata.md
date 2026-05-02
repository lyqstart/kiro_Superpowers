# Superpowers PR Template and Finish Metadata

## Purpose

Harden branch finishing and PR creation without making destructive choices automatic.

## PR Body Template

When user chooses PR path, prepare or request this structure:

```markdown
## Summary
- ...

## Spec / Task
- Spec: ...
- Requirement: ...
- Task(s): ...

## Test Plan
- [ ] Command: ... Result: ...

## Review Evidence
- Spec review: ...
- Code review: ...
- Fresh verification: ...

## Risks / Follow-ups
- ...
```

## Finish Metadata

Before merge/PR/keep/discard, record:

```text
.kiro/superpowers-runtime/FINISH_METADATA.md
```

Fields:

- branch
- base branch
- worktree path
- changed files
- commits
- verification evidence
- chosen option
- cleanup decision

## Safety

Cleaning worktree remains explicit. Do not default-delete.
