from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user

from src.modules.auth import login_by_email, register_user

bl = Blueprint("auth", __name__)


@bl.post("/login")
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    if email is None and password is None:
        return jsonify({"msg": "Missing `email` or `password`", "status": 401}), 401

    user, error = login_by_email(email, password)

    if error:
        return jsonify({**error, "status": 401}), 401

    auth = user.pop("auth")

    return jsonify({"user": user, "auth_token": auth})


@bl.post("/register")
def register():
    email = request.json.get("email")
    password1 = request.json.get("password1")
    password2 = request.json.get("password2")

    if email is None and password1 is None:
        return jsonify({"msg": "Missing `email` or `password`", "status": 400}), 400

    if password1 != password2:
        return jsonify({"msg": "Passwords don't match", "status": 400}), 400

    user, error = register_user(email, password1)

    if error:
        return jsonify({**error, "status": 400}), 400

    auth = user.pop("auth")

    return jsonify({"user": user, "auth_token": auth})


@bl.get("/me")
@jwt_required()
def me():
    return jsonify({"user": {**current_user}})
