import dj_database_url as db_url
from decouple import config

from anion.settings.base import *  # noqa: F401, F403
from anion.settings.base import INSTALLED_APPS

# Secret key

SECRET_KEY = "secret-key-tests"


# Apps

INSTALLED_APPS += [
    "tests",
]


# Databases

DATABASES = {
    "postgres": db_url.parse(
        "postgres://postgres:postgres@localhost:5432/postgres"
    ),
}

DATABASES["default"] = DATABASES[config("DATABASE_ENGINE", default="postgres")]
