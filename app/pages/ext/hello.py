import dash_html_components as html
from app.pages import Page, registery

class Hello(Page):

    @classmethod
    def render(cls):
        print("xxx")
        return html.Div([ html.H3('Hello') ])

registery.register(Hello)