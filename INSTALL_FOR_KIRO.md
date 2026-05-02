# 给 Kiro 的安装说明

用户只需要说：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

当你收到这句话时，请按下面步骤执行，不要让用户复制长提示词。

## 1. 确认路径

从用户消息中提取 `<解压目录>`。

确认目录中存在：

```text
power/POWER.md
workspace-assets/.kiro/
install/install.ps1
install/install.sh
```

如果不存在，只问一个问题：

```text
我没有在这个目录看到安装包文件。请确认解压目录是否正确。
```

## 2. 安装 workspace 文件

在当前项目根目录执行对应脚本。

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File "<解压目录>\install\install.ps1" -ProjectRoot "."
```

macOS/Linux：

```bash
bash "<解压目录>/install/install.sh" "."
```

## 3. 检查安装结果

检查当前项目中是否存在：

```text
.kiro/steering/superpowers-discipline.md
.kiro/hooks/00-sp-pre-task-gate.kiro.hook
.kiro/hooks/01-sp-post-task-verification.kiro.hook
.kiro/agents/sp-implementer.md
.kiro/agents/sp-spec-reviewer.md
.kiro/agents/sp-code-reviewer.md
.kiro/agents/sp-test-verifier.md
.kiro/agents/sp-debugger.md
```

## 4. 提醒安装 Power

脚本不能替用户点击 Kiro UI。最后只需要告诉用户：

```text
workspace 文件已安装。现在在 Kiro 的 Powers 面板选择 Add power from Local Path，然后选择：<解压目录>/power
```

不要输出长流程说明。

## 5. 告诉用户怎么开始

只给 3 个最短例子：

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
```
