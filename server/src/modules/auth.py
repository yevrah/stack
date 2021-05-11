import copy

from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, jsonify

from src.schemas.user import User


def login_by_email(email, password):
    user = User.get_by_email(email)

    if user is None:
        return None, {
            "error": "Oops! Your email and password don't match. Please check again."
        }

    if check_password_hash(user["password"], password) is False:
        return None, {
            "error": "Oops! Your email and password don't match. Please check again."
        }

    session["user"] = copy.deepcopy(user)
    del user["password"]

    return user, None


def register_user(email, password):
    user, error = User.insert_eh(
        {"email": email, "password": generate_password_hash(password)}
    )

    if user is not None:
        session["user"] = copy.deepcopy(user)
        del user["password"]

    return user, error


def logout_user():
    if "user" in session:
        session.pop("user")

    return True, None


def protected():
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            user = session.get("user")

            if user is None:
                return jsonify({"error": "Unauthorized", "status": 403}), 403

            return func(*args, **kwargs)

        return decorated_view

    return decorator
