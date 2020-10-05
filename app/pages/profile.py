from logging import disable
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import no_update
from dash.dependencies import Input, Output, State
from flask_login import current_user

from app import app, models


success_alert = dbc.Alert(
    'Profile changed',
    color='success',
    dismissable=True
)
failure_alert = dbc.Alert(
    'Failed to change profile',
    color='danger',
    dismissable=True
)


def render():
    return dbc.Row(
        dbc.Col(
            [
                dcc.Location(id='profile-url', refresh=True),
                html.Div(id='profile-trigger', style=dict(display='none')),

                dbc.FormGroup(
                    [
                        dbc.Label("Profile", className="profile-title mb-5"),

                        html.Div(id='profile-alert'),

                        dbc.Input(id='name-input', placeholder="Name"),
                        html.Br(),
                        dbc.Input(id='email-input', placeholder="Email", disabled=True),

                        html.Br(),
                        dbc.Button('Submit', color='primary',
                                   block=True, id='profile-button', disabled=False),
                        html.Br()
                    ]
                )
            ],
            width={"size": 4, "offset": 4},
        )
    )


@app.callback(
    [
        Output('name-input', 'value'),
        Output('email-input', 'value')
    ],
    [Input('profile-trigger', 'children')]
)
def profile_values(trigger):
    if current_user.is_authenticated:
        return (
            current_user.name,
            current_user.email
        )


@app.callback(
    [
        Output('name-input', 'invalid'),
        Output('profile-button', 'disabled')
    ],
    [Input('name-input', 'value')]
)
def validate(name):
    name_invalid = False
    disabled = False

    name_invalid = name in ['', None]
    disabled = name_invalid

    return (
        name_invalid,
        disabled
    )


@app.callback(
    [Output('profile-alert', 'children'),
     Output('profile-url', 'pathname'), ],

    [Input('profile-button', 'n_clicks')],
    [State('name-input', 'value')]
)
def submit(n_clicks, name):
    if n_clicks > 0:
        user = models.User.find_by_email(email=current_user.email).first()

        if user:
            user.name = name
            models.db.session.commit()
            return success_alert, no_update
        else:
            return failure_alert, no_update
    else:
        return '', no_update