# Kiro Task Execution Contract

## 目标

在执行任何 Kiro task 前，先把 task 当成工程合同审查，而不是直接开写。

## 执行前必须检查

Kiro main agent 必须先读取并批判性检查：

- `.kiro/specs/<spec>/requirements.md` 或 bugfix spec；
- `.kiro/specs/<spec>/design.md`；
- `.kiro/specs/<spec>/tasks.md`；
- 当前 task 的编号、标题、依赖、完成定义；
- 当前 task 关联的 requirement / design section；
- 当前 task 的范围和不做范围；
- 预计修改文件、测试/验证命令、风险。

## Gate 规则

以下任一情况出现时，必须暂停，不许猜：

1. task 有歧义，无法判断目标或验收标准。
2. task 缺少 requirement/design 关联。
3. task 太大，无法在一个可验证单元内完成。
4. task 要求修改范围外内容。
5. task 与现有 design 或 requirements 冲突。
6. task 没有可执行验证方式，也没有替代验证方案。

## 太大的 task 怎么处理

不要硬做。先建议拆分为更小 task，并给出编号选项：

1. 先拆后做。
2. 只执行其中一个明确子任务。
3. 暂停回到 design/tasks 更新。

## 范围控制

禁止顺手做：

- 无关重构；
- 无关性能优化；
- 无关 UI 调整；
- 无关依赖升级；
- 未写进 task 的数据库/API 改动。

如果发现必须做范围外修改，先说明原因并等待用户确认。
