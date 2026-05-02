#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
errors = []

required = [
    'README.md', 'INSTALL.md', 'INSTALL_FOR_KIRO.md', 'UNINSTALL.md', 'USAGE.md',
    'TROUBLESHOOTING.md', 'CHANGELOG.md', 'MIGRATION.md', 'SUPERPOWERS_CAPABILITY_MATRIX.md',
    'power/POWER.md',
    'power/steering/auto-routing.md',
    'power/steering/status-banner.md',
    'power/steering/superpowers-router.md',
    'power/steering/worktree-automation.md',
    'power/steering/branch-finishing.md',
    'power/steering/task-by-task-subagent-loop.md',
    'power/steering/review-feedback-loop.md',
    'power/steering/parallel-agent-policy.md',
    'power/steering/kiro-task-execution-contract.md',
    'power/steering/executing-plans-discipline.md',
    'power/steering/task-completion-contract.md',
    'power/steering/tdd-discipline.md',
    'power/steering/tdd-evidence-contract.md',
    'workspace-assets/.kiro/steering/superpowers-discipline.md',
    'workspace-assets/.kiro/steering/superpowers-status-banner.md',
    'workspace-assets/.kiro/steering/superpowers-router.md',
    'workspace-assets/.kiro/steering/superpowers-worktree-automation.md',
    'workspace-assets/.kiro/steering/superpowers-branch-finishing.md',
    'workspace-assets/.kiro/steering/superpowers-task-by-task-subagent-loop.md',
    'workspace-assets/.kiro/steering/superpowers-review-feedback-loop.md',
    'workspace-assets/.kiro/steering/superpowers-parallel-agent-policy.md',
    'workspace-assets/.kiro/steering/superpowers-kiro-task-execution-contract.md',
    'workspace-assets/.kiro/steering/superpowers-executing-plans-discipline.md',
    'workspace-assets/.kiro/steering/superpowers-task-completion-contract.md',
    'workspace-assets/.kiro/steering/superpowers-tdd-evidence-contract.md',
    'workspace-assets/.kiro/hooks/00-sp-pre-task-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/01-sp-post-task-verification.kiro.hook',
    'workspace-assets/.kiro/hooks/02-sp-agent-stop-sanity-check.kiro.hook',
    'workspace-assets/.kiro/hooks/03-sp-manual-task-readiness-review.kiro.hook',
    'workspace-assets/.kiro/hooks/04-sp-manual-final-review.kiro.hook',
    'workspace-assets/.kiro/hooks/05-sp-worktree-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/06-sp-branch-finishing.kiro.hook',
    'workspace-assets/.kiro/hooks/07-sp-parallel-safety-check.kiro.hook',
    'workspace-assets/.kiro/hooks/08-sp-task-execution-contract.kiro.hook',
    'workspace-assets/.kiro/hooks/09-sp-task-completion-contract.kiro.hook',
    'workspace-assets/.kiro/hooks/10-sp-post-task-branch-finishing-check.kiro.hook',
    'workspace-assets/.kiro/hooks/11-sp-tdd-evidence-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/12-sp-tdd-evidence-completion.kiro.hook',
    'workspace-assets/.kiro/hooks/13-sp-tdd-verification-review.kiro.hook',
    'workspace-assets/.kiro/agents/sp-implementer.md',
    'workspace-assets/.kiro/agents/sp-spec-reviewer.md',
    'workspace-assets/.kiro/agents/sp-code-reviewer.md',
    'workspace-assets/.kiro/agents/sp-test-verifier.md',
    'workspace-assets/.kiro/agents/sp-debugger.md',
    'workspace-assets/.kiro/agents/sp-review-feedback-handler.md',
    'workspace-assets/.kiro/scripts/sp-worktree-create.sh',
    'workspace-assets/.kiro/scripts/sp-finish-branch.sh',
    'workspace-assets/.kiro/scripts/sp-worktree-create.ps1',
    'workspace-assets/.kiro/scripts/sp-finish-branch.ps1',
    'scripts/sp-worktree-create.sh',
    'scripts/sp-finish-branch.sh',
    'scripts/sp-worktree-create.ps1',
    'scripts/sp-finish-branch.ps1',
    'install/install.ps1',
    'install/install.sh',
]

for rel in required:
    if not (root / rel).exists():
        errors.append(f'Missing: {rel}')

