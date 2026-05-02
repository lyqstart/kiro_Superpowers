# Subagent Routing

## 可用 custom subagents

- `sp-implementer`：实现明确 task。
- `sp-spec-reviewer`：检查实现是否符合 spec。
- `sp-code-reviewer`：检查代码质量、安全、可维护性。
- `sp-test-verifier`：运行/检查验证命令和结果。
- `sp-debugger`：复现、查根因、最小修复。

## 调用建议

### 执行功能 task

```text
主 agent 读取 spec/task
  ↓
sp-implementer 实现
  ↓
sp-spec-reviewer 审规格
  ↓
sp-code-reviewer 审质量
  ↓
sp-test-verifier 验证
```

### 修 bug

```text
sp-debugger 查根因并提出失败测试
  ↓
sp-implementer 最小修复
  ↓
sp-test-verifier 验证 bug 和回归
  ↓
sp-spec-reviewer 确认不变行为未破坏
```

## 调度原则

- 子 agent 只拿自己需要的上下文。
- 不把整段无关聊天历史交给子 agent。
- 子 agent 报告阻塞时，主 agent 不能强行重试，必须补上下文、换模型、拆任务或询问用户。


## v0.5 固定 task loop

实现类 Kiro task 必须进入固定 loop：

1. `sp-implementer`
2. `sp-test-verifier`
3. `sp-spec-reviewer`
4. `sp-code-reviewer`

main agent 必须先读取 requirements/design/tasks 并提供完整 task context。spec review 不通过，不进入 code review；code review 不通过，不标记完成。
