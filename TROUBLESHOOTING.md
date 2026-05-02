# TROUBLESHOOTING

## 1. Kiro 没有显示状态标识

检查是否已安装 workspace 文件：

```text
.kiro/steering/superpowers-status-banner.md
.kiro/steering/superpowers-router.md
```

并确认 Kiro Powers 面板已经添加本包的 `power/` 目录。

## 2. Kiro 直接改代码，没有先走 spec/task

先停止它，然后说：

```text
停止。请显示当前状态标识，并说明当前是否绑定 Kiro spec/task。没有通过 task execution contract 前不要改代码。
```

如果仍然不生效，重新运行安装脚本并确认 Power 指向新版 `power/`。

## 3. Worktree 没有创建

不是所有请求都强制 worktree。文档修改、只读分析、小文本修改可以不创建。实现类任务、bugfix、重构、数据库/API 变更应进入 worktree gate。

如果当前分支是 `main/master`，Kiro 不应直接开发，除非你明确确认。

## 4. Branch finishing 没有出现

只有代码变更任务通过 verification、spec review、code review 后，才应该给出四个选项。

如果验证失败或缺失，不能进入合并选项。

## 5. Subagent 没有按固定顺序执行

确认这些文件存在：

```text
.kiro/agents/sp-implementer.md
.kiro/agents/sp-test-verifier.md
.kiro/agents/sp-spec-reviewer.md
.kiro/agents/sp-code-reviewer.md
.kiro/steering/superpowers-task-by-task-subagent-loop.md
```

Kiro main agent 必须先读取 requirements/design/tasks，并把完整 task context 传给 subagent。

## 6. Review feedback 被盲目接受

应使用 review feedback loop：

```text
blocker / major / minor / question
```

question 必须暂停提问，不许猜。blocker/major 必须修复并重新 review。

## 7. 并行执行看起来危险

并行前必须有 `Parallel Dispatch Plan`。如果多个任务共享文件、接口、数据库表、迁移脚本或状态机，应禁止并行 implementation。

## 8. 安装脚本无法运行

Windows 可以尝试：

```powershell
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectRoot "<项目根目录>" -Force
```

macOS/Linux 可以尝试：

```bash
bash ./install/install.sh "<项目根目录>"
```

## 9. 如何确认包本身没问题

在解压目录运行：

```bash
python scripts/validate_package.py
```

应看到 `Compatibility validation passed`。
