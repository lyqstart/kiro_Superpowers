# TDD Violation Recovery Rule

## Purpose

Close the gap with Superpowers TDD: if production code was written before a failing test, the agent must not pretend TDD happened.

## Detection Signals

Treat these as possible TDD violations:

- No RED evidence before implementation.
- Test was added after implementation.
- Test passed immediately without proving the failure.
- GREEN evidence exists but RED evidence is missing.
- Behavior changed with no test or approved exception.

## Required Recovery

If a violation is detected:

1. Stop implementation work.
2. Report `TDD_VIOLATION_DETECTED`.
3. Explain what evidence is missing.
4. If safe and small, revert the implementation change and write the failing test first.
5. If revert is unsafe, ask user whether to:
   1. revert and redo TDD,
   2. keep code and create characterization test,
   3. accept a documented TDD exception.
6. Do not claim COMPLETE until the recovery path is documented and verified.

## Testing Anti-Patterns Gate

Reject or flag tests that:

- Assert implementation details instead of behavior.
- Mock the unit under test.
- Only test the happy path when bug was edge-case.
- Do not fail for the intended reason.
- Depend on fixed sleep when condition-based waiting is possible.

## Output

```text
TDD Recovery Status: clean / violation-detected / exception-approved
Missing evidence: ...
Recovery path: ...
User approval required: yes/no
Verification after recovery: ...
```
