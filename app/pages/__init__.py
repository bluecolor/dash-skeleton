import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
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
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False, href='/'),
        navbar(),
        html.Div(id='page-content')
    ])


def init_app(app):
    set_layout(app)

    @app.callback(
        dash.dependencies.Output('page-content', 'children'),
        [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        page = registery.get(pathname.split("/")[2])()
        return page.render(app)
