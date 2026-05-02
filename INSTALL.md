# 安装说明

## 最简单方式

1. 解压压缩包。
2. 在 Kiro 打开你的项目。
3. 对 Kiro 说一句：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

例如：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：D:\tools\kiro_superpowers_discipline_v1_3_0
```

Kiro 应读取 `INSTALL_FOR_KIRO.md`，根据系统运行安装脚本。

## Kiro Power 添加

安装脚本只复制 workspace 文件；Power 需要在 Kiro UI 中添加：

```text
Powers → Add power from Local Path → 选择 <解压目录>/power
```

## 手动命令

Windows：

```powershell
cd <解压目录>
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectRoot "<你的项目根目录>" -Force
```

macOS/Linux：

```bash
cd <解压目录>
bash ./install/install.sh "<你的项目根目录>"
```

## 安装后检查

项目中应该出现：

```text
.kiro/steering/superpowers-*.md
.kiro/hooks/*sp-*.kiro.hook
.kiro/agents/sp-*.md
.kiro/scripts/sp-*.sh
.kiro/scripts/sp-*.ps1
```

至少包含：

```text
.kiro/steering/superpowers-discipline.md
.kiro/steering/superpowers-status-banner.md
.kiro/steering/superpowers-router.md
.kiro/hooks/00-sp-pre-task-gate.kiro.hook
.kiro/hooks/09-sp-task-completion-contract.kiro.hook
.kiro/agents/sp-implementer.md
.kiro/agents/sp-spec-reviewer.md
.kiro/agents/sp-code-reviewer.md
.kiro/agents/sp-test-verifier.md
.kiro/agents/sp-debugger.md
.kiro/agents/sp-review-feedback-handler.md
```

## 安装后怎么用

不用写长提示词。直接说：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
检查当前任务是否真的完成
```

## 卸载

见 `UNINSTALL.md`。
