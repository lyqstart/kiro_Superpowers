# Kiro Spec Brainstorming Gate

## Purpose

Make Kiro's requirements/design flow behave as close as possible to Superpowers `brainstorming`, without creating a second spec system outside `.kiro/specs`.

## Required Flow

For new features, behavior changes, components, substantial refactors, or anything creative:

1. Explore project context before proposing implementation.
2. Ask clarifying questions one at a time.
3. Prefer numbered options when useful.
4. If the request is too broad, decompose into independent specs before details.
5. Propose 2-3 approaches with trade-offs and a recommendation.
6. Present the design in short sections and ask for confirmation.
7. Use Kiro `requirements.md` and `design.md` as the written spec location.
8. Run a spec self-review before implementation.
9. Ask the user to approve the written spec before writing implementation tasks.
10. Only after approval, move to task planning/execution.

## Spec Self-Review Checklist

- No placeholders: no TBD/TODO/fill later.
- No contradictions between requirements, design, APIs, data flow, and tests.
- Scope is small enough for one spec; otherwise split.
- Ambiguous requirements are made explicit.
- Acceptance criteria are testable.
- Design covers architecture, components, data flow, error handling, testing.

## Visual Companion Adaptation

Kiro does not provide the original Superpowers browser visual companion as part of this package. If the feature involves UI, mockups, diagrams, layout, or visual comparison, ask whether the user wants a visual aid, but do not block text-only progress if they decline.

## Hard Gate

Do not write code, scaffold implementation, or run implementation scripts until the design is approved, except for read-only context exploration.
