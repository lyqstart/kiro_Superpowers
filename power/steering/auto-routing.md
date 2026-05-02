# Auto Routing

用户不需要说明流程。根据用户自然语言自动判断工作类型。

## 新功能

触发词：新增、增加、开发、实现、构建、添加、支持、做一个、新页面、新接口、新模块、feature。

动作：

1. 如果没有相关 spec，创建 Feature Spec。
2. 需求不清只问最少问题，优先编号选择。
3. 生成 requirements/design/tasks。
4. 执行任务前进入 task readiness gate。

## Bugfix

触发词：修复、bug、报错、异常、失败、不对、500、崩溃、空数据、卡住、fix。

动作：

1. 先复现。
2. 查根因。
3. 写失败测试或替代复现验证。
4. 最小修复。
5. 验证 bug 和回归。

## 继续执行

触发词：继续、接着、下一个任务、往下做、继续当前 spec。

动作：

1. 找当前 spec。
2. 找未完成 task。
3. 读取 requirements/design/tasks。
4. 执行 pre-task gate。
5. 执行、验证、审查。

## 完成检查

触发词：检查、是否完成、能交付吗、验收、最终审查、确认完成。

动作：

1. 查看 diff。
2. 运行验证命令。
3. 检查 spec compliance。
4. 检查 code quality。
5. 给出完成/未完成/阻塞结论。

## 禁止

不要让用户每次手动说：TDD、验证、审查、读取 spec。这些是系统责任。
