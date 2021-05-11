import importlib
import glob
import redis

from pathlib import Path
from os.path import dirname, basename, isfile, join
from flask import Flask, jsonify
from flask_session import Session
from flask_cors import CORS

from src.schemas.base import db
from config import config

app = Flask(__name__)

app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = redis.from_url(config["REDIS_URL"])
Session(app)
CORS(app)

route_path = Path(dirname(__file__) + "/src/routes").resolve()
routes = [basename(f)[:-3] for f in glob.glob(join(route_path, "*.py")) if isfile(f)]

for route in routes:
    module = importlib.import_module(f"src.routes.{route}")
    app.register_blueprint(module.bl, url_prefix=f"/{route}")


@app.before_request
def open_connection():
    db.connect()


@app.teardown_request
def close_connection(exc):
    db.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found", "status": 404}), 404


@app.errorhandler(500)
def page_bad(e):
    return jsonify({"error": "Internal server error", "status": 500}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
