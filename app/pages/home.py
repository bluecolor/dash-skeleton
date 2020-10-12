import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app.pages import registery


def render():
    return dbc.Row(
        dbc.Col(
            className="home",
            children=[
                dbc.Row(
                    dbc.Col(
                        dcc.Link(
                            dbc.Card(
                                dbc.CardBody(
                                    children = [
                                        html.H4(page["name"]),
                                        html.P(
                                            page.get("description", ""),
                                            className="report-desc"
                                        )
                                    ]
                                ),
                                className="mb-3",
                            ),
                            href=f"{page['id']}",
                            className="card-report-link"
                        )
                    )
                )
                for page in sorted(registery.pages, key = lambda i: i['name'])
            ],
            width={"size": 6, "offset": 3},
        )
    )
