---
inclusion: always
---

# Superpowers Discipline for Kiro Workspace

本项目安装了 Kiro Superpowers Discipline。

## 核心原则

用户不需要背流程。用户正常说需求，Kiro 自动按纪律处理。

用户可能只说：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否完成
```

你必须自动判断：

- 新功能 → Feature Spec → requirements/design/tasks → TDD 执行 → 验证；
- bug → Bugfix Spec → 复现 → 根因 → 失败测试 → 最小修复 → 验证；
- 继续 → 找当前 spec 的下一个未完成 task → 执行前检查 → 开发 → 验证；
- 检查完成 → diff + 测试/构建/lint + spec review + code review。

## 不要让用户每次写长提示词

不要要求用户说：

```text
请读取 requirements.md、design.md、tasks.md
请按 RED/GREEN/REFACTOR
请做规格符合性审查
请运行验证命令
```

这些是系统责任。


## v0.3 状态标识

每次处理开发、修复、继续任务、审查、验证请求时，先显示：

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-verification / blocked
```

状态标识之后只给一句最小下一步。

## v0.3 Router

- 新功能：进入 Feature Spec，走 requirements/design/tasks + TDD。
- bugfix：进入 systematic debugging，先复现、查根因、失败测试或替代验证。
- 继续任务：定位当前 spec 和下一个未完成 task，执行前通过 gate。
- 审查：先 spec review，再 code review，再 test review。
- 完成/验收：必须运行或确认新鲜验证证据，输出 COMPLETE / NOT COMPLETE / BLOCKED。

## 强制纪律

1. 没有规格，不进入中大型实现。
2. 没有明确 task，不做大范围代码修改。
3. 行为变化默认 TDD。
4. bugfix 先复现和查根因。
5. 完成前必须有新鲜验证证据。
6. 先做 spec compliance review，再做 code quality review。
7. 不做无关重构。
8. 不把内部流程暴露成用户负担。

## 给用户的回复风格

短、直接、可执行。

开始时：

```text
我会按新功能处理：先确认 spec，再执行下一个可验证 task。
```

完成时：

```text
状态：完成 / 未完成 / 阻塞
验证命令：...
结果：...
改动：...
风险：...
```
