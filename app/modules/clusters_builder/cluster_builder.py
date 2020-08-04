import hdbscan
from app.modules.clusters_builder.distances import distances
from app.modules.metrics.metric import UnsupervisedMetrics

class ClusterBuilder:
    def __init__(self):
        ...

    def get_best_clusters(self, matrix):
        best_metric = -1
        best_clusters = []
        for dist in distances.keys():
            hdbscan_clustering = hdbscan.HDBSCAN(min_cluster_size=10, metric=dist, min_samples=5,
                                                 allow_single_cluster=False)
            clustered = hdbscan_clustering.fit_predict(matrix)
            score = UnsupervisedMetrics.get_score(matrix, clustered)
            if score > best_metric:
                best_metric = score
                best_clusters = clustered.copy()
        return best_clusters


    def get_clusters(self, matrix):
        clusters = self.get_best_clusters(matrix)
        return clusters