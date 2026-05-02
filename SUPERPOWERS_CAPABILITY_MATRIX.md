# Superpowers Capability Matrix

版本：v1.5.0

说明：本表对照原 Superpowers 项目的核心能力，说明 Kiro 版落点、覆盖状态和后续计划。v1.5.0 是稳定版整理，不新增新的开发流程能力。

| 原 Superpowers 能力 | Kiro 版落点 | v1.5.0 覆盖状态 | 当前说明 | 后续计划 |
|---|---|---|---|---|
| using-superpowers | POWER.md + superpowers-router + status-banner + stable-output-contract | 部分覆盖 | 通过 Power/Steering/Hooks 引导，不是原版 skill tool 强制调用 | 后续可补 Skill Activation Ledger |
| brainstorming | Kiro requirements/design gate | 部分覆盖 | 借 Kiro spec 主控，未完全复刻原版 2-3 方案和逐段确认 | 可补 Spec Brainstorming Gate |
| writing-plans | Kiro tasks + Kiro Task Refinement Gate | 强化覆盖 | v1.0 要求 task 清晰、范围、验证、完成定义和拆分判断 | 保持 Kiro 原生 tasks，不另建 Superpowers plans |
| executing-plans | task execution contract + task completion contract | 覆盖 | v0.7 明确执行前/完成前合同 | 继续用 hooks 守门 |
| test-driven-development | tdd-discipline + TDD Evidence Contract | 强化覆盖 | v0.9 要求 RED/GREEN/REFACTOR 证据和例外确认 | 继续与 Fresh Verification Evidence 联动 |
| systematic-debugging | systematic-debugging + debugging-deep-techniques + sp-debugger | 强化覆盖 | v1.3 增加 root-cause-tracing、defense-in-depth、condition-based-waiting、multi-component diagnostics、architecture stop gate | 可继续补更多诊断模板 |
| verification-before-completion | verification-before-completion + fresh-verification-evidence | 强化覆盖 | v1.4 要求 fresh verification evidence、exit code、pass/fail/skip count、UNVERIFIED/PARTIAL | 保持完成声明硬化 |
| requesting-code-review | sp-spec-reviewer + sp-code-reviewer + Review Evidence Contract | 强化覆盖 | v1.1 要求 BASE_SHA、HEAD_SHA、Changed files 和问题分级 | 可补更细的 PR review 模板 |
| receiving-code-review | review-feedback-loop + sp-review-feedback-handler | 覆盖 | blocker/major/minor/question 分级，question 暂停，不盲改 | 可补 human/external reviewer 区分 |
| subagent-driven-development | task-by-task-subagent-loop + Subagent Task Packet + Subagent Result Contract | 强化覆盖 | v1.1 统一任务包和 agent 输出格式 | Kiro subagents 不等于原版 skill runtime，继续以 main agent 调度 |
| dispatching-parallel-agents | parallel-agent-policy + Parallel Dispatch Plan | 保守覆盖 | 默认只并行 context gathering/review，不默认并行 implementation | 并行 implementation 仍需人工确认 |
| using-git-worktrees | worktree scripts + worktree-hardening | 强化覆盖 | v1.2 增加 .gitignore 检查、baseline、metadata | 不默认删除用户代码 |
| finishing-a-development-branch | branch finishing scripts + branch-finishing-hardening | 强化覆盖 | v1.2 增加 verification、changed files、commits、二次确认、CLEAN_WORKTREE | 保持安全优先 |
| writing-skills | 未实现 | 未覆盖 | 不是当前 Kiro 版目标 | 低优先级 |

## v1.5.0 稳定版整理

- 新增 `stable-output-contract.md`。
- 统一状态词：DONE / COMPLETE / NOT COMPLETE / BLOCKED / NEEDS_CONTEXT / FAILED / PARTIAL / UNVERIFIED。
- 统一 `SP Agent Result` 输出格式。
- 更新 README / INSTALL / UNINSTALL / USAGE / TROUBLESHOOTING / CHANGELOG / MIGRATION。
- 增强 validate-package.py，检查所有 hooks JSON、agents frontmatter、scripts、Power 结构、能力矩阵、文档完整性、自然语言入口和 ai_dev_os 禁止项。

## v1.4.0 Fresh Verification Evidence

- `fresh-verification-evidence.md`
- verification result contract
- completion claim hardening
- `Verification Evidence`
- `exit code`
- `pass count`
- `fail count`
- `skip count`
- `UNVERIFIED`
- `PARTIAL`

## v1.3.0 Debugging Deep Techniques

- `debugging-deep-techniques.md`
- root-cause-tracing
- defense-in-depth
- condition-based-waiting
- multi-component diagnostics
- architecture stop gate

## v1.2.0 Worktree / Branch Finishing Hardening

- `worktree-hardening.md`
- `branch-finishing-hardening.md`
- baseline verification
- worktree metadata
- DISCARD_WORK
- CLEAN_WORKTREE

## v1.1.0 Subagent Task Packet + Review Evidence

- `subagent-task-packet.md`
- `review-evidence-contract.md`
- Subagent Task Packet
- Review Evidence Contract
- Git diff evidence
- BASE_SHA
- HEAD_SHA
- Changed files

## v1.0.0 Kiro Task Refinement Gate

- `kiro-task-refinement-gate.md`
- Task Refinement Gate
- 任务拆分
- requirement/design/task 绑定

## v0.9.0 TDD Evidence Contract

- `tdd-evidence-contract.md`
- TDD Evidence Contract
- RED/GREEN/REFACTOR
- RED 验证命令
- GREEN 验证命令

## v0.8.0 稳定化整理

- 统一术语
- 统一状态标识
- 统一 hook 命名
- 统一 agent 输出格式
- 整理 README / INSTALL / UNINSTALL / USAGE / TROUBLESHOOTING
- 增强 validate-package.py
