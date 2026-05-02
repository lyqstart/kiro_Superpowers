---
inclusion: always
---

# Superpowers Discipline for Kiro Workspace

本项目安装了 Kiro Superpowers Discipline。

## 核心原则

用户不需要背流程。用户正常说需求，Kiro 自动按纪律处理。

用户可能只说：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否完成
```

你必须自动判断：

- 新功能 → Feature Spec → requirements/design/tasks → TDD 执行 → 验证；
- bug → Bugfix Spec → 复现 → 根因 → 失败测试 → 最小修复 → 验证；
- 继续 → 找当前 spec 的下一个未完成 task → 执行前检查 → 开发 → 验证；
- 检查完成 → diff + 测试/构建/lint + spec review + code review。

## 不要让用户每次写长提示词

不要要求用户说：

```text
请读取 requirements.md、design.md、tasks.md
请按 RED/GREEN/REFACTOR
请做规格符合性审查
请运行验证命令
```

这些是系统责任。


## v0.3 状态标识

每次处理开发、修复、继续任务、审查、验证请求时，先显示：

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-verification / blocked
```

状态标识之后只给一句最小下一步。

## v0.3 Router

- 新功能：进入 Feature Spec，走 requirements/design/tasks + TDD。
- bugfix：进入 systematic debugging，先复现、查根因、失败测试或替代验证。
- 继续任务：定位当前 spec 和下一个未完成 task，执行前通过 gate。
- 审查：先 spec review，再 code review，再 test review。
- 完成/验收：必须运行或确认新鲜验证证据，输出 COMPLETE / NOT COMPLETE / BLOCKED。

## 强制纪律

1. 没有规格，不进入中大型实现。
2. 没有明确 task，不做大范围代码修改。
3. 行为变化默认 TDD。
4. bugfix 先复现和查根因。
5. 完成前必须有新鲜验证证据。
6. 先做 spec compliance review，再做 code quality review。
7. 不做无关重构。
8. 不把内部流程暴露成用户负担。

## 给用户的回复风格

短、直接、可执行。

开始时：

```text
我会按新功能处理：先确认 spec，再执行下一个可验证 task。
```

完成时：

```text
状态：完成 / 未完成 / 阻塞
验证命令：...
结果：...
改动：...
风险：...
```


## v0.5 Subagent task loop

实现类 Kiro task 必须按固定顺序执行：

1. `sp-implementer`
2. `sp-test-verifier`
3. `sp-spec-reviewer`
4. `sp-code-reviewer`

Kiro main agent 必须先读取 requirements.md、design.md、tasks.md，并把完整 task context 传给 subagent。spec review 不通过，不进入 code review；code review 不通过，不允许标记完成。

## v0.5 Review feedback loop

Review feedback 必须分级为 `blocker / major / minor / question`。blocker/major 必须修复并重新 review；question 必须暂停提问，不许猜；minor 只能作为建议记录，不扩大任务范围。


## v0.7 Kiro task execution contract

执行 Kiro task 前必须批判性阅读当前 task：确认目标、范围、不做范围、完成定义、requirement/design 关联、验证命令和风险。

如果 task 有歧义、缺少 requirement/design 关联、太大、或要求范围外内容，必须暂停，不许猜。

完成 task 前必须输出：

```text
状态：COMPLETE / NOT COMPLETE / BLOCKED
验证命令：...
验证结果：...
改动文件：...
满足的 requirement/design/task：...
剩余风险：...
```

测试失败、verification 失败、spec review 不通过、code review 有 blocker/major 时，不能标记完成，不能继续下一个 task。


## v0.9 TDD evidence contract

新功能、行为变更、bugfix 默认必须提供 TDD 证据。

完成前必须说明：

```text
TDD Evidence：完整 / 不适用 / 例外待确认 / 缺失
RED 验证命令：...
RED 输出结果：...
失败原因：...
失败测试文件路径：...
GREEN 验证命令：...
GREEN 输出结果：...
通过测试文件路径：...
对应实现文件路径：...
REFACTOR：有/无 + 原因 + 验证结果
```

没有 RED 失败证据和 GREEN 通过证据，不允许把行为变更、bugfix 或新功能标记为 COMPLETE。无法 TDD 时必须说明原因、给出替代验证方案，并等待用户确认。


## v1.1 Subagent Task Packet / Review Evidence

Kiro main agent 派发任何 `sp-*` subagent 前，必须构造 Subagent Task Packet，包含 spec、requirement、design section、task、范围、允许/禁止修改、验证命令、预期输出和完成定义。

每个 subagent 必须按 Subagent Result Contract 返回结果。spec/code review 必须基于 changed files、BASE_SHA/HEAD_SHA（如可用）和 requirement/design/task coverage，不允许空泛 review。
