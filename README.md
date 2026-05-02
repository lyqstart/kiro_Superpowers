# Kiro Superpowers Discipline v0.7.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

v0.7.0 保持 v0.2-v0.6 的安装、卸载和日常使用方式不变，只新增：

1. **Kiro task execution contract**：执行前必须批判性阅读 task，检查 requirement/design/task 关联、范围、不做范围、完成定义和验证方式。
2. **Executing-plans 完整纪律**：task 有歧义先问，不许猜；遇到 blocker 停止；测试或 verification 失败不能继续下一个 task。
3. **Task completion contract**：完成前必须给出验证命令、验证结果、改动文件、满足的 requirement/design/task 和剩余风险。
4. **增强 hooks**：task 执行前检查 contract，task 完成后检查 completion contract，完成后检查是否需要 branch finishing。

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
新功能 → Feature Spec → requirements/design/tasks → worktree gate → TDD → subagent loop → 审查 → completion contract → branch finishing
Bug → Bugfix Spec → 复现 → 根因 → worktree gate → 失败测试/替代验证 → 修复 → completion contract → branch finishing
继续 → 找当前 spec 未完成 task → task execution contract → worktree gate → subagent loop → completion contract → branch finishing
审查/验收 → diff + test/build/lint + spec review + code review + completion contract
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

## v0.7 Task execution contract

执行 Kiro task 前，Kiro main agent 必须先检查：

- 当前 task 目标；
- 范围和不做范围；
- 完成定义；
- requirement/design/task 关联；
- 预计修改文件；
- 验证命令；
- 剩余风险。

如果 task 有歧义、缺少 requirement/design 关联、太大、或要求范围外内容，必须暂停，不许猜。

## v0.7 Task completion contract

完成前必须输出：

```text
状态：COMPLETE / NOT COMPLETE / BLOCKED
验证命令：...
验证结果：...
改动文件：...
满足的 requirement/design/task：...
剩余风险：...
下一步：...
```

测试失败、verification 失败、spec review 不通过、code review 有 blocker/major 时，不能标记完成，不能继续下一个 task。

## v0.6 Parallel Agents 行为

并行前必须先输出 Parallel Dispatch Plan。默认允许并行 context gathering / review，不默认并行 implementation。如果边界不清晰，必须禁止并行。

## v0.5 Subagent Task Loop 行为

实现类 Kiro task 固定经过：

1. `sp-implementer`
2. `sp-test-verifier`
3. `sp-spec-reviewer`
4. `sp-code-reviewer`

Kiro main agent 必须先读取 `requirements.md`、`design.md`、`tasks.md`，把完整 task 上下文传给 subagent。不允许 subagent 自己猜 spec 背景。

## v0.4 Worktree 和 Branch finishing

实现类任务默认进入 worktree gate；在 `main/master` 上不直接开发，除非用户明确确认。任务完成并验证通过后不自动合并，而是给用户四个编号选项：

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
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:\tools\kiro_superpowers_discipline_v0_7_0
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
