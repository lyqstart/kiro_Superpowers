# 日常使用

目标：用户不背流程。你正常说需求，Kiro 自动按纪律执行。

## 统一状态标识

每次开始开发、修复、继续任务、审查或验收时，你应该先看到类似：

```text
【Kiro规格主控：启用】
【Superpowers执行纪律：启用】
当前阶段：implement
当前流程：task-execution
当前Task：TASK-003
当前Gate：passed
```

状态标识要短。用户不需要手动声明 Superpowers Discipline。

## 新功能

用户说：

```text
新增数据导出功能
```

Kiro 应自动：显示状态标识 → 创建/更新 Feature Spec → requirements/design/tasks → worktree gate → TDD Evidence Contract → subagent task loop → task completion contract → branch finishing。

## 修 bug

用户说：

```text
修复登录接口偶发 500 的问题
```

Kiro 应自动：显示状态标识 → 判断为 bugfix → 先复现 → 查根因 → RED 失败测试/替代验证 → GREEN 最小修复 → review → task completion contract。

## 继续任务

用户说：

```text
继续当前 spec 的下一个任务
```

Kiro 应自动：找到当前 spec 和下一个未完成 task → 读取 requirements/design/tasks → 执行 task execution contract → worktree gate → subagent loop → completion contract。

## 检查是否完成

用户说：

```text
检查当前任务是否真的完成
```

Kiro 应自动：查看 diff → 运行测试/构建/lint → spec review → code review → 输出 `COMPLETE / NOT COMPLETE / BLOCKED`。


## Kiro Task Refinement Gate

执行任何 task 前，Kiro 应自动确认：

```text
Spec：...
Requirement：...
Design section：...
Task：...
目标：...
范围：...
不做：...
完成定义：...
验证命令：...
```

如果 task 有歧义、太大、缺少 requirement/design 关联、缺少验证方式或完成定义，Kiro 必须暂停，不许猜。

如果 task 太大，Kiro 必须给出编号拆分建议，而不是直接执行。

## Task execution contract

执行前必须确认：

```text
目标：...
范围：...
不做：...
完成定义：...
requirement/design/task：...
验证命令：...
```

如果 task 有歧义、缺少 requirement/design 关联、太大、或包含范围外内容，必须暂停，不许猜。

## Task completion contract

完成前必须输出：

```text
状态：COMPLETE / NOT COMPLETE / BLOCKED
验证命令：...
验证结果：...
改动文件：...
满足的 requirement/design/task：...
剩余风险：...
下一步：...
```

不能用“已经完成”代替验证证据。

## Subagent task loop

实现类 task 应自动进入固定 loop：

```text
Kiro main agent 读取 requirements/design/tasks
  ↓
整理完整 task context
  ↓
sp-implementer
  ↓
sp-test-verifier
  ↓
sp-spec-reviewer
  ↓
sp-code-reviewer
```

如果 spec review 不通过，不能进入 code review。如果 code review 有 blocker/major，不能标记完成。

## Review feedback loop

审查反馈必须分级：

```text
blocker：必须修复
major：必须修复并重新 review
minor：记录建议，不影响核心完成判断
question：暂停提问，不许猜
```

## Parallel agents

用户不需要主动要求并行。Kiro 判断多个任务可能并行时，必须先输出 `Parallel Dispatch Plan`。默认允许并行 context gathering / review，不默认并行 implementation。边界不清晰时禁止并行。

## Branch finishing

任务通过验证后，Kiro 不应该自动合并，而应该给出：

```text
1. 合并回主分支
2. 推送并创建 PR
3. 保留分支
4. 丢弃本次工作
```

选择 4 时必须二次确认。


> 稳定规则：不要求用户写长提示词。


## TDD Evidence Contract

新功能、行为变更、bugfix 默认需要 TDD 证据。用户不用手动声明。

完成前应看到：

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

没有 RED 失败证据和 GREEN 通过证据，不能把新功能、行为变更或 bugfix 标记为 COMPLETE。无法 TDD 时必须说明原因、给出替代验证方案，并等待用户确认。

> 稳定规则：不要求用户写长提示词。


## Subagent Task Packet

Kiro main agent 派发任何 `sp-*` subagent 前，必须先构造任务包：

```text
Subagent Task Packet
Spec：...
Requirement：...
Design section：...
Task：...
Task 原文：...
目标：...
范围：...
不做：...
允许修改：...
禁止修改：...
验证命令：...
预期输出：...
完成定义：...
```

如果任务包不完整，subagent 必须返回 `NEEDS_CONTEXT`，不能自己猜。

## Review Evidence Contract

spec/code review 必须基于实际改动：

```text
BASE_SHA：...
HEAD_SHA：...
Changed files：...
Requirement/design/task coverage：...
Blockers：...
Major issues：...
Minor issues：...
Questions：...
```

无法获取 SHA 时必须说明原因，但仍然要记录 changed files。review 不能脱离实际改动做空泛建议。
