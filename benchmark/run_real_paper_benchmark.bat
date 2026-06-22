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

python benchmark\scripts\build_real_paper_analysis_tasks.py

if "%LIMIT%"=="0" (
  powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_real_paper_benchmark.ps1 -Condition %CONDITION%
) else (
  powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_real_paper_benchmark.ps1 -Condition %CONDITION% -Limit %LIMIT%
)

python benchmark\scripts\score_real_paper_outputs.py --condition %CONDITION%

echo.
echo Results:
echo   benchmark\real_paper_analysis_tasks\results\summary.json
echo   benchmark\real_paper_analysis_tasks\results\scores.csv
echo   benchmark\real_paper_analysis_tasks\results\run_log.jsonl
endlocal
