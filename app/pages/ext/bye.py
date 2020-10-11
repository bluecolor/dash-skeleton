import dash_html_components as html
from app.pages import Page, registery
from app.cache import cache

class Bye(Page):

    @classmethod
    @cache.memoize(10)
    def render(cls):
        import random
        import time
        time.sleep(4)
        return html.Div([ html.H3('Bye ' + str(random.randrange(0, 100000))) ])

registery.register(Bye)