class HeatMap:
    """
    Heatmap visualization class
    """
    def __init__(self):
        ...

    def create_data(self, corr_matrix):
        keywords = corr_matrix.index.tolist()
        contexts = corr_matrix.columns.tolist()
        data = []
        for i in keywords:
            cell = {}
            cell['keyword'] = i
            for j in contexts:
                cell[j] = round(corr_matrix[j][i], 2)
            data.append(cell)
        return data

    def create_body(self, corr_matrix):
        data = self.create_data(corr_matrix)
        contexts = corr_matrix.columns.tolist()
        body = {
            "width": 800,
            "height": 800,
            "data": data,
            "keys": contexts,
            "indexBy": "keyword",
            "margin": {
                "top": 100,
                "right": 60,
                "bottom": 30,
                "left": 60
            },
            "minValue": "auto",
            "maxValue": "auto",
            "forceSquare": True,
            "sizeVariation": 0,
            "padding": 0,
            "colors": "nivo",
            "axisTop": {
                "orient": "top",
                "tickSize": 5,
                "tickPadding": 5,
                "tickRotation": -55,
                "legend": "",
                "legendOffset": 36
            },
            "axisRight": None,
            "axisBottom": None,
            "axisLeft": {
                "orient": "left",
                "tickSize": 5,
                "tickPadding": 5,
                "tickRotation": 0,
                "legend": "keyword",
                "legendPosition": "middle",
                "legendOffset": -40
            },
            "enableGridX": False,
            "enableGridY": True,
            "cellShape": "rect",
            "cellOpacity": 1,
            "cellBorderWidth": 0
        }
        return body

    def get_visualization_request(self, corr_matrix):
        return self.create_body(corr_matrix)


