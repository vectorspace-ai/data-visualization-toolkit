from flask import request
from flask import Blueprint
from flask import render_template
from os import path
from app.modules.graph_network_processer.graph_network_processer import GraphNetwork
from app.modules.models.word2vec import Word2Vec
from app.modules.correlation_matrix.correlationmatrix import CorrelationMatrix
from app.modules.utils import *

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

MOCK_PATH = 'data/models/word2vec/'
MOCK_MODEL_NAME = 'base_model.model'
MOCK_WORD2VEC = Word2Vec(path_to_model=MOCK_PATH, model_filename=MOCK_MODEL_NAME,
                         model_type='Word2Vec', embeddings_shape=300)
MOCK_WORD2VEC.load_model()
MOCK_ROWS = read_file_to_lst('data/columns/pharma_symbols.txt')
MOCK_COLUMNS = read_file_to_lst('data/rows/pharma_symbols.txt')
MOCK_DISTANCE = 'pearson'


def create_correlation_matrix():
    corr_matrix_object = CorrelationMatrix(MOCK_WORD2VEC, MOCK_ROWS, MOCK_COLUMNS, [])
    corr_matrix_object.context_controlled_filtering()
    gen = corr_matrix_object.generate_matrix(MOCK_DISTANCE)
    mock_path_dataset = 'data/datasets/'
    filename = 'correlation_matrix_pharm_real_time'
    corr_matrix_object.save_dataset(mock_path_dataset, filename)
    return corr_matrix_object.path_to_dataset




@api.route('/', methods=['POST'])
def graph_network():
    #TODO upload rows and columns and create corr matrix then make graph visualization
    #dataset_dir = "data/datasets"
    dataset = request.form['dataset']
    # transponse_flag=int(request.form['transponse_flag'])

    MOCK_PATH_DATASET = create_correlation_matrix()
    transponse_flag = 0
    root_node = request.form['root_node']
    max_depth = int(request.form['max_depth'])
    branches = int(request.form['branches'])
    nodes = int(request.form['nodes'])
    min_score = float(request.form['min_score'])

    graph_network = GraphNetwork(root_node, max_depth, branches, nodes, min_score, transponse_flag,
                                 MOCK_PATH_DATASET)
    graph = graph_network.pipeline()
    # print(graph)

    if graph["data"] == EMPTY_GRAPH:
        return render_template('error.html')
    else:
        return render_template('result_graph.html', data=graph["data"], root_node=root_node, depth=graph["max_depth"],
                               branches=branches, found_nodes=graph["total_nodes"], min_score=min_score,
                               file_name=MOCK_PATH_DATASET,
                               time=graph["elapsed_time"])
