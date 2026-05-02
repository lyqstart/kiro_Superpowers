# Review Feedback Loop

版本：v0.5.0

本规则把 Superpowers 的 receiving-code-review 纪律迁移到 Kiro。重点不是盲目接受审查意见，而是验证、分级、修复、再审查。

## Feedback 分级

所有 review feedback 必须归类为：

- `blocker`：阻止完成，必须修复。
- `major`：重要问题，必须修复后重新 review。
- `minor`：非阻塞建议，可以记录，不影响核心完成判断。
- `question`：信息不足，必须暂停提问，不许猜。

## 处理流程

收到 review feedback 后，main agent 必须：

1. 逐条编号。
2. 判断等级：blocker / major / minor / question。
3. 验证问题是否真实存在。
4. 与 requirements/design 冲突时，暂停并说明冲突。
5. 对 `question` 先问用户或补上下文，不许凭空假设。
6. 对 `blocker` / `major` 逐项修复。
7. 每修复一类问题，运行对应验证。
8. 修复后重新触发 `sp-spec-reviewer` 和 `sp-code-reviewer`。

## 禁止行为

- 不要看到 reviewer 意见就表演式同意。
- 不要盲目实现不适合当前代码库的建议。
- 不要把 minor 建议变成范围外重构。
- 不要在 question 没澄清前继续改代码。

## Review Feedback 输出模板

```text
Feedback handling status: DONE / NEEDS_USER_INPUT / BLOCKED
Blockers fixed: ...
Major issues fixed: ...
Minor notes recorded: ...
Questions needing answer: ...
Verification command: ...
Verification result: ...
Re-review required: yes/no
```
