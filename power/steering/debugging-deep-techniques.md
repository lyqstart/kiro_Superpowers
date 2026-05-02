# v1.3 Debugging Deep Techniques

This steering file hardens Superpowers-style systematic debugging inside Kiro. It applies to bugfix work, failing tests, production errors, async flakes, integration failures, and repeated failed fixes.

## 1. Root-cause tracing

Debugging must trace from observable failure to root cause before any fix is made.

Required chain:

```text
Observable error: ...
Input / trigger: ...
Expected behavior: ...
Actual behavior: ...
Where data changes: ...
First bad component/output: ...
Failing condition: ...
Root cause: ...
Evidence: ...
```

Rules:

- Do not repair a symptom when the root cause is unknown.
- Do not patch based on a guess.
- If the root cause is not found, return `BLOCKED` or `NEEDS_CONTEXT`; do not enter implementation.
- A bugfix may proceed only after a reproducible failure and a root-cause hypothesis have been verified.

## 2. Defense in depth

When fixing a bug, decide whether a single-point fix is enough or whether multiple defensive layers are needed.

Check at least:

- Input validation.
- Boundary conditions.
- External dependency failures.
- Empty/null/missing values.
- Timeout/retry states.
- Queue/task state transitions.
- API/database contract assumptions.

Output required:

```text
Defense layers added: ...
Defense layers intentionally not added: ...
Reason: ...
Residual risk: ...
```

Do not use defense in depth as an excuse for scope creep. Defensive changes must remain inside the bugfix scope.

## 3. Condition-based waiting

When debugging or testing async behavior, queues, background jobs, generated files, network calls, UI waits, or eventual consistency, fixed sleep must not be the primary strategy.

Prefer condition-based waiting:

```text
Wait condition: ...
Polling/check method: ...
Timeout: ...
Failure output: ...
```

Rules:

- Avoid blind `sleep 5` / `setTimeout` / arbitrary waits as the main solution.
- Use a specific observable condition.
- Include a timeout.
- On timeout, expose the last observed state and useful diagnostics.

## 4. Multi-component diagnostics

For bugs crossing frontend, backend, database, cache, task queue, filesystem, or external APIs, diagnose by component boundary.

Required table:

```text
Component | Input | Output | State/logs | Finding
Frontend  | ...   | ...    | ...        | ...
Backend   | ...   | ...    | ...        | ...
Database  | ...   | ...    | ...        | ...
Queue     | ...   | ...    | ...        | ...
```

Rules:

- Do not conclude root cause from one component only when the bug crosses components.
- Mark the root-cause component and affected components separately.
- If logs are unavailable, say so and explain the fallback evidence.

## 5. Three-fix architecture stop gate

If the same issue has been fixed three times and still fails, stop patching.

Required re-evaluation:

```text
Fix attempt count: 3+
Could the requirement be misunderstood? ...
Could the root cause be wrong? ...
Could the architecture assumption be wrong? ...
Could the test/verification be wrong? ...
Should this return to design/spec? ...
Decision: continue / ask user / return to design / blocked
```

Rules:

- Do not attempt a fourth patch without this stop-gate review.
- If design/spec assumptions are questionable, return to Kiro spec/design before coding.
- If user input is needed, ask one focused question with numbered options.
