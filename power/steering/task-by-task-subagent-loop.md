# Task-by-task Subagent Loop

版本：v0.5.0

本规则把 Superpowers 的 subagent-driven-development 改造成 Kiro-native 的 task 执行循环。

## 核心原则

Kiro subagents 是执行载体，不是规格主控。Kiro main agent 必须做 controller。

main agent 必须先读取并整理：

- `.kiro/specs/<spec>/requirements.md`
- `.kiro/specs/<spec>/design.md`
- `.kiro/specs/<spec>/tasks.md`
- 当前 task 原文
- 当前 task 的完成定义
- 当前 task 的范围和不做范围

然后把完整 task context 传给 subagent。不要让 subagent 自己猜 spec 背景。

## 固定执行顺序

每个实现类 Kiro task 必须按下面顺序执行：

1. `sp-implementer`
2. `sp-test-verifier`
3. `sp-spec-reviewer`
4. `sp-code-reviewer`

## Gate 规则

- 没有完整 task context，不调用 implementer。
- `sp-test-verifier` 未验证，不进入 reviewer 阶段。
- `sp-spec-reviewer` 输出 `BLOCKED` 或 `NEEDS_CHANGES`，不进入 code review。
- `sp-code-reviewer` 输出 `BLOCKED` 或存在 blocker/major，不允许标记完成。
- 任何 reviewer 要求补上下文时，main agent 必须暂停并补上下文，不许猜。

## Task Context 模板

main agent 派发给 subagent 时必须包含：

```text
Spec: <name>
Task: <task id/title>
Requirement links: <REQ ids or sections>
Design links: <design sections>
Goal: <one sentence>
Scope: <what to change>
Non-goals: <what not to change>
Expected behavior: <observable behavior>
Verification command: <command or ask to discover>
Relevant files: <known files or unknown>
Risks: <known risks>
```

## 完成条件

一个 task 只有同时满足以下条件，才能标记完成：

1. 实现完成。
2. 测试或替代验证完成。
3. spec review 通过。
4. code review 通过。
5. 没有 blocker/major 未解决项。
6. 输出验证命令和结果。

## 用户体验

用户不需要手动说“请调用这些 subagent”。用户只说：

```text
继续当前 spec 的下一个任务
```

Kiro main agent 必须自动执行本 loop。
