# MIGRATION

## 从 v0.6.0 升级到 v0.7.0

升级方式不变：重新运行安装脚本即可覆盖/补充项目级文件，然后在 Kiro Powers 面板确认 Power 指向新版 `power/` 目录。

新增文件：

```text
power/steering/kiro-task-execution-contract.md
power/steering/executing-plans-discipline.md
power/steering/task-completion-contract.md
workspace-assets/.kiro/steering/superpowers-kiro-task-execution-contract.md
workspace-assets/.kiro/steering/superpowers-executing-plans-discipline.md
workspace-assets/.kiro/steering/superpowers-task-completion-contract.md
workspace-assets/.kiro/hooks/08-sp-task-execution-contract.kiro.hook
workspace-assets/.kiro/hooks/09-sp-task-completion-contract.kiro.hook
workspace-assets/.kiro/hooks/10-sp-post-task-branch-finishing-check.kiro.hook
```

保留行为：

- 原安装提示不变。
- 原卸载方式仍然有效，因为 `.kiro/steering/superpowers-*.md`、`.kiro/hooks/*sp-*.kiro.hook`、`.kiro/agents/sp-*.md` 和 `.kiro/scripts/sp-*` 会覆盖新增文件。
- v0.4 worktree 自动化和 branch finishing 不变。
- v0.5 subagent task loop 和 review feedback loop 不变。
- v0.6 parallel agents 安全策略不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

注意：

v0.7 增强的是 Kiro task 执行合同和完成合同。用户仍然只需要说“新增 xxx / 修复 xxx / 继续当前 spec 的下一个任务 / 检查当前任务是否完成”。

## 是否需要重新安装

需要。因为 v0.7.0 新增 workspace steering 和 hooks。

请按原安装方式重新执行：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板确认 Power 指向新版解压目录的 `power/`。

## 卸载方式

卸载方式不变：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

然后在 Kiro Powers 面板卸载本 Power。
