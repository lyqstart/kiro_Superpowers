#!/usr/bin/env python3
from pathlib import Path
import json, re, subprocess, sys
root = Path(__file__).resolve().parents[1]
errors=[]

def read(rel):
    p=root/rel
    return p.read_text(encoding='utf-8') if p.exists() else ''

def require(rel):
    if not (root/rel).exists(): errors.append(f'Missing: {rel}')

required = [
 'README.md','INSTALL.md','INSTALL_FOR_KIRO.md','UNINSTALL.md','USAGE.md','TROUBLESHOOTING.md','CHANGELOG.md','MIGRATION.md',
 'SUPERPOWERS_CAPABILITY_MATRIX.md','KIRO_LIMITATIONS.md','SUPERPOWERS_REMAINING_GAPS.md','power/POWER.md',
 'install/install.sh','install/install.ps1','scripts/validate_package.py',
 'scripts/sp-worktree-create.sh','scripts/sp-finish-branch.sh','scripts/sp-worktree-create.ps1','scripts/sp-finish-branch.ps1',
 'scripts/sp-skill-activate.sh','scripts/sp-skill-activate.ps1'
]
for rel in required: require(rel)

v2_steering = [
 'skill-runtime-lite.md','spec-brainstorming-gate.md','kiro-task-micro-plan-contract.md','task-execution-ledger.md',
 'review-reception-hardening.md','final-whole-feature-review-gate.md','tdd-violation-recovery.md','debug-pattern-analysis.md',
 'parallel-agent-dispatch-contract.md','worktree-directory-strategy.md','pr-template-and-finish-metadata.md','verification-transcript-capture.md','kiro-mechanism-limitations.md'
]
for name in v2_steering:
    require(f'power/steering/{name}')
    require(f'workspace-assets/.kiro/steering/superpowers-{name}')

skills = ['using-superpowers','brainstorming','writing-plans','executing-plans','subagent-driven-development','test-driven-development','systematic-debugging','verification-before-completion','requesting-code-review','receiving-code-review','dispatching-parallel-agents','using-git-worktrees','finishing-a-development-branch','writing-skills']
for s in skills:
    require(f'superpowers-skills/{s}.md')
    require(f'workspace-assets/.kiro/superpowers-skills/{s}.md')

for t in ['SKILL_ACTIVATION_LEDGER_TEMPLATE.md','TASK_EXECUTION_LEDGER_TEMPLATE.md','MICRO_PLAN_TEMPLATE.md','REVIEW_REQUEST_TEMPLATE.md','PR_TEMPLATE.md']:
    require(f'templates/{t}')
    require(f'workspace-assets/.kiro/superpowers-templates/{t}')

# Hooks
hook_dir=root/'workspace-assets/.kiro/hooks'
hooks=sorted(hook_dir.glob('*.kiro.hook')) if hook_dir.exists() else []
if len(hooks) < 41: errors.append(f'Expected at least 41 hooks, found {len(hooks)}')
for p in hooks:
    if not re.match(r'^\d{2}-sp-[a-z0-9-]+\.kiro\.hook$', p.name): errors.append(f'Bad hook name: {p.name}')
    try:
        data=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'Invalid hook JSON {p.name}: {e}'); continue
    for k in ['enabled','name','description','when','then']:
        if k not in data: errors.append(f'{p.name} missing {k}')

# Agents
agents=sorted((root/'workspace-assets/.kiro/agents').glob('sp-*.md'))
expected={'sp-implementer.md','sp-spec-reviewer.md','sp-code-reviewer.md','sp-test-verifier.md','sp-debugger.md','sp-review-feedback-handler.md','sp-skill-router.md','sp-plan-refiner.md','sp-final-reviewer.md','sp-review-reception-handler.md'}
found={p.name for p in agents}
for e in expected:
    if e not in found: errors.append(f'Missing agent: {e}')
for p in agents:
    txt=p.read_text(encoding='utf-8')
    for token in ['---','name:','description:','tools:','SP Agent Result']:
        if token not in txt: errors.append(f'{p.name} missing {token}')

# Shell syntax
for rel in ['install/install.sh','scripts/sp-worktree-create.sh','scripts/sp-finish-branch.sh','scripts/sp-skill-activate.sh','workspace-assets/.kiro/scripts/sp-worktree-create.sh','workspace-assets/.kiro/scripts/sp-finish-branch.sh','workspace-assets/.kiro/scripts/sp-skill-activate.sh']:
    p=root/rel
    if p.exists():
        try: subprocess.run(['bash','-n',str(p)], check=True, capture_output=True, text=True)
        except Exception as e: errors.append(f'Shell syntax failed {rel}: {e}')

# Version and user entrypoints
power=read('power/POWER.md')
if 'version: "2.0.0"' not in power: errors.append('POWER.md version is not 2.0.0')
combined='\n'.join(read(r) for r in ['README.md','INSTALL.md','INSTALL_FOR_KIRO.md','USAGE.md','UNINSTALL.md','TROUBLESHOOTING.md','power/POWER.md','SUPERPOWERS_CAPABILITY_MATRIX.md'])
for token in ['新增数据导出功能','修复登录失败的问题','继续当前 spec 的下一个任务','检查当前任务是否真的完成','请安装这个目录里的 Kiro Superpowers Discipline 到当前项目','不要求用户写长提示词','Skill Runtime Lite','Skill Activation Ledger','Kiro Spec Brainstorming Gate','Kiro Task Micro-Plan Contract','Task Execution Ledger','Review Reception Hardening','Final Whole-Feature Review','TDD Violation Recovery','Debug Pattern Analysis','Verification Transcript Capture','KIRO_LIMITATIONS.md','SUPERPOWERS_REMAINING_GAPS.md']:
    if token not in combined: errors.append(f'Missing token: {token}')

# No forbidden ai_dev_os path
for p in root.rglob('*'):
    if 'ai_dev_os' in p.relative_to(root).as_posix(): errors.append(f'Forbidden ai_dev_os path: {p}')

if errors:
    for e in errors: print('FAIL:', e)
    sys.exit(1)
print('Compatibility validation passed')
print('- Package structure: PASS')
print('- Power structure/version: PASS')
print('- Hook JSON and naming: PASS')
print('- Agent frontmatter and v2 agents: PASS')
print('- Scripts and shell syntax: PASS')
print('- v0.2-v1.5 user entrypoints: PASS')
print('- v2.0 runtime-completion layer: PASS')
print('- ai_dev_os absent: PASS')
print('- Docs/matrix/limitations/gaps: PASS')
