# MIGRATION

## 从 v0.4.0 升级到 v0.5.0

升级方式不变：重新运行安装脚本即可覆盖/补充项目级文件，然后在 Kiro Powers 面板确认 Power 指向新版 `power/` 目录。

新增文件：

```text
power/steering/task-by-task-subagent-loop.md
power/steering/review-feedback-loop.md
workspace-assets/.kiro/steering/superpowers-task-by-task-subagent-loop.md
workspace-assets/.kiro/steering/superpowers-review-feedback-loop.md
workspace-assets/.kiro/agents/sp-review-feedback-handler.md
```

保留行为：

- 原安装提示不变。
- 原卸载方式仍然有效，因为 `.kiro/agents/sp-*.md` 会覆盖新增 agent。
- v0.4 worktree 自动化和 branch finishing 不变。
- 不引入 ai_dev_os。

注意：

v0.5 增强的是 subagent 执行顺序和 review feedback 处理，不改变用户日常入口。用户仍然只需要说“新增 xxx / 修复 xxx / 继续当前 spec 的下一个任务”。

# Migration Guide

## v0.3.0 → v0.5.0

v0.5.0 是兼容性增强版本，不改变 v0.3.0 的安装、卸载和日常使用方式。

## 是否需要重新安装

需要。因为 v0.5.0 新增 workspace steering、hooks 和 scripts。

请按原安装方式重新执行：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板确认 Power 指向新版解压目录的 `power/`。

## 兼容性

保持不变：

- 安装入口不变。
- 卸载方式不变。
- 日常使用方式不变。
- 旧 hooks 保留。
- 旧 agents 保留。
- 状态标识保留。
- Superpowers Router 保留。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## 新增文件

```text
power/steering/worktree-automation.md
power/steering/branch-finishing.md
workspace-assets/.kiro/steering/superpowers-worktree-automation.md
workspace-assets/.kiro/steering/superpowers-branch-finishing.md
workspace-assets/.kiro/hooks/05-sp-worktree-gate.kiro.hook
workspace-assets/.kiro/hooks/06-sp-branch-finishing.kiro.hook
workspace-assets/.kiro/scripts/sp-worktree-create.sh
workspace-assets/.kiro/scripts/sp-finish-branch.sh
workspace-assets/.kiro/scripts/sp-worktree-create.ps1
workspace-assets/.kiro/scripts/sp-finish-branch.ps1
scripts/sp-worktree-create.sh
scripts/sp-finish-branch.sh
scripts/sp-worktree-create.ps1
scripts/sp-finish-branch.ps1
```

## 卸载变化

卸载仍然简单，但要额外删除 `.kiro/scripts/sp-*`：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

## 安全说明

- worktree 创建脚本不会覆盖脏工作区。
- finishing 脚本不会默认合并。
- 丢弃未提交改动必须二次确认。
- 脚本不会默认删除 worktree 目录。
