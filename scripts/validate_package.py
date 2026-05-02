#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess

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
    'power/steering/worktree-hardening.md',
    'power/steering/branch-finishing.md',
    'power/steering/branch-finishing-hardening.md',
    'power/steering/task-by-task-subagent-loop.md',
    'power/steering/review-feedback-loop.md',
    'power/steering/parallel-agent-policy.md',
    'power/steering/kiro-task-execution-contract.md',
    'power/steering/executing-plans-discipline.md',
    'power/steering/task-completion-contract.md',
    'power/steering/tdd-discipline.md',
    'power/steering/tdd-evidence-contract.md',
    'power/steering/kiro-task-refinement-gate.md',
    'power/steering/subagent-task-packet.md',
    'power/steering/review-evidence-contract.md',
    'power/steering/debugging-deep-techniques.md',
    'power/steering/fresh-verification-evidence.md',
    'workspace-assets/.kiro/steering/superpowers-discipline.md',
    'workspace-assets/.kiro/steering/superpowers-status-banner.md',
    'workspace-assets/.kiro/steering/superpowers-router.md',
    'workspace-assets/.kiro/steering/superpowers-worktree-automation.md',
    'workspace-assets/.kiro/steering/superpowers-worktree-hardening.md',
    'workspace-assets/.kiro/steering/superpowers-branch-finishing.md',
    'workspace-assets/.kiro/steering/superpowers-branch-finishing-hardening.md',
    'workspace-assets/.kiro/steering/superpowers-task-by-task-subagent-loop.md',
    'workspace-assets/.kiro/steering/superpowers-review-feedback-loop.md',
    'workspace-assets/.kiro/steering/superpowers-parallel-agent-policy.md',
    'workspace-assets/.kiro/steering/superpowers-kiro-task-execution-contract.md',
    'workspace-assets/.kiro/steering/superpowers-executing-plans-discipline.md',
    'workspace-assets/.kiro/steering/superpowers-task-completion-contract.md',
    'workspace-assets/.kiro/steering/superpowers-tdd-evidence-contract.md',
    'workspace-assets/.kiro/steering/superpowers-kiro-task-refinement-gate.md',
    'workspace-assets/.kiro/steering/superpowers-subagent-task-packet.md',
    'workspace-assets/.kiro/steering/superpowers-review-evidence-contract.md',
    'workspace-assets/.kiro/steering/superpowers-debugging-deep-techniques.md',
    'workspace-assets/.kiro/steering/superpowers-fresh-verification-evidence.md',
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
    'workspace-assets/.kiro/hooks/14-sp-task-refinement-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/15-sp-task-split-review.kiro.hook',
    'workspace-assets/.kiro/hooks/16-sp-scope-creep-blocker.kiro.hook',
    'workspace-assets/.kiro/hooks/17-sp-subagent-task-packet.kiro.hook',
    'workspace-assets/.kiro/hooks/18-sp-subagent-result-contract.kiro.hook',
    'workspace-assets/.kiro/hooks/19-sp-review-evidence-contract.kiro.hook',
    'workspace-assets/.kiro/hooks/20-sp-worktree-hardening.kiro.hook',
    'workspace-assets/.kiro/hooks/21-sp-baseline-verification-hardening.kiro.hook',
    'workspace-assets/.kiro/hooks/22-sp-branch-finishing-hardening.kiro.hook',
    'workspace-assets/.kiro/hooks/23-sp-root-cause-tracing.kiro.hook',
    'workspace-assets/.kiro/hooks/24-sp-debugging-deep-techniques.kiro.hook',
    'workspace-assets/.kiro/hooks/25-sp-architecture-stop-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/26-sp-fresh-verification-evidence.kiro.hook',
    'workspace-assets/.kiro/hooks/27-sp-verification-result-contract.kiro.hook',
    'workspace-assets/.kiro/hooks/28-sp-completion-claim-hardening.kiro.hook',
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

# Hook JSON must parse and follow stable numbering/name.
hook_dir = root / 'workspace-assets/.kiro/hooks'
expected_hook_count = 29
hooks = sorted(hook_dir.glob('*.kiro.hook')) if hook_dir.exists() else []
if len(hooks) != expected_hook_count:
    errors.append(f'Expected {expected_hook_count} hooks, found {len(hooks)}')
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

# Agent frontmatter and standardized output.
agent_dir = root / 'workspace-assets/.kiro/agents'
for p in sorted(agent_dir.glob('sp-*.md')):
    text = p.read_text(encoding='utf-8')
    if not text.startswith('---'):
        errors.append(f'Agent missing frontmatter: {p.name}')
    for token in ['name:', 'description:', 'tools:', 'SP Agent Result']:
        if token not in text:
            errors.append(f'Agent missing token {token}: {p.name}')

