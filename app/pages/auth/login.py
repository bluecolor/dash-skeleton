from logging import PlaceHolder
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import no_update
from dash.dependencies import Input,Output,State
from flask_login import login_user

from app import app, models


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
            [
                dcc.Location(id='login-url', refresh=True, pathname='/login'),
                html.Div(id='login-trigger', style=dict(display='none')),
                html.Div(id='login-alert'),
                dbc.FormGroup(
                    [
                        dbc.Label("Login", className="login-title mb-5"),

                        dbc.Input(id='login-email', autoFocus=True, placeholder="Email"),
                        html.Br(),
                        dbc.Input(id='login-password', type='password', placeholder="Password"),


                        html.Br(),
                        dbc.Button('Submit', color='primary',block=True, id='login-button'),
                        html.Br(),
                        dcc.Link('Register', href='/register'),
                        html.Br(),
                        dcc.Link('Forgot Password', href='/forgot')
                    ]
                )
            ],
            width={"size": 4, "offset": 4},
        )
    )


@app.callback(
    [Output('login-url', 'pathname'),
     Output('login-alert', 'children')],
    [Input('login-button', 'n_clicks')],
    [State('login-email', 'value'),
     State('login-password', 'value')]
)
def login_success(n_clicks, email, password):

    if n_clicks > 0:
        user = models.User.find_by_email(email=email).first()

        if user and user.verify_password(password):
            login_user(user)
            return '/home', success_alert
        else:
            return no_update,failure_alert
    else:
        return no_update,''