# Hook JSON must parse and follow the stable naming shape.
hook_dir = root / 'workspace-assets/.kiro/hooks'
expected_hook_count = 14
hooks = sorted(hook_dir.glob('*.kiro.hook')) if hook_dir.exists() else []
if len(hooks) != expected_hook_count:
    errors.append(f'Expected {expected_hook_count} hooks, found {len(hooks)}')
for p in hooks:
    if not re.match(r'^\d{2}-sp-[a-z0-9-]+\.kiro\.hook$', p.name):
        errors.append(f'Hook filename does not follow NN-sp-name.kiro.hook: {p.name}')
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'Invalid hook JSON: {p.relative_to(root)}: {exc}')
        continue
    for key in ['enabled', 'name', 'description', 'version', 'when', 'then']:
        if key not in data:
            errors.append(f'Hook missing key {key}: {p.relative_to(root)}')
    if not str(data.get('name', '')).startswith('SP '):
        errors.append(f'Hook display name must start with SP: {p.relative_to(root)}')
    if not isinstance(data.get('when'), dict) or 'type' not in data.get('when', {}):
        errors.append(f'Hook missing when.type: {p.relative_to(root)}')
    if not isinstance(data.get('then'), dict) or 'prompt' not in data.get('then', {}):
        errors.append(f'Hook missing then.prompt: {p.relative_to(root)}')

# Agent frontmatter must exist and include name/description/tools; output format must be standardized.
agent_dir = root / 'workspace-assets/.kiro/agents'
agents = sorted(agent_dir.glob('sp-*.md')) if agent_dir.exists() else []
expected_agents = {
    'sp-implementer', 'sp-spec-reviewer', 'sp-code-reviewer', 'sp-test-verifier', 'sp-debugger', 'sp-review-feedback-handler'
}
seen_agents = set()
for p in agents:
    text = p.read_text(encoding='utf-8')
    if not text.startswith('---'):
        errors.append(f'Missing frontmatter: {p.relative_to(root)}')
        continue
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        errors.append(f'Bad frontmatter block: {p.relative_to(root)}')
        continue
    fm = m.group(1)
    name_match = re.search(r'^name:\s*(.+)$', fm, re.M)
    if not name_match:
        errors.append(f'Agent frontmatter missing name: {p.relative_to(root)}')
        continue
    name = name_match.group(1).strip().strip('"\'')
    seen_agents.add(name)
    if name != p.stem:
        errors.append(f'Agent name must match filename: {p.relative_to(root)}')
    for key in ['description:', 'tools:']:
        if key not in fm:
            errors.append(f'Agent frontmatter missing {key}: {p.relative_to(root)}')
    if 'SP Agent Result:' not in text:
        errors.append(f'Agent missing standardized SP Agent Result output: {p.relative_to(root)}')
missing_agents = expected_agents - seen_agents
if missing_agents:
    errors.append(f'Missing agents: {sorted(missing_agents)}')

# Power metadata and steering consistency checks.
power = (root / 'power/POWER.md').read_text(encoding='utf-8') if (root / 'power/POWER.md').exists() else ''
for token in [
    'version: "0.9.0"', 'status-banner.md', 'superpowers-router.md', 'worktree-automation.md',
    'branch-finishing.md', 'task-by-task-subagent-loop.md', 'review-feedback-loop.md',
    'parallel-agent-policy.md', 'kiro-task-execution-contract.md', 'executing-plans-discipline.md',
    'task-completion-contract.md', 'tdd-evidence-contract.md', 'v0.8 Stability and Documentation Rules', 'v0.9 TDD Evidence Contract'
]:
    if token not in power:
        errors.append(f'POWER.md missing token: {token}')

# User entrypoint and UX compatibility checks.
combined = ''
for rel in ['README.md', 'INSTALL.md', 'INSTALL_FOR_KIRO.md', 'UNINSTALL.md', 'USAGE.md', 'TROUBLESHOOTING.md', 'power/POWER.md']:
    p = root / rel
    if p.exists():
        combined += '\n' + p.read_text(encoding='utf-8')
for token in [
    '请安装这个目录里的 Kiro Superpowers Discipline 到当前项目',
    '新增数据导出功能', '修复登录失败的问题', '继续当前 spec 的下一个任务',
    '检查当前任务是否真的完成', '用户不需要说“使用 Superpowers Discipline”',
    '不要求用户写长提示词', 'Powers → Add power from Local Path',
    '.kiro/steering/superpowers-*.md', '.kiro/hooks/*sp-*.kiro.hook', '.kiro/agents/sp-*.md',
    '合并回主分支', '丢弃本次工作', 'Parallel Dispatch Plan',
    'task execution contract', 'task completion contract', 'COMPLETE / NOT COMPLETE / BLOCKED', 'TDD Evidence', 'RED 验证命令', 'GREEN 验证命令'
]:
    if token not in combined:
        errors.append(f'Compatibility/user-experience token missing: {token}')

