param(
  [string]$ProjectRoot = ".",
  [string]$TaskName = "kiro-task",
  [string]$BaselineCommand = "",
  [string]$RelatedSpecTask = ""
)

$ErrorActionPreference = "Stop"
Set-Location $ProjectRoot

try {
  $root = (git rev-parse --show-toplevel).Trim()
} catch {
  throw "Not inside a git repository."
}

Set-Location $root
$currentBranch = (git branch --show-current).Trim()
if ([string]::IsNullOrWhiteSpace($currentBranch)) {
  throw "Detached HEAD is not supported by this safety script."
}

$status = git status --short
if ($status) {
  Write-Error "Working tree is not clean. Commit, stash, or resolve changes before creating an isolated worktree.`n$status"
  exit 1
}

$safeTask = $TaskName.ToLowerInvariant() -replace '[^a-z0-9._-]+','-'
$safeTask = $safeTask.Trim('-')
if ([string]::IsNullOrWhiteSpace($safeTask)) { $safeTask = "kiro-task" }
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$branch = "sp/$safeTask-$stamp"
$worktreesRoot = Join-Path $root ".worktrees"
$worktreeDir = Join-Path $worktreesRoot "$safeTask-$stamp"
$metadataDir = Join-Path $worktreesRoot ".metadata"
$metadataFile = Join-Path $metadataDir "$safeTask-$stamp.json"

New-Item -ItemType Directory -Force -Path $worktreesRoot | Out-Null
New-Item -ItemType Directory -Force -Path $metadataDir | Out-Null

$gitignore = Join-Path $root ".gitignore"
if ((Test-Path $gitignore) -and ((Get-Content $gitignore) -contains ".worktrees/")) {
  Write-Host "Gitignore OK: .worktrees/"
} else {
  Write-Host "WARNING: .worktrees/ is not listed in .gitignore."
  Write-Host "This can make isolated worktree directories appear as untracked files."
  $addGitignore = Read-Host "Add .worktrees/ to .gitignore now? 输入 y 添加，其他任意键跳过"
  if ($addGitignore -eq "y" -or $addGitignore -eq "Y") {
    if (!(Test-Path $gitignore)) { New-Item -ItemType File -Path $gitignore | Out-Null }
    Add-Content -Path $gitignore -Value "`n.worktrees/"
    Write-Host "Added .worktrees/ to .gitignore."
    Write-Host "NOTE: This script does not auto-commit .gitignore. Review and commit it yourself if appropriate."
  } else {
    Write-Host "Skipped .gitignore update. Continuing only because user explicitly skipped."
  }
}

function Get-BaselineCommand {
  param([string]$Provided)
  if (-not [string]::IsNullOrWhiteSpace($Provided)) { return $Provided }
  if (Test-Path "package.json") {
    $pkg = Get-Content "package.json" -Raw
    if ($pkg -match '"test"\s*:') {
      if ((Test-Path "pnpm-lock.yaml") -and (Get-Command pnpm -ErrorAction SilentlyContinue)) { return "pnpm test" }
      if ((Test-Path "yarn.lock") -and (Get-Command yarn -ErrorAction SilentlyContinue)) { return "yarn test" }
      if (Get-Command npm -ErrorAction SilentlyContinue) { return "npm test" }
    }
  }
  if ((Test-Path "go.mod") -and (Get-Command go -ErrorAction SilentlyContinue)) { return "go test ./..." }
  if ((Test-Path "Cargo.toml") -and (Get-Command cargo -ErrorAction SilentlyContinue)) { return "cargo test" }
  if (((Test-Path "tests") -or (Test-Path "pyproject.toml")) -and (Get-Command pytest -ErrorAction SilentlyContinue)) { return "pytest" }
  return ""
}

$detectedBaseline = Get-BaselineCommand -Provided $BaselineCommand
if ([string]::IsNullOrWhiteSpace($detectedBaseline)) {
  Write-Host "WARNING: Could not identify a baseline verification command automatically."
  $detectedBaseline = Read-Host "请输入 baseline 验证命令；留空则取消创建 worktree"
  if ([string]::IsNullOrWhiteSpace($detectedBaseline)) {
    throw "Baseline command is required unless the user explicitly decides to stop. Worktree creation cancelled."
  }
}

Write-Host "Creating isolated worktree:"
Write-Host "  base:     $currentBranch"
Write-Host "  branch:   $branch"
Write-Host "  location: $worktreeDir"
git worktree add -b $branch $worktreeDir HEAD

Write-Host "Running baseline verification in worktree: $detectedBaseline"
Push-Location $worktreeDir
try {
  powershell -NoProfile -ExecutionPolicy Bypass -Command $detectedBaseline
  $baselineExit = $LASTEXITCODE
} finally {
  Pop-Location
}
if ($null -eq $baselineExit) { $baselineExit = 0 }
$baselineResult = if ($baselineExit -eq 0) { "passed" } else { "failed" }

$metadata = [ordered]@{
  worktree_path = $worktreeDir
  branch_name = $branch
  base_branch = $currentBranch
  created_time = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
  related_spec_task = $RelatedSpecTask
  task_name = $TaskName
  baseline_command = $detectedBaseline
  baseline_result = $baselineResult
  baseline_exit_code = $baselineExit
}
$metadata | ConvertTo-Json -Depth 5 | Set-Content -Path $metadataFile -Encoding UTF8
Write-Host "Metadata written: $metadataFile"

if ($baselineExit -ne 0) {
  Write-Error "Baseline verification failed in the new worktree. Do not continue implementation unless the user explicitly confirms."
  Write-Host "WORKTREE_CREATED=$worktreeDir"
  Write-Host "BRANCH_CREATED=$branch"
  Write-Host "METADATA_FILE=$metadataFile"
  exit $baselineExit
}

Write-Host "WORKTREE_CREATED=$worktreeDir"
Write-Host "BRANCH_CREATED=$branch"
Write-Host "METADATA_FILE=$metadataFile"
Write-Host "BASELINE_RESULT=$baselineResult"
