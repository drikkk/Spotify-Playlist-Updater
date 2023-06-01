@echo off
set PYTHON_SCRIPT=Main.py
set SCRIPT_PATH=%~dp0

cd /d "%SCRIPT_PATH%\..\.."

pip install -r "%SCRIPT_PATH%\requirements.txt"
python.exe "%PYTHON_SCRIPT%"
