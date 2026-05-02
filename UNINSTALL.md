# 卸载说明

## 最简单卸载

在项目根目录删除这些文件：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

然后在 Kiro Powers 面板卸载：

```text
Powers → Kiro Superpowers Discipline → Remove / Uninstall
```

最后可以删除解压目录。

## Windows PowerShell

在项目根目录运行：

```powershell
Remove-Item ".kiro\steering\superpowers-*.md" -Force -ErrorAction SilentlyContinue
Remove-Item ".kiro\hooks\*sp-*.kiro.hook" -Force -ErrorAction SilentlyContinue
Remove-Item ".kiro\agents\sp-*.md" -Force -ErrorAction SilentlyContinue
Remove-Item ".kiro\scripts\sp-*.sh" -Force -ErrorAction SilentlyContinue
Remove-Item ".kiro\scripts\sp-*.ps1" -Force -ErrorAction SilentlyContinue
```

## macOS/Linux

在项目根目录运行：

```bash
rm -f .kiro/steering/superpowers-*.md
rm -f .kiro/hooks/*sp-*.kiro.hook
rm -f .kiro/agents/sp-*.md
rm -f .kiro/scripts/sp-*.sh
rm -f .kiro/scripts/sp-*.ps1
```

## 不会删除什么

卸载不会删除：

```text
.kiro/specs/
.kiro/steering/product.md
.kiro/steering/tech.md
.kiro/steering/structure.md
你的源码
你的 git 分支
你的 worktree
```

如果曾经创建过 git worktree，请根据自己的项目情况手动确认后再清理，不要盲删。
