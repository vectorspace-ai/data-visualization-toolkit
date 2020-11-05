from app.modules.reduce_dimension.reduce_dimension import DimensionalReducing
import pandas as pd
from app.modules.clusters_builder.cluster_builder import ClusterBuilder

class ScatterPlot:
    """
     ScatterPlot visualization class
     """
    def __init__(self):
        ...

    def get_visualization_request(self, filepath):
        corr_matrix = pd.read_csv(filepath, index_col='SYMBOL').values.tolist()
        coords = DimensionalReducing().get_xy(corr_matrix)
        clusters = ClusterBuilder().get_clusters(corr_matrix)
        list_of_clusters = {}
        for i, v in enumerate(clusters):
            if str(v) not in list_of_clusters.keys():
                list_of_clusters[str(v)] = []
            list_of_clusters[str(v)].append(coords[i])
        return list_of_clusters

