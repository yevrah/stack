from flask import Blueprint, jsonify, request

from src.modules.auth import login_by_email, register_user, logout_user, protected

bl = Blueprint("auth", __name__)


@bl.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    if email is None and password is None:
        return jsonify({"error": "Missing `email` or `password`", "status": 401}), 401

    user, error = login_by_email(email, password)

    if error:
        return jsonify({**error, "status": 401}), 401

    return jsonify({"user": user})


@bl.route("/register", methods=["POST"])
def register():
    email = request.json.get("email")
    password1 = request.json.get("password1")
    password2 = request.json.get("password2")

    if email is None and password1 is None:
        return jsonify({"error": "Missing `email` or `password`", "status": 400}), 400

    if password1 != password2:
        return jsonify({"error": "Passwords don't match", "status": 400}), 400

    user, error = register_user(email, password1)

    if error:
        return jsonify({**error, "status": 400}), 400

    return jsonify({"user": user})


@bl.route("/logout", methods=["GET"])
@protected()
def logout():
    success, _ = logout_user()
    return jsonify({"success": success})


@bl.route("/valid", methods=["GET"])
@protected()
def valid():
    return jsonify({"success": True})
