# CHANGELOG

## v1.1.0

新增：

1. Subagent Task Packet：Kiro main agent 派发 subagent 前必须构造标准任务包，包含 spec、requirement、design section、task、目标、范围、允许/禁止修改、验证命令、预期输出和完成定义。
2. Subagent Result Contract：所有 `sp-*` subagent 必须返回统一 `SP Agent Result` 格式，包含 `DONE / BLOCKED / NEEDS_CONTEXT / FAILED` 状态、改动文件、验证命令、验证结果、风险和需要 main agent 决策的问题。
3. Review Evidence Contract：spec/code review 必须基于 changed files、requirement/design/task coverage 和 Git diff evidence；所有问题必须分级为 blocker/major/minor/question。
4. Git diff evidence：review 前尽量记录 BASE_SHA，review 后尽量记录 HEAD_SHA；无法获取 SHA 必须说明原因。
5. 增强 agents：更新 `sp-implementer`、`sp-test-verifier`、`sp-spec-reviewer`、`sp-code-reviewer`、`sp-debugger`、`sp-review-feedback-handler` 输出格式。
6. 新增 hooks：`17-sp-subagent-task-packet.kiro.hook`、`18-sp-subagent-result-contract.kiro.hook`、`19-sp-review-evidence-contract.kiro.hook`。
7. 新增 steering：`subagent-task-packet.md`、`review-evidence-contract.md` 和对应 workspace steering。

保持兼容：

- v0.2-v1.0 的安装方式不变。
- v0.2-v1.0 的卸载方式不变。
- 日常自然语言入口不变。
- v0.4 worktree 和 branch finishing 保持不变。
- v0.5 subagent task loop 和 review feedback loop 保持不变。
- v0.6 parallel agents 安全策略保持不变。
- v0.7 task execution/completion contract 保持不变。
- v0.8 稳定化文档和校验保持不变。
- v0.9 TDD Evidence Contract 保持不变。
- v1.0 Task Refinement Gate 保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。


## v1.0.0

新增：

1. Kiro Task Refinement Gate：执行 task 前检查 task 是否清晰、足够小、可验证，并且绑定 requirement/design/task。
2. task 执行前必须确认：spec、requirement、design section、task 编号、目标、范围、不做范围、完成定义、验证命令。
3. task 拆分规则：task 太大、跨多个不相关模块、跨后端/前端/数据库/队列、无法形成清晰验证闭环时，必须给出编号拆分建议。
4. 增强 hooks：新增 `14-sp-task-refinement-gate.kiro.hook`、`15-sp-task-split-review.kiro.hook`、`16-sp-scope-creep-blocker.kiro.hook`。
5. 新增 steering：`kiro-task-refinement-gate.md` 和 `superpowers-kiro-task-refinement-gate.md`。

保持兼容：

- v0.2-v0.9 的安装方式不变。
- v0.2-v0.9 的卸载方式不变。
- 日常自然语言入口不变。
- v0.4 worktree 和 branch finishing 保持不变。
- v0.5 subagent task loop 和 review feedback loop 保持不变。
- v0.6 parallel agents 安全策略保持不变。
- v0.7 task execution/completion contract 保持不变。
- v0.8 稳定化文档和校验保持不变。
- v0.9 TDD Evidence Contract 保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。


## v0.9.0

新增：

1. TDD Evidence Contract：新功能、行为变更、bugfix 默认必须提供 RED/GREEN/REFACTOR 证据。
2. TDD 例外处理：无法 TDD 时必须说明原因、给出替代验证方案，并等待用户确认。
3. TDD 完成检查：没有 RED 失败证据和 GREEN 通过证据，不允许声称 COMPLETE；测试失败不能进入下一个 task。
4. 增强 hooks：新增 `11-sp-tdd-evidence-gate.kiro.hook`、`12-sp-tdd-evidence-completion.kiro.hook`、`13-sp-tdd-verification-review.kiro.hook`。
5. 新增 steering：`tdd-evidence-contract.md` 和 `superpowers-tdd-evidence-contract.md`。

保持兼容：

- v0.2-v0.8 的安装方式不变。
- v0.2-v0.8 的卸载方式不变。
- 日常自然语言入口不变。
- v0.4 worktree 和 branch finishing 保持不变。
- v0.5 subagent task loop 和 review feedback loop 保持不变。
- v0.6 parallel agents 安全策略保持不变。
- v0.7 task execution/completion contract 保持不变。
- v0.8 稳定化文档和校验保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## v0.8.0

新增/整理：

1. 稳定化整理：检查 v0.3 到 v0.7 的能力描述，统一术语、状态标识、hook 展示名称和 agent 输出格式。
2. 文档整理：重写 README、INSTALL、UNINSTALL、USAGE、TROUBLESHOOTING，保留一句话安装和自然语言日常入口。
3. 验证增强：增强 `scripts/validate_package.py`，检查 hooks、agents、scripts、能力矩阵、文档入口、版本号和禁用路径。
4. 用户体验简化：继续要求用户只说自然语言，不要求手动声明 Superpowers Discipline，不要求写长提示词。

保持兼容：

- v0.2-v0.7 的安装方式不变。
- v0.2-v0.7 的卸载方式不变。
- 日常自然语言入口不变。
- v0.4 worktree 和 branch finishing 保持不变。
- v0.5 subagent task loop 和 review feedback loop 保持不变。
- v0.6 parallel agents 安全策略保持不变。
- v0.7 task execution/completion contract 保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## v0.7.0

- 新增 Kiro task execution contract。
- 新增 executing-plans 完整纪律。
- 新增 task completion contract。
- 新增 hooks：`08-sp-task-execution-contract.kiro.hook`、`09-sp-task-completion-contract.kiro.hook`、`10-sp-post-task-branch-finishing-check.kiro.hook`。

## v0.6.0

- 新增 parallel agents 安全并行策略。
- 新增 Parallel Dispatch Plan。
- 新增 `parallel-agent-policy.md` steering。
- 新增 `07-sp-parallel-safety-check.kiro.hook`。

## v0.5.0

- 新增 subagent task loop。
- 新增 review feedback loop。
- 新增 `sp-review-feedback-handler`。

## v0.4.0

- 新增 worktree 自动化纪律。
- 新增 branch finishing 纪律。
- 新增安全脚本：`sp-worktree-create.*`、`sp-finish-branch.*`。

## v0.3.0

- 新增状态标识。
- 新增 Superpowers Router。
- 新增 `SUPERPOWERS_CAPABILITY_MATRIX.md`。

## v0.2.0

- 将日常入口改为自然语言。
- 新增 `INSTALL_FOR_KIRO.md`。
- 重写 README、INSTALL、USAGE。

## v0.1.0

- 初始版本。
- 提供 Kiro Power、Steering、Hooks、Custom Subagents、安装脚本。
