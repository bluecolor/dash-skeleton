from dash_auth.auth import Auth
import flask, base64, hashlib
from types import MethodType
class EncryptedAuth(Auth):
    def __init__(self, app, username_password_list):
        Auth.__init__(self, app)
        self._users = username_password_list \
            if isinstance(username_password_list, dict) \
            else {k: v for k, v in username_password_list}

    def is_authorized(self):
        header = flask.request.headers.get('Authorization', None)
        if not header:
            return False
        username_password = base64.b64decode(header.split('Basic ')[1])
        username_password_utf8 = username_password.decode('utf-8')
        username, password = username_password_utf8.split(':')
        return self._users.get(username) == hashlib.new('sha224', password.encode()).hexdigest()

    def login_request(self):
        return flask.Response(
            'Login Required',
            headers={'WWW-Authenticate': 'Basic realm="User Visible Realm"'},
            status=401)

    def auth_wrapper(self, f):
        def wrap(*args, **kwargs):
            if not self.is_authorized():
                return flask.Response(status=403)

            response = f(*args, **kwargs)
            return response
        return wrap

    def index_auth_wrapper(self, original_index):
        def wrap(*args, **kwargs):
            if self.is_authorized():
                return original_index(*args, **kwargs)
            else:
                return self.login_request()
        return wrap



def init_app(app):
    VALID_USERNAME_PASSWORD_PAIRS = {
        'hello': '06d2dbdb71973e31e4f1df3d7001fa7de268aa72fcb1f6f9ea37e0e5'
    }
    auth = EncryptedAuth(
        app,
        VALID_USERNAME_PASSWORD_PAIRS
    )
