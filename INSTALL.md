# 安装 Kiro Superpowers Discipline v1.5.0

## 一句话安装

在 Kiro 打开目标项目后，对 Kiro 说：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

例子：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:	ools\kiro_superpowers_discipline_v1_5_0
```

Kiro 应根据系统自动运行安装脚本，将项目级文件复制到当前项目的 `.kiro/` 目录。

## Power 安装

项目级文件安装后，还需要在 Kiro Powers 面板添加 Power：

```text
Powers → Add power from Local Path → 选择 <解压目录>/power
```

## 手动安装

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File "<解压目录>\install\install.ps1" -ProjectRoot "<项目根目录>"
```

macOS/Linux：

```bash
bash "<解压目录>/install/install.sh" "<项目根目录>"
```

## 安装后检查

项目内应出现：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

## 用户体验要求

安装后用户仍然只需要说：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```
