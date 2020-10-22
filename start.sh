#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]
then
	virtualenv dataset_toolkit_env

	source dataset_toolkit_env/bin/activate

	pip3 install -r requirements.txt
fi

DATADIR=data
if [ ! -d "$DATADIR" ]
then
	curl -L -o data.zip "https://drive.google.com/uc?export=download&id=13H6QkQ2_Rd4qesxgEsTcvr7FPW9CNrdu"
	unzip data.zip
	rm -f data.zip
fi

export FLASK_APP=app/application.py
export PYTHONPATH=$PYTHONPATH:$PWD
flask run
