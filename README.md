# Kiro Superpowers Discipline v1.5.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

**v1.5.0 是稳定版整理。** 它不新增新的开发流程能力；只统一 v0.9-v1.4 的术语、状态标识、agent 输出格式、hook 说明、文档入口和校验脚本。安装、卸载和日常使用方式保持不变。

## 最简单使用

用户不需要说“使用 Superpowers Discipline”，也不需要写长提示词。正常说业务目标即可：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```

## 统一状态标识

每次任务开始，Kiro 应显示短状态标识：

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification / branch-finishing
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-refinement / needs-tdd-evidence / needs-verification / blocked
```

## 统一状态词

```text
DONE：单个 agent 的限定职责完成。
COMPLETE：整个 task 满足完成定义，并有 fresh verification evidence。
NOT COMPLETE：完成定义未满足或验证失败。
BLOCKED：被 gate、验证、review 或用户决策阻塞。
NEEDS_CONTEXT：缺少 spec/task/文件/验证上下文。
FAILED：命令、测试或执行失败。
PARTIAL：只完成部分内容。
UNVERIFIED：无法验证，必须说明原因、风险和下一步。
```

## 工作方式

```text
新功能 → Feature Spec → requirements/design/tasks → Task Refinement Gate → Subagent Task Packet → worktree gate → TDD evidence → subagent loop → review evidence → fresh verification evidence → completion contract → branch finishing
Bugfix → 复现 → root-cause-tracing → multi-component diagnostics（如适用）→ defense-in-depth 判断 → condition-based waiting（如适用）→ Task Refinement Gate → RED 失败测试/替代验证 → 最小修复 → review evidence → fresh verification evidence → completion contract → branch finishing
继续任务 → 找当前 spec 未完成 task → 读取 requirements/design/tasks → Task Refinement Gate → Subagent Task Packet → subagent loop → fresh verification evidence → completion contract
审查/验收 → changed files + BASE_SHA/HEAD_SHA（如可用）+ spec review + code review + completion contract
并行 → Parallel Dispatch Plan → 冲突检查 → 并行收集/审查 → 统一 review/verification
```

## 已稳定保留的能力

- v0.3：状态标识、Superpowers Router、能力矩阵。
- v0.4：worktree 自动化、branch finishing、安全脚本。
- v0.5：subagent task loop、review feedback loop、`sp-review-feedback-handler`。
- v0.6：parallel agents 安全并行策略、Parallel Dispatch Plan。
- v0.7：Kiro task execution contract、executing-plans 纪律、task completion contract。
- v0.8：稳定化文档和校验脚本。
- v0.9：TDD Evidence Contract，要求 RED/GREEN/REFACTOR 证据和 TDD 例外确认。
- v1.0：Kiro Task Refinement Gate。
- v1.1：Subagent Task Packet、Subagent Result Contract、Review Evidence Contract、Git diff evidence。
- v1.2：Worktree hardening、baseline verification hardening、worktree metadata、branch finishing hardening。
- v1.3：Debugging Deep Techniques：root-cause-tracing、defense-in-depth、condition-based-waiting、multi-component diagnostics、3-fix architecture stop gate。
- v1.4：Fresh Verification Evidence：完成声明前必须提供本次验证命令、执行时间、exit code、pass/fail/skip count 或成功判断依据，未验证不得说 COMPLETE。
- v1.5：稳定版整理：统一术语、状态标识、agent 输出格式、hook 说明、文档入口和 validate-package.py。

## 定位

- Kiro 是主控软件。
- Kiro Specs 是规格骨架。
- 本包把 Superpowers 风格纪律放进 Kiro Power / Steering / Hooks / Agents。
- 不安装原版 Superpowers 插件。
- 不包含 ai_dev_os。
- 不提供多平台插件能力。

## 一句话安装

在 Kiro 打开项目后说：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板添加 Power：

```text
Powers → Add power from Local Path → 选择 <解压目录>/power
```

## 一句话卸载

按 `UNINSTALL.md` 删除项目中的 `.kiro/steering/superpowers-*.md`、`.kiro/hooks/*sp-*.kiro.hook`、`.kiro/agents/sp-*.md`、`.kiro/scripts/sp-*`，再从 Kiro Powers 面板卸载本 Power。

> 稳定规则：用户日常只说自然语言，不写长提示词。
