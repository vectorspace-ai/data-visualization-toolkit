from flask import Flask, render_template
from graph_network_processer import GraphNetwork

app = Flask(__name__)

@app.route('/')
def generate_cluster(name=None):

    #Load Dataset with inputs: node, dataset, transpose_flag
    root_node = "ABBV_sym"
    max_depth=3
    branches=3
    nodes=15
    min_score=0.001
    transpose_flag = 0
    dataset = 'dataset/pharma_pharma_dataset.csv'
    graph_network=GraphNetwork(root_node, max_depth, branches, nodes, min_score, transpose_flag, dataset)
    graph=graph_network.pipeline()
    #Extract Clusters
    print(graph["data"])
    #visualize that cluster on index.html
    return render_template('index.html', name=name)