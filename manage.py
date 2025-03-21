from os import environ
from sys import argv

if __name__ == "__main__":
    environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project_conf.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(argv)
