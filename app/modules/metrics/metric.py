from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score


class UnsupervisedMetrics:
    """
    A class with metrics
    """
    def get_score(self, matrix, clusters):
        """
        :param matrix: correlation matrix
        :type list of lists
        :param clusters:
        :type list of ints
        :return: This function returns the mean Silhouette Coefficient over all samples
        """
        return silhouette_score(matrix, clusters)