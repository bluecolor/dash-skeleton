from dash import Dash
import dash_bootstrap_components as dbc


def create_dash():
    app = Dash(__name__, server=False, url_base_pathname='/',
               external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.config.suppress_callback_exceptions = True

    return app
