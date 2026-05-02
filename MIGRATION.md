# Migration Guide

## v0.2.0 → v0.3.0

v0.3.0 是兼容性增强版本，不改变 v0.2.0 的安装、卸载和日常使用方式。

## 是否需要重新安装

需要。因为 v0.3.0 新增了 workspace steering 文件：

```text
.kiro/steering/superpowers-status-banner.md
.kiro/steering/superpowers-router.md
```

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
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## 新增文件

```text
SUPERPOWERS_CAPABILITY_MATRIX.md
MIGRATION.md
power/steering/status-banner.md
power/steering/superpowers-router.md
workspace-assets/.kiro/steering/superpowers-status-banner.md
workspace-assets/.kiro/steering/superpowers-router.md
```

## 卸载变化

卸载命令仍然可以用：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
```

也可以手动删除新增的两个 steering 文件。
