@echo off
REM Change to the WSGI server directory
cd /d "%~dp0"

REM Activate virtual environment (if using one)
REM call venv\Scripts\activate

REM Start the Flask WSGI server
echo Starting Flask WSGI server...
python wsgi.py

REM Prevent the window from closing immediately after the server stops
pause
