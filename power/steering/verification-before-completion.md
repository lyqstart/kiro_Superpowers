# Verification Before Completion

## 核心规则

没有新鲜验证证据，不允许说完成。

## 完成前必须执行

1. 指出证明当前结论的命令。
2. 运行完整命令。
3. 读取输出和退出码。
4. 汇报实际结果。
5. 再判断是否完成。

## 不能接受的说法

- 应该可以；
- 看起来没问题；
- 我认为已经修好；
- 之前跑过；
- agent 报告成功；
- lint 通过所以 build 应该也通过。

## 报告格式

```text
验证命令：...
退出状态：...
通过：...
失败：...
关键输出：...
结论：通过 / 未通过 / 阻塞
```


## v1.4 Fresh Verification Evidence

完成声明前必须引用本次新鲜验证证据。验证报告必须包含验证命令、执行时间、exit code、pass/fail/skip count（或成功判断依据）、关键输出摘要和失败信息摘要。

状态扩展为：

- COMPLETE：fresh verification 通过，且 review gate 通过。
- NOT COMPLETE：验证失败或 blocker/major 未处理。
- PARTIAL：只完成部分内容，或仍有未验证路径。
- BLOCKED：缺少环境、凭据、数据、用户确认或 git 安全状态。
- UNVERIFIED：实现可能完成，但没有本次新鲜验证证据。

禁止用“之前跑过”或 subagent 口头成功报告作为完成依据。
