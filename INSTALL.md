# 安装说明

## 最简单方式

1. 解压压缩包。
2. 在 Kiro 打开你的项目。
3. 对 Kiro 说：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

例如：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:\tools\kiro_superpowers_discipline_v0_3_0
```

Kiro 会读取本包的 `INSTALL_FOR_KIRO.md`，运行安装脚本。

## 还需要手动做的一步

安装脚本会把 workspace 文件复制到当前项目，但 Power 需要在 Kiro UI 里添加：

```text
Powers → Add power from Local Path → 选择 <解压目录>/power
```

## 手动命令

Windows：

```powershell
cd <解压目录>
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectRoot "<你的项目根目录>"
```

macOS/Linux：

```bash
cd <解压目录>
bash ./install/install.sh "<你的项目根目录>"
```

## 安装后检查

项目中应该出现：

```text
.kiro/steering/superpowers-discipline.md
.kiro/steering/superpowers-status-banner.md
.kiro/steering/superpowers-router.md
.kiro/hooks/*.kiro.hook
.kiro/agents/sp-*.md
```

## 卸载

删除项目中的这些文件即可：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
```

Power 在 Kiro Powers 面板中卸载。
