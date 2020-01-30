#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import signal
import sys
import hydra
from init_bigpipe import init_bigpie

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@hydra.main(config_path="../config/app_config.yaml")
def main(cfg):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigpipe_response_example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if os.environ.get('RUN_MAIN') == 'true':
        from data.app_instance import AppInstance
        init_bigpie(cfg.bigpipe)
        AppInstance.init(cfg.demo)  # Setup app instance

    execute_from_command_line(setup_django_params(cfg))
    # execute_from_command_line(sys.argv)


def setup_django_params(cfg):  # sys.argv is a list of string, django expect port to be a string.
    result = [str(cfg.django.params[i]) for i in range(len(cfg.django.params))]
    result.insert(0, __file__)  # set manage.py
    return result


def handle_kill(signum, frame):
    print('Signal terminate received will shutdown bigpipe')
    from bigpipe_response.bigpipe import Bigpipe
    Bigpipe.get().shutdown()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM , handle_kill)
    signal.signal(signal.SIGINT, handle_kill)
    main()
