#!/usr/bin/env python3
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
required = [
    'README.md',
    'INSTALL.md',
    'INSTALL_FOR_KIRO.md',
    'USAGE.md',
    'CHANGELOG.md',
    'MIGRATION.md',
    'SUPERPOWERS_CAPABILITY_MATRIX.md',
    'power/POWER.md',
    'power/steering/auto-routing.md',
    'power/steering/status-banner.md',
    'power/steering/superpowers-router.md',
    'workspace-assets/.kiro/steering/superpowers-discipline.md',
    'workspace-assets/.kiro/steering/superpowers-status-banner.md',
    'workspace-assets/.kiro/steering/superpowers-router.md',
    'workspace-assets/.kiro/hooks/00-sp-pre-task-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/01-sp-post-task-verification.kiro.hook',
    'workspace-assets/.kiro/hooks/02-sp-agent-stop-sanity-check.kiro.hook',
    'workspace-assets/.kiro/hooks/03-sp-manual-task-readiness-review.kiro.hook',
    'workspace-assets/.kiro/hooks/04-sp-manual-final-review.kiro.hook',
    'workspace-assets/.kiro/hooks/05-sp-worktree-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/06-sp-branch-finishing.kiro.hook',
    'workspace-assets/.kiro/steering/superpowers-worktree-automation.md',
    'workspace-assets/.kiro/steering/superpowers-branch-finishing.md',
    'workspace-assets/.kiro/scripts/sp-worktree-create.sh',
    'workspace-assets/.kiro/scripts/sp-finish-branch.sh',
    'workspace-assets/.kiro/scripts/sp-worktree-create.ps1',
    'workspace-assets/.kiro/scripts/sp-finish-branch.ps1',
    'power/steering/worktree-automation.md',
    'power/steering/branch-finishing.md',
    'scripts/sp-worktree-create.sh',
    'scripts/sp-finish-branch.sh',
    'scripts/sp-worktree-create.ps1',
    'scripts/sp-finish-branch.ps1',
    'workspace-assets/.kiro/agents/sp-implementer.md',
    'workspace-assets/.kiro/agents/sp-spec-reviewer.md',
    'workspace-assets/.kiro/agents/sp-code-reviewer.md',
    'workspace-assets/.kiro/agents/sp-test-verifier.md',
    'workspace-assets/.kiro/agents/sp-debugger.md',
    'power/steering/task-by-task-subagent-loop.md',
    'power/steering/review-feedback-loop.md',
    'workspace-assets/.kiro/steering/superpowers-task-by-task-subagent-loop.md',
    'workspace-assets/.kiro/steering/superpowers-review-feedback-loop.md',
    'workspace-assets/.kiro/agents/sp-review-feedback-handler.md',
    'power/steering/parallel-agent-policy.md',
    'workspace-assets/.kiro/steering/superpowers-parallel-agent-policy.md',
    'workspace-assets/.kiro/hooks/07-sp-parallel-safety-check.kiro.hook',
    'install/install.ps1',
    'install/install.sh',
]

errors = []
for rel in required:
    if not (root / rel).exists():
        errors.append(f'Missing: {rel}')

# Hook JSON must parse.
for p in (root / 'workspace-assets/.kiro/hooks').glob('*.kiro.hook'):
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'Invalid hook JSON: {p.relative_to(root)}: {exc}')

# Agent frontmatter must exist and include name/description.
for p in (root / 'workspace-assets/.kiro/agents').glob('sp-*.md'):
    text = p.read_text(encoding='utf-8')
    if not text.startswith('---'):
        errors.append(f'Missing frontmatter: {p.relative_to(root)}')
        continue
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        errors.append(f'Bad frontmatter block: {p.relative_to(root)}')
        continue
    fm = m.group(1)
    if 'name:' not in fm or 'description:' not in fm:
        errors.append(f'Incomplete frontmatter: {p.relative_to(root)}')

# Power metadata checks.
power = (root / 'power/POWER.md').read_text(encoding='utf-8')
for token in ['version: "0.6.0"', 'status-banner.md', 'superpowers-router.md', 'worktree-automation.md', 'branch-finishing.md', 'task-by-task-subagent-loop.md', 'review-feedback-loop.md', 'parallel-agent-policy.md']:
    if token not in power:
        errors.append(f'POWER.md missing token: {token}')

# Backward compatibility checks.
readme = (root / 'README.md').read_text(encoding='utf-8')
usage = (root / 'USAGE.md').read_text(encoding='utf-8')
install = (root / 'INSTALL.md').read_text(encoding='utf-8')
for token in [
    '用户日常不需要写长提示词',
    '请安装这个目录里的 Kiro Superpowers Discipline 到当前项目',
    '新增数据导出功能',
    '修复登录失败的问题',
    '继续当前 spec 的下一个任务',
    '合并回主分支',
    '丢弃本次工作',
    'sp-review-feedback-handler',
    'blocker',
    'major',
    'minor',
    'question',
    'Parallel Dispatch Plan',
    '允许并行',
    '禁止并行',
]:
    if token not in readme and token not in usage and token not in install:
        errors.append(f'Compatibility token missing: {token}')

# No ai_dev_os in this package.
for p in root.rglob('*'):
    rel = p.relative_to(root).as_posix()
    if 'ai_dev_os' in rel:
        errors.append(f'Forbidden ai_dev_os path: {rel}')

# Capability matrix must mention core statuses.
matrix = (root / 'SUPERPOWERS_CAPABILITY_MATRIX.md').read_text(encoding='utf-8')
for token in ['using-superpowers', 'subagent-driven-development', 'using-git-worktrees', 'finishing-a-development-branch', 'Worktree 自动化', 'Branch finishing', 'Review feedback loop', 'Subagent task loop', 'dispatching-parallel-agents', 'Parallel Dispatch Plan']:
    if token not in matrix:
        errors.append(f'Matrix missing capability: {token}')

if errors:
    for e in errors:
        print(f'FAIL: {e}')
    raise SystemExit(1)

print('Compatibility validation passed')
print('- Package structure: PASS')
print('- Power structure: PASS')
print('- Hook JSON: PASS')
print('- Agent frontmatter: PASS')
print('- v0.2/v0.3/v0.4 user entrypoints: PASS')
print('- ai_dev_os absent: PASS')
print('- CHANGELOG/MIGRATION/capability matrix: PASS')
print('- v0.4 worktree/branch finishing files: PASS')
print('- v0.5 subagent loop/review feedback files: PASS')
print('- v0.6 parallel agents safety files: PASS')
