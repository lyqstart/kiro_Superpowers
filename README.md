# Kiro Superpowers Discipline v0.4.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

v0.4.0 保持 v0.3.0 的安装、卸载和日常使用方式不变，只新增：

1. **worktree 自动化**：实现类任务默认检查 git 状态，避免直接在 main/master 上开发，优先创建隔离 worktree。
2. **branch finishing**：实现任务验证通过后，提供合并、PR、保留、丢弃四个编号选项；不自动合并或丢弃。
3. **安全脚本**：新增 Windows PowerShell 和 macOS/Linux shell 脚本，用于创建 worktree 和分支收尾。

## 用户日常不需要写长提示词

用户只需要正常说：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否完成
```

Kiro 应该自动判断流程：

```text
新功能 → Feature Spec → requirements/design/tasks → worktree gate → TDD → 审查 → 验证 → branch finishing
Bug → Bugfix Spec → 复现 → 根因 → worktree gate → 失败测试/替代验证 → 修复 → 验证 → branch finishing
继续 → 找当前 spec 未完成 task → worktree gate → 执行 → 审查 → 验证 → branch finishing
审查/验收 → diff + test/build/lint + spec review + code review
```

## 状态标识示例

```text
【Kiro规格主控：启用】
【Superpowers执行纪律：启用】
当前阶段：implement
当前流程：task-execution
当前Task：TASK-003
当前Gate：passed
```

## v0.4 Worktree 行为

实现类任务默认进入 worktree 流程：

- 当前分支是 `main` / `master` 时，不直接开发，除非用户明确确认。
- 创建 worktree 前检查 git 状态。
- 工作区不干净时停止，不覆盖用户改动。
- 如果能识别 baseline 验证命令，创建 worktree 后先运行 baseline。
- 小修改、文档修改、只读分析不强制 worktree。

## v0.4 Branch finishing 行为

任务完成后不自动合并，而是给用户四个编号选项：

1. 合并回主分支
2. 推送并创建 PR
3. 保留分支
4. 丢弃本次工作

丢弃必须二次确认。

## 定位

- Kiro 是主控软件。
- Kiro Specs 是规格骨架。
- 本包把 Superpowers 风格纪律放进 Kiro Power / Steering / Hooks / Agents。
- 不安装原版 Superpowers 插件。
- 不包含 ai_dev_os。

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

INSTALL_FOR_KIRO.md
USAGE.md
SUPERPOWERS_CAPABILITY_MATRIX.md
MIGRATION.md
```

## 最简单安装

1. 解压这个包。
2. 在 Kiro 打开你的项目。
3. 对 Kiro 说一句：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

例如：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:\tools\kiro_superpowers_discipline_v0_4_0
```

Kiro 应该读取 `INSTALL_FOR_KIRO.md`，运行对应脚本，并提示你把 `power/` 目录添加到 Kiro Powers。

## 卸载

删除项目中的：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

然后在 Kiro Powers 面板卸载本 Power。
