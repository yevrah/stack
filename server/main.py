import importlib
import glob

from pathlib import Path
from os.path import dirname, basename, isfile, join
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from src.schemas.base import db
from src.schemas.user import User
from config import config

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = config["JWT_SECRET_KEY"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = config["JWT_EXPIRES_SECS"]
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = config["JWT_REFRESH_EXPIRES_SECS"]

jwt = JWTManager(app)
CORS(app, supports_credentials=True)

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
    return jsonify({"msg": "Not found", "status": 404}), 404


@app.errorhandler(500)
def page_bad(e):
    return jsonify({"msg": "Internal server error", "status": 500}), 500


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return identity


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
