# Superpowers Capability Matrix for Kiro

版本：v0.3.0

本文件说明原 Superpowers 能力在 Kiro Superpowers Discipline 中的覆盖情况。目标不是复制原插件，而是把适合 Kiro 的执行纪律改造成 Power / Steering / Hooks / Custom Subagents。

| 原 Superpowers 能力 | Kiro 版落点 | v0.3.0 覆盖状态 | 当前说明 | 后续计划 |
|---|---|---|---|---|
| using-superpowers | Power keywords + `superpowers-router.md` + workspace steering | 部分覆盖 | 用户自然语言触发，Kiro 自动路由到 feature/bugfix/task/review/verification。没有原版 skill tool。 | 继续增强路由准确性。 |
| brainstorming | Kiro requirements 阶段 + `requirements-gate.md` | 部分覆盖 | 新功能优先进入可验收需求澄清。 | 保持，不另建一套 spec。 |
| writing-plans | Kiro design/tasks + `design-gate.md` / `task-execution-discipline.md` | 部分覆盖 | 使用 Kiro 原生 design/tasks 作为计划来源。 | v0.7 强化 task execution contract。 |
| executing-plans | Kiro task execution + hooks | 部分覆盖 | 执行前后已有 gate，但还不是完整计划执行合同。 | v0.7 补完整执行合同。 |
| test-driven-development | `tdd-discipline.md` + pre-task gate | 部分覆盖 | 行为变化默认 TDD；当前主要是纪律约束，不是强制代码级验证器。 | 后续增强验证证据检查。 |
| systematic-debugging | `systematic-debugging.md` + `sp-debugger` | 基础覆盖 | bugfix 要先复现、查根因、失败测试/替代验证。 | 保持并结合 review loop。 |
| verification-before-completion | post-task hook + `verification-before-completion.md` + `sp-test-verifier` | 基础覆盖 | 完成前必须有新鲜验证证据。 | v0.7 强化 completion contract。 |
| requesting-code-review | `sp-spec-reviewer` + `sp-code-reviewer` + `review-discipline.md` | 基础覆盖 | 先 spec review，再 code review。 | v0.5 补闭环。 |
| receiving-code-review | 暂无完整闭环 | 未覆盖 | 当前有 reviewer，但没有 review feedback 分级和回修闭环。 | v0.5 补 review feedback loop。 |
| subagent-driven-development | `subagent-routing.md` + 5 个 custom subagents | 部分覆盖 | 有角色，但 task-by-task loop 还未强制完整闭环。 | v0.5 补完整 subagent task loop。 |
| dispatching-parallel-agents | 暂无 | 未覆盖 | 不急于并行，避免冲突。 | v0.6 补安全并行策略。 |
| using-git-worktrees | `worktree-discipline.md` | 规则覆盖 | 只是建议和纪律，没有自动创建 worktree。 | v0.4 补 worktree 自动化。 |
| finishing-a-development-branch | 暂无 | 未覆盖 | 当前没有合并/PR/保留/丢弃四选项收尾。 | v0.4 补 branch finishing。 |
| writing-skills | 暂不计划 | 未覆盖 | Kiro 版不鼓励用户自行维护 Superpowers-style skill 系统。 | 暂不补。 |

## v0.3.0 新增能力

1. 状态标识：每次任务开始显示 Kiro/Superpowers 是否启用、当前阶段、流程、task、gate。
2. Superpowers Router：把自然语言请求自动分流到新功能、bugfix、继续任务、审查、验证。
3. 能力矩阵：明确哪些 Superpowers 能力已经迁移，哪些未覆盖，后续怎么补。

## 明确边界

- 不包含 ai_dev_os。
- 不安装原版 Superpowers 插件。
- 不提供多平台插件能力。
- 不要求用户写长提示词。
- Kiro 仍然是主控；Superpowers Discipline 是执行纪律。
