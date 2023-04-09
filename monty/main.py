import os
import sys

import django

import gunicorn.app.wsgiapp as wsgi
from django.core import management

def run():
    # setup django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monty.settings.development")
    django.setup()

    try:
        production = sys.argv[1] == "production"
    except IndexError:
        production = False

    if production:
        # This is just a simple way to supply args to gunicorn
        sys.argv = [".", "monty.wsgi", "--bind=0.0.0.0:8000"]

        wsgi.run()
    else:
        management.call_command("migrate")


if __name__ == "__main__":
    run()
