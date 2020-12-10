import logging
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_login import logout_user, current_user

from app.settings import BRAND
from .registery import Registery

logger = logging.getLogger("pages.pages")

registery = Registery()


def register_pages():
    black_list = ['__pycache__']
    for f in os.listdir("app/pages/ext"):
        if os.path.isdir(f"app/pages/ext/{f}") and f not in black_list:
            if os.path.exists(f"app/pages/ext/{f}/app.py"):
                __import__(f"app.pages.ext.{f}.app")
            else:
                logger.warning(f"No app.py exists under {f}")


def set_layout(app):
    from .components import navbar

    def serve_layout():
        if current_user and current_user.is_authenticated:
            return html.Div([
                dcc.Location(id='url', refresh=False, href='/'),
                navbar(registery),
                dcc.Loading(
                    id="loading-1",
                    children=[
                        html.Div(id='page-content')
                    ],
                    type="circle",
                )
            ])
        else:
            return html.Div([
                dcc.Location(id='url', refresh=False, href='/'),
                dcc.Loading(
                    id="loading-1",
                    children=[html.Div(id='page-content')],
                    type="circle",
                )
            ])

    app.layout = serve_layout


def init_app(app):
    set_layout(app)

    from .auth import login, change_pass, unauthorized
    from . import home, profile

    @app.callback(
        dash.dependencies.Output('page-content', 'children'),
        [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):

        logger.info("Page %s User %s", pathname, current_user)

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

        page = registery.get(pathname.split("/")[1])

        if not current_user.is_authenticated:
            return login.render()

        # check if there is a match in groups
        page_groups = set([g.lower() for g in page.get('groups', [])])
        user_groups = set([g.lower() for g in current_user.groups.split("`")])
        if len(page_groups.intersection(user_groups)) > 0:
            return page["render"]()

        if '$admin$' in user_groups:
            return page["render"]()
        else:
            return unauthorized.render()
