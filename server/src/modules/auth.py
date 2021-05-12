from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity

from src.schemas.user import User


def login_by_email(email, password):
    user = User.get_by_email(email)

    if user is None:
        return None, {
            "msg": "Oops! Your email and password don't match. Please check again."
        }

    if check_password_hash(user["password"], password) is False:
        return None, {
            "msg": "Oops! Your email and password don't match. Please check again."
        }

    user["auth"] = create_access_token(identity=user)

    del user["password"]

    return user, None


def register_user(email, password):
    user, error = User.insert_eh(
        {"email": email, "password": generate_password_hash(password)}
    )

    if user is not None:
        del user["password"]

    user["auth"] = create_access_token(identity=user["email"])

    return user, error
