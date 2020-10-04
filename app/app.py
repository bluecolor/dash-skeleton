import os
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from . import settings
from .dash import create_dash


class App(Flask):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(__name__, *args, **kwargs)
        # Make sure we get the right referral address even behind proxies like nginx.
        self.wsgi_app = ProxyFix(
            self.wsgi_app, x_for=settings.PROXIES_COUNT, x_host=1)
        # Configure App using our settings
        self.config.from_object("app.settings")

app = create_dash()

def create_app():
    server = App()
    server.title = settings.TITLE
    app.init_app(server)

    from . import pages, auth
    pages.register_pages()
    pages.init_app(app)

    # pages.init_app(app)
    # auth.init_app(dash)

    return server




