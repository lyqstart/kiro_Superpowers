# CHANGELOG

## v1.3.0

新增：

1. root-cause-tracing：debug 时必须从可观察错误追踪到根因，说明输入、数据变化、异常组件、触发条件和根因证据；没有根因结论不允许进入修复阶段。
2. defense-in-depth：修复 bug 时必须判断是否需要输入、边界、外部依赖、异常状态、契约假设等多层防护；不能只在一个点打补丁。
3. condition-based-waiting：涉及异步任务、队列、后台任务、文件生成、网络请求、测试等待时，禁止把固定 sleep 作为主要方案，必须优先使用条件等待、超时和失败诊断。
4. multi-component diagnostics：涉及前端、后端、数据库、缓存、任务队列、外部 API 多组件时，必须按组件边界诊断，标记根因组件和受影响组件。
5. 3-fix failure architecture stop gate：同一问题连续修复 3 次仍失败时，必须停止，重新质疑需求、根因、架构假设、测试方式或是否回到 design/spec 阶段。
6. 增强 `sp-debugger`：增加根因链路、假设验证记录、防护判断、条件等待判断、多组件诊断、修复失败计数和 architecture stop gate 状态。
7. 新增 hooks：`23-sp-root-cause-tracing.kiro.hook`、`24-sp-debugging-deep-techniques.kiro.hook`、`25-sp-architecture-stop-gate.kiro.hook`。
8. 新增 steering：`debugging-deep-techniques.md` 和对应 workspace steering。

保持兼容：

- v0.2-v1.2 的安装方式不变。
- v0.2-v1.2 的卸载方式不变。
- 日常自然语言入口不变。
- v0.4-v1.2 的 worktree、branch finishing、subagent、review、parallel、task、TDD、refinement、review evidence 能力保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## v1.2.0

新增：

1. Worktree hardening：创建 worktree 前检查当前 git 分支、干净工作区、`.worktrees/` 是否被 `.gitignore` 忽略；未忽略时提示用户确认是否添加，不自动 commit `.gitignore`。
2. Worktree metadata：创建 worktree 后记录 worktree path、branch name、base branch、created time、related spec/task、baseline command、baseline result、baseline exit code。
3. Baseline verification hardening：创建 worktree 后必须尝试 baseline 验证；可识别 npm/pnpm/yarn/pytest/go/cargo 常见验证命令；无法识别时要求用户指定。
4. Branch finishing hardening：显示 finishing 四选项前必须先执行 fresh verification；合并前显示 branch/base/changed files；丢弃前显示 branch/worktree/changed files/commits。
5. 安全确认增强：合并需要输入 `确认合并`；丢弃需要输入 `DISCARD_WORK`；worktree cleanup 是独立确认步骤，需要输入 `CLEAN_WORKTREE`。
6. 脚本增强：增强 `sp-worktree-create.sh`、`sp-worktree-create.ps1`、`sp-finish-branch.sh`、`sp-finish-branch.ps1`，并同步到 `workspace-assets/.kiro/scripts/`。
7. 新增 hooks：`20-sp-worktree-hardening.kiro.hook`、`21-sp-baseline-verification-hardening.kiro.hook`、`22-sp-branch-finishing-hardening.kiro.hook`。
8. 新增 steering：`worktree-hardening.md`、`branch-finishing-hardening.md` 和对应 workspace steering。

保持兼容：

- v0.2-v1.1 的安装方式不变。
- v0.2-v1.1 的卸载方式不变。
- 日常自然语言入口不变。
- v0.4 worktree 和 branch finishing 基础入口保持不变，本版只增强安全性和证据。
- v0.5-v1.1 的 subagent/review/task/TDD/refinement 能力保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。


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
