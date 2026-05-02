# 日常使用

目标：用户不背流程。你正常说需求，Kiro 自动按纪律执行。

每次开始任务时，你应该先看到类似：

```text
【Kiro规格主控：启用】
【Superpowers执行纪律：启用】
当前阶段：implement
当前流程：task-execution
当前Task：TASK-003
当前Gate：passed
```

## 1. 新功能

用户说：

```text
新增数据导出功能
```

Kiro 应该自动做：

```text
显示状态标识
  ↓
判断为新功能
  ↓
创建或更新 Feature Spec
  ↓
生成 requirements/design/tasks
  ↓
判断是否是实现类任务
  ↓
需要时进入 worktree gate
  ↓
按 TDD 执行任务
  ↓
完成前验证和审查
  ↓
通过后进入 branch finishing 四选项
```

## 2. 修 bug

用户说：

```text
修复登录接口偶发 500 的问题
```

Kiro 应该自动做：

```text
显示状态标识
  ↓
判断为 bugfix
  ↓
先复现
  ↓
查根因
  ↓
需要时创建隔离 worktree
  ↓
写失败测试或替代复现验证
  ↓
最小修复
  ↓
验证 bug 修复和回归行为
  ↓
通过后进入 branch finishing 四选项
```

## 3. 继续任务

用户说：

```text
继续当前 spec 的下一个任务
```

Kiro 应该自动做：

```text
显示状态标识
  ↓
找到当前 spec 和下一个未完成 task
  ↓
读取 requirements/design/tasks
  ↓
执行 pre-task gate
  ↓
如果是实现类任务，执行 worktree gate
  ↓
执行、验证、审查
  ↓
通过后标记完成并进入 branch finishing
```

## 4. 检查是否完成

用户说：

```text
检查当前任务是否真的完成
```

Kiro 应该自动做：

```text
显示状态标识
  ↓
查看 diff
  ↓
运行测试/构建/lint
  ↓
检查 spec compliance
  ↓
检查代码质量
  ↓
给出：完成 / 未完成 / 阻塞
```


## 5. v0.5 subagent task loop

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
  ↓
通过后才允许标记 task 完成
```

如果 spec review 不通过，不能进入 code review。如果 code review 有 blocker/major，不能标记完成。

## 6. v0.5 review feedback loop

审查反馈必须分级：

```text
blocker：必须修复
major：必须修复并重新 review
minor：记录建议，不影响核心完成判断
question：暂停提问，不许猜
```

Kiro 可以调用 `sp-review-feedback-handler` 处理反馈，但用户不需要手动点名。

## 7. 分支收尾

任务通过验证后，Kiro 不应该自动合并，而应该给出：

```text
1. 合并回主分支
2. 推送并创建 PR
3. 保留分支
4. 丢弃本次工作
```

选择 4 时必须二次确认。

## 用户不需要再说的话

日常不要要求用户写：

```text
必须先读取 requirements.md、design.md、tasks.md
必须创建 worktree
必须按 RED/GREEN/REFACTOR
必须运行验证命令
```

这些是系统纪律，不是用户输入负担。
