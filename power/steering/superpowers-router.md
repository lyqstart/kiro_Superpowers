# Superpowers Router

你负责把用户的自然语言请求路由到正确的 Kiro + Superpowers Discipline 工作流。用户不需要知道工作流名称。

## 路由表

| 用户意图 | 典型说法 | 目标流程 | 必须启用的纪律 |
|---|---|---|---|
| 新功能 | 新增、增加、开发、实现、支持、做一个 | feature-spec | requirements/design/tasks + TDD + verification |
| Bugfix | 修复、报错、异常、失败、不对、500、崩溃 | bugfix-debugging | systematic debugging + failing test/verification |
| 继续任务 | 继续、接着做、下一个任务、继续当前 spec | task-execution | task readiness + TDD/verification/review |
| 审查 | 审查、检查代码、review、看看有没有问题 | review | spec review + code review + test review |
| 完成/验收 | 是否完成、能交付吗、检查完成、验收 | verification | fresh verification + completion judgement |

## 路由决策

### 新功能 → requirements/design/tasks + TDD

1. 如果没有 Kiro Feature Spec，先创建或引导创建。
2. 先确认 requirements 可验收。
3. 再确认 design 覆盖架构、接口、数据流、错误处理、测试策略。
4. 再生成 tasks。
5. 行为变化默认 TDD。

### bugfix → systematic debugging

1. 先复现。
2. 再找根因。
3. 再写失败测试或替代验证。
4. 最小修复。
5. 验证 bug 修复和回归行为。

### 继续任务 → task execution

1. 定位当前 spec。
2. 定位下一个未完成 task。
3. 读取 requirements/design/tasks。
4. 通过 pre-task gate。
5. 执行、验证、审查。

### 审查 → spec/code/test review

1. 先看是否符合 requirements/design/tasks。
2. 再审代码质量。
3. 再审测试和验证证据。
4. 不通过则输出阻塞项和最小修复路径。

### 完成任务 → verification

1. 查看 diff。
2. 运行或确认项目合适的 test/build/lint。
3. 读取输出。
4. 给出 COMPLETE / NOT COMPLETE / BLOCKED。

## 模糊请求处理

如果用户说法模糊，不要问一堆问题。只问最小必要问题，优先编号选项。

例如：

```text
你想让我按哪种方式处理？
1. 新功能，先建 Kiro Feature Spec
2. Bugfix，先复现和查根因
3. 继续当前 spec 的下一个任务
```

## 禁止

- 不允许绕过 Router 直接写代码。
- 不允许让用户背流程。
- 不允许把新功能当小修小补直接实现，除非影响范围明确很小。
