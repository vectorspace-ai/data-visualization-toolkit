from flask import Blueprint, request
api = Blueprint(__name__, __name__, url_prefix='/dataset')


@api.route('/', methods=['POST'])
def endpoint():
	dataset = request.files.get("dataset")
	return {}