# Fresh Verification Evidence

## 目标

完成声明前必须提供本次新鲜验证证据。不能用口头成功、历史验证或 subagent 成功报告替代验证。

## 适用场景

适用于所有完成声明、task completion、final verification、branch finishing 前检查，以及任何用户问“是否完成 / 能否交付 / 检查是否真的完成”的场景。

## 硬规则

1. 完成声明前必须提供本次新鲜验证证据。
2. 不允许使用“之前跑过”“刚才跑过但没有输出”“subagent 说通过了”作为完成依据。
3. 不允许只说“测试通过”。必须给出命令和结果。
4. 没有 fresh verification evidence，只能输出 `UNVERIFIED`、`NOT COMPLETE` 或 `BLOCKED`，不能输出 `COMPLETE`。
5. 如果验证失败，必须输出 `NOT COMPLETE` 或 `BLOCKED`。
6. 如果只完成部分内容，必须输出 `PARTIAL`。
7. 如果无法验证，必须输出 `UNVERIFIED` 并说明原因、风险和下一步。

## Verification Result Contract

每次 verification 必须包含：

```text
Verification Evidence: fresh / missing / failed / partial / unavailable
验证命令：...
执行时间：...
Exit code：...
Pass count：...
Fail count：...
Skip count：...
关键输出摘要：...
完整失败信息位置或摘要：...
判断结论：COMPLETE / NOT COMPLETE / PARTIAL / BLOCKED / UNVERIFIED
```

如果命令没有结构化 pass/fail/skip count，必须说明如何判断成功，例如：exit code 为 0、构建产物存在、接口返回期望状态码、关键断言全部通过等。

## Completion Claim Hardening

状态只能按证据输出：

- `COMPLETE`：fresh verification 通过，exit code/关键检查成功，spec review/code review 无 blocker/major。
- `NOT COMPLETE`：验证失败、测试失败、构建失败、lint 失败或 review 阻塞。
- `PARTIAL`：部分完成，但仍有未完成 task、未验证路径或待处理 blocker/major。
- `BLOCKED`：缺少环境、凭据、数据、用户确认、git 安全状态或外部依赖。
- `UNVERIFIED`：实现可能完成，但没有可接受的新鲜验证证据。

## 禁止行为

- 禁止说“应该完成了”。
- 禁止用“之前跑过”替代本次验证。
- 禁止用 subagent 的口头结果替代命令输出。
- 禁止把未验证状态包装成完成状态。
- 禁止在 verification 失败后继续下一个 task。

## 与其他纪律的关系

- TDD Evidence Contract 负责 RED/GREEN/REFACTOR 证据。
- Fresh Verification Evidence 负责完成声明前的最终新鲜证据。
- Task Completion Contract 必须引用本合同输出。
- Branch finishing 显示四选项前必须先满足本合同。
