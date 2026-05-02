#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess

root = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    p = root / rel
    return p.read_text(encoding='utf-8') if p.exists() else ''

def require_file(rel):
    if not (root / rel).exists():
        errors.append(f'Missing: {rel}')

required = [
    'README.md', 'INSTALL.md', 'INSTALL_FOR_KIRO.md', 'UNINSTALL.md', 'USAGE.md',
    'TROUBLESHOOTING.md', 'CHANGELOG.md', 'MIGRATION.md', 'SUPERPOWERS_CAPABILITY_MATRIX.md',
    'power/POWER.md', 'prompts/kiro-install-prompt.md', 'prompts/kiro-first-use-prompt.md',
    'install/install.ps1', 'install/install.sh',
    'scripts/validate_package.py',
    'scripts/sp-worktree-create.sh', 'scripts/sp-finish-branch.sh',
    'scripts/sp-worktree-create.ps1', 'scripts/sp-finish-branch.ps1',
    'power/steering/auto-routing.md', 'power/steering/status-banner.md',
    'power/steering/superpowers-router.md', 'power/steering/stable-output-contract.md',
    'power/steering/worktree-automation.md', 'power/steering/worktree-hardening.md',
    'power/steering/branch-finishing.md', 'power/steering/branch-finishing-hardening.md',
    'power/steering/task-by-task-subagent-loop.md', 'power/steering/review-feedback-loop.md',
    'power/steering/parallel-agent-policy.md',
    'power/steering/kiro-task-execution-contract.md', 'power/steering/executing-plans-discipline.md',
    'power/steering/task-completion-contract.md',
    'power/steering/tdd-discipline.md', 'power/steering/tdd-evidence-contract.md',
    'power/steering/kiro-task-refinement-gate.md',
    'power/steering/subagent-task-packet.md', 'power/steering/review-evidence-contract.md',
    'power/steering/debugging-deep-techniques.md', 'power/steering/fresh-verification-evidence.md',
    'workspace-assets/.kiro/steering/superpowers-stable-output-contract.md',
    'workspace-assets/.kiro/scripts/sp-worktree-create.sh', 'workspace-assets/.kiro/scripts/sp-finish-branch.sh',
    'workspace-assets/.kiro/scripts/sp-worktree-create.ps1', 'workspace-assets/.kiro/scripts/sp-finish-branch.ps1',
]
for rel in required:
    require_file(rel)

# Hook JSON: check every hook, preserve stable numbering/naming.
hook_dir = root / 'workspace-assets/.kiro/hooks'
hooks = sorted(hook_dir.glob('*.kiro.hook')) if hook_dir.exists() else []
if len(hooks) < 29:
    errors.append(f'Expected at least 29 hooks, found {len(hooks)}')
for p in hooks:
    if not re.match(r'^\d{2}-sp-[a-z0-9-]+\.kiro\.hook$', p.name):
        errors.append(f'Hook name not stable: {p.name}')
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'Invalid hook JSON: {p}: {exc}')
        continue
    for key in ['enabled', 'name', 'description', 'when', 'then']:
        if key not in data:
            errors.append(f'Hook missing {key}: {p.name}')

# Agents: check all sp-* agents, frontmatter, standardized output, status lexicon.
agent_dir = root / 'workspace-assets/.kiro/agents'
agents = sorted(agent_dir.glob('sp-*.md')) if agent_dir.exists() else []
expected_agents = {'sp-implementer.md','sp-spec-reviewer.md','sp-code-reviewer.md','sp-test-verifier.md','sp-debugger.md','sp-review-feedback-handler.md'}
found_agents = {p.name for p in agents}
for name in expected_agents:
    if name not in found_agents:
        errors.append(f'Missing agent: {name}')
for p in agents:
    text = p.read_text(encoding='utf-8')
    if not text.startswith('---'):
        errors.append(f'Agent missing frontmatter: {p.name}')
    for token in ['name:', 'description:', 'tools:', 'SP Agent Result', 'v1.5 Stable Output Contract']:
        if token not in text:
            errors.append(f'Agent missing token {token}: {p.name}')
    for token in ['DONE', 'BLOCKED', 'NEEDS_CONTEXT', 'FAILED']:
        if token not in text:
            errors.append(f'Agent missing canonical status {token}: {p.name}')

# Scripts: existence and shell syntax.
script_files = list((root/'scripts').glob('sp-*')) + list((root/'workspace-assets/.kiro/scripts').glob('sp-*'))
if len(script_files) < 8:
    errors.append(f'Expected at least 8 worktree/finishing scripts, found {len(script_files)}')
for rel in ['scripts/sp-worktree-create.sh', 'scripts/sp-finish-branch.sh', 'install/install.sh',
            'workspace-assets/.kiro/scripts/sp-worktree-create.sh', 'workspace-assets/.kiro/scripts/sp-finish-branch.sh']:
    p = root / rel
    if p.exists():
        try:
            subprocess.run(['bash', '-n', str(p)], check=True, capture_output=True, text=True)
        except Exception as exc:
            errors.append(f'Shell syntax check failed: {rel}: {exc}')

# Power/version docs.
power = read('power/POWER.md')
if 'version: "1.5.0"' not in power:
    errors.append('POWER.md version is not 1.5.0')
for token in ['stable-output-contract.md', 'v1.5 Stable Terminology and Output Contract', 'fresh verification evidence', 'TDD Evidence', 'Kiro Task Refinement Gate', 'Subagent Task Packet', 'Review Evidence Contract', 'root-cause-tracing']:
    if token not in power:
        errors.append(f'POWER.md missing token: {token}')

