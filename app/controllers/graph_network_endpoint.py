from flask import request
from flask import Blueprint
from flask import render_template
from os import path
import json
from app.modules.set_labels.set_labels import set_labels_from_file
from app.modules.graph_network_processer.graph_network_processer import GraphNetwork

api = Blueprint(__name__, __name__, url_prefix='/graph_network')

EMPTY_GRAPH = "empty_graph"


@api.route('/')
def graph_parameters():
    return render_template('graph_network.html', dataset=json.loads(set_labels_from_file()))
@api.route('/graph', methods=['POST'])
def graph_network():
    dataset_dir = "data/datasets"
    transponse_flag = 0
    labels = request.form["labels"]
    if labels == "columns":
        transponse_flag = 1

    dataset = request.form['dataset']
    # transponse_flag=int(request.form['transponse_flag'])
    root_node = request.form['root_node']
    max_depth = int(request.form['max_depth'])
    branches = int(request.form['branches'])
    nodes = int(request.form['nodes'])
    min_score = float(request.form['min_score'])

    graph_network = GraphNetwork(root_node, max_depth, branches, nodes, min_score, transponse_flag,
                                 path.join(dataset_dir, dataset))
    graph = graph_network.pipeline()
    # print(graph)

    if graph["data"] == EMPTY_GRAPH:
        return render_template('error.html')
    else:
        return render_template('result_graph.html', data=graph["data"], root_node=root_node, depth=graph["max_depth"],
                               branches=branches, found_nodes=graph["total_nodes"], min_score=min_score,
                               file_name=dataset, labels=labels, time=graph["elapsed_time"])
