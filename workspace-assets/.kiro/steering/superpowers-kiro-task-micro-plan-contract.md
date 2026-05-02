# Superpowers Kiro Task Micro-Plan Contract

## Purpose

Bring Superpowers `writing-plans` granularity into Kiro tasks without creating a separate `docs/superpowers/plans` source of truth.

## When Required

Before implementing a Kiro task, create a micro-plan if any of these are true:

- The task touches more than one module.
- The task changes behavior.
- The task affects tests, APIs, DB, queue, auth, data transformation, or UI flow.
- The task would take more than one clear verification loop.
- The task lacks exact files or commands.

## Micro-Plan Required Fields

```text
Micro-Plan for TASK-...
Goal: ...
Requirement/design source: ...
Files to create: ...
Files to modify: ...
Files not allowed: ...
Test file(s): ...
Steps:
1. Write failing test: command + expected failure
2. Implement minimal change: files + exact intent
3. Run green verification: command + expected result
4. Refactor if needed: files + verification
5. Review: spec/code/test
6. Commit suggestion: message
```

## Granularity Rule

Each step must be small enough to verify independently. For complex work, prefer 2-5 minute steps similar to Superpowers plans. Do not require this for trivial read-only or documentation-only tasks.

## No Placeholder Rule

Never allow:

- TBD
- TODO
- implement later
- appropriate error handling without specifics
- write tests without test name/path/command
- similar to previous without repeated details

## Gate

If no micro-plan is required, state why. If required and missing, do not implement.
