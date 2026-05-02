# Kiro Superpowers Discipline v0.2.0

把 Superpowers 的核心执行纪律改造成 Kiro 可用的 Power / Steering / Hooks / Custom Subagents。

这版重点修正 v0.1.0 的问题：**用户日常不需要写长提示词**。

用户只需要正常说：

```text
新增数据导出功能
修复登录失败的问题
继续下一个任务
检查当前实现是否完成
```

Kiro 应该自动判断流程：

```text
新功能 → Feature Spec → requirements/design/tasks → 执行 task → 验证
Bug → Bugfix Spec → 复现 → 根因 → 失败测试 → 修复 → 验证
继续 → 找当前 spec 未完成 task → 执行前检查 → TDD/验证/审查
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
  steering/superpowers-discipline.md
  hooks/*.kiro.hook
  agents/*.md

install/
  install.ps1
  install.sh

INSTALL_FOR_KIRO.md
USAGE.md
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
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:\tools\kiro_superpowers_discipline_v0_2_0
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

## v0.2.0 的改动

- 用户入口改成自然语言。
- 安装提示改成一句话。
- Power 增加自动路由规则。
- Steering 增加“用户不背流程”原则。
- Hooks 保留检查能力，但不要求用户手动描述 TDD/Review/Verification。
- 使用文档改为“用户怎么说 → Kiro 应该怎么做”。
