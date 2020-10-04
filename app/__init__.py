from . import settings
from .app import create_app, app
from flask_migrate import Migrate

__version__ = "0.0.0-alpha"

migrate = Migrate()
