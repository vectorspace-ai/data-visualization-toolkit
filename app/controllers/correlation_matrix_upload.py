from flask import Blueprint, request
from app.modules.correlation_matrix.correlationmatrix import CorrelationMatrix

api = Blueprint(__name__, __name__, url_prefix='/correlationmatrix')

@api.route('/', methods=['POST'])
def correlationmatrix_endpoint():
    corr_matrix = request.files.get("correlationmatrix")
    print(corr_matrix)
    if corr_matrix:
        cm = CorrelationMatrix(corr_matrix)

