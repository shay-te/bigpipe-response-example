#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import signal
import sys

import hydra
from omegaconf import OmegaConf
from hydra.plugins.common.utils import HydraConfig

from bigpipe_response.bigpipe import Bigpipe
from data.app_instance import AppInstance


@hydra.main(config_path="../config/app_config.yaml")
def main(cfg):
# def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigpipe_response_example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


    # cfg = OmegaConf.load('../config/app_config.yaml')
    # OmegaConf.register_resolver('cwd')
    OmegaConf.register_resolver("_hydra", lambda path:HydraConfig().select("hydra." + path))
    Bigpipe.init(cfg.bigpipe)  # Setup bigpipe
    AppInstance.init(cfg.demo)  # Setup app instance

    # execute_from_command_line(setup_django_params(cfg))
    execute_from_command_line(sys.argv)



def setup_django_params(cfg):
    cfg.django.params.insert(0, __file__)  # set manage.py
    cfg.django.params[2] = str(cfg.django.params[2])  # django expect port to be a string
    return cfg.django.params


def handle_kill(signum, frame):
    print('Signal terminate received will shutdown bigpipe')
    Bigpipe.get().shutdown()
    sys.exit(0)


if __name__ == '__main__':
    # hydra.verbose=true
    signal.signal(signal.SIGTERM, handle_kill)
    signal.signal(signal.SIGINT, handle_kill)
    main()
