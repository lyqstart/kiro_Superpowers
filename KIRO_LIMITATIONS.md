# Kiro Mechanism Limitations

This package intentionally pushes Kiro as close as possible to Superpowers without pretending Kiro has the same runtime.

## Remaining Differences Caused by Kiro Mechanisms

1. **No native Superpowers Skill tool**
   - Original Superpowers invokes skills through platform-specific skill tools.
   - Kiro has Power/Steering/Hooks/Subagents/MCP, but no identical native Skill tool.
   - v2.0 provides Skill Runtime Lite with ledger and scripts.

2. **Kiro IDE main agent is not fully replaced**
   - Kiro IDE uses its own main chat agent.
   - v2.0 can add subagents and rules, but cannot make a custom sp-controller fully own the IDE main chat unless Kiro adds that capability.

3. **Subagent internals are not fully hook-governed**
   - Kiro main agent can gate inputs/outputs.
   - Subagent internal reasoning/actions cannot be fully forced through hooks from this package.
   - v2.0 mitigates with task packets, result contracts, ledgers, and final review gates.

4. **No native TodoWrite clone**
   - v2.0 uses Task Execution Ledger as a Kiro-native substitute.

5. **Visual Companion is not replicated**
   - v2.0 can ask whether visual aids are needed but does not provide the original browser companion tool.

## Not Treated as Limitations

The following are intentionally conservative safety choices, not Kiro limitations:

- no automatic `.gitignore` commit
- no default worktree deletion
- no default branch deletion
- no default parallel implementation
- no automatic destructive cleanup
