# Kiro Superpowers Discipline v0.6.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

v0.6.0 保持 v0.5.0 的安装、卸载和日常使用方式不变，只新增：

1. **parallel agents 安全并行策略**：只有通过冲突检查的任务才允许并行。
2. **Parallel Dispatch Plan**：并行前必须列出目标、文件、接口、数据库表、迁移脚本、状态机、验证命令、agent 和风险。
3. **并行后统一收口**：并行结束后统一进入 spec review / code review / test verification。

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
新功能 → Feature Spec → requirements/design/tasks → worktree gate → TDD → subagent loop → 审查 → 验证 → branch finishing
Bug → Bugfix Spec → 复现 → 根因 → worktree gate → 失败测试/替代验证 → 修复 → 验证 → branch finishing
继续 → 找当前 spec 未完成 task → worktree gate → subagent loop → 审查 → 验证 → branch finishing
审查/验收 → diff + test/build/lint + spec review + code review
并行 → 先输出 Parallel Dispatch Plan → 通过冲突检查才允许并行
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

## v0.5 Subagent Task Loop 行为

实现类 Kiro task 不直接由一个 agent 从头做到尾，而是固定经过：

1. `sp-implementer` 实现一个明确 task。
2. `sp-test-verifier` 检查新鲜验证证据。
3. `sp-spec-reviewer` 检查是否符合 requirements/design/task。
4. `sp-code-reviewer` 检查代码质量。

Kiro main agent 必须先读取 `requirements.md`、`design.md`、`tasks.md`，把完整 task 上下文传给 subagent。不允许 subagent 自己猜 spec 背景。

## v0.5 Review Feedback 行为

Review feedback 必须分级：

- `blocker`：阻止完成，必须修复。
- `major`：重要问题，必须修复后重新 review。
- `minor`：建议，可以记录，不影响核心完成判断。
- `question`：信息不足，必须暂停提问，不许猜。

## v0.6 Parallel Agents 行为

并行前必须先输出 Parallel Dispatch Plan。

只允许并行满足以下条件的任务：

- 不改同一批文件。
- 不改同一个接口契约。
- 不改同一张数据库表。
- 不共享迁移脚本。
- 不共享状态机。
- 每个并行任务有独立验证命令。

默认允许并行 context gathering / review，不默认并行 implementation。如果边界不清晰，必须禁止并行。并行结束后，必须统一汇总、检查冲突，并进入 spec review / code review / test verification。

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
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:	ools\kiro_superpowers_discipline_v0_6_0
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
