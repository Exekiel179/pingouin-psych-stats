@echo off
setlocal
cd /d "%~dp0\.."

if "%~1"=="" (
  set CONDITION=both
) else (
  set CONDITION=%~1
)

if "%~2"=="" (
  set LIMIT=0
) else (
  set LIMIT=%~2
)

python benchmark\scripts\build_existing_task_pool.py

if "%LIMIT%"=="0" (
  powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_opencode_benchmark.ps1 -Condition %CONDITION%
) else (
  powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_opencode_benchmark.ps1 -Condition %CONDITION% -Limit %LIMIT%
)

python benchmark\scripts\score_outputs.py --condition %CONDITION%

echo.
echo Results:
echo   benchmark\results\summary.json
echo   benchmark\results\scores.csv
echo   benchmark\results\run_log.jsonl
endlocal

