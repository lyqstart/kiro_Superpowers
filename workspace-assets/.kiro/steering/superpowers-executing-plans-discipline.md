---
inclusion: always
---


# Executing Kiro Tasks Discipline

## 一句话

Kiro tasks 是执行计划的来源。执行时必须逐项验证，不允许靠感觉推进下一个 task。

## 每个 task 执行前

输出简短确认：

```text
目标：...
范围：...
不做：...
完成定义：...
验证命令：...
```

这段必须短。不要把内部流程变成用户负担。

## 执行中

- 一次只执行当前 task。
- 遇到 blocker 必须停止并说明。
- 测试失败不能继续下一个 task。
- verification 失败不能标记完成。
- review 发现 blocker/major，必须修复并重新 review。
- question 类型反馈必须暂停提问，不许猜。

## 执行后

只有满足以下条件，才允许进入下一个 task：

1. 当前 task 的代码修改完成。
2. 验证命令已运行或明确说明无法运行及替代验证。
3. 验证结果已读取并总结。
4. `sp-test-verifier` 通过。
5. `sp-spec-reviewer` 通过。
6. `sp-code-reviewer` 没有 blocker/major。
7. 剩余风险已说明。

## 全部 task 完成后

如果当前工作发生代码修改并且验证通过，进入 branch finishing：

1. 合并回主分支。
2. 推送并创建 PR。
3. 保留分支。
4. 丢弃本次工作。

不允许自动选择。
