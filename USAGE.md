# 日常使用

目标：用户不背流程。你正常说需求，Kiro 自动按纪律执行。

## 用户只需要说自然语言

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```

不要手动声明 Superpowers Discipline，不要复制长提示词。

## 统一状态标识

每次开始开发、修复、继续任务、审查或验收时，你应该先看到：

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification / branch-finishing
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-refinement / needs-tdd-evidence / needs-verification / blocked
```

## 新功能

用户说：

```text
新增数据导出功能
```

Kiro 应自动：显示状态标识 → 创建/更新 Feature Spec → requirements/design/tasks → Kiro Task Refinement Gate → worktree gate → TDD Evidence Contract → Subagent Task Packet → subagent task loop → Review Evidence Contract → Fresh Verification Evidence → task completion contract → branch finishing。

## 修 bug

用户说：

```text
修复登录接口偶发 500 的问题
```

Kiro 应自动：显示状态标识 → 判断为 bugfix → 先复现 → root-cause-tracing → multi-component diagnostics（如适用）→ defense-in-depth 判断 → condition-based waiting（如适用）→ RED 失败测试/替代验证 → GREEN 最小修复 → review → Fresh Verification Evidence → completion contract。

## 继续任务

用户说：

```text
继续当前 spec 的下一个任务
```

Kiro 应自动：找到当前 spec 和下一个未完成 task → 读取 requirements/design/tasks → Kiro Task Refinement Gate → Subagent Task Packet → subagent loop → Fresh Verification Evidence → completion contract。

## 检查是否完成

用户说：

```text
检查当前任务是否真的完成
```

Kiro 应自动：查看 changed files / BASE_SHA / HEAD_SHA（如可用）→ 运行 fresh verification → spec review → code review → 输出 `COMPLETE / NOT COMPLETE / PARTIAL / BLOCKED / UNVERIFIED`。

## 统一状态词

- `DONE`：单个 agent 的限定职责完成。
- `COMPLETE`：整个 task 满足完成定义，并且 fresh verification evidence 完整。
- `NOT COMPLETE`：完成定义未满足或验证失败。
- `BLOCKED`：存在阻塞。
- `NEEDS_CONTEXT`：缺少上下文，必须暂停。
- `FAILED`：命令、测试或执行失败。
- `PARTIAL`：只完成部分内容。
- `UNVERIFIED`：无法验证。

## TDD Evidence Contract

新功能、行为变更、bugfix 默认需要 TDD 证据：

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

## Fresh Verification Evidence

完成声明前必须输出本次新鲜验证证据：

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

## Branch finishing

任务通过验证后，Kiro 不应该自动合并，而应该给出：

```text
1. 合并回主分支
2. 推送并创建 PR
3. 保留分支
4. 丢弃本次工作
```

危险操作必须二次确认。
