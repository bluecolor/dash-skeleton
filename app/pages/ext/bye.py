import dash_html_components as html
from app.pages import registery
from app.cache import cache

# registery item props
# render: Render method
# name: Report name
# id: Report id
# groups: [Report group]
# descripttion: Report description


@cache.memoize(10)
def render():
    import random
    import time
    time.sleep(4)
    return html.Div([ html.H3('Bye ' + str(random.randrange(0, 100000))) ])


item = {
    "render": render,
    "name": "Bye report",
    "id": "10",
    "groups": ["analytics"],
    "description": """My awesome report"""
}

registery.register(item)
