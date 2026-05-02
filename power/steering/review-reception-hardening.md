# Review Reception Hardening

## Purpose

Make receiving code review feedback as rigorous as the original Superpowers skill: verify before implementing, do not blindly agree, and do not perform social agreement instead of technical reasoning.

## Required Flow

When receiving feedback:

1. READ all feedback before reacting.
2. UNDERSTAND each item; restate unclear items or ask.
3. VERIFY against codebase reality.
4. EVALUATE whether the suggestion is technically correct for this project.
5. RESPOND with action or technical pushback.
6. IMPLEMENT one item at a time.
7. TEST each fix.
8. RE-REVIEW blocker/major fixes.

## Source Handling

- User feedback: trusted, but clarify unclear scope.
- External reviewer feedback: suggestions to evaluate, not orders.
- Automated tool output: verify false positives.
- Architecture-changing feedback: ask user before changing design.

## Feedback Status

- blocker: must fix before completion.
- major: must fix before completion or get explicit user deferral.
- minor: record; do not expand scope.
- question: stop and ask; do not guess.
- rejected-with-reason: document technical reason and evidence.

## YAGNI Rule

If feedback suggests building a larger or more generic system, grep/search for actual usage first. If unused, ask whether to remove/defer instead of expanding scope.

## Forbidden Responses

- Do not write empty agreement like “absolutely right” and immediately implement without verification.
- Do not implement partially understood feedback.
- Do not batch multiple complex fixes without testing each.

## Output Contract

```text
Review Reception Result
Feedback source: user / external reviewer / tool / unknown
Items reviewed: ...
Clarification needed: ...
Accepted items: ...
Rejected/deferred items with reason: ...
Implementation order: ...
Verification per item: ...
Re-review required: yes/no
```
