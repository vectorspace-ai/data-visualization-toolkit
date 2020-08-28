from flask import Blueprint, render_template
from app.modules.jsonfiles.constants import DATASET

api = Blueprint(__name__, __name__, url_prefix='/')


@api.route('/',  methods=['GET'])
def index():
    return render_template('index.html', dataset=DATASET)