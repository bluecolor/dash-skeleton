from logging import PlaceHolder
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import no_update
from dash.dependencies import Input, Output, State
from flask_login import login_user

from app import app, models, settings
from app.utils import ldap

success_alert = dbc.Alert(
    'Logged in successfully. Taking you home!',
    color='success',
    dismissable=True
)
failure_alert = dbc.Alert(
    'Login unsuccessful. Try again.',
    color='danger',
    dismissable=True
)
already_login_alert = dbc.Alert(
    'User already logged in. Taking you home!',
    color='warning',
    dismissable=True
)


def render():
    return dbc.Row(
        dbc.Col(
            id="login-container",
            children=[
                html.Div(
                    id="form-container",
                    children=[
                        dcc.Location(id='login-url', refresh=True,
                                     pathname='/login'),
                        html.Div(id='login-trigger',
                                 style=dict(display='none')),
                        html.Div(id='login-alert'),
                        dbc.FormGroup(
                            [
                                dbc.Label(
                                    "Login", className="login-title mb-5"),

                                dbc.Input(id='login-username',
                                          autoFocus=True, placeholder="Username"),
                                html.Br(),
                                dbc.Input(
                                    id='login-password', type='password', placeholder="Password"),
                                html.Br(),
                                dbc.Button('Login', color='primary',
                                           block=True, id='login-button'),
                            ]
                        )
                    ])
            ],
            width={"size": 4, "offset": 4},
        )
    )


@app.callback(
    [
        Output('login-url', 'pathname'),
        Output('login-alert', 'children')
    ],
    [
        Input('login-button', 'n_clicks'),
        Input('login-password', 'n_submit')
    ],
    [
        State('login-username', 'value'),
        State('login-password', 'value')
    ]
)
def login_success(n_clicks, n_submit, username, password):

    if (n_submit and n_submit > 0) or (n_clicks and n_clicks > 0):

        if settings.AUTH_METHOD == 'db':
            user = models.User.find_by_username(username).first()
            if user and user.verify_password(password):
                login_user(user)
                return '/home', success_alert
            else:
                return no_update, failure_alert
        elif settings.AUTH_METHOD == 'ldap':
            user = ldap.auth_user(username, password)
            if user:
                login_user(user)
                return '/home', success_alert
            else:
                return no_update, failure_alert
        else:
            raise ValueError("Unsupported login method: " + settings.AUTH_METHOD)

    else:
        return no_update, ''
