# Kiro 安装指令

用户会在 Kiro Chat 里说：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

你应该按下面流程执行，不要让用户手动复制复杂命令。

## 1. 判断系统

- Windows：使用 `install/install.ps1`
- macOS/Linux：使用 `install/install.sh`

## 2. 执行安装

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File "<解压目录>\install\install.ps1" -ProjectRoot "."
```

macOS/Linux：

```bash
bash "<解压目录>/install/install.sh" "."
```

## 3. 安装后检查

检查当前项目是否存在：

```text
.kiro/steering/superpowers-discipline.md
.kiro/steering/superpowers-status-banner.md
.kiro/steering/superpowers-router.md
.kiro/steering/superpowers-worktree-automation.md
.kiro/steering/superpowers-branch-finishing.md
.kiro/hooks/00-sp-pre-task-gate.kiro.hook
.kiro/hooks/01-sp-post-task-verification.kiro.hook
.kiro/hooks/05-sp-worktree-gate.kiro.hook
.kiro/hooks/06-sp-branch-finishing.kiro.hook
.kiro/agents/sp-implementer.md
.kiro/agents/sp-spec-reviewer.md
.kiro/agents/sp-code-reviewer.md
.kiro/agents/sp-test-verifier.md
.kiro/agents/sp-debugger.md
.kiro/scripts/sp-worktree-create.sh
.kiro/scripts/sp-finish-branch.sh
.kiro/scripts/sp-worktree-create.ps1
.kiro/scripts/sp-finish-branch.ps1
```

## 4. 提醒用户添加 Power

安装脚本不会自动替用户在 Kiro UI 添加 Power。请提醒：

```text
Powers → Add power from Local Path → 选择 <解压目录>/power
```

## 5. 最后只给用户三个使用例子

```text
新增数据导出功能
修复登录失败的问题
继续当前 spec 的下一个任务
```

不要输出长流程。不要创建 ai_dev_os。
