import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'likes.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'secretballot',
    'likes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'likes.middleware.SecretBallotUserIpUseragentMiddleware',
)

CELERY_ALWAYS_EAGER = True
CELERY_IMPORTS = ('likes.tasks', )
