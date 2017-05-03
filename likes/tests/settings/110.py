import os


USE_TZ = True

TIME_ZONE = "Africa/Johannesburg"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "skeleton.db", # Or path to database file if using sqlite3.
        "USER": "skeleton", # Not used with sqlite3.
        "PASSWORD": "skeleton", # Not used with sqlite3.
        "HOST": "", # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "", # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS = (
    "likes.tests",
    "likes",
    "secretballot",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
)

ROOT_URLCONF = "likes.urls"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "likes.middleware.SecretBallotUserIpUseragentMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.template.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]

STATIC_URL = "/static/"

SECRET_KEY = "SECRET_KEY"

DEBUG = True
