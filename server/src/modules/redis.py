import redis
from config import config

red = redis.StrictRedis(
    host=config["REDIS_HOST"], port=config["REDIS_PORT"], db=0, decode_responses=True
)
