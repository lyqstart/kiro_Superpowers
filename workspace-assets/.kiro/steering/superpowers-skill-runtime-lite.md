# Superpowers Skill Runtime Lite

## Purpose

Kiro does not expose the exact Superpowers `Skill` tool runtime. This file defines the closest Kiro-native runtime: explicit skill activation, a visible activation ledger, and checklist enforcement before execution and before completion.

## Runtime Rule

Before any development, bugfix, review, verification, planning, or branch-finishing action, the Kiro main agent must perform a skill activation step.

The activation step must happen before implementation and before asking broad follow-up questions. If a focused clarification is required to choose a skill, ask one numbered question only.

## Skill Activation Banner

At the start of applicable work, output this short block:

```text
【Kiro规格主控：启用/待创建/未启用】
【Superpowers执行纪律：启用】
【Skill Runtime Lite：启用】
匹配到的Skills：using-superpowers, <skill names>
当前阶段：requirements/design/tasks/implement/debug/review/verify/finalize
当前流程：...
当前Task：...
当前Gate：passed / blocked / needs-context
```

## Activation Ledger

Create or update a project-local ledger at:

```text
.kiro/superpowers-runtime/SKILL_ACTIVATION_LEDGER.md
```

Each entry must record:

- Timestamp
- User request summary
- Matched skills
- Activated skills
- Why each skill applies
- Skills intentionally not activated and why
- Checklist items that must be satisfied
- Current gate status

If the helper script exists, prefer:

```bash
.kiro/scripts/sp-skill-activate.sh --skill <skill-name> --purpose "<why>"
```

Windows:

```powershell
.kiro\scripts\sp-skill-activate.ps1 -Skill <skill-name> -Purpose "<why>"
```

If scripts are unavailable, write the ledger manually.

## Skill Checklist Enforcement

If an activated skill has checklist items, those items must be converted into visible execution gates. Kiro does not have Superpowers' native TodoWrite skill runtime, so the substitute is:

1. Add checklist items to the status block or task ledger.
2. Do not mark the task complete until all blocking checklist items are satisfied.
3. If a checklist item cannot be satisfied, report `BLOCKED` or `UNVERIFIED`, not `COMPLETE`.

## Mandatory Skill Routing

- New feature / behavior change: `using-superpowers`, `brainstorming`, `writing-plans`, `using-git-worktrees`, `test-driven-development`, `subagent-driven-development`, `requesting-code-review`, `verification-before-completion`.
- Bugfix / failure: `using-superpowers`, `systematic-debugging`, `test-driven-development`, `requesting-code-review`, `verification-before-completion`.
- Continue task: `using-superpowers`, `executing-plans` or `subagent-driven-development`, `verification-before-completion`.
- Code review feedback: `using-superpowers`, `receiving-code-review`, then relevant fix/verification skills.
- Branch finish: `using-superpowers`, `finishing-a-development-branch`, `verification-before-completion`.
- Multiple independent failures/domains: `dispatching-parallel-agents` only after safety check.

## Hard Limitation

This is not the same as the original Superpowers Skill tool. It is the closest Kiro-native replacement using Power, Steering, Hooks, Agents, scripts, and ledgers.
