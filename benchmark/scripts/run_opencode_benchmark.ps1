param(
  [string]$Model = "",
  [ValidateSet("baseline", "plugin_guided", "both")]
  [string]$Condition = "both",
  [int]$Limit = 0
)

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Conditions = if ($Condition -eq "both") { @("baseline", "plugin_guided") } else { @($Condition) }

foreach ($cond in $Conditions) {
  $promptDir = Join-Path $Root "prompts\$cond"
  $outputDir = Join-Path $Root "outputs\$cond"
  New-Item -ItemType Directory -Force $outputDir | Out-Null
  $prompts = Get-ChildItem $promptDir -Filter *.md | Sort-Object Name
  if ($Limit -gt 0) { $prompts = $prompts | Select-Object -First $Limit }

  foreach ($prompt in $prompts) {
    $out = Join-Path $outputDir ($prompt.BaseName + ".jsonl")
    $err = Join-Path $outputDir ($prompt.BaseName + ".stderr.txt")
    $msg = Get-Content -Raw $prompt.FullName
    Write-Host "[$cond] $($prompt.Name)"
    $args = @("run", "--format", "json", "--dir", $Root)
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
    } | ConvertTo-Json -Compress | Add-Content (Join-Path $Root "results\run_log.jsonl")
  }
}

