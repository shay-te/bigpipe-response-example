#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import signal
import sys

from omegaconf import OmegaConf

from bigpipe_response.bigpipe import Bigpipe
from data.app_instance import AppInstance


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigpipe_response_example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    Bigpipe.init('../config/config_bigpipe.py')
    AppInstance.init(OmegaConf.load('../config/config_demo.yaml'))
    execute_from_command_line(sys.argv)


def handle_kill(signum, frame):
    print('Signal terminate received will shutdown bigpipe')
    Bigpipe.get().shutdown()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM , handle_kill)
    signal.signal(signal.SIGINT, handle_kill)
    main()
