import os, uuid
from dotenv import load_dotenv


load_dotenv()

config = {
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY", uuid.uuid4()),
    "JWT_EXPIRES": os.getenv("JWT_EXPIRES", 900),  # 15 mins
    "JWT_REFRESH_EXPIRES": os.getenv("JWT_REFRESH_EXPIRES", 604800),  # 7 days
    # TODO: change default with your db
    "DB_NAME": os.getenv("DB_NAME", "stack"),
    "DB_HOST": os.getenv("DB_HOST", "localhost"),
    "DB_USER": os.getenv("DB_USER", "postgres"),
    "DB_PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
    "REDIS_HOST": os.getenv("REDIS_HOST", "127.0.0.1"),
    "REDIS_PORT": os.getenv("REDIS_PORT", 6379),
}
