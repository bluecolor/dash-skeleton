import dash_bootstrap_components as dbc
from app.pages import registery
from app.settings import BRAND

def menu(registery):
    return dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem(page.name(), id=page.code(), href=page.code())
            for page in registery.pages
        ],
        nav=True,
        in_navbar=True,
        label="Applications",
        id='nav-dropdown'
    )

def navbar(registery):
    return dbc.NavbarSimple(
        children=[
            menu(),
            dbc.Button('Logout',  color="link")
        ],
        brand=BRAND,
        brand_href="#",
        sticky="top",
        className="mb-5",
    )