# Natural-language entrypoints and key compatibility tokens.
combined_files = ['README.md','INSTALL.md','INSTALL_FOR_KIRO.md','USAGE.md','UNINSTALL.md','TROUBLESHOOTING.md','power/POWER.md']
combined = '\n'.join(read(rel) for rel in combined_files)
for token in [
    '新增数据导出功能', '修复登录失败的问题', '继续当前 spec 的下一个任务', '检查当前任务是否真的完成',
    '请安装这个目录里的 Kiro Superpowers Discipline 到当前项目',
    '不要求用户写长提示词', '不包含 ai_dev_os',
    '【Kiro规格主控', '【Superpowers执行纪律',
    'DONE', 'COMPLETE', 'NOT COMPLETE', 'BLOCKED', 'NEEDS_CONTEXT', 'FAILED', 'PARTIAL', 'UNVERIFIED',
    'TDD Evidence', 'RED 验证命令', 'GREEN 验证命令',
    'Kiro Task Refinement Gate', 'Subagent Task Packet', 'Review Evidence Contract',
    'BASE_SHA', 'HEAD_SHA', 'Changed files',
    'Worktree hardening', 'branch finishing hardening', 'baseline verification', 'worktree metadata',
    'root-cause-tracing', 'defense-in-depth', 'condition-based-waiting', 'multi-component diagnostics', 'architecture stop gate',
    'fresh verification evidence', 'Verification Evidence', 'exit code', 'pass count', 'fail count', 'skip count'
]:
    if token not in combined:
        errors.append(f'Compatibility/user-experience token missing: {token}')

# Capability matrix coverage.
matrix = read('SUPERPOWERS_CAPABILITY_MATRIX.md')
for token in [
    '版本：v1.5.0', 'v1.5.0 稳定版整理',
    'using-superpowers', 'brainstorming', 'writing-plans', 'executing-plans',
    'test-driven-development', 'systematic-debugging', 'verification-before-completion',
    'requesting-code-review', 'receiving-code-review', 'subagent-driven-development',
    'dispatching-parallel-agents', 'using-git-worktrees', 'finishing-a-development-branch', 'writing-skills',
    'v0.9.0 TDD Evidence Contract', 'v1.0.0 Kiro Task Refinement Gate', 'v1.1.0 Subagent Task Packet',
    'v1.2.0 Worktree / Branch Finishing Hardening', 'v1.3.0 Debugging Deep Techniques', 'v1.4.0 Fresh Verification Evidence',
    'stable-output-contract.md', 'SP Agent Result'
]:
    if token not in matrix:
        errors.append(f'Matrix missing capability/token: {token}')

# Documentation completeness.
for rel, tokens in {
    'README.md': ['Kiro Superpowers Discipline v1.5.0', 'v1.5.0 是稳定版整理', '一处一处', 'v1.5'],
    'INSTALL.md': ['一 kõ']
}.items():
    pass
# Explicit docs checks without accidental fake tokens.
for rel, tokens in {
    'README.md': ['Kiro Superpowers Discipline v1.5.0', 'v1.5.0 是稳定版整理', '统一状态词'],
    'INSTALL.md': ['安装 Kiro Superpowers Discipline v1.5.0', '一ែ句话安装'.replace('ែ',''), 'Add power from Local Path'],
    'UNINSTALL.md': ['卸载 Kiro Superpowers Discipline v1.5.0', '.kiro/steering/superpowers-*.md', '不会删除你的业务代码'],
    'USAGE.md': ['日常使用', '统一状态标识', 'Fresh Verification Evidence'],
    'TROUBLESHOOTING.md': ['故障排查', 'verification 失败怎么办', '状态词混乱怎么办'],
    'CHANGELOG.md': ['v1.5.0', '稳定版整理', 'validate-package.py 增强'],
    'MIGRATION.md': ['从 v1.4.0 升级到 v1.5.0', '原安装提示不变', '不引入 ai_dev_os']
}.items():
    text = read(rel)
    for token in tokens:
        if token not in text:
            errors.append(f'{rel} missing token: {token}')

# No ai_dev_os in package paths or important text.
for p in root.rglob('*'):
    rel = p.relative_to(root).as_posix()
    if 'ai_dev_os' in rel:
        errors.append(f'Forbidden ai_dev_os path/token: {rel}')
# Intentional documentation may mention that ai_dev_os is not included. Only paths are forbidden.

# No stale package path in user-facing install prompts.
for rel in ['README.md','INSTALL.md','INSTALL_FOR_KIRO.md','USAGE.md','MIGRATION.md','prompts/kiro-install-prompt.md','install/install.sh','install/install.ps1']:
    text = read(rel)
    for stale in ['kiro_superpowers_discipline_v1_0_0','kiro_superpowers_discipline_v1_1_0','kiro_superpowers_discipline_v1_2_0','kiro_superpowers_discipline_v1_3_0','kiro_superpowers_discipline_v1_4_0']:
        if stale in text:
            errors.append(f'Stale package path in {rel}: {stale}')

if errors:
    for e in errors:
        print(f'FAIL: {e}')
    raise SystemExit(1)

print('Compatibility validation passed')
print('- Package structure: PASS')
print('- Power structure/version: PASS')
print('- Hook JSON and naming: PASS')
print('- Agent frontmatter and standardized output: PASS')
print('- Scripts and shell syntax: PASS')
print('- v0.2-v1.4 user entrypoints: PASS')
print('- ai_dev_os absent: PASS')
print('- CHANGELOG/MIGRATION/capability matrix: PASS')
print('- README/INSTALL/UNINSTALL/USAGE/TROUBLESHOOTING: PASS')
print('- v0.9-v1.4 capabilities preserved: PASS')
print('- v1.5 stable terminology/output contract: PASS')
