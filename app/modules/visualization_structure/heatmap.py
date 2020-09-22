from app.modules.datasets.get_labels import *
import pandas as pd


class HeatMap:
    """
    Heatmap visualization class
    """

    def get_rows_columns(self, path):
        columns = get_columns(path)
        rows = get_rows(path)
        return columns, rows

    def create_body(self, path):
        data = []
        corr_matrix = pd.read_csv(path)
        for r_ind, values in enumerate(corr_matrix.values.tolist()):
            for c_ind, v in enumerate(values[1:]):
                data.append([c_ind, r_ind, round(v, 2)])
        return data

    def get_visualization_request(self, path):
        rows, columns = self.get_rows_columns(path)
        return rows, columns, self.create_body(path)


