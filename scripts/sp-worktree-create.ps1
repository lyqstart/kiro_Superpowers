param(
  [string]$ProjectRoot = ".",
  [string]$TaskName = "kiro-task",
  [string]$BaselineCommand = ""
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
$worktreeDir = Join-Path $root ".worktrees\$safeTask-$stamp"

New-Item -ItemType Directory -Force -Path (Join-Path $root ".worktrees") | Out-Null

$gitignore = Join-Path $root ".gitignore"
if ((Test-Path $gitignore) -and ((Get-Content $gitignore) -contains ".worktrees/")) {
  Write-Host "Gitignore OK: .worktrees/"
} else {
  Write-Host "NOTICE: .worktrees/ is not listed in .gitignore. Add it if you do not want worktree directories to appear as untracked files."
}

Write-Host "Creating isolated worktree:"
Write-Host "  branch:   $branch"
Write-Host "  location: $worktreeDir"
git worktree add -b $branch $worktreeDir HEAD

if (-not [string]::IsNullOrWhiteSpace($BaselineCommand)) {
  Write-Host "Running baseline verification in worktree: $BaselineCommand"
  Push-Location $worktreeDir
  try {
    powershell -NoProfile -ExecutionPolicy Bypass -Command $BaselineCommand
  } finally {
    Pop-Location
  }
} else {
  Write-Host "No baseline command provided. Baseline verification skipped."
}

Write-Host "WORKTREE_CREATED=$worktreeDir"
Write-Host "BRANCH_CREATED=$branch"
