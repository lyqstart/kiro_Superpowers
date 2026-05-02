# Superpowers Capability Matrix for Kiro

版本：v0.6.0

本文件说明原 Superpowers 能力在 Kiro Superpowers Discipline 中的覆盖情况。目标不是复制原插件，而是把适合 Kiro 的执行纪律改造成 Power / Steering / Hooks / Custom Subagents。

| 原 Superpowers 能力 | Kiro 版落点 | v0.6.0 覆盖状态 | 当前说明 | 后续计划 |
|---|---|---|---|---|
| using-superpowers | Power keywords + `superpowers-router.md` + workspace steering | 部分覆盖 | 用户自然语言触发，Kiro 自动路由到 feature/bugfix/task/review/verification。没有原版 skill tool。 | 继续增强路由准确性。 |
| brainstorming | Kiro requirements 阶段 + `requirements-gate.md` | 部分覆盖 | 新功能优先进入可验收需求澄清。 | 保持，不另建一套 spec。 |
| writing-plans | Kiro design/tasks + `design-gate.md` / `task-execution-discipline.md` | 部分覆盖 | 使用 Kiro 原生 design/tasks 作为计划来源。 | v0.7 强化 task execution contract。 |
| executing-plans | Kiro task execution + hooks | 部分覆盖 | 执行前后已有 gate，但还不是完整计划执行合同。 | v0.7 补完整执行合同。 |
| test-driven-development | `tdd-discipline.md` + pre-task gate | 部分覆盖 | 行为变化默认 TDD；当前主要是纪律约束，不是强制代码级验证器。 | 后续增强验证证据检查。 |
| systematic-debugging | `systematic-debugging.md` + `sp-debugger` | 基础覆盖 | bugfix 要先复现、查根因、失败测试/替代验证。 | 保持并结合 review loop。 |
| verification-before-completion | post-task hook + `verification-before-completion.md` + `sp-test-verifier` | 基础覆盖 | 完成前必须有新鲜验证证据。 | v0.7 强化 completion contract。 |
| requesting-code-review | `sp-spec-reviewer` + `sp-code-reviewer` + `review-discipline.md` | 增强覆盖 | 先 spec review，再 code review；不通过不得标记完成。 | 后续结合 completion contract。 |
| receiving-code-review | `review-feedback-loop.md` + `sp-review-feedback-handler` | 基础覆盖 | feedback 分为 blocker/major/minor/question；blocker/major 必须修复后重新 review；question 必须暂停提问。 | 后续结合完整 completion contract。 |
| subagent-driven-development | `task-by-task-subagent-loop.md` + 6 个 custom subagents | 增强覆盖 | 固定顺序：implementer → test-verifier → spec-reviewer → code-reviewer；main agent 必须传完整 task context。 | 后续可结合 parallel agents。 |
| dispatching-parallel-agents | `parallel-agent-policy.md` + `07-sp-parallel-safety-check.kiro.hook` | 基础覆盖 | 默认允许并行 context gathering / review，不默认并行 implementation；并行前必须输出 Parallel Dispatch Plan；边界不清晰时禁止并行。 | 后续结合真实项目验证冲突检查准确性。 |
| using-git-worktrees | `worktree-discipline.md` + `worktree-automation.md` + `05-sp-worktree-gate.kiro.hook` + `sp-worktree-create.*` | 基础覆盖 | 实现类任务默认 worktree gate；脚本可安全创建隔离 worktree。不会覆盖脏工作区。 | 后续结合 task loop 自动选择 baseline 命令。 |
| finishing-a-development-branch | `branch-finishing.md` + `06-sp-branch-finishing.kiro.hook` + `sp-finish-branch.*` | 基础覆盖 | 任务验证通过后提供合并/PR/保留/丢弃四选项；不自动合并或丢弃。 | 后续结合 review loop 和 completion contract。 |
| writing-skills | 暂不计划 | 未覆盖 | Kiro 版不鼓励用户自行维护 Superpowers-style skill 系统。 | 暂不补。 |


## v0.6.0 新增能力

1. Parallel agents 安全并行策略：只有满足不共享文件、接口、数据库表、迁移脚本、状态机，并且每个任务有独立验证命令时，才允许并行。
2. Parallel Dispatch Plan：并行前必须列出任务目标、文件、接口、数据库表、迁移脚本、状态机、验证命令、agent、风险和最终结论。
3. 并行结束后统一收口：Kiro main agent 汇总结果、检查冲突，并统一进入 spec review / code review / test verification。
4. 保持用户自然语言入口，不要求用户手动点名 parallel agents。

## v0.5.0 新增能力

1. Subagent task loop：每个 Kiro task 必须由 main agent 先读取 spec，再按 `sp-implementer → sp-test-verifier → sp-spec-reviewer → sp-code-reviewer` 顺序推进。
2. Review feedback loop：feedback 必须按 `blocker / major / minor / question` 分级，blocker/major 修复后必须重新 review。
3. 新增 `sp-review-feedback-handler`，负责处理 reviewer 反馈，防止盲目接受建议或跳过问题。
4. 保持用户自然语言入口，不要求用户手动点名 subagent。


## v0.4.0 保留能力

1. Worktree 自动化：实现类任务默认进行 git 状态检查，不在 main/master 上直接开发，优先创建隔离 worktree。
2. Branch finishing：任务完成并验证通过后提供合并、PR、保留、丢弃四个编号选项。
3. 安全脚本：Windows PowerShell 和 macOS/Linux shell 脚本仍然保留。

## 明确边界

- 不包含 ai_dev_os。
- 不安装原版 Superpowers 插件。
- 不提供多平台插件能力。
- 不要求用户写长提示词。
- Kiro 仍然是主控；Superpowers Discipline 是执行纪律。
