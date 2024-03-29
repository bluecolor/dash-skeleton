import os
from .helpers import (
    parse_boolean
)

LOG_LEVEL = os.environ.get("DASH_LOG_LEVEL", "INFO")
LOG_STDOUT = parse_boolean(os.environ.get("DASH_LOG_STDOUT", "false"))
LOG_PREFIX = os.environ.get("DASH_LOG_PREFIX", "")
LOG_FORMAT = os.environ.get(
    "DASH_LOG_FORMAT",
    LOG_PREFIX + "[%(asctime)s][PID:%(process)d][%(levelname)s][%(name)s] %(message)s",
)


SQLALCHEMY_DATABASE_URI = os.environ.get(
    "APP_DATABASE_URL", os.environ.get("DATABASE_URL", "postgresql:///postgres")
)

SQLALCHEMY_ENABLE_POOL_PRE_PING = parse_boolean(
   os.environ.get("SQLALCHEMY_ENABLE_POOL_PRE_PING", "false")
)

SQLALCHEMY_DISABLE_POOL = parse_boolean(
    os.environ.get("SQLALCHEMY_DISABLE_POOL", "false")
)

SQLALCHEMY_TRACK_MODIFICATIONS = parse_boolean(
    os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", "false")
)

PROXIES_COUNT = int(os.environ.get("DASH_PROXIES_COUNT", "1"))

SUPPRESS_CALLBACK_EXCEPTIONS = parse_boolean(
    os.environ.get('DASH_SUPPRESS_CALLBACK_EXCEPTIONS', 'true'))


SECRET_KEY = os.environ.get(
    "DASH_SECRET_KEY", "151ef7f3e4790057309ef99be3ee3c569b1aac10f18a0088baaf557d8282eb86"
)


CACHE_TYPE = os.environ.get("DASH_CACHE_TYPE", "simple")


TITLE = os.environ.get('DASH_TITLE', 'Dash')
BRAND = os.environ.get('DASH_BRAND', 'Dash')

# available auth methods: ldap, db
AUTH_METHOD = os.environ.get('DASH_AUTH_METHOD', 'ldap')

# ldap
LDAP_URL = os.environ.get('DASH_LDAP_URL', 'ldap://localhost:389')
LDAP_USERNAME = os.environ.get('DASH_LDAP_USERNAME', 'cn=admin,dc=example,dc=org')
LDAP_PASSWORD = os.environ.get('DASH_LDAP_PASSWORD', 'admin')
LDAP_BASE_DN = os.environ.get("DASH_LDAP_BASE_DN", "dc=example,dc=org")
LDAP_QUERY = os.environ.get('DASH_LDAP_QUERY', '(cn=%s)')

LDAP_PROP_EMAIL = os.environ.get("DASH_LDAP_PROP_IMAIL", "mail")
