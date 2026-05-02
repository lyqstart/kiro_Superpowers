# Subagent Task Packet and Result Contract

版本：v1.1.0

目标：让 Kiro main agent 派发 subagent 时不靠“自己理解”，而是提供完整、可审查、可回传的标准任务包。

## 一、Controller 规则

Kiro main agent 是 controller。任何 subagent 执行前，main agent 必须先读取并整理：

- `.kiro/specs/<spec>/requirements.md`
- `.kiro/specs/<spec>/design.md`
- `.kiro/specs/<spec>/tasks.md`
- 当前 task 的目标、范围、不做范围、完成定义和验证命令

subagent 不负责自己猜测 spec 背景。缺少上下文时，subagent 必须返回 `NEEDS_CONTEXT`。

## 二、Subagent Task Packet

派发 subagent 前必须构造任务包：

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
TDD 证据要求：RED/GREEN/REFACTOR / 不适用 / 例外待确认
Git evidence：BASE_SHA / changed files / 无法获取原因
```

## 三、范围边界

任务包必须明确：

- 允许修改的文件或目录；
- 禁止修改的文件或目录；
- 是否允许修改 API 契约；
- 是否允许修改数据库表或迁移；
- 是否允许修改状态机；
- 是否允许重构。

没有明确允许的内容，默认禁止。

## 四、Subagent Result Contract

每个 subagent 返回结果必须使用统一格式：

```text
SP Agent Result: <agent-name>
Status: DONE / BLOCKED / NEEDS_CONTEXT / FAILED
Task: ...
Spec: ...
Requirement/design/task coverage: ...
Completed work: ...
Changed files: ...
Verification command: ...
Verification result: ...
Risks: ...
Needs main-agent decision: ...
Next step: ...
```

## 五、禁止事项

- 不允许 subagent 自己扩大范围。
- 不允许 subagent 脱离任务包改代码。
- 不允许 subagent 跳过验证结果。
- 不允许 subagent 在缺少 spec/task/context 时继续执行。
- 不允许 main agent 把一句模糊任务直接丢给 subagent。

## 六、与既有流程关系

执行顺序：

```text
Task Refinement Gate
  ↓
Subagent Task Packet
  ↓
sp-implementer
  ↓
sp-test-verifier
  ↓
sp-spec-reviewer
  ↓
sp-code-reviewer
  ↓
Review Feedback Loop
  ↓
Task Completion Contract
```
