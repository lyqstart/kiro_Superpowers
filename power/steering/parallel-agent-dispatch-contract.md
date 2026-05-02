# Parallel Agent Dispatch Contract

## Purpose

Make parallel agents closer to Superpowers: one focused, self-contained prompt per independent problem domain, then conflict review and full verification.

## Parallel Dispatch Rules

Allowed by default:

- context gathering
- review
- independent diagnostics

Not allowed by default:

- parallel implementation
- shared files
- shared API contracts
- shared DB tables
- shared migrations
- shared state machines

## Per-Agent Prompt Contract

Each parallel agent prompt must include:

- Problem domain
- Exact files/tests/logs to inspect
- Goal
- Constraints
- Files forbidden to modify
- Expected output
- Verification command if implementation is allowed

## Integration Checklist

After agents return:

1. Read every summary.
2. Check overlapping files.
3. Check conflicting conclusions.
4. Run relevant focused tests.
5. Run full suite if any code changed.
6. Spot check one representative change per agent.
7. Do unified spec/code/test review.

## Output

```text
Parallel Integration Result
Agents dispatched: ...
Independent domains: ...
Conflicts found: yes/no
Full verification: ...
Spot checks: ...
Unified review result: ...
```
