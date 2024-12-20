@echo off
color 0A

title Discord DMall

echo Checking for required Python modules...
pip show discord.py >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing discord.py...
    pip install discord.py
)

pip show colorama >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing colorama...
    pip install colorama
)

echo Starting the tool...
python main.py