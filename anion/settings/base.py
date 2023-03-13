from pathlib import Path

# Paths

PROJECT_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = PROJECT_DIR.parent


# Apps

INSTALLED_APPS = [
    "anion.contrib.authentication",
    "anion.contrib.evaluation",
    "anion.contrib.output",
    "anion.contrib.staff",
    "anion.contrib.units",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


# Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# URLconf

ROOT_URLCONF = "anion.urls.base"


# Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Internationalization

USE_TZ = True

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

LANGUAGES = [
    ("en", "English"),
    ("pl", "polski"),
]

LOCALE_PATHS = [
    PROJECT_DIR / "locale",
]


# Static files

STATIC_URL = "static/"

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# Media files

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
