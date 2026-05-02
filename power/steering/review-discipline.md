# Review Discipline

## 审查顺序

### 1. Spec Compliance Review

先检查实现是否符合：

- requirements.md / bugfix.md；
- design.md；
- tasks.md；
- task 完成定义；
- 不做范围。

输出：

```text
规格符合性：通过 / 不通过
覆盖的 requirements：...
缺口：...
额外实现：...
风险：...
```

### 2. Code Quality Review

再检查：

- 正确性；
- 安全；
- 错误处理；
- 可维护性；
- 复杂度；
- 测试质量；
- 是否有无关改动。

输出：

```text
代码质量：通过 / 需修改
必须修改：...
建议修改：...
不阻塞事项：...
```

## 禁止

- 只跑测试不审 spec。
- 只看代码风格不看业务目标。
- 发现缺口但仍标记完成。
