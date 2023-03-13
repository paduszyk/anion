import dj_database_url as db_url
from decouple import config

from .base import *  # noqa: F401, F403
from .base import INSTALLED_APPS, MIDDLEWARE

# Secret key

SECRET_KEY = "secret-key-local"


# Debugging

DEBUG = True


# Allowed hosts and internal IPs

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ["127.0.0.1"]


# Apps

INSTALLED_APPS += [
    "debug_toolbar",
]


# Middleware

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


# URLconf

ROOT_URLCONF = "anion.urls.local"


# Databases

DATABASES = {
    "postgres": db_url.parse(
        "postgres://postgres:postgres@localhost:5432/postgres"
    ),
}

DATABASES["default"] = DATABASES[config("DATABASE_ENGINE", default="postgres")]
