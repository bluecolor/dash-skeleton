import dash_html_components as html
from app.pages import Page, registery

class Bye(Page):
    def render(self, dash):
        return html.Div([ html.H3('Bye') ])

registery.register(Bye)