# Kiro Task Refinement Gate

## 目标

在执行任何 Kiro task 之前，先判断 task 是否足够清晰、足够小、可验证、并且和 requirements/design 有明确关联。

这个 gate 的作用不是替代 Kiro tasks，而是防止 AI 拿着过大的、模糊的、缺少验证方式的 task 直接开写。

## 适用范围

以下场景必须触发本 gate：

- 执行 Kiro spec task；
- 用户说“继续当前 spec 的下一个任务”；
- 用户要求实现、修改、修 bug、重构；
- subagent task loop 开始前；
- worktree 创建前；
- TDD Evidence Contract 开始前。

以下场景不强制触发，但仍可参考：

- 只读分析；
- 文档解释；
- 不改代码的代码审查；
- 用户只是询问流程。

## 执行前必须确认

Kiro main agent 在执行 task 前必须确认并简短输出：

```text
Task Refinement Gate：passed / blocked / needs-split / needs-context
Spec：<spec-name>
Requirement：<REQ-id or section>
Design：<design-section>
Task：<TASK-id>
目标：...
范围：...
不做：...
完成定义：...
验证命令：...
```

如果这些字段无法从 spec/task 中得到，不能猜。必须暂停并提问，或者建议回到 Kiro requirements/design/tasks 阶段补齐。

## 阻止执行的情况

以下任一情况出现时，必须暂停，不许开始实现：

1. task 目标不清楚。
2. task 有多个可能解释。
3. task 缺少 requirement 关联。
4. task 缺少 design 关联。
5. task 缺少完成定义。
6. task 缺少验证方式或替代验证方式。
7. task 太大，无法在一个清晰验证闭环内完成。
8. task 要求顺手做范围外内容。
9. task 与 requirements/design 冲突。
10. task 会跨越多个高风险边界但没有拆分，例如同时改数据库、后端、前端和任务队列。

## task 太大时怎么拆

发现 task 太大时，必须给出编号拆分建议，而不是直接执行。

拆分建议格式：

```text
当前 task 过大，建议拆分：
1. TASK-A：...
   - 范围：...
   - 验证：...
2. TASK-B：...
   - 范围：...
   - 验证：...
3. TASK-C：...
   - 范围：...
   - 验证：...

请选择：
1. 先拆分 tasks
2. 只执行其中一个明确子任务
3. 暂停，回到 design/tasks 更新
```

拆分判断标准：

- 一个 task 同时修改多个不相关模块；
- 一个 task 同时包含后端、前端、数据库、任务队列多类改动；
- 一个 task 无法用一个验证命令或一个验证闭环证明完成；
- 一个 task 同时包含实现、重构、性能优化、UI 调整等不同目标；
- 一个 task 的失败会让原因不可定位。

## 范围控制

禁止顺手做：

- 无关重构；
- 无关性能优化；
- 无关 UI 调整；
- 无关依赖升级；
- 未写进 task 的数据库/API 改动；
- 未写进 task 的数据结构变更；
- 未写进 task 的安全策略修改。

如果发现必须做范围外修改，必须先说明：

```text
发现范围外必要修改：...
原因：...
不做的风险：...
建议：
1. 当前 task 暂停，更新 design/tasks
2. 创建新 task
3. 用户明确确认后合并到当前 task
```

## 和已有纪律的关系

通过 Task Refinement Gate 之后，才进入：

1. worktree gate；
2. TDD Evidence Contract；
3. subagent task loop；
4. task completion contract；
5. branch finishing。

如果 Task Refinement Gate 被阻塞，不允许用 subagent 实现来绕过。
