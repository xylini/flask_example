@echo off
call venv\Scripts\activate.bat
set FLASK_APP=main.py
set FLASK_ENV=development
flask run