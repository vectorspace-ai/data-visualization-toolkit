from sklearn.manifold import TSNE

class DimensionalReducing:
    def __init__(self):
        ...

    def get_xy(self, matrix):
        tsne = TSNE(n_components=2)
        tsne_result = tsne.fit_transform(matrix)
        return tsne_result[:, 0], tsne_result[:, 1]