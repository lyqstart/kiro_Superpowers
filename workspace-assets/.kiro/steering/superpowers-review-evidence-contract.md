# Review Evidence Contract

版本：v1.1.0

目标：让 spec review 和 code review 基于真实证据，而不是空泛评论。

## 一、Review 前证据

review 前尽量记录：

```text
BASE_SHA：...
HEAD_SHA：...
Changed files：...
Spec：...
Requirement：...
Design section：...
Task：...
Verification command：...
Verification result：...
```

如果无法获取 SHA，必须说明原因。不能因为没有 SHA 就跳过 changed files 和实际 diff 审查。

## 二、Spec Review Evidence

`sp-spec-reviewer` 必须说明：

- 满足了哪些 requirement；
- 未满足哪些 requirement；
- 是否符合 design section；
- 是否完成当前 task；
- 是否做了范围外内容；
- 哪些 acceptance criteria 有验证证据；
- 哪些 acceptance criteria 缺少验证证据。

没有 requirements/design/task 上下文时，返回 `NEEDS_CONTEXT`。

## 三、Code Review Evidence

`sp-code-reviewer` 必须基于实际 diff、changed files 或文件内容审查。必须检查：

- 正确性；
- 安全性；
- 错误处理；
- 可维护性；
- 测试质量；
- 无关改动；
- 是否有隐藏范围扩大。

## 四、问题分级

所有 review issue 必须分级：

- `blocker`：阻止完成，必须修复；
- `major`：重要问题，必须修复并重新 review；
- `minor`：建议，记录即可，不影响核心完成；
- `question`：信息不足，必须暂停提问，不许猜。

## 五、Review Result Contract

review 输出必须使用：

```text
SP Agent Result: <agent-name>
Review status: PASS / NEEDS_CHANGES / NEEDS_CONTEXT / BLOCKED
BASE_SHA: ...
HEAD_SHA: ...
Changed files: ...
Requirement/design/task coverage: ...
Blockers: ...
Major issues: ...
Minor issues: ...
Questions: ...
Required fixes: ...
Re-review required: yes/no
```

## 六、硬规则

- spec review 不通过，不允许进入 code review。
- code review 有 blocker/major，不允许标记完成。
- blocker/major 修复后必须重新 review。
- question 必须先解决，不允许猜。
- review 不允许脱离实际改动做空泛建议。
