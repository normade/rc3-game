"""Django settings for production"""
import dj_database_url
from project.settings.base import *

DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    ".herokuapp.com",
]

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES["default"].update(db_from_env)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
