from monty.settings.common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c6rjn3^_qy%_eei8b(s_rm+xdg1#asbfr9a^#8199!&k!i&*ee"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "monty_dev",
        "USER": "zacksiri",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
