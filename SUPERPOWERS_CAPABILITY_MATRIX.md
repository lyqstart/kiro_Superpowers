# Superpowers Capability Matrix for Kiro

版本：v1.3.0

本文件说明原 Superpowers 能力在 Kiro Superpowers Discipline 中的覆盖情况。目标不是复制原插件，而是把适合 Kiro 的执行纪律改造成 Power / Steering / Hooks / Custom Subagents。

| 原 Superpowers 能力 | Kiro 版落点 | v1.3.0 覆盖状态 | 当前说明 | 后续计划 |
|---|---|---|---|---|
| using-superpowers | Power keywords + `superpowers-router.md` + workspace steering | 部分覆盖 | 用户自然语言触发，Kiro 自动路由到 feature/bugfix/task/review/verification。没有原版 skill tool。 | 持续根据真实使用调优路由。 |
| brainstorming | Kiro requirements 阶段 + `requirements-gate.md` | 部分覆盖 | 新功能优先进入可验收需求澄清。 | 保持 Kiro 原生 spec 主控。 |
| writing-plans | Kiro design/tasks + `design-gate.md` / `task-execution-discipline.md` + `kiro-task-refinement-gate.md` | 增强覆盖 | 使用 Kiro 原生 design/tasks 作为计划来源；执行前检查 task 是否过大、模糊、缺少验证或缺少 requirement/design 关联。 | 不另建一套 Superpowers plan。 |
| executing-plans | `executing-plans-discipline.md` + `kiro-task-execution-contract.md` + `kiro-task-refinement-gate.md` + hooks 08/09/10/14/15/16 | 增强覆盖 | task 执行前确认目标、范围、不做范围、完成定义、验证命令；task 太大/模糊/缺少 requirement/design 关联时阻止执行并建议拆分。 | 继续结合真实项目验证输出质量。 |
| test-driven-development | `tdd-discipline.md` + `tdd-evidence-contract.md` + hooks 11/12/13 | 增强覆盖 | 新功能、行为变更、bugfix 默认要求 RED/GREEN/REFACTOR 证据；没有 RED/GREEN 证据不能 COMPLETE。 | 后续可结合真实项目增强自动识别测试命令。 |
| systematic-debugging | `systematic-debugging.md` + `debugging-deep-techniques.md` + `sp-debugger` + hooks 23/24/25 | 增强覆盖 | bugfix 要先复现、root-cause-tracing、defense-in-depth、condition-based-waiting、multi-component diagnostics；同一问题三次修复失败触发 architecture stop gate。 | 继续结合真实复杂项目调优。 |
| verification-before-completion | `task-completion-contract.md` + post-task hook + `sp-test-verifier` | 增强覆盖 | 完成前必须有验证命令、验证结果、改动文件、满足的 requirement/design/task 和剩余风险。 | 继续增强自动识别验证命令。 |
| requesting-code-review | `sp-spec-reviewer` + `sp-code-reviewer` + `review-discipline.md` + `review-evidence-contract.md` | 增强覆盖 | 先 spec review，再 code review；review 必须基于 changed files、BASE_SHA/HEAD_SHA（如可用）和 requirement/design/task coverage。 | 与 completion contract 共同生效。 |
| receiving-code-review | `review-feedback-loop.md` + `sp-review-feedback-handler` + `review-evidence-contract.md` | 增强覆盖 | feedback 分为 blocker/major/minor/question；blocker/major 必须修复后重新 review；question 必须暂停提问；每项反馈必须尽量绑定实际改动证据。 | 继续结合真实审查调优。 |
| subagent-driven-development | `task-by-task-subagent-loop.md` + `subagent-task-packet.md` + 6 个 custom subagents | 增强覆盖 | 固定顺序：implementer → test-verifier → spec-reviewer → code-reviewer；main agent 必须传完整 Subagent Task Packet；subagent 必须返回 Subagent Result Contract。 | 后续结合真实项目调优。 |
| dispatching-parallel-agents | `parallel-agent-policy.md` + `07-sp-parallel-safety-check.kiro.hook` | 基础覆盖 | 默认允许并行 context gathering / review，不默认并行 implementation；并行前必须输出 Parallel Dispatch Plan；边界不清晰时禁止并行。 | 真实项目中谨慎启用。 |
| using-git-worktrees | `worktree-discipline.md` + `worktree-automation.md` + `worktree-hardening.md` + hooks 05/20/21 + `sp-worktree-create.*` | 增强覆盖 | 实现类任务默认 worktree gate；创建前检查分支、干净工作区和 `.worktrees/` gitignore；创建后记录 worktree metadata 并运行/要求 baseline verification。 | 继续结合真实项目调优 baseline 命令识别。 |
| finishing-a-development-branch | `branch-finishing.md` + `branch-finishing-hardening.md` + hooks 06/10/22 + `sp-finish-branch.*` | 增强覆盖 | 显示四选项前要求 fresh verification；合并前显示 branch/base/changed files；丢弃前显示 branch/worktree/changed files/commits；清理 worktree 单独确认。 | 后续结合更多 Git 平台。 |
| writing-skills | 暂不计划 | 未覆盖 | Kiro 版不鼓励用户自行维护 Superpowers-style skill 系统。 | 暂不补。 |


