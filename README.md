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

- Setup database (tested with postgre)
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

Enjoy.