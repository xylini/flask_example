@echo off

title Init

IF EXIST venv (
echo venv exists...
) ELSE (
echo Creating venv...
python -m venv venv
echo Venv installed...
)
call venv/Scripts/activate.bat

echo Installing requirements...
pip install -r requirements.txt
echo OK

set FLASK_APP=main.py
echo FLASK_APP variable set...

IF EXIST migrations (
echo migrations exists...
) ELSE (
echo Initiation of migrations folder...
flask db init
echo OK
)

echo Generate migration DDL code...
flask db migrate
echo OK

echo Run the DDL code and migrate...
echo This is the DDL code that will be run...
flask db upgrade
echo OK

echo Generating test fake data...
python test_data.py
echo COMPLETED. THAT'S ALL FOLKS.
echo ##############################
echo # NOW RUN: START_PROJECT.BAT #
echo ##############################
pause
