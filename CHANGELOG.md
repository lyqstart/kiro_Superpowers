# Changelog

## v0.4.0

- 新增 worktree 自动化纪律：实现类任务默认检查 git 状态，避免直接在 main/master 上开发。
- 新增 branch finishing 纪律：任务验证通过后提供合并、PR、保留、丢弃四个编号选项。
- 新增安全脚本：`sp-worktree-create.sh`、`sp-worktree-create.ps1`、`sp-finish-branch.sh`、`sp-finish-branch.ps1`。
- 新增 workspace scripts 安装：脚本会复制到项目 `.kiro/scripts/`。
- 新增 hooks：`05-sp-worktree-gate.kiro.hook` 和 `06-sp-branch-finishing.kiro.hook`。
- 新增 steering：`superpowers-worktree-automation.md` 和 `superpowers-branch-finishing.md`。
- 更新 `POWER.md`、`README.md`、`USAGE.md`、`INSTALL.md`、`INSTALL_FOR_KIRO.md`、`MIGRATION.md`、能力矩阵和校验脚本。
- 保持 v0.3.0 的安装、卸载、日常使用方式不变。
- 仍不包含 ai_dev_os。


## v0.4.0

- 新增状态标识：任务开始时显示 Kiro 规格主控、Superpowers 执行纪律、当前阶段、当前流程、当前 task、当前 gate。
- 新增 Superpowers Router：自然语言自动路由到新功能、bugfix、继续任务、审查、验证。
- 新增 `SUPERPOWERS_CAPABILITY_MATRIX.md`：记录原 Superpowers 能力在 Kiro 版中的覆盖情况、未覆盖情况、后续计划。
- 新增 workspace steering：`superpowers-status-banner.md` 和 `superpowers-router.md`。
- 更新 `POWER.md`、`README.md`、`USAGE.md`、`INSTALL.md`、`INSTALL_FOR_KIRO.md`。
- 保持 v0.2.0 的安装、卸载、日常使用方式不变。
- 仍不包含 ai_dev_os。


## v0.4.0

- 将日常入口改为自然语言，不再要求用户每次写长提示词。
- 新增 `INSTALL_FOR_KIRO.md`：用户只需告诉 Kiro 解压目录。
- 重写 `README.md`、`INSTALL.md`、`USAGE.md`。
- 重写 `POWER.md`：增加自动识别新功能、bugfix、继续任务、完成检查的规则。
- 重写 workspace steering：把复杂纪律藏到后台。
- 保留 hooks 和 subagents，但默认让它们服务于自动流程。
- 暂不包含 ai_dev_os。

## v0.1.0

- 初始版本。
- 提供 Kiro Power、Steering、Hooks、Custom Subagents、安装脚本。
