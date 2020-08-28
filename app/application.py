import flask
from app.controllers import graph_network_endpoints
from app.controllers import main_page
from app.controllers import dataset

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(graph_network_endpoints.api)
app.register_blueprint(main_page.api)
app.register_blueprint(dataset.api)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4000)


