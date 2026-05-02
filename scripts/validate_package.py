#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
required = [
    'README.md',
    'INSTALL_FOR_KIRO.md',
    'USAGE.md',
    'power/POWER.md',
    'power/steering/auto-routing.md',
    'workspace-assets/.kiro/steering/superpowers-discipline.md',
    'workspace-assets/.kiro/hooks/00-sp-pre-task-gate.kiro.hook',
    'workspace-assets/.kiro/hooks/01-sp-post-task-verification.kiro.hook',
    'workspace-assets/.kiro/agents/sp-implementer.md',
    'install/install.ps1',
    'install/install.sh',
]
for rel in required:
    p = root / rel
    if not p.exists():
        raise SystemExit(f'Missing: {rel}')

for p in (root / 'workspace-assets/.kiro/hooks').glob('*.kiro.hook'):
    json.loads(p.read_text(encoding='utf-8'))

readme = (root / 'README.md').read_text(encoding='utf-8')
assert '用户日常不需要写长提示词' in readme
assert '请安装这个目录里的 Kiro Superpowers Discipline 到当前项目' in readme
print('Package validation passed')
