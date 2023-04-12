from monty.settings.common import *

import dj_database_url
import os

from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = "Set the {} environment variable".format(env_variable)
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_value("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["monty.artello.network"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

MAX_CONN_AGE = 600

DATABASES = {
    "default": dj_database_url.config(conn_max_age=MAX_CONN_AGE)
}
