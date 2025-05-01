import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "pool_recycle": 1800,
}
# SQLALCHEMY_ENGINE_OPTIONS = {
#     "pool_pre_ping": True,
#     "pool_recycle": 1800,
#     "pool_size": 10,
#     "max_overflow": 20,
#     "pool_timeout": 30,
#     "poolclass": "QueuePool",
#     "pool_use_lifo": True,
#     "pool_logging_name": "my_pool",
#     "pool_logging_level": "DEBUG",
#     "pool_logging_format": "%(asctime)s - %(levelname)s - %(message)s",