from flask import Blueprint, render_template
import os

api = Blueprint(__name__, __name__, url_prefix='/')
PATH = os.path.join(os. getcwd(), "app")

@api.route('/',  methods=['GET'])
def index():	
	return render_template('index.html')

