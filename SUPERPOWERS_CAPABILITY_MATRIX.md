# Superpowers Capability Matrix for Kiro

版本：v0.7.0

本文件说明原 Superpowers 能力在 Kiro Superpowers Discipline 中的覆盖情况。目标不是复制原插件，而是把适合 Kiro 的执行纪律改造成 Power / Steering / Hooks / Custom Subagents。

| 原 Superpowers 能力 | Kiro 版落点 | v0.7.0 覆盖状态 | 当前说明 | 后续计划 |
|---|---|---|---|---|
| using-superpowers | Power keywords + `superpowers-router.md` + workspace steering | 部分覆盖 | 用户自然语言触发，Kiro 自动路由到 feature/bugfix/task/review/verification。没有原版 skill tool。 | 持续增强路由准确性。 |
| brainstorming | Kiro requirements 阶段 + `requirements-gate.md` | 部分覆盖 | 新功能优先进入可验收需求澄清。 | 保持，不另建一套 spec。 |
| writing-plans | Kiro design/tasks + `design-gate.md` / `task-execution-discipline.md` | 部分覆盖 | 使用 Kiro 原生 design/tasks 作为计划来源。 | 保持 Kiro 原生主控。 |
| executing-plans | `executing-plans-discipline.md` + `kiro-task-execution-contract.md` + hooks 08/09/10 | 增强覆盖 | task 执行前必须确认目标、范围、不做范围、完成定义、验证命令；blocker/测试失败/verification 失败不能继续。 | 后续结合真实项目验证输出质量。 |
| test-driven-development | `tdd-discipline.md` + pre-task gate | 部分覆盖 | 行为变化默认 TDD；当前主要是纪律约束，不是强制代码级验证器。 | 后续增强验证证据检查。 |
| systematic-debugging | `systematic-debugging.md` + `sp-debugger` | 基础覆盖 | bugfix 要先复现、查根因、失败测试/替代验证。 | 保持并结合 review loop。 |
| verification-before-completion | `task-completion-contract.md` + post-task hook + `sp-test-verifier` | 增强覆盖 | 完成前必须有验证命令、验证结果、改动文件、满足的 requirement/design/task 和剩余风险。 | 继续增强自动识别验证命令。 |
| requesting-code-review | `sp-spec-reviewer` + `sp-code-reviewer` + `review-discipline.md` | 增强覆盖 | 先 spec review，再 code review；不通过不得标记完成。 | 与 completion contract 共同生效。 |
| receiving-code-review | `review-feedback-loop.md` + `sp-review-feedback-handler` | 基础覆盖 | feedback 分为 blocker/major/minor/question；blocker/major 必须修复后重新 review；question 必须暂停提问。 | 后续结合更多审查模板。 |
| subagent-driven-development | `task-by-task-subagent-loop.md` + 6 个 custom subagents | 增强覆盖 | 固定顺序：implementer → test-verifier → spec-reviewer → code-reviewer；main agent 必须传完整 task context。 | 后续结合真实项目调优。 |
| dispatching-parallel-agents | `parallel-agent-policy.md` + `07-sp-parallel-safety-check.kiro.hook` | 基础覆盖 | 默认允许并行 context gathering / review，不默认并行 implementation；并行前必须输出 Parallel Dispatch Plan；边界不清晰时禁止并行。 | 后续结合真实项目验证冲突检查准确性。 |
| using-git-worktrees | `worktree-discipline.md` + `worktree-automation.md` + `05-sp-worktree-gate.kiro.hook` + `sp-worktree-create.*` | 基础覆盖 | 实现类任务默认 worktree gate；脚本可安全创建隔离 worktree。不会覆盖脏工作区。 | 后续结合 task loop 自动选择 baseline 命令。 |
| finishing-a-development-branch | `branch-finishing.md` + `06-sp-branch-finishing.kiro.hook` + `10-sp-post-task-branch-finishing-check.kiro.hook` + `sp-finish-branch.*` | 增强覆盖 | 任务验证通过后提供合并/PR/保留/丢弃四选项；不自动合并或丢弃；v0.7 会在 completion contract 通过后检查是否需要进入 branch finishing。 | 后续结合更多 Git 平台。 |
| writing-skills | 暂不计划 | 未覆盖 | Kiro 版不鼓励用户自行维护 Superpowers-style skill 系统。 | 暂不补。 |

## v0.7.0 新增能力

1. Kiro task execution contract：执行前批判性阅读 task，检查 requirement/design/task 关联、范围、不做范围、完成定义、验证命令和风险。
2. Executing-plans 完整纪律：task 有歧义先问，不许猜；遇到 blocker 停止；测试失败或 verification 失败不能继续下一个 task。
3. Task completion contract：完成前必须输出状态、验证命令、验证结果、改动文件、满足的 requirement/design/task、剩余风险和下一步。
4. 增强 hooks：task 执行前检查 contract，task 完成后检查 completion contract，完成后检查是否需要 branch finishing。
5. 保持用户自然语言入口，不要求用户手动点名 execution contract。

## v0.6.0 保留能力

1. Parallel agents 安全并行策略。
2. Parallel Dispatch Plan。
3. 并行结束后统一收口。

## v0.5.0 保留能力

1. Subagent task loop。
2. Review feedback loop。
3. `sp-review-feedback-handler`。

## v0.4.0 保留能力

1. Worktree 自动化。
2. Branch finishing。
3. 安全脚本。

## 明确边界

- 不包含 ai_dev_os。
- 不安装原版 Superpowers 插件。
- 不提供多平台插件能力。
- 不要求用户写长提示词。
- Kiro 仍然是主控；Superpowers Discipline 是执行纪律。
