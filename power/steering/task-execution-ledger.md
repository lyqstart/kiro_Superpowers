# Task Execution Ledger

## Purpose

Kiro task status is useful, but Superpowers execution expects task-level progress and evidence. Use a lightweight ledger when executing implementation plans or multiple tasks.

## Location

```text
.kiro/superpowers-runtime/TASK_EXECUTION_LEDGER.md
```

## Status Words

- PENDING
- IN_PROGRESS
- BLOCKED
- NEEDS_CONTEXT
- COMPLETED
- VERIFIED
- PARTIAL
- UNVERIFIED

## Required Entry

```text
Task: TASK-...
Spec: ...
Requirement/design source: ...
Status: PENDING / IN_PROGRESS / BLOCKED / COMPLETED / VERIFIED
Activated skills: ...
Micro-plan: required / not required / path
Subagents used: ...
RED evidence: ...
GREEN evidence: ...
Review evidence: ...
Fresh verification: ...
Changed files: ...
Risks: ...
Next step: ...
```

## Rules

- Mark one task IN_PROGRESS before work begins.
- Do not mark COMPLETED without review gates.
- Do not mark VERIFIED without fresh verification evidence.
- If blocked, state exact blocker and required user decision.
- Do not continue to the next task while current task is BLOCKED or UNVERIFIED.
