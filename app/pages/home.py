import dash_html_components as html
from app.pages import Page


def render(self):
    return html.Div([ html.H3('Home') ])