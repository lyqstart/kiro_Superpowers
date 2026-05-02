# MIGRATION

## 从 v1.0.0 升级到 v1.1.0

升级方式不变：重新运行安装脚本即可覆盖/补充项目级文件，然后在 Kiro Powers 面板确认 Power 指向新版 `power/` 目录。

## 本版变化

v1.1.0 只增强 subagent 派发任务包、subagent 返回格式、review 证据链和 Git diff evidence，不改变安装、卸载和日常使用方式。

主要新增：

```text
power/steering/subagent-task-packet.md
power/steering/review-evidence-contract.md
workspace-assets/.kiro/steering/superpowers-subagent-task-packet.md
workspace-assets/.kiro/steering/superpowers-review-evidence-contract.md
workspace-assets/.kiro/hooks/17-sp-subagent-task-packet.kiro.hook
workspace-assets/.kiro/hooks/18-sp-subagent-result-contract.kiro.hook
workspace-assets/.kiro/hooks/19-sp-review-evidence-contract.kiro.hook
```

主要增强：

```text
workspace-assets/.kiro/agents/sp-implementer.md
workspace-assets/.kiro/agents/sp-test-verifier.md
workspace-assets/.kiro/agents/sp-spec-reviewer.md
workspace-assets/.kiro/agents/sp-code-reviewer.md
workspace-assets/.kiro/agents/sp-debugger.md
workspace-assets/.kiro/agents/sp-review-feedback-handler.md
```

## 保留行为

- 原安装提示不变。
- 原卸载方式仍然有效。
- 用户日常仍然只需要说“新增 xxx / 修复 xxx / 继续当前 spec 的下一个任务 / 检查当前任务是否完成”。
- v0.4 worktree 自动化和 branch finishing 不变。
- v0.5 subagent task loop 和 review feedback loop 不变。
- v0.6 parallel agents 安全策略不变。
- v0.7 task execution/completion contract 不变。
- v0.8 稳定化整理不变。
- v0.9 TDD Evidence Contract 不变。
- v1.0 Task Refinement Gate 不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## 是否需要重新安装

建议重新安装。因为 v1.1.0 新增 workspace steering 和 hooks，并增强 agents 输出格式。

请按原安装方式重新执行：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板确认 Power 指向新版解压目录的 `power/`。

## 卸载方式

卸载方式不变，详见 `UNINSTALL.md`。

---

# MIGRATION

## 从 v0.9.0 升级到 v1.0.0

升级方式不变：重新运行安装脚本即可覆盖/补充项目级文件，然后在 Kiro Powers 面板确认 Power 指向新版 `power/` 目录。

## 本版变化

v1.0.0 只增强 task 执行前的细化检查，不改变安装、卸载和日常使用方式。

主要新增：

```text
power/steering/kiro-task-refinement-gate.md
workspace-assets/.kiro/steering/superpowers-kiro-task-refinement-gate.md
workspace-assets/.kiro/hooks/14-sp-task-refinement-gate.kiro.hook
workspace-assets/.kiro/hooks/15-sp-task-split-review.kiro.hook
workspace-assets/.kiro/hooks/16-sp-scope-creep-blocker.kiro.hook
```

## 保留行为

- 原安装提示不变。
- 原卸载方式仍然有效。
- 用户日常仍然只需要说“新增 xxx / 修复 xxx / 继续当前 spec 的下一个任务 / 检查当前任务是否完成”。
- v0.4 worktree 自动化和 branch finishing 不变。
- v0.5 subagent task loop 和 review feedback loop 不变。
- v0.6 parallel agents 安全策略不变。
- v0.7 task execution/completion contract 不变。
- v0.8 稳定化整理不变。
- v0.9 TDD Evidence Contract 不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## 是否需要重新安装

建议重新安装。因为 v1.0.0 新增 workspace steering 和 hooks。

请按原安装方式重新执行：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板确认 Power 指向新版解压目录的 `power/`。

## 卸载方式

卸载方式不变，详见 `UNINSTALL.md`。

---

# MIGRATION

## 从 v0.8.0 升级到 v1.0.0

升级方式不变：重新运行安装脚本即可覆盖/补充项目级文件，然后在 Kiro Powers 面板确认 Power 指向新版 `power/` 目录。

## 本版变化

v1.0.0 只增强 TDD 证据要求，不改变安装、卸载和日常使用方式。

主要新增：

```text
power/steering/tdd-evidence-contract.md
workspace-assets/.kiro/steering/superpowers-tdd-evidence-contract.md
workspace-assets/.kiro/hooks/11-sp-tdd-evidence-gate.kiro.hook
workspace-assets/.kiro/hooks/12-sp-tdd-evidence-completion.kiro.hook
workspace-assets/.kiro/hooks/13-sp-tdd-verification-review.kiro.hook
```

## 保留行为

- 原安装提示不变。
- 原卸载方式仍然有效。
- 用户日常仍然只需要说“新增 xxx / 修复 xxx / 继续当前 spec 的下一个任务 / 检查当前任务是否完成”。
- v0.4 worktree 自动化和 branch finishing 不变。
- v0.5 subagent task loop 和 review feedback loop 不变。
- v0.6 parallel agents 安全策略不变。
- v0.7 task execution/completion contract 不变。
- v0.8 稳定化整理不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## 是否需要重新安装

建议重新安装。因为 v1.0.0 新增 workspace steering 和 hooks。

请按原安装方式重新执行：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板确认 Power 指向新版解压目录的 `power/`。

## 卸载方式

卸载方式不变，详见 `UNINSTALL.md`。


---

# MIGRATION

## 从 v0.7.0 升级到 v0.8.0

升级方式不变：重新运行安装脚本即可覆盖/补充项目级文件，然后在 Kiro Powers 面板确认 Power 指向新版 `power/` 目录。

## 本版变化

v0.8.0 是稳定化整理版，不新增新的开发流程能力。

主要变化：

```text
README.md
INSTALL.md
INSTALL_FOR_KIRO.md
UNINSTALL.md
USAGE.md
TROUBLESHOOTING.md
SUPERPOWERS_CAPABILITY_MATRIX.md
scripts/validate_package.py
workspace-assets/.kiro/hooks/*.kiro.hook
workspace-assets/.kiro/agents/sp-*.md
```

## 保留行为

- 原安装提示不变。
- 原卸载方式仍然有效。
- 用户日常仍然只需要说“新增 xxx / 修复 xxx / 继续当前 spec 的下一个任务 / 检查当前任务是否完成”。
- v0.4 worktree 自动化和 branch finishing 不变。
- v0.5 subagent task loop 和 review feedback loop 不变。
- v0.6 parallel agents 安全策略不变。
- v0.7 task execution/completion contract 不变。
- 不引入 ai_dev_os。
- 不要求用户写长提示词。

## 是否需要重新安装

建议重新安装。因为 v0.8.0 整理了 workspace steering、hooks 和 agent 输出格式。

请按原安装方式重新执行：

```text
请安装这个目录里的 Kiro Superpowers Discipline 到当前项目：<解压目录>
```

然后在 Kiro Powers 面板确认 Power 指向新版解压目录的 `power/`。

## 卸载方式

卸载方式不变，详见 `UNINSTALL.md`。
