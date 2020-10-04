from dash import Dash
import dash_bootstrap_components as dbc


def create_dash():
    app = Dash(__name__, server=False, url_base_pathname='/app/',
               external_stylesheets=[dbc.themes.BOOTSTRAP])
    return app
