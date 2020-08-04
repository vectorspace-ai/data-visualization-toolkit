import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# app.register_blueprint(_.api)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4000)