# Capability matrix must mention original skills and current Kiro implementation assets.
matrix = (root / 'SUPERPOWERS_CAPABILITY_MATRIX.md').read_text(encoding='utf-8') if (root / 'SUPERPOWERS_CAPABILITY_MATRIX.md').exists() else ''
for token in [
    'using-superpowers', 'brainstorming', 'writing-plans', 'executing-plans',
    'test-driven-development', 'systematic-debugging', 'verification-before-completion',
    'requesting-code-review', 'receiving-code-review', 'subagent-driven-development',
    'dispatching-parallel-agents', 'using-git-worktrees', 'finishing-a-development-branch',
    'writing-skills', 'v0.8.0 稳定化整理', 'SP Agent Result',
    'Parallel Dispatch Plan', 'kiro-task-execution-contract.md', 'task-completion-contract.md',
    'tdd-evidence-contract.md', 'v0.9.0 TDD Evidence Contract', 'RED/GREEN/REFACTOR'
]:
    if token not in matrix:
        errors.append(f'Matrix missing capability/token: {token}')

# Version docs must mention v0.8.0 and upgrade path.
for rel, tokens in {
    'CHANGELOG.md': ['v0.9.0', 'TDD Evidence Contract', 'RED/GREEN/REFACTOR'],
    'MIGRATION.md': ['从 v0.8.0 升级到 v0.9.0', 'v0.9.0 只增强 TDD 证据要求', '原安装提示不变'],
    'README.md': ['Kiro Superpowers Discipline v0.9.0', 'v0.9.0 是 TDD Evidence Contract 版本'],
}.items():
    text = (root / rel).read_text(encoding='utf-8') if (root / rel).exists() else ''
    for token in tokens:
        if token not in text:
            errors.append(f'{rel} missing token: {token}')

# Scripts must exist and shell scripts must pass bash syntax checks when available.
for rel in ['scripts/sp-worktree-create.sh', 'scripts/sp-finish-branch.sh', 'install/install.sh',
            'workspace-assets/.kiro/scripts/sp-worktree-create.sh', 'workspace-assets/.kiro/scripts/sp-finish-branch.sh']:
    p = root / rel
    if p.exists():
        try:
            subprocess.run(['bash', '-n', str(p)], check=True, capture_output=True, text=True)
        except Exception as exc:
            errors.append(f'Shell syntax check failed: {rel}: {exc}')

# No ai_dev_os in this package.
for p in root.rglob('*'):
    rel = p.relative_to(root).as_posix()
    if 'ai_dev_os' in rel:
        errors.append(f'Forbidden ai_dev_os path/token: {rel}')

# No accidental stale top-level version in important files.
for rel in ['README.md', 'INSTALL.md', 'INSTALL_FOR_KIRO.md', 'USAGE.md', 'MIGRATION.md', 'SUPERPOWERS_CAPABILITY_MATRIX.md', 'install/install.sh', 'install/install.ps1']:
    p = root / rel
    if p.exists():
        text = p.read_text(encoding='utf-8')
        if 'kiro_superpowers_discipline_v0_8_0' in text:
            errors.append(f'Stale package path in {rel}')

if errors:
    for e in errors:
        print(f'FAIL: {e}')
    raise SystemExit(1)

print('Compatibility validation passed')
print('- Package structure: PASS')
print('- Power structure: PASS')
print('- Hook JSON and naming: PASS')
print('- Agent frontmatter and standardized output: PASS')
print('- Scripts and shell syntax: PASS')
print('- v0.2-v0.7 user entrypoints: PASS')
print('- ai_dev_os absent: PASS')
print('- CHANGELOG/MIGRATION/capability matrix: PASS')
print('- README/INSTALL/UNINSTALL/USAGE/TROUBLESHOOTING: PASS')
print('- v0.4 worktree/branch finishing files: PASS')
print('- v0.5 subagent loop/review feedback files: PASS')
print('- v0.6 parallel agents safety files: PASS')
print('- v0.7 task execution/completion contract files: PASS')
print('- v0.8 stabilization checks: PASS')
print('- v0.9 TDD evidence contract files: PASS')
