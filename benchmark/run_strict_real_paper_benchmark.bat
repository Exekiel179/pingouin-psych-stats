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

python benchmark\scripts\build_strict_real_paper_benchmark.py

if "%LIMIT%"=="0" (
  powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_strict_real_paper_benchmark.ps1 -Condition %CONDITION%
) else (
  powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_strict_real_paper_benchmark.ps1 -Condition %CONDITION% -Limit %LIMIT%
)

python benchmark\scripts\score_strict_real_paper_outputs.py --condition %CONDITION%

echo.
echo Results:
echo   benchmark\strict_real_paper_benchmark\results\summary.json
echo   benchmark\strict_real_paper_benchmark\results\scores.csv
echo   benchmark\strict_real_paper_benchmark\results\run_log.jsonl
endlocal
