from flask import request
from flask import Blueprint
from modules.inputfillings.inputfillings import InputFillings

api = Blueprint(__name__, __name__, url_prefix='/endpoints')





@api.route('/', methods=['POST'])
def endpoint():
	dataset = request.files.get("dataset")
	return {}