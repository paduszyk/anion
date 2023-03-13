#!/usr/bin/env python

import os
import sys

from django.core.management import execute_from_command_line


def main():
    """
    Run tests.
    """
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    execute_from_command_line(["manage.py", "test", *sys.argv[1:]])


if __name__ == "__main__":
    main()
