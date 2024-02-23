#!/usr/bin/python3
""" Flask App """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def CloseStorage(exception):
    """ close storage """
    storage.close()


@app.errorhandler(404)
def NotFound(error):
    """ 404 not found response """
    return jsonify({"error": "Not found"}), 404


host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")
if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
