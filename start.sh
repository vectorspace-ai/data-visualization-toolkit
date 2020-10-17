#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]
then
	virtualenv dataset_toolkit_env

	source dataset_toolkit_env/bin/activate

	pip install -r requirements.txt
fi

DATADIR=data
if [ ! -d "$DATADIR" ]
then
	curl -L -o data.zip "https://drive.google.com/uc?export=download&id=10DyFcaWG-W7cswO95QuqoxlpEHVPT36y"
	unzip data.zip
	rm -f data.zip
fi

export FLASK_APP=app/application.py
export PYTHONPATH=$PYTHONPATH:$PWD
flask run
