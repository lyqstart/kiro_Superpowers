param(
  [string]$ProjectRoot = "."
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

$mainBranch = ""
git show-ref --verify --quiet refs/heads/main
if ($LASTEXITCODE -eq 0) { $mainBranch = "main" }
else {
  git show-ref --verify --quiet refs/heads/master
  if ($LASTEXITCODE -eq 0) { $mainBranch = "master" }
}

$status = git status --short
Write-Host "Branch finishing check"
Write-Host "  repo:    $root"
Write-Host "  branch:  $currentBranch"
Write-Host "  target:  $(if ($mainBranch) { $mainBranch } else { 'not found' })"
Write-Host ""
if ($status) {
  Write-Host "Changed files:"
  $status | ForEach-Object { Write-Host $_ }
} else {
  Write-Host "Changed files: none"
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
    $confirm = Read-Host "确认合并？输入 '确认合并' 继续"
    if ($confirm -ne "确认合并") { Write-Host "Merge cancelled."; exit 0 }
    git checkout $mainBranch
    git merge --no-ff $currentBranch
    Write-Host "Merge completed. Worktree cleanup, if needed, must be done after confirming no data is needed."
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
    Write-Host "DANGER: This can discard work."
    git status --short
    $confirmDelete = Read-Host "二次确认：输入 DELETE 才会尝试丢弃未提交改动"
    if ($confirmDelete -ne "DELETE") { Write-Host "Discard cancelled."; exit 0 }
    git reset --hard
    git clean -fd
    Write-Host "Uncommitted changes discarded in current worktree. Worktree directory was not removed automatically."
  }
  default {
    throw "Invalid choice. No action taken."
  }
}