# Key user experience and compatibility tokens.
combined_files = ['README.md', 'INSTALL.md', 'INSTALL_FOR_KIRO.md', 'USAGE.md', 'UNINSTALL.md', 'TROUBLESHOOTING.md', 'power/POWER.md']
combined = '\n'.join((root / rel).read_text(encoding='utf-8') for rel in combined_files if (root / rel).exists())
for token in [
    '新增数据导出功能', '修复登录失败的问题', '继续当前 spec 的下一个任务', '检查当前任务是否真的完成',
    '请安装这个目录里的 Kiro Superpowers Discipline 到当前项目',
    '【Kiro规格主控', '【Superpowers执行纪律', 'Parallel Dispatch Plan',
    'task execution contract', 'task completion contract', 'COMPLETE / NOT COMPLETE / BLOCKED',
    'TDD Evidence', 'RED 验证命令', 'GREEN 验证命令', 'Kiro Task Refinement Gate', 'Task Refinement Gate', '任务拆分',
    'Subagent Task Packet', 'Subagent Result Contract', 'Review Evidence Contract', 'BASE_SHA', 'HEAD_SHA', 'Changed files', 'Worktree hardening', 'Branch finishing hardening', 'baseline verification', 'worktree metadata', 'DISCARD_WORK', 'CLEAN_WORKTREE', 'root-cause-tracing', 'defense-in-depth', 'condition-based-waiting', 'multi-component diagnostics', 'architecture stop gate', 'fresh verification evidence', 'Verification Evidence', 'exit code', 'pass count', 'fail count', 'skip count', 'UNVERIFIED', 'PARTIAL'
]:
    if token not in combined:
        errors.append(f'Compatibility/user-experience token missing: {token}')

# Capability matrix must mention original skills and current implementation assets.
matrix = (root / 'SUPERPOWERS_CAPABILITY_MATRIX.md').read_text(encoding='utf-8') if (root / 'SUPERPOWERS_CAPABILITY_MATRIX.md').exists() else ''
for token in [
    'using-superpowers', 'brainstorming', 'writing-plans', 'executing-plans',
    'test-driven-development', 'systematic-debugging', 'verification-before-completion',
    'requesting-code-review', 'receiving-code-review', 'subagent-driven-development',
    'dispatching-parallel-agents', 'using-git-worktrees', 'finishing-a-development-branch',
    'writing-skills', 'v0.8.0 稳定化整理', 'SP Agent Result',
    'Parallel Dispatch Plan', 'kiro-task-execution-contract.md', 'task-completion-contract.md',
    'tdd-evidence-contract.md', 'v0.9.0 TDD Evidence Contract', 'RED/GREEN/REFACTOR',
    'kiro-task-refinement-gate.md', 'v1.0.0 Kiro Task Refinement Gate', 'Task Refinement Gate',
    'subagent-task-packet.md', 'review-evidence-contract.md', 'v1.1.0 Subagent Task Packet', 'Review Evidence Contract', 'Git diff evidence', 'worktree-hardening.md', 'branch-finishing-hardening.md', 'v1.2.0 Worktree / Branch Finishing Hardening', 'baseline verification', 'worktree metadata', 'debugging-deep-techniques.md', 'v1.3.0 Debugging Deep Techniques', 'root-cause-tracing', 'defense-in-depth', 'condition-based-waiting', 'multi-component diagnostics', 'architecture stop gate', 'fresh-verification-evidence.md', 'v1.4.0 Fresh Verification Evidence', 'verification result contract', 'completion claim hardening', 'UNVERIFIED', 'PARTIAL', 'fresh verification evidence', 'Verification Evidence', 'exit code', 'pass count', 'fail count', 'skip count', 'UNVERIFIED', 'PARTIAL'
]:
    if token not in matrix:
        errors.append(f'Matrix missing capability/token: {token}')

# Version docs must mention v1.2.0 and upgrade path.
for rel, tokens in {
    'CHANGELOG.md': ['v1.4.0', 'fresh verification evidence', '26-sp-fresh-verification-evidence'],
    'MIGRATION.md': ['从 v1.3.0 升级到 v1.4.0', 'v1.4.0 只增强完成声明前的新鲜验证证据', '原安装提示不变'],
    'README.md': ['Kiro Superpowers Discipline v1.4.0', 'v1.4.0 是 Fresh Verification Evidence 版本'],
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

# No accidental stale package path in important files.
for rel in ['README.md', 'INSTALL.md', 'INSTALL_FOR_KIRO.md', 'USAGE.md', 'MIGRATION.md', 'SUPERPOWERS_CAPABILITY_MATRIX.md', 'install/install.sh', 'install/install.ps1', 'prompts/kiro-install-prompt.md', 'prompts/kiro-first-use-prompt.md']:
    p = root / rel
    if p.exists():
        text = p.read_text(encoding='utf-8')
        for stale in ['kiro_superpowers_discipline_v1_0_0', 'kiro_superpowers_discipline_v1_1_0', 'kiro_superpowers_discipline_v1_2_0', 'kiro_superpowers_discipline_v1_3_0']:
            if stale in text:
                errors.append(f'Stale package path in {rel}: {stale}')

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
print('- v0.2-v1.3 user entrypoints: PASS')
print('- ai_dev_os absent: PASS')
print('- CHANGELOG/MIGRATION/capability matrix: PASS')
print('- README/INSTALL/UNINSTALL/USAGE/TROUBLESHOOTING: PASS')
print('- v0.4 worktree/branch finishing files: PASS')
print('- v0.5 subagent loop/review feedback files: PASS')
print('- v0.6 parallel agents safety files: PASS')
print('- v0.7 task execution/completion contract files: PASS')
print('- v0.8 stabilization checks: PASS')
print('- v0.9 TDD evidence contract files: PASS')
print('- v1.0 task refinement gate files: PASS')
print('- v1.1 subagent task packet/review evidence files: PASS')
print('- v1.2 worktree/branch finishing hardening files: PASS')
print('- v1.3 debugging deep techniques files: PASS')
print('- v1.4 fresh verification evidence files: PASS')
