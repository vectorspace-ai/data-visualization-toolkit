from app.modules.set_labels.set_labels import set_labels_from_file
from flask import Blueprint, render_template
import json
import os

api = Blueprint(__name__, __name__, url_prefix='/')
PATH = os.path.join(os. getcwd(), "app")

@api.route('/',  methods=['GET'])
def index():
	DATASET = json.loads(set_labels_from_file())
	return render_template('index.html', dataset=DATASET)

