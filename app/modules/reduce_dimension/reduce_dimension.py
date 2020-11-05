from sklearn.manifold import TSNE

class DimensionalReducing:
    """
    Class to visualize high-dimensional data
    """

    def get_xy(self, matrix):
        """
        :param matrix:
        :type list of lists
        :return: x-coordinate, y-coordinate
        :rtype: tuple
        """
        tsne = TSNE(n_components=2)
        tsne_result = tsne.fit_transform(matrix)
        return tsne_result.tolist()