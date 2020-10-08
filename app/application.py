import time
import flask
from app.controllers import dataset, scatter_plot_endpoint, main_page, graph_network_endpoint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(graph_network_endpoint.api)
app.register_blueprint(main_page.api)
app.register_blueprint(dataset.api)
app.register_blueprint(scatter_plot_endpoint.api)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4000)


