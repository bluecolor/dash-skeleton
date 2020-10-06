### Plotly Dash Skeleton App


- [x] create user with cli
- [x] login
- [x] logout
- [x] home
- [x] change password
- [x] edit profile
- [x] logging
- [x] gunicorn `gunicorn -w 4 "app:create_app()"`
- [x] https `gunicorn --certfile=server.crt --keyfile=server.key --bind 0.0.0.0:443 "app:create_app()"`


### Usage

- Create virtual environment
```
virtualenv -p python3 venv
```

- Activate
```
. venv/bin/activate
```

- Install dependencies
```
pip install -r requirements.txt
```

- Setup database (tested with postgre and sqlite)

if you use sqlite
```
export APP_DATABASE_URL=sqlite:///dash.db
```
if you use postgre
```
export APP_DATABASE_URL=postgresql://dash:dash@localhost:5432/dash
```

- Create tables
```sh
python manage.py database create-tables
```

- Create user
```
python manage.py user create <name> <email> <password>
```

- Run
```
chmod +x debug.sh
./debug.sh
```


### Adding new pages

Put new pages under app/pages/ext folder like the `hello.py` example.
It will automacilly appear in "Applications" in navigation bar.

Basic example:

```py
import dash_html_components as html
from app.pages import Page, registery

class Hello(Page):
    def render(self, app):
        return html.Div([ html.H3('Hello') ])

registery.register(Hello)
```


Example with custom navigation title:
```py
import dash_html_components as html
from app.pages import Page, registery

class MyPage(Page):
    # Custom Navigation title
    @classmethod
    def name(cls):
        return "My Awesome Dashboard"

    def render(self, app):
        return html.Div([ html.H3('Hello') ])


Enjoy.