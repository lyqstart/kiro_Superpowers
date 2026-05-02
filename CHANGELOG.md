# CHANGELOG

## v0.6.0

新增：

1. parallel agents 安全并行策略：只有满足安全条件才允许并行。
2. Parallel Dispatch Plan：并行前必须列出目标、文件、接口、数据库表、迁移脚本、状态机、验证命令、agent 和风险。
3. 新增 `parallel-agent-policy.md` steering。
4. 新增 `superpowers-parallel-agent-policy.md` workspace steering。
5. 新增 `07-sp-parallel-safety-check.kiro.hook` 手动并行安全检查 hook。
6. 更新 POWER、README、USAGE、能力矩阵和校验脚本。

保持兼容：

- v0.2/v0.3/v0.4/v0.5 的安装方式不变。
- 日常自然语言入口不变。
- v0.4 worktree 和 branch finishing 保持不变。
- v0.5 subagent task loop 和 review feedback loop 保持不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## v0.5.0

- 新增 subagent task loop：每个 Kiro task 固定经过 `sp-implementer → sp-test-verifier → sp-spec-reviewer → sp-code-reviewer`。
- 新增 review feedback loop：feedback 按 `blocker / major / minor / question` 分级处理。
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
