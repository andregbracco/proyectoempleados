from .base import *
import dj_database_url
import django_heroku

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

django_heroku.settings(locals())