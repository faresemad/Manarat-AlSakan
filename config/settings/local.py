from .base import *  # noqa
from .base import env  # noqa

SECRET_KEY = env.str("SECRET_KEY", default="django-insecure-u97!+%92@smvr8q(&mb^cjg49*ygcj_ko*+7faw+f42nk*8l8k")

DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOST", default=["localhost", "127.0.0.1"])
DATABASES = {"default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3")}
