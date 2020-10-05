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