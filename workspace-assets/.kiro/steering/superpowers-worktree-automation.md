# Superpowers Worktree Automation

实现类任务默认使用隔离 worktree，不在 main/master 上直接开发，除非用户明确确认。

触发场景：功能实现、bugfix、重构、数据库/API/任务执行类变更。

非强制场景：只读分析、文档修改、拼写/文案、小配置说明。

执行前必须检查：

1. 是否是 git 仓库。
2. 当前分支是否为 main/master。
3. `git status --short` 是否干净。
4. `.worktrees/` 是否适合放置隔离 worktree。
5. 是否有可运行的 baseline 验证命令。

安全原则：不自动删除、不自动合并、不强制清理用户修改。
