# TDD Discipline

## 默认规则

新功能、bugfix、重构、行为变化：默认 TDD。

流程：

```text
RED：写一个最小失败测试
  ↓
确认失败原因正确
  ↓
GREEN：写最小实现
  ↓
确认测试通过
  ↓
REFACTOR：只在绿灯后清理
  ↓
确认仍然通过
```

## 例外

以下情况可以不做完整 TDD，但必须说明原因并提供替代验证：

- 纯文档；
- 纯配置；
- 一次性探索原型；
- 很难自动化验证的 UI 微调。

## 红线

- 不允许“先实现，后补测试”伪装成 TDD。
- 测试一写就通过，不算 RED。
- 不允许为了让测试通过而削弱测试。
- 不能解释为什么测试失败，就不能继续实现。


## v0.9 TDD Evidence Contract

新功能、行为变更、bugfix 不再只要求“应该 TDD”，还必须留下 RED/GREEN/REFACTOR 证据。

执行前必须判断是否适用 TDD；完成前必须检查：RED 失败证据、GREEN 通过证据、REFACTOR 记录或不重构说明。

完整规则见 `tdd-evidence-contract.md`。
