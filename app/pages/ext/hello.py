import dash_html_components as html
from app.pages import Page, registery

class Hello(Page):
    def render(self, app):
        return html.Div([ html.H3('Hello') ])

registery.register(Hello)