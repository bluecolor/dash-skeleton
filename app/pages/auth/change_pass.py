from logging import disable
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import no_update
from dash.dependencies import Input, Output, State
from flask_login import current_user

from app import app, models


success_alert = dbc.Alert(
    'Password changed',
    color='success',
    dismissable=True
)
failure_alert = dbc.Alert(
    'Failed to verify current password',
    color='danger',
    dismissable=True
)


def render():
    return dbc.Row(
        dbc.Col(
            [
                dcc.Location(id='change-password-url', refresh=True),
                html.Div(id='change-password-trigger',
                         style=dict(display='none')),
                dbc.FormGroup(
                    [
                        dbc.Label("Change Password",
                                  className="change-password-title mb-5"),

                        html.Div(id='change-password-alert'),

                        dbc.Input(id='current-password', type='password',
                                  placeholder="Current password"),
                        html.Br(),
                        dbc.Input(id='new-password', type='password',
                                  placeholder="New password"),

                        html.Br(),
                        dbc.Button('Submit', color='primary',
                                   block=True, id='change-password-button', disabled=True),
                        html.Br()
                    ]
                )
            ],
            width={"size": 4, "offset": 4},
        )
    )



@app.callback(
    [Output('current-password','invalid'),
     Output('new-password','invalid'),
     Output('change-password-button','disabled')],
    [Input('current-password','value'),
     Input('new-password','value')]
)
def validate(current_password, new_password):
    current_invalid = False
    new_invalid = True
    disabled = True

    black_list = [None, '']

    current_invalid = current_password in black_list
    new_invalid = new_password in black_list
    disabled = current_invalid or new_invalid

    return (
        current_invalid,
        new_invalid,
        disabled
    )

@app.callback(
    [Output('change-password-alert', 'children'),
     Output('change-password-url', 'pathname'), ],

    [Input('change-password-button', 'n_clicks')],
    [State('current-password', 'value'),
     State('new-password', 'value')]
)
def change_password(n_clicks, current_password, new_password):

    if n_clicks > 0:
        user = models.User.find_by_email(email=current_user.email).first()

        if user and user.verify_password(current_password):
            user.hash_password(new_password)
            models.db.session.commit()
            return success_alert, no_update
        else:
            return failure_alert, no_update
    else:
        return '', no_update
