param(
  [string]$ProjectRoot = ".",
  [switch]$Force
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PackageRoot = Split-Path -Parent $ScriptDir
$Source = Join-Path $PackageRoot "workspace-assets\.kiro"
$ResolvedProjectRoot = (Resolve-Path $ProjectRoot).Path
$Target = Join-Path $ResolvedProjectRoot ".kiro"

if (!(Test-Path $Source)) {
  throw "Source assets not found: $Source"
}

Write-Host "Installing Kiro Superpowers Discipline v0.7.0"
Write-Host "Project: $ResolvedProjectRoot"

New-Item -ItemType Directory -Force -Path $Target | Out-Null

$Dirs = @("steering", "hooks", "agents", "scripts")
foreach ($dir in $Dirs) {
  $srcDir = Join-Path $Source $dir
  $dstDir = Join-Path $Target $dir
  if (Test-Path $srcDir) {
    New-Item -ItemType Directory -Force -Path $dstDir | Out-Null
    Get-ChildItem -Path $srcDir -File | ForEach-Object {
      $dst = Join-Path $dstDir $_.Name
      if ((Test-Path $dst) -and (-not $Force)) {
        Write-Host "Skip existing: $dst"
      } else {
        Copy-Item $_.FullName $dst -Force
        Write-Host "Installed: $dst"
      }
    }
  }
}

$hookDir = Join-Path $Target "hooks"
if (Test-Path $hookDir) {
  Get-ChildItem -Path $hookDir -Filter "*.kiro.hook" | ForEach-Object {
    try {
      Get-Content $_.FullName -Raw | ConvertFrom-Json | Out-Null
      Write-Host "Hook JSON OK: $($_.Name)"
    } catch {
      throw "Invalid hook JSON: $($_.FullName)"
    }
  }
}

Write-Host ""
Write-Host "Installed workspace files."
Write-Host "Now add the Power in Kiro: Powers -> Add power from Local Path -> $PackageRoot\power"
Write-Host "Daily use: say '新增xxx', '修复xxx', or '继续当前 spec 的下一个任务'."
