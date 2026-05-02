param(
  [string]$ProjectRoot = ".",
  [string]$VerifyCommand = ""
)

$ErrorActionPreference = "Stop"
Set-Location $ProjectRoot

try {
  $root = (git rev-parse --show-toplevel).Trim()
} catch {
  throw "Not inside a git repository."
}

Set-Location $root
$gitCommonDir = (git rev-parse --git-common-dir).Trim()
if (-not [System.IO.Path]::IsPathRooted($gitCommonDir)) { $gitCommonDir = Join-Path $root $gitCommonDir }
$worktreePath = $root
$currentBranch = (git branch --show-current).Trim()
if ([string]::IsNullOrWhiteSpace($currentBranch)) {
  throw "Detached HEAD is not supported by this safety script."
}

$mainBranch = ""
git show-ref --verify --quiet refs/heads/main
if ($LASTEXITCODE -eq 0) { $mainBranch = "main" }
else {
  git show-ref --verify --quiet refs/heads/master
  if ($LASTEXITCODE -eq 0) { $mainBranch = "master" }
}

$status = git status --short
$changedFiles = @()
$changedFiles += git diff --name-only
$changedFiles += git diff --cached --name-only
$changedFiles = $changedFiles | Where-Object { $_ } | Sort-Object -Unique

if ([string]::IsNullOrWhiteSpace($VerifyCommand)) {
  Write-Host "A fresh verification command is required before branch finishing options are shown."
  $VerifyCommand = Read-Host "请输入 verification 命令；留空则取消 finishing"
  if ([string]::IsNullOrWhiteSpace($VerifyCommand)) { throw "Verification command is required before finishing." }
}

Write-Host "Running fresh verification before branch finishing: $VerifyCommand"
powershell -NoProfile -ExecutionPolicy Bypass -Command $VerifyCommand
$verifyExit = $LASTEXITCODE
if ($null -eq $verifyExit) { $verifyExit = 0 }
if ($verifyExit -ne 0) { throw "Verification failed. Do not merge, push PR, or discard as completed." }

$commits = @()
if ($mainBranch) { $commits = git log --oneline "$mainBranch..$currentBranch" 2>$null }

Write-Host "Branch finishing check"
Write-Host "  repo:      $root"
Write-Host "  branch:    $currentBranch"
Write-Host "  base:      $(if ($mainBranch) { $mainBranch } else { 'not found' })"
Write-Host "  worktree:  $worktreePath"
Write-Host "  verify:    $VerifyCommand"
Write-Host ""
if ($status) { Write-Host "Working tree status:"; $status | ForEach-Object { Write-Host $_ } } else { Write-Host "Working tree status: clean" }
if ($changedFiles) { Write-Host "Changed files:"; $changedFiles | ForEach-Object { Write-Host $_ } } else { Write-Host "Changed files: none" }
if ($commits) { Write-Host "Commits since ${mainBranch}:"; $commits | ForEach-Object { Write-Host $_ } } else { Write-Host "Commits since base: none or base unavailable" }

function Invoke-WorktreeCleanupPrompt {
  param([string]$Path, [string]$GitCommonDir)
  $cleanConfirm = Read-Host "是否清理当前 worktree？输入 CLEAN_WORKTREE 才会执行 git worktree remove"
  if ($cleanConfirm -ne "CLEAN_WORKTREE") { Write-Host "Worktree cleanup skipped."; return }
  Set-Location ([System.IO.Path]::GetTempPath())
  git --git-dir="$GitCommonDir" worktree remove "$Path"
  Write-Host "Worktree removed: $Path"
}

Write-Host ""
Write-Host "Choose next action:"
Write-Host "1. 合并回主分支"
Write-Host "2. 推送并创建 PR"
Write-Host "3. 保留分支"
Write-Host "4. 丢弃本次工作"
$choice = Read-Host "请输入 1/2/3/4"

switch ($choice) {
  "1" {
    if (-not $mainBranch) { throw "Cannot find main or master branch." }
    if ($status) { throw "Working tree has uncommitted changes. Commit them before merging." }
    Write-Host "About to merge $currentBranch into $mainBranch."
    Write-Host "Current branch: $currentBranch"
    Write-Host "Base branch: $mainBranch"
    Write-Host "Changed files:"
    if ($changedFiles) { $changedFiles | ForEach-Object { Write-Host $_ } } else { Write-Host "none" }
    $confirm = Read-Host "确认合并？输入 '确认合并' 继续"
    if ($confirm -ne "确认合并") { Write-Host "Merge cancelled."; exit 0 }
    git checkout $mainBranch
    git merge --no-ff $currentBranch
    Write-Host "Merge completed. Suggested: run verification again on ${mainBranch}: $VerifyCommand"
    $runVerify = Read-Host "是否现在重新运行验证？输入 RUN_VERIFY 继续"
    if ($runVerify -eq "RUN_VERIFY") { powershell -NoProfile -ExecutionPolicy Bypass -Command $VerifyCommand }
    Invoke-WorktreeCleanupPrompt -Path $worktreePath -GitCommonDir $gitCommonDir
  }
  "2" {
    Write-Host "Pushing current branch: $currentBranch"
    git push -u origin $currentBranch
    if (Get-Command gh -ErrorAction SilentlyContinue) {
      $confirmPr = Read-Host "GitHub CLI detected. 输入 '创建PR' 继续"
      if ($confirmPr -eq "创建PR") { gh pr create } else { Write-Host "PR creation skipped." }
    } else {
      Write-Host "Branch pushed. GitHub CLI not found; create PR manually if needed."
    }
  }
  "3" {
    Write-Host "Keeping branch/worktree unchanged."
  }
  "4" {
    Write-Host "DANGER: This can discard work. Review carefully before confirming."
    Write-Host "Branch: $currentBranch"
    Write-Host "Worktree path: $worktreePath"
    Write-Host "Changed files:"
    if ($changedFiles) { $changedFiles | ForEach-Object { Write-Host $_ } } else { Write-Host "none" }
    Write-Host "Commits since $(if ($mainBranch) { $mainBranch } else { 'base' }):"
    if ($commits) { $commits | ForEach-Object { Write-Host $_ } } else { Write-Host "none or base unavailable" }
    $confirmDelete = Read-Host "二次确认：输入 DISCARD_WORK 才会丢弃未提交改动"
    if ($confirmDelete -ne "DISCARD_WORK") { Write-Host "Discard cancelled."; exit 0 }
    git reset --hard
    git clean -fd
    Write-Host "Uncommitted changes discarded in current worktree."
    Invoke-WorktreeCleanupPrompt -Path $worktreePath -GitCommonDir $gitCommonDir
  }
  default {
    throw "Invalid choice. No action taken."
  }
}
