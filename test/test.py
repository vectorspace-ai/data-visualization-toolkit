from graph_network_processer import GraphNetwork


#dataset="dataset-demo-02.tsv"
#dataset="dataset_large.tsv"

dataset="dataset-demo-01-cc-artificial-intelligence.tsv"

transponse_flag=0
root_node = "GNW"
max_depth = 4
branches  = 4
nodes = 50
min_score  = 0.0001


graph_network=GraphNetwork(root_node, max_depth, branches, nodes, min_score, transponse_flag, dataset)
graph=graph_network.pipeline()
print(graph)