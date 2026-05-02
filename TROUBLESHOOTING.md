# 故障排查

## 1. Kiro 直接开始写代码

这说明 gate 没生效。你可以说：

```text
停止。请先显示状态标识，并说明当前是否启用 Kiro Spec 和 Superpowers执行纪律。
```

正确状态标识应包含：

```text
【Kiro规格主控：...】
【Superpowers执行纪律：启用】
当前阶段：...
当前流程：...
当前Task：...
当前Gate：...
```

## 2. Kiro 要求你写长提示词

这是错误用法。用户只需要说自然语言：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```

## 3. task 太大或不清楚

v1.0 要求 Kiro Task Refinement Gate。task 有歧义、缺少 requirement/design 关联、缺少验证命令或完成定义时，Kiro 应暂停并给出编号拆分建议。

## 4. TDD 证据缺失

v0.9 要求 TDD Evidence Contract。新功能、行为变更、bugfix 没有 RED/GREEN 证据时，不能说 COMPLETE。无法 TDD 时必须说明原因、替代验证和用户确认需求。

## 5. review 很空泛

v1.1 要求 Review Evidence Contract。review 必须基于 changed files、BASE_SHA/HEAD_SHA（如可用）、requirement/design/task coverage，不能只给泛泛建议。

## 6. worktree 或 branch finishing 看起来危险

v1.2 要求危险操作二次确认。丢弃必须显示 branch、worktree path、changed files、commits 列表，并要求明确确认。默认不删除用户代码。

## 7. 修 bug 只打补丁不查根因

v1.3 要求 root-cause-tracing。没有根因链路时不能进入修复阶段。同一个问题三次修复失败时必须触发 architecture stop gate。

## 8. verification 失败怎么办

v1.4 要求 Fresh Verification Evidence。验证失败时必须输出 `NOT COMPLETE` 或 `BLOCKED`，不能说 COMPLETE。无法验证时输出 `UNVERIFIED`，并说明原因、风险和下一步。

## 9. 状态词混乱怎么办

v1.5 统一状态词：

```text
DONE / COMPLETE / NOT COMPLETE / BLOCKED / NEEDS_CONTEXT / FAILED / PARTIAL / UNVERIFIED
```

如果 Kiro 使用其他含糊状态，你可以要求它重新按 v1.5 状态词输出。

## 10. 安装不生效

检查：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

并确认 Kiro Powers 面板已经添加 `<解压目录>/power`。

## v2.0 Troubleshooting

### Kiro does not show Skill Runtime Lite
Ask:

```text
请显示 Skill Activation Ledger，并说明本次匹配到哪些 Superpowers skills。
```

### Kiro starts coding without brainstorming
Stop it and say:

```text
停止。请先通过 v2.0 Kiro Spec Brainstorming Gate，不要进入实现。
```

### Kiro says COMPLETE without final review
Ask:

```text
请先运行 Final Whole-Feature Review Gate 和 Fresh Verification Evidence，再判断是否 COMPLETE。
```
