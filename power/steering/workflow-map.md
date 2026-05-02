# Workflow Map

## 用户看到的流程

用户只需要自然语言描述目标：

```text
新增 xxx
修复 xxx
继续下一个任务
检查是否完成
```

## 系统内部流程

```text
识别工作类型
  ↓
Feature Spec / Bugfix Spec / Continue Task / Final Verification
  ↓
读取或生成 requirements / bugfix、design、tasks
  ↓
任务准备检查
  ↓
TDD / 系统化调试 / 最小实现
  ↓
规格符合性审查
  ↓
代码质量审查
  ↓
完成前验证
  ↓
标记 task 完成
```

## 决策规则

- 新功能：Feature Spec。
- 关键 bug：Bugfix Spec。
- 简单小改：可简化，但不能跳过验证。
- 涉及业务行为变化：必须有 spec/task。
- 涉及多个模块：拆分 task。

## 禁止行为

- 没读 spec 就写代码。
- 没确认验收标准就写代码。
- 没有复现就修 bug。
- 没有验证证据就说完成。
- 顺手重构无关代码。
- 把内部流程要求转嫁给用户。