## v1.3.0 Debugging Deep Techniques

1. 新增 `debugging-deep-techniques.md`。
2. 新增 workspace steering：`superpowers-debugging-deep-techniques.md`。
3. 新增 hooks 23/24/25，分别检查 root-cause-tracing、debugging deep techniques 和 architecture stop gate。
4. 增强 `sp-debugger` 输出格式，要求记录 root-cause chain、hypothesis validation、defense-in-depth decision、condition-based waiting decision、multi-component diagnostics、fix attempt count 和 architecture stop gate。
5. bugfix 没有根因结论时不能进入修复阶段。
6. 涉及异步/队列/后台任务/文件生成/网络请求/测试等待时，禁止把固定 sleep 作为主要方案。
7. 同一问题连续修复 3 次仍失败时，必须停止并重新评估需求、根因、架构假设、测试方式或是否回到 Kiro design/spec。

## v1.2.0 Worktree / Branch Finishing Hardening

1. 新增 `worktree-hardening.md`。
2. 新增 `branch-finishing-hardening.md`。
3. 新增 workspace steering：`superpowers-worktree-hardening.md`、`superpowers-branch-finishing-hardening.md`。
4. 新增 hooks 20/21/22，分别检查 worktree hardening、baseline verification hardening 和 branch finishing hardening。
5. `sp-worktree-create.*` 创建 worktree 前检查 git 分支、干净工作区和 `.worktrees/` gitignore；不会自动 commit `.gitignore`。
6. `sp-worktree-create.*` 创建后记录 worktree metadata：worktree path、branch name、base branch、created time、related spec/task、baseline command、baseline result。
7. baseline verification 会优先使用显式命令，并尝试识别 `npm test` / `pnpm test` / `yarn test` / `pytest` / `go test ./...` / `cargo test`。
8. `sp-finish-branch.*` 显示四选项前必须执行 verification；合并、丢弃和 cleanup 都需要显式确认。

## v1.1.0 Subagent Task Packet + Review Evidence

1. 新增 `subagent-task-packet.md`。
2. 新增 `review-evidence-contract.md`。
3. 新增 workspace steering：`superpowers-subagent-task-packet.md`、`superpowers-review-evidence-contract.md`。
4. 新增 hooks 17/18/19，分别检查 Subagent Task Packet、Subagent Result Contract 和 Review Evidence Contract。
5. Kiro main agent 派发 subagent 前必须构造标准任务包。
6. 每个 subagent 必须返回统一 `DONE / BLOCKED / NEEDS_CONTEXT / FAILED` 结果。
7. Review Evidence Contract 要求 spec/code review 基于 changed files、BASE_SHA/HEAD_SHA（如可用）和 requirement/design/task coverage。
8. Git diff evidence 无法获取时必须说明原因，不能脱离实际改动做空泛 review。

## v1.0.0 Kiro Task Refinement Gate

1. 新增 `kiro-task-refinement-gate.md`。
2. 新增 workspace steering：`superpowers-kiro-task-refinement-gate.md`。
3. 新增 hooks 14/15/16，分别检查 task refinement、task split review 和 scope creep blocker。
4. 执行 task 前必须确认 spec、requirement、design section、task 编号、目标、范围、不做范围、完成定义和验证命令。
5. task 太大、模糊、缺少 requirement/design 关联、缺少验证方式或包含范围外内容时，必须暂停或建议拆分。

## v0.9.0 TDD Evidence Contract

1. 新增 `tdd-evidence-contract.md`。
2. 新增 workspace steering：`superpowers-tdd-evidence-contract.md`。
3. 新增 hooks 11/12/13，分别检查 TDD 适用性、完成证据和 verification 阶段 RED/GREEN/REFACTOR 证据。
4. 新功能、行为变更、bugfix 必须记录 RED/GREEN/REFACTOR 证据。
5. 无法 TDD 时必须说明原因、给出替代验证方案，并等待用户确认。

## v0.8.0 稳定化整理

1. 统一状态标识格式。
2. 统一 hook 展示名称，保留原文件名。
3. 统一 agent 输出格式，加入 `SP Agent Result`。
4. 整理 README / INSTALL / UNINSTALL / USAGE / TROUBLESHOOTING。
5. 增强 `validate_package.py`，检查 hooks、agents、scripts、能力矩阵和文档入口。

## 明确边界

- 不包含 ai_dev_os。
- 不安装原版 Superpowers 插件。
- 不提供多平台插件能力。
- 不要求用户写长提示词。
- Kiro 仍然是主控；Superpowers Discipline 是执行纪律。
