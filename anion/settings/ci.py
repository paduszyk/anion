import dj_database_url as db_url
from decouple import config

from .base import *  # noqa: F401, F403

# Secret key

SECRET_KEY = "secret-key-ci"


# Databases

DATABASES = {
    "postgres": db_url.parse(
        "postgres://postgres:postgres@localhost:5432/postgres"
    ),
}

DATABASES["default"] = DATABASES[config("DATABASE_ENGINE", default="postgres")]
