from flask import request
from flask import Blueprint
from flask import render_template
from os import path
import json
from app.modules.set_labels.set_labels import set_dataset
from app.modules.visualization_structure.scatterplot import ScatterPlot


api = Blueprint(__name__, __name__, url_prefix='/scatter_plot')

@api.route('/')
def graph_parameters():
    return render_template('scatterplot.html', dataset=json.loads(set_dataset()))

#@api.route('/', methods=['GET'])
@api.route('/plot', methods=['POST'])
def heatmap():
    dataset_dir = "data/datasets"
    dataset = request.form["dataset"]
    #dataset = "heatmap-realtime-pharmaprices-by-dateprices-0x923fcaB5b510C16c656312cFd503B83Fb1A0b2F4-matrix.csv"
    coords_with_clusters = ScatterPlot().get_visualization_request(path.join(dataset_dir, dataset))
    row_name = dataset.split('-')[2]
    col_name = dataset.split('-')[4]
    return render_template('result_scatter_plot.html', coords_with_clusters=coords_with_clusters, dataname=dataset,
                           row_name=row_name, col_name=col_name)