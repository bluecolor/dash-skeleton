import os
from flask import Flask, request
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix

from . import settings
from .dash import create_dash
from app import models

class App(Flask):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(__name__, *args, **kwargs)
        # Make sure we get the right referral address even behind proxies like nginx.
        self.wsgi_app = ProxyFix(
            self.wsgi_app, x_for=settings.PROXIES_COUNT, x_host=1)
        # Configure App using our settings
        self.config.from_object("app.settings")


app = create_dash()
login_manager = LoginManager()

def create_app():
    server = App()
    server.title = settings.TITLE
    from .models import db
    from . import migrate, cache

    db.init_app(server)
    app.init_app(server)
    cache.init_app(server)
    migrate.init_app(server, db)

    login_manager.init_app(server)
    login_manager.login_view = '/login'

    from . import pages
    pages.register_pages()
    pages.init_app(app)

    return server

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return models.User.query.get(int(user_id.split("-")[0]))


