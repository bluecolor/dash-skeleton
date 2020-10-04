import os
from .helpers import (
    parse_boolean,
    array_from_string
)


PROXIES_COUNT = int(os.environ.get("DASH_PROXIES_COUNT", "1"))

SUPPRESS_CALLBACK_EXCEPTIONS = parse_boolean(
    os.environ.get('DASH_SUPPRESS_CALLBACK_EXCEPTIONS', 'true'))

TITLE = os.environ.get('DASH_TITLE', 'Dash')
BRAND = os.environ.get('DASH_BRAND', 'Dash')

# PLUGINS_DIRECTORY = array_from_string(
#     os.environ.get('DASH_PLUGINS_DIRECTORY', 'app.plugins.ext')
# )