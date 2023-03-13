#!/usr/bin/env python
import os
import sys

from decouple import config

DJANGO_SETTINGS_MODULE = config(
    "DJANGO_SETTINGS_MODULE", "anion.settings.local"
)


def main():
    """
    Run administrative tasks.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django could not be imported.") from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
