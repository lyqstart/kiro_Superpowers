# Worktree Discipline

## 什么时候使用 worktree

建议在这些场景创建独立 git worktree：

- 中大型功能；
- 高风险 bugfix；
- 需要多任务并行；
- 不希望污染当前工作区；
- 需要保持主工作区可运行。

## 创建前检查

- 优先使用 `.worktrees/`；
- 如果项目已有 `worktrees/`，遵守现有约定；
- 项目内 worktree 目录必须被 `.gitignore` 忽略；
- 创建后先运行基线测试。

## 如果不使用 worktree

必须明确说明原因，例如：

- 当前 task 很小；
- 用户要求直接在当前分支做；
- 当前环境不允许创建 worktree。

但仍然必须保持变更最小、可审查、可回滚。
