# Kiro Superpowers Discipline v1.2.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

**v1.2.0 是 Worktree / Branch Finishing Hardening 版本。** 它只在 v1.1.0 基础上增强 worktree 安全检查、baseline verification、worktree metadata 和 branch finishing 安全收尾；安装、卸载和日常使用方式保持不变。

## 最简单使用

用户不需要说“使用 Superpowers Discipline”，也不需要写长提示词。正常说业务目标即可：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```

Kiro 应该自动判断流程，并在任务开始时显示短状态标识。

## 统一状态标识

```text
【Kiro规格主控：启用/未启用/待创建】
【Superpowers执行纪律：启用】
当前阶段：requirements / design / tasks / implement / debug / review / verify / finalize
当前流程：feature-spec / bugfix-debugging / task-execution / review / verification / branch-finishing
当前Task：TASK-xxx / 未绑定 / 待选择
当前Gate：passed / needs-spec / needs-task / needs-verification / blocked
```

## 工作方式

```text
新功能 → Feature Spec → requirements/design/tasks → Task Refinement Gate → Subagent Task Packet → worktree gate → TDD evidence → subagent loop → review evidence → completion contract → branch finishing
Bugfix → 复现 → 根因 → Task Refinement Gate → Subagent Task Packet → RED 失败测试/替代验证 → 最小修复 → review evidence → completion contract → branch finishing
继续任务 → 找当前 spec 未完成 task → 读取 requirements/design/tasks → Task Refinement Gate → Subagent Task Packet → subagent loop → completion contract
审查/验收 → changed files + BASE_SHA/HEAD_SHA（如可用）+ spec review + code review + completion contract
并行 → Parallel Dispatch Plan → 冲突检查 → 并行收集/审查 → 统一 review/verification
```

## 已稳定保留的能力

- v0.3：状态标识、Superpowers Router、能力矩阵。
- v0.4：worktree 自动化、branch finishing、安全脚本。
- v0.5：subagent task loop、review feedback loop、`sp-review-feedback-handler`。
- v0.6：parallel agents 安全并行策略、Parallel Dispatch Plan。
- v0.7：Kiro task execution contract、executing-plans 纪律、task completion contract。
- v0.8：统一术语、统一状态标识、统一 hook 命名、统一 agent 输出格式、整理 README/INSTALL/UNINSTALL/USAGE/TROUBLESHOOTING、增强校验脚本。
- v0.9：TDD Evidence Contract，要求 RED/GREEN/REFACTOR 证据和 TDD 例外确认。
- v1.0：Kiro Task Refinement Gate，执行前检查 task 清晰度、范围、requirement/design 关联、完成定义、验证命令和是否需要拆分。
- v1.1：Subagent Task Packet、Subagent Result Contract、Review Evidence Contract、Git diff evidence。
- v1.2：Worktree hardening、baseline verification hardening、worktree metadata、branch finishing hardening。

## 定位

- Kiro 是主控软件。
- Kiro Specs 是规格骨架。
- 本包把 Superpowers 风格纪律放进 Kiro Power / Steering / Hooks / Agents。
- 不安装原版 Superpowers 插件。
- 不包含 ai_dev_os。
- 不提供多平台插件能力。

## 包含内容

```text
power/
  POWER.md
  steering/*.md

workspace-assets/.kiro/
  steering/*.md
  hooks/*.kiro.hook
  agents/*.md
  scripts/sp-*.sh
  scripts/sp-*.ps1

install/
  install.ps1
  install.sh

scripts/
  validate_package.py
  sp-*.sh
  sp-*.ps1

README.md
INSTALL.md
INSTALL_FOR_KIRO.md
UNINSTALL.md
USAGE.md
TROUBLESHOOTING.md
SUPERPOWERS_CAPABILITY_MATRIX.md
CHANGELOG.md
MIGRATION.md
```

## 一句话安装

在 Kiro 打开项目后说：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

脚本安装项目级文件后，还需要在 Kiro Powers 面板添加 Power：

```text
Powers → Add power from Local Path → 选择 <解压目录>/power
```

## 一句话卸载

按 `UNINSTALL.md` 删除项目中的 `.kiro/steering/superpowers-*.md`、`.kiro/hooks/*sp-*.kiro.hook`、`.kiro/agents/sp-*.md`、`.kiro/scripts/sp-*`，再从 Kiro Powers 面板卸载本 Power。

> 稳定规则：不要求用户写长提示词。


关键词：Branch finishing hardening, baseline verification, worktree metadata, DISCARD_WORK, CLEAN_WORKTREE.
