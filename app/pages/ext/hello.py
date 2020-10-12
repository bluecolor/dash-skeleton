import dash_html_components as html
from app.pages import registery

# registery item props
# render: Render method
# name: Report name
# id: Report id
# groups: [Report group]
# descripttion: Report description

def render():
    return html.Div([ html.H3('Hello') ])


item = {
    "render": render,
    "name": "Hello report",
    "id": "20",
    "groups": ["analytics", "ai"],
    "description": """My another awesome report"""
}

registery.register(item)
