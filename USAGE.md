# 日常使用

目标：用户不背流程。你正常说需求，Kiro 自动按纪律执行。

v0.3.0 新增状态标识。每次开始任务时，你应该先看到类似：

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
生成 requirements.md
  ↓
确认关键验收标准
  ↓
生成 design.md
  ↓
生成 tasks.md
  ↓
执行前检查 task 是否可测试、可验证、可审查
  ↓
按 TDD 执行任务
  ↓
完成前验证和审查
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
记录复现步骤、当前行为、期望行为、不变行为
  ↓
先复现
  ↓
查根因
  ↓
写失败测试或替代复现验证
  ↓
最小修复
  ↓
验证 bug 修复和回归行为
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
找到当前 spec
  ↓
找到下一个未完成 task
  ↓
读取 requirements/design/tasks
  ↓
执行 pre-task gate
  ↓
执行、验证、审查
  ↓
通过后标记完成
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

## 用户不需要再说的话

日常不要要求用户写：

```text
必须先读取 requirements.md、design.md、tasks.md
必须按 RED/GREEN/REFACTOR
必须运行验证命令
```

这些是系统纪律，不是用户输入负担。
