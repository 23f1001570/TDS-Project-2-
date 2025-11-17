@echo off
REM Quick start script for Windows

echo ========================================
echo LLM Analysis Quiz - Quick Start
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo [WARNING] .env file not found!
    echo Please copy .env.example to .env and fill in your credentials.
    echo.
    pause
    exit /b 1
)

echo [1/3] Activating virtual environment...
call .venv\Scripts\activate.bat

echo [2/3] Checking dependencies...
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Dependencies not installed. Installing now...
    pip install -r requirements.txt
)

echo [3/3] Starting Flask server...
echo.
echo Server will start on http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

python app.py
