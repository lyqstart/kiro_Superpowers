# Superpowers Remaining Gaps after v2.0.0

v2.0.0 is designed to leave no practical Kiro-native improvement space except where Kiro's mechanism is the blocker or where we intentionally keep safer behavior than upstream Superpowers.

## Still Different Because of Kiro Mechanisms

1. Native Superpowers Skill tool is not available in Kiro. v2.0 implements Skill Runtime Lite with ledger, skill cards, scripts, hooks, and router agent.
2. Kiro IDE main chat agent cannot be fully replaced by a custom sp-controller. v2.0 uses Power/Steering/Hooks/Subagents.
3. Kiro hooks cannot fully govern every internal subagent action. v2.0 gates task packets, subagent outputs, review evidence, and final review at main-agent boundaries.
4. Native TodoWrite is not available. v2.0 substitutes Task Execution Ledger.
5. Original Visual Companion is not implemented. v2.0 only asks whether visual aids are needed.

## Intentionally Safer Than Upstream

1. No automatic `.gitignore` commit.
2. No default worktree deletion.
3. No default branch deletion.
4. No default parallel implementation.
5. No destructive cleanup without typed confirmation.

## Low-Priority Not Implemented

`writing-skills` as a full skill-authoring framework is not implemented. v2.0 includes a skill card only. This is outside the current goal of Kiro execution discipline.
