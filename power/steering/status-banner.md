# Status Banner

每次开始处理开发、修复、继续任务、审查、验证类请求时，先输出一个极短状态标识。状态标识不是长解释，只让用户知道当前是否启用了 Kiro 规格主控和 Superpowers 执行纪律。

## 固定格式

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-verification / blocked
```

## 输出规则

1. 新功能开始时，`Kiro规格主控` 如果还没有 spec，显示 `待创建`。
2. 修 bug 开始时，当前流程显示 `bugfix-debugging`。
3. 继续任务时，必须显示当前 spec 和 task；找不到时显示 `未绑定`，并先定位。
4. 审查/验收时，当前阶段显示 `review` 或 `verify`。
5. 状态标识之后再给一句最小下一步，不要输出长流程。

## 示例

```text
【Kiro规格主控：待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements
当前流程：feature-spec
当前Task：未绑定
当前Gate：needs-spec

我会先把这个需求整理成可验收的 Kiro Feature Spec。
```

```text
【Kiro规格主控：启用】
【Superpowers执行纪律：启用】
当前阶段：implement
当前流程：task-execution
当前Task：TASK-003
当前Gate：passed

我会执行当前 task，并在完成前做验证和审查。
```

## 禁止

- 不要省略状态标识。
- 不要把状态标识扩写成大段说明。
- 不要要求用户手动说明是否启用 Superpowers Discipline。
