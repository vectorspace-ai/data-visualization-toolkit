from flask import Blueprint, request
from app.modules.visualization_structure.heatmap import HeatMap

api = Blueprint(__name__, __name__, url_prefix='/heatmap')

@api.route('/', methods=['GET'])
def heatmap_endpoint():
    return HeatMap.get_visualization_request(corr_matrix)