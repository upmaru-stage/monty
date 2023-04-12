import os
import sys

import django

import gunicorn.app.wsgiapp as wsgi
from django.core import management


def run():
    # setup django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monty.settings.development")
    django.setup()

    match sys.argv[1]:
        case "web":
            # This is just a simple way to supply args to gunicorn
            sys.argv = [".", "monty.wsgi", "--bind=0.0.0.0:8000", "-p tmp/server.pid"]

            wsgi.run()
        case "migrate":
            management.call_command("migrate")
        case _:
            sys.stdout.write("please pass in a valid command [web, migrate]")


if __name__ == "__main__":
    run()
