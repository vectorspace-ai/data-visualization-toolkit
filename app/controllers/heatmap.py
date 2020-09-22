from flask import request
from flask import Blueprint
from flask import render_template
from os import path
from app.modules.visualization_structure.heatmap import HeatMap

api = Blueprint(__name__, __name__, url_prefix='/heatmap')


@api.route('/', methods=['GET'])
def heatmap():
    dataset_dir = "data/datasets"
    # dataset = request.form['dataset']
    dataset = 'small_test.csv'
    columns, rows, data = HeatMap().get_visualization_request(path.join(dataset_dir, dataset))
    return render_template('heatmap.html', data=data, rows=rows, columns=columns)
