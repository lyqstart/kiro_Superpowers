# Task Completion Contract

## 不允许“口头完成”

完成前必须给出新鲜验证证据。没有证据，只能说未验证，不能说完成。

## 完成报告必须包含

```text
状态：COMPLETE / NOT COMPLETE / BLOCKED
验证命令：...
验证结果：...
改动文件：...
满足的 requirement/design/task：...
剩余风险：...
下一步：...
```

## COMPLETE 条件

只有同时满足以下条件，才能输出 COMPLETE：

1. 已绑定明确 Kiro task。
2. 已说明满足哪个 requirement/design/task。
3. 已运行验证命令，或给出合理替代验证。
4. 已读取验证输出。
5. 已通过 spec review。
6. 已通过 code review。
7. 没有 blocker/major 未处理。
8. 没有范围外修改未确认。

## NOT COMPLETE 条件

以下任一情况必须输出 NOT COMPLETE：

- 测试失败；
- 构建失败；
- lint 失败且与本 task 相关；
- spec review 未通过；
- code review 有 blocker/major；
- 验证命令未运行且没有合理替代验证；
- task 目标只完成一部分。

## BLOCKED 条件

以下任一情况输出 BLOCKED：

- 缺少需求/design/task 关联；
- 需要用户确认范围；
- 需要外部系统、凭据、数据或环境；
- 当前 git 状态不安全；
- worktree/branch 操作需要用户选择。
