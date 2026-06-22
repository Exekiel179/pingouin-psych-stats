param(
  [string]$Model = "",
  [ValidateSet("baseline", "plugin_guided", "both")]
  [string]$Condition = "both",
  [int]$Limit = 0
)

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Dataset = Join-Path $Root "real_paper_analysis_tasks"
$Conditions = if ($Condition -eq "both") { @("baseline", "plugin_guided") } else { @($Condition) }

if (-not (Test-Path $Dataset)) {
  python (Join-Path $Root "scripts\build_real_paper_analysis_tasks.py")
}

foreach ($cond in $Conditions) {
  $promptDir = Join-Path $Dataset "prompts\$cond"
  $outputDir = Join-Path $Dataset "outputs\$cond"
  New-Item -ItemType Directory -Force $outputDir | Out-Null
  $prompts = Get-ChildItem $promptDir -Filter *.md | Sort-Object Name
  if ($Limit -gt 0) { $prompts = $prompts | Select-Object -First $Limit }

  foreach ($prompt in $prompts) {
    $out = Join-Path $outputDir ($prompt.BaseName + ".jsonl")
    $err = Join-Path $outputDir ($prompt.BaseName + ".stderr.txt")
    $msg = Get-Content -Raw $prompt.FullName
    Write-Host "[real-paper:$cond] $($prompt.Name)"
    $args = @("run", "--format", "json", "--dir", $Dataset)
    if ($Model -ne "") { $args += @("--model", $Model) }
    $args += @($msg)
    $start = Get-Date
    & opencode @args 1> $out 2> $err
    $exit = $LASTEXITCODE
    $elapsed = [Math]::Round(((Get-Date) - $start).TotalSeconds, 2)
    [pscustomobject]@{
      condition = $cond
      task = $prompt.BaseName
      exit_code = $exit
      seconds = $elapsed
      output = $out
      stderr = $err
    } | ConvertTo-Json -Compress | Add-Content (Join-Path $Dataset "results\run_log.jsonl")
  }
}
