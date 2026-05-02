# Debug Pattern Analysis Contract

## Purpose

Strengthen systematic debugging beyond root-cause tracing by comparing broken and working examples before patching.

## Required When

Use when a bug has unclear cause, repeated failures, multiple components, or a similar working path exists.

## Flow

1. Find a working example in the codebase, test suite, logs, or similar feature.
2. Read enough of the working example to understand its full path.
3. Compare broken vs working behavior.
4. List differences.
5. Create one hypothesis at a time.
6. Test or inspect one hypothesis at a time.
7. Patch only after a root cause is supported.

## Output

```text
Debug Pattern Analysis
Working example: ...
Broken path: ...
Key differences:
1. ...
Hypothesis tested: ...
Evidence: ...
Root cause confidence: high / medium / low
Allowed to fix: yes/no
```

If root cause confidence is low, do not patch. Ask for missing evidence or run another diagnostic.
