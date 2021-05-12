import os
from dotenv import load_dotenv

load_dotenv()

config = {
    # TODO: Change secret key
    "JWT_SECRET_KEY": os.getenv(
        "JWT_SECRET_KEY", "\x98X\xfd\x8a\x87\xfb\xf7k\x11\xfe\xcb\xc1"
    ),
    "JWT_EXPIRES": os.getenv("JWT_EXPIRES", 3600),  # 1 hour
    "JWT_REFRESH_EXPIRES": os.getenv("JWT_REFRESH_EXPIRES", 2592000),  # 30 days
    # TODO: change default with your db
    "DB_NAME": os.getenv("DB_NAME", "stack"),
    "DB_HOST": os.getenv("DB_HOST", "localhost"),
    "DB_USER": os.getenv("DB_USER", "postgres"),
    "DB_PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
}
