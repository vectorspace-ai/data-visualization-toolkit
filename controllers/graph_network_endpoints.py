from flask import jsonify
from flask import request
#from flask import Blueprint
from flask import render_template
from jsonfiles.constants import DATASET
from modules.graph_network_processer import GraphNetwork

api = Blueprint(__name__, __name__, url_prefix='/app')

EMPTY_GRAPH = "empty_graph"


@api.route('/')
def index():
    return render_template('index.html', dataset=DATASET)


@api.route('/visualize', methods=['POST'])
def visualize():
    dataset=request.form['dataset']
    transponse_flag=int(request.form['transponse_flag'])
    root_node = request.form['root_node']
    transponse_flag=int(request.form['transponse_flag'])
    max_depth = int(request.form['max_depth'])
    branches  = int(request.form['branches'])
    nodes = int(request.form['nodes'])
    min_score  = float(request.form['min_score'])

    graph_network=GraphNetwork(root_node, max_depth, branches, nodes, min_score, transponse_flag, dataset)
    graph=graph_network.pipeline()

    if graph["data"]==EMPTY_GRAPH:
        return render_template('error.html')
    else:
        return render_template('result_graph.html', data=graph["data"], root_node=root_node, depth=graph["max_depth"], 
            branches=branches, found_nodes=graph["total_nodes"], min_score=min_score, file_name=dataset.filename, 
            time=graph["elapsed_time"])