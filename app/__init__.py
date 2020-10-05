import os
import logging
import sys

from . import settings
from .app import create_app, app
from flask_migrate import Migrate

__version__ = "0.0.0-alpha"

migrate = Migrate()

if os.environ.get("REMOTE_DEBUG"):
    import ptvsd

    ptvsd.enable_attach(address=("0.0.0.0", 5678))

def setup_logging():
    handler = logging.StreamHandler(sys.stdout if settings.LOG_STDOUT else sys.stderr)
    formatter = logging.Formatter(settings.LOG_FORMAT)
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(settings.LOG_LEVEL)

    # Make noisy libraries less noisy
    if settings.LOG_LEVEL != "DEBUG":
        for name in [
            "passlib",
        ]:
            logging.getLogger(name).setLevel("ERROR")


setup_logging()
