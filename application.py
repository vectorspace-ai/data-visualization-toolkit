'''Main API'''
from os import path
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from jsonfiles.constants import DATASET
from modules.graph_network_processer import GraphNetwork

EMPTY_GRAPH = "empty_graph"

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html', dataset=DATASET)


@app.route('/visualize', methods=['POST'])
def visualize():
    dataset_dir="datasets"
    dataset=request.form['dataset']
    #transponse_flag=int(request.form['transponse_flag'])
    transponse_flag=0
    root_node = request.form['root_node']
    max_depth = int(request.form['max_depth'])
    branches  = int(request.form['branches'])
    nodes = int(request.form['nodes'])
    min_score  = float(request.form['min_score'])

    graph_network=GraphNetwork(root_node, max_depth, branches, nodes, min_score, transponse_flag, path.join(dataset_dir, dataset))
    graph=graph_network.pipeline()
    print(graph)

    if graph["data"]==EMPTY_GRAPH:
        return render_template('error.html')
    else:
        return render_template('result_graph.html', data=graph["data"], root_node=root_node, depth=graph["max_depth"], 
            branches=branches, found_nodes=graph["total_nodes"], min_score=min_score, file_name=dataset,
            time=graph["elapsed_time"])

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4000)
