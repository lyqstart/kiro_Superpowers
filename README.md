# Kiro Superpowers Discipline v0.3.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

v0.3.0 保持 v0.2.0 的安装、卸载和日常使用方式不变，只新增三件事：

1. **状态标识**：每次任务开始显示 Kiro 规格主控、Superpowers 执行纪律、当前阶段、当前流程、当前 task、当前 gate。
2. **Superpowers Router**：根据自然语言自动路由到新功能、bugfix、继续任务、审查、验证。
3. **能力矩阵**：新增 `SUPERPOWERS_CAPABILITY_MATRIX.md`，说明原 Superpowers 能力在 Kiro 版中的覆盖情况和后续计划。

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
新功能 → Feature Spec → requirements/design/tasks → TDD → 审查 → 验证
Bug → Bugfix Spec → 复现 → 根因 → 失败测试/替代验证 → 修复 → 验证
继续 → 找当前 spec 未完成 task → 执行前检查 → 执行 → 审查 → 验证
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

install/
  install.ps1
  install.sh

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
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:\tools\kiro_superpowers_discipline_v0_3_0
```

Kiro 应该读取 `INSTALL_FOR_KIRO.md`，运行对应脚本，并提示你把 `power/` 目录添加到 Kiro Powers。

## 最简单使用

```text
新增一个数据导出功能
```

```text
修复登录接口偶发 500 的问题
```

```text
继续当前 spec 的下一个任务
```

```text
检查当前任务是否真的完成
```

你不需要说“使用 Superpowers Discipline”。安装完成后，它应该作为后台纪律生效。

## 卸载

删除项目中的：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
```

然后在 Kiro Powers 面板卸载本 Power。
