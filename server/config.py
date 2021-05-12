import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY", "\x98X\xfd\x8a\x87\xfb\xf7k\x11\xfe\xcb\xc1"),
    "JWT_EXPIRES_SECS": os.getenv("JWT_EXPIRES_SECS", 259200),
    "REDIS_URL": os.getenv("REDIS_URL", "redis://127.0.0.1:6379"),
    # TODO: change default with your db
    "DB_NAME": os.getenv("DB_NAME", "stack"),
    "DB_HOST": os.getenv("DB_HOST", "localhost"),
    "DB_USER": os.getenv("DB_USER", "postgres"),
    "DB_PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
}
