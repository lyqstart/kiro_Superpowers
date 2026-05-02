# Superpowers Final Whole-Feature Review Gate

## Purpose

Superpowers reviews after tasks and before merge. v2.0 adds a whole-feature gate after all Kiro tasks in a spec or feature are complete.

## When Required

Run before branch finishing, PR creation, merge, or any final COMPLETE claim for a feature/spec.

## Required Checks

1. Spec coverage: every requirement has implementation and verification evidence.
2. Design coverage: implementation follows approved design or deviations are documented and approved.
3. Task coverage: every required Kiro task is completed/verified or explicitly deferred.
4. Diff coverage: changed files match scope; no unrelated refactor.
5. TDD evidence: RED/GREEN/REFACTOR evidence exists where required.
6. Review evidence: spec review and code review completed.
7. Fresh verification: latest verification evidence is present.
8. Risks: remaining risks listed with owner/decision.
9. Branch finishing: user gets finish options.

## Final Review Result

```text
Final Whole-Feature Review
Status: APPROVED / BLOCKED / PARTIAL / UNVERIFIED
Spec: ...
Requirement coverage: ...
Design deviations: ...
Task coverage: ...
Changed files: ...
Fresh verification evidence: ...
Open blockers: ...
Open major issues: ...
Risks: ...
Allowed next step: branch finishing / ask user / return to implementation
```

No final COMPLETE without APPROVED.
