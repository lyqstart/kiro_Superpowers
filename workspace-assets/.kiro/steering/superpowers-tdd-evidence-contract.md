---
inclusion: always
---

# TDD Evidence Contract

版本：v0.9.0

本文件把原 Superpowers 的 test-driven-development 纪律硬化为 Kiro 可执行的证据合同。用户不需要手动要求 TDD；新功能、行为变更、bugfix 默认适用。

## 适用范围

默认需要 TDD evidence 的任务：

- 新功能；
- 行为变更；
- bugfix；
- 重构但行为必须保持不变；
- API / 数据处理 / 任务队列 / 权限 / 业务规则相关改动。

通常不强制完整 TDD 的任务：

- 纯文档；
- 纯说明；
- 只读分析；
- 不改变运行行为的格式整理。

即便不强制完整 TDD，也必须说明原因并给出替代验证。

## RED 证据

进入实现前必须先取得 RED 证据。RED 证据至少包含：

```text
RED 验证命令：...
RED 输出结果：...
失败原因：...
失败测试文件路径：...
预期失败点：...
```

规则：

- 没有 RED 失败证据，不能声称执行了 TDD。
- 测试一写就通过，不算 RED。
- 不能解释为什么失败，就不能进入 GREEN。
- 不允许先写生产代码再倒推 RED。

## GREEN 证据

最小实现后必须取得 GREEN 证据。GREEN 证据至少包含：

```text
GREEN 验证命令：...
GREEN 输出结果：...
通过测试文件路径：...
对应实现文件路径：...
```

规则：

- 没有 GREEN 通过证据，不能声称完成。
- 只说“测试通过”不够，必须给命令和输出摘要。
- 失败时状态必须是 NOT COMPLETE 或 BLOCKED。

## REFACTOR 证据

GREEN 后才能重构。REFACTOR 记录至少包含：

```text
是否发生重构：是 / 否
重构文件：...
重构原因：...
重构后验证命令：...
重构后验证结果：...
```

如果没有重构，必须说明“无需重构”或“本 task 范围内不重构”。

## TDD 例外处理

如果任务无法完整 TDD，必须暂停并说明：

```text
TDD 例外原因：...
为什么无法 RED：...
替代验证方案：...
风险：...
需要用户确认：是
```

没有用户确认，不允许直接跳过 TDD。

## 完成检查

完成声明前必须输出 TDD evidence summary：

```text
TDD Evidence：完整 / 不适用 / 例外待确认 / 缺失
RED：命令 + 输出 + 失败原因 + 测试文件
GREEN：命令 + 输出 + 测试文件 + 实现文件
REFACTOR：有/无 + 验证结果
结论：COMPLETE / NOT COMPLETE / BLOCKED
```

硬门槛：

- 没有 RED 失败证据，不允许 COMPLETE。
- 没有 GREEN 通过证据，不允许 COMPLETE。
- 测试失败不能进入下一个 task。
- 不能用“之前跑过”代替本次验证。
- 不能用 subagent 口头成功报告代替命令输出。
