#!/usr/bin/env bash

if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    python3 -m venv venv
fi

pip install -r requirements.txt

export FLASK_APP=main.py
if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    export FLASK_APP=main.py; flask db init
fi

echo Generate migration DDL code...
flask db migrate

echo Run the DDL code and migrate...

echo This is the DDL code that will be run...
flask db upgrade

echo Generating test data...
source venv/bin/activate; python test_data.py