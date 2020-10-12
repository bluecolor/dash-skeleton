import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app.pages import registery


def render():
    return dbc.Row(
        dbc.Col(
            children=[
                dbc.Row(
                    dbc.Col(
                        dcc.Link(
                            dbc.Card(
                                dbc.CardBody(page["name"]),
                                className="mb-3",
                            ),
                            href=f"{page['id']}"
                        )
                    )
                )
                for page in registery.pages
            ],
            width={"size": 6, "offset": 3},
        )
    )
