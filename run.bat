@echo off
set "APP_DIR=path to your app"
cd /d %APP_DIR%
start /min cmd /k "poetry run python main.py"