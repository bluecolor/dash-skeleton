import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app.pages import registery


def render():
    return dbc.Row(
        dbc.Col(
            className="settings-permissions",
            children=[
            ],
            width={"size": 6, "offset": 3},
        )
    )
