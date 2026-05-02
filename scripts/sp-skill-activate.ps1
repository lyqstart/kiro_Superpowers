param(
  [Parameter(Mandatory=$true)][string]$Skill,
  [string]$Purpose = "not specified"
)
$ErrorActionPreference = "Stop"
try {
  $root = (git rev-parse --show-toplevel 2>$null)
  if (-not $root) { $root = (Get-Location).Path }
} catch { $root = (Get-Location).Path }
$runtime = Join-Path $root ".kiro\superpowers-runtime"
New-Item -ItemType Directory -Force -Path $runtime | Out-Null
$ledger = Join-Path $runtime "SKILL_ACTIVATION_LEDGER.md"
$ts = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
Add-Content -Path $ledger -Encoding UTF8 -Value "`n## $ts | $Skill`n- Purpose: $Purpose`n- Status: activated"
Write-Host "Skill activated: $Skill"
Write-Host "Ledger: $ledger"
