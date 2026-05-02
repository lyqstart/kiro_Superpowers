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


## TDD evidence 缺失

现象：Kiro 想标记 COMPLETE，但没有 RED/GREEN/REFACTOR 证据。

处理：要求 Kiro 补充：

```text
RED 验证命令和输出
失败原因
失败测试文件路径
GREEN 验证命令和输出
通过测试文件路径
对应实现文件路径
REFACTOR 记录或无需重构原因
```

如果任务确实无法 TDD，Kiro 必须说明例外原因、替代验证方案，并等待用户确认。


## Task Refinement Gate 阻塞

如果 Kiro 提示 task 有歧义、太大、缺少 requirement/design 关联、缺少验证命令或缺少完成定义，这是正常保护，不是失败。

处理方式：

1. 选择 Kiro 给出的编号拆分方案；
2. 回到 Kiro spec 更新 requirements/design/tasks；
3. 明确当前 task 的范围、不做范围和验证方式；
4. 不要要求 Kiro “先直接改”，否则会破坏 Superpowers Discipline 的执行纪律。


## Subagent Task Packet 缺失

现象：Kiro 直接调用 subagent，但没有提供 spec、requirement、design section、task、范围、允许/禁止修改或验证命令。

处理：要求 Kiro 先输出 Subagent Task Packet。缺少任务包时，subagent 应返回 `NEEDS_CONTEXT`，不能自己猜。

## Review Evidence 缺失

现象：review 只给了泛泛建议，没有 changed files、BASE_SHA/HEAD_SHA、requirement/design/task coverage。

处理：要求 Kiro 重新执行 Review Evidence Contract。没有实际 diff 或 changed files 的 review 不能作为完成依据。


## 调试时一直修不好

如果同一个问题连续修复 3 次仍失败，v1.3 要求停止继续打补丁。你应该看到 architecture stop gate 输出：

```text
是否理解错需求？
是否定位错根因？
是否架构假设错误？
是否测试方式错误？
是否应该回到 design/spec 阶段？
```

这不是拖慢开发，而是防止 AI 在错误方向上连续堆补丁。

## Agent 使用固定 sleep 修异步问题

v1.3 要求优先使用 condition-based waiting。正确输出应说明等待条件、超时策略和失败诊断。固定 sleep 只能作为最后的辅助措施，不能作为主要方案。
