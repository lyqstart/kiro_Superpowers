---
inclusion: always
---

# Superpowers Status Banner

每次处理开发、修复、继续任务、审查、验证请求时，先显示状态标识。

固定格式：

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-verification / blocked
```

状态标识之后只给一句最小下一步。不要输出长流程。用户不需要手动声明是否使用 Superpowers Discipline。
