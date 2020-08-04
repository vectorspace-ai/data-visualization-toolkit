from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score


class UnsupervisedMetrics:
    def __init__(self):
        ...
    def get_score(self, matrix, clusters):
        return silhouette_score(matrix, clusters)