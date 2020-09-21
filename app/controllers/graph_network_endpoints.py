from flask import request
from flask import Blueprint
from flask import render_template
from os import path
from app.modules.graph_network_processer.graph_network_processer import GraphNetwork

api = Blueprint(__name__, __name__, url_prefix='/graph_network')

EMPTY_GRAPH = "empty_graph"


# @api.route('/visualize', methods=['POST'])
# def visualize():
#     dataset=request.form['dataset']
#     transponse_flag=int(request.form['transponse_flag'])
#     root_node = request.form['root_node']
#     transponse_flag=int(request.form['transponse_flag'])
#     max_depth = int(request.form['max_depth'])
#     branches  = int(request.form['branches'])
#     nodes = int(request.form['nodes'])
#     min_score  = float(request.form['min_score'])
#
#     graph_network=GraphNetwork(root_node, max_depth, branches, nodes, min_score, transponse_flag, dataset)
#     graph=graph_network.pipeline()
#
#     if graph["data"]==EMPTY_GRAPH:
#         return render_template('error.html')
#     else:
#         return render_template('result_graph.html', data=graph["data"], root_node=root_node, depth=graph["max_depth"],
#             branches=branches, found_nodes=graph["total_nodes"], min_score=min_score, file_name=dataset.filename,
#             time=graph["elapsed_time"])

@api.route('/', methods=['POST'])
def graph_network():
    dataset_dir = "data/datasets"

    dataset = request.form['dataset']
    print(path.join(dataset_dir, dataset))
    # transponse_flag=int(request.form['transponse_flag'])
    transponse_flag = 0
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
                               file_name=dataset,
                               time=graph["elapsed_time"])
