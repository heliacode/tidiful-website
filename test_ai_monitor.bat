@echo off
REM Test script for AI Visibility Monitor (Windows)
REM Simulates GitHub Action environment

echo Testing AI Visibility Monitor...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    exit /b 1
)

REM Check if required files exist
if not exist "ai_visibility_monitor.py" (
    echo Error: Required file ai_visibility_monitor.py not found
    exit /b 1
)

if not exist "ai_monitoring_config.json" (
    echo Error: Required file ai_monitoring_config.json not found
    exit /b 1
)

echo All required files found

REM Run the monitoring script
echo Running AI visibility monitoring...
python ai_visibility_monitor.py --config ai_monitoring_config.json

REM Check if results were generated
if exist "ai_visibility_results.json" (
    echo Results file generated successfully
) else (
    echo Results file not generated
    exit /b 1
)

if exist "ai_visibility_report.md" (
    echo Report file generated successfully
) else (
    echo Report file not generated
    exit /b 1
)

echo.
echo === MONITORING SUMMARY ===
echo Check ai_visibility_results.json and ai_visibility_report.md for details
echo.
echo AI Visibility Monitor test completed successfully!
pause
