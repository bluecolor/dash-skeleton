from flask_caching import Cache
from . import settings

cache = Cache()

def init_app(app):
    cache.init_app(app)
