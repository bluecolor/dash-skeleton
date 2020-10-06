import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_login import logout_user, current_user

from app.settings import BRAND
from .registery import Registery
from .base import Page

registery = Registery()


def register_pages():
    for f in os.listdir("app/pages/ext"):
        if os.path.isfile(f"app/pages/ext/{f}") and ".".join(f.split(".")[-1:]) == "py":
            name = ".".join(f.split(".")[:-1])
            __import__(f"app.pages.ext.{name}")


def set_layout(app):
    from .components import navbar

    def serve_layout():
        if current_user and current_user.is_authenticated:
            return html.Div([
                dcc.Location(id='url', refresh=False, href='/'),
                navbar(registery),
                html.Div(id='page-content')
            ])
        else:
            return html.Div([
                dcc.Location(id='url', refresh=False, href='/'),
                html.Div(id='page-content')
            ])

    app.layout = serve_layout


def init_app(app):
    set_layout(app)

    from .auth import login, change_pass
    from . import home, profile

    @app.callback(
        dash.dependencies.Output('page-content', 'children'),
        [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):

        if not pathname:
            return

        if not current_user or not current_user.is_authenticated:
            return login.render()

        if pathname == '/login':
            if not current_user.is_authenticated:
                return login.render()

        if pathname == '/logout':
            logout_user()
            return login.render()

        if pathname == '/home' or pathname == "/" or not pathname:
            return home.render()

        if pathname == '/change-password':
            return change_pass.render()

        if pathname == '/profile':
            return profile.render()

        page = registery.get(pathname.split("/")[1])()

        if current_user.is_authenticated:
            return page.render(app)

        return login.render()


