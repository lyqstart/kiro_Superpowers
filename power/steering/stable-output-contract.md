# Superpowers Stable Output Contract v1.5

目的：统一 v0.9-v1.4 中出现的 verification / TDD / review / debugging / agent 输出状态词，避免同一含义出现多套表达。

## 用户入口保持不变

用户日常仍然只需要说：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```

不要要求用户手动声明 Superpowers Discipline，也不要要求用户复制长提示词。

## 统一状态标识

每个开发、bugfix、继续任务、审查或完成检查场景开始时，输出：

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification / branch-finishing
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-refinement / needs-tdd-evidence / needs-verification / blocked
```

## Canonical status words

- `DONE`：单个 agent 的职责完成，不等于整个 task 完成。
- `COMPLETE`：整个 task 满足完成定义，并且具有 fresh verification evidence。
- `NOT COMPLETE`：完成定义未满足或验证失败。
- `BLOCKED`：存在阻塞，需要用户决策、补上下文、修复问题或通过 gate。
- `NEEDS_CONTEXT`：缺少 spec/task/文件/验证上下文，必须暂停。
- `FAILED`：命令、测试或执行失败。
- `PARTIAL`：只完成部分内容，不能声称 COMPLETE。
- `UNVERIFIED`：无法验证，必须说明原因、风险和下一步。

## Standard SP Agent Result

所有 `sp-*` agents 必须使用 `SP Agent Result`，并尽量包含：

```text
SP Agent Result: <agent-name>
Status: DONE / BLOCKED / NEEDS_CONTEXT / FAILED / PARTIAL / UNVERIFIED
Task: ...
Spec: ...
Requirement/design/task coverage: ...
Changed files: ...
Verification command: ...
Verification result: ...
Risks: ...
Needs main-agent decision: ...
Next step: ...
```

## Gate 顺序

默认 gate 顺序保持：

```text
status banner
→ Kiro spec/task context
→ Task Refinement Gate
→ Worktree/Baseline Gate（实现类任务）
→ TDD Evidence Contract（行为变化/bugfix）
→ Subagent Task Packet
→ Subagent Result Contract
→ Review Evidence Contract
→ Fresh Verification Evidence
→ Task Completion Contract
→ Branch Finishing（完成后）
```
