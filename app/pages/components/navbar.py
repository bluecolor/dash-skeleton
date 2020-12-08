import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app.pages import registery
from app.settings import BRAND
from flask_login import current_user


def is_authorized(page):
    page_groups = set([g.lower() for g in page.get('groups', [])])
    user_groups = set([g.lower() for g in current_user.groups.split("`")])
    if len(page_groups.intersection(user_groups)) > 0:
        return True

    if '$admin$' in [g.lower() for g in current_user.groups.split("`")]:
        return True

    return False


def apps(registery):
    return dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem(page["name"], id=f"{page['id']}", href=f"{page['id']}")
            for page in sorted(registery.pages, key = lambda i: i['name']) if is_authorized(page)
        ],
        nav=True,
        in_navbar=True,
        label="Applications",
        id='nav-apps'
    )

def account():
    return dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Profile", id='profile', href="/profile"),
            dbc.DropdownMenuItem("Change password", id='change-password', href="/change-password"),
            dbc.DropdownMenuItem("Logout", id='logout', href="/logout")
        ],
        nav=True,
        in_navbar=True,
        label="Account",
        id='nav-account'
    )


def navbar(registery):
    return dbc.NavbarSimple(
        children=[
            apps(registery),
            account(),
        ],
        brand=BRAND,
        brand_href="/",
        sticky="top",
        className="mb-5",
    